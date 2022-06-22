import io
import streamlit as st
from app import get_filetype, read_dicom, get_prediction
from PIL import Image

st.title('X-ab: Detecting Chest X-ray Abnormality')
st.markdown('---')

# layout
col1, col2, col3 = st.columns([4, 1, 2])  # col2 for empty space
col1.subheader("Chest X-ray Image")
col3.subheader("Analysis Result")

# file uploader
with col1:
    # By default, uploaded files are limited to 200MB
    # You can configure this using the server.maxUploadSize config option
    uploaded_file = st.file_uploader("Supported file formats: DICOM, JPG, PNG")
    with opoen('web.png', "rb") as f:
        st.download_button('Sample image', f, file_name='web.png')

if uploaded_file is not None:
    file_ext = uploaded_file.name.split(".")[-1]
    file_type = get_filetype("." + file_ext)
    # print('file type: ', file_type)

    # Read file and open image with PIL
    if file_type == "0":  # DICOM
        image = read_dicom(uploaded_file, f_type='pil')  # f_type: bytes or pil
    elif file_type == "1" or file_type == "2":  # JPG or PNG
        bytes_data = uploaded_file.read()
        data_io = io.BytesIO(bytes_data)
        image = Image.open(data_io)
    else:
        image = None
        st.error("[Error] Unsupported file type")

    # Show image
    with col1:
        st.image(image)

    # Analysis
    with col3:
        st.caption('Click the button')
        if st.button('Analyze'):
            output = io.BytesIO()
            image.save(output, 'PNG')
            bytes_data = output.getvalue()
            class_name = get_prediction(image_bytes=bytes_data)
            st.info(class_name)


