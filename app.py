# ai analysis server
import io
import os
from custom_model import MyEfficientNet
import torch
from torchvision.transforms import *
from PIL import Image
from collections import OrderedDict
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np

vinbig_class_index = {"0": "normal", "1": "abnormal"}
device = torch.device("cpu")


# load model
model = MyEfficientNet(model_name="efficientnet-b5", out_features=1)  # 요청 시마다 model 불러오는 것 불필요하므로 전역 변수 설정

# load weights
checkpoint = "./checkpoints/exp_024/2022_0112_1822_ep14.pth"
if os.path.isfile(checkpoint):
    state = torch.load(checkpoint, map_location=device)
    # state_dict의 key가 불일치하는 경우에 대한 보정
    new_state = OrderedDict()
    for k, v in state['model'].items():
        name = k[7:]  # remove 'module.'
        new_state[name] = v
    model.load_state_dict(new_state)
    print(f"loaded checkpoint '{checkpoint}'")
    model.to(device)
    model.eval()  # set evaluation mode
else:
    print(f"no checkpoint found at '{checkpoint}'")
    raise SystemExit


def transform_image(image_bytes):
    trans = Compose([Resize((456, 456)), ToTensor()])
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')  # 1 channel to 3 channel(RGB)

    return trans(image).unsqueeze(0)


def get_prediction(image_bytes):

    tensor = transform_image(image_bytes=image_bytes)
    tensor = tensor.to(device)
    outputs = model.forward(tensor)
    pred_score = torch.round(torch.sigmoid(outputs)*100).item()
    pred_idx = int(torch.round(torch.sigmoid(outputs)).item())
    return vinbig_class_index[str(pred_idx)]
    
    #if pred_score < 50:
    #    return vinbig_class_index[str(pred_idx)]
    #else:
    #    return vinbig_class_index[str(pred_idx)] + '\n' + str(pred_score) + '%'


def read_dicom(filePath, f_type, voi_lut=True, fix_monochrome=True):
    dicom = pydicom.read_file(filePath)

    # VOI LUT is used to transformed raw DICOM data to human-friendly view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array

    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data
    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)

    # numpy array -> PIL image -> bytes
    img = Image.fromarray(data)
    if f_type == 'bytes':
        output = io.BytesIO()
        img.save(output, 'PNG')
        binary_pil = output.getvalue()
        return binary_pil
    else:
        return img


# 파일 확장자 label 획득
def get_filetype(file_ext):
    file_ext = file_ext.lower()
    if file_ext == ".dicom" or file_ext == ".dcm":
        file_type = "0"
    elif file_ext == ".jpg" or file_ext == ".jpeg":
        file_type = "1"
    elif file_ext == ".png":
        file_type = "2"
    elif file_ext == ".gif":
        file_type = "3"
    elif file_ext == ".tif" or file_ext == ".tiff":
        file_type = "4"
    else:
        file_type = "-1"
    return file_type


def analysis(filePath):
    print(" analysis Call Start ====")
    try:
        file = open(filePath, 'rb')
        print("filepath : " + filePath)
        _, file_ext = os.path.splitext(filePath)
        file_type = get_filetype(file_ext)  # 파일 타입(확장자) label

        print(file_type)
        if file_type == "0":  # DICOM
            img_bytes = read_dicom(file, f_type='bytes')
        elif file_type == "1" or file_type == "2":  # JPG or PNG
            img_bytes = file.read()
        else:
            return {'result': '1', 'msg': "Unsupported file type"}
        class_name = get_prediction(image_bytes=img_bytes)
        return class_name

    except Exception as e:
        print(e)
        return str(e)


class ChestXrayAnalysis2():
    filePath = "Cradle"

    def analysis(self, filepath):
        result = analysis(filepath)
        print(result)
        return result
