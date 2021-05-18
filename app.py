import streamlit as st 
import cv2
from PIL import Image , ImageEnhance
import numpy as np
import os

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

def app():
    st.title('Pixy - Quick Editor')
    activities = ['Edit','About']
    choice = st.sidebar.selectbox('Go to ',activities)
    if choice == 'Edit':
        st.subheader('')
        st.subheader('')

        image_file = st.file_uploader("Upload Image",type = ['jpg','png','jpeg'])
        if image_file is  None:
            st.subheader("")
            st.write("Upload Image to remove error  ")
        if image_file is not None:
                our_image = Image.open(image_file)
                st.header('Image')
                st.subheader("")
                st.image(our_image,width=400)

        enhance_type = st.sidebar.radio('Enhance Type',['Original','Gray-scale','Contrast','Brightness','Bluring'])
        if enhance_type == 'Gray-scale':
            new_img = np.array(our_image.convert('RGB'))
            img = cv2.cvtColor(new_img,1)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            st.header('Gray scale')
            st.subheader("")
            st.image(img,width=400)

        elif enhance_type == 'Contrast':
            c_rate = st.sidebar.slider('Constrast',0.5,4.5)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_rate)
            st.header('Contrast')
            st.subheader("")
            st.image(img_output,width=400)

        elif enhance_type == 'Brightness':
            br_rate = st.sidebar.slider('Brightness',0.5,4.5)
            enhancer = ImageEnhance.Brightness(our_image)
            img_out = enhancer.enhance(br_rate)
            st.header('Brightness')
            st.subheader("")
            st.image(img_out,width=400)
        
        elif enhance_type == 'Bluring':
            new_img = np.array(our_image.convert('RGB'))
            b_rate = st.sidebar.slider('Bluring',0.5,4.5)
            img = cv2.cvtColor(new_img,1)
            blur_img = cv2.GaussianBlur(img,(11,11),b_rate)
            st.header('Blured')
            st.subheader("")
            st.image(blur_img,width=400)
        else:
            
            st.header('Final Image ')
            st.subheader("")
            st.image(our_image,width=400)
    elif choice == 'About':
        st.header('Thank you for using our app :smile:')
        st.subheader('')
        st.write("Regards Team Proxlight. ")
if __name__ == "__main__":
    app()
