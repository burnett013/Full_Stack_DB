"""
This pages is used to incorporate images, and their use and storage, into the application.
"""
import streamlit as st
from PIL import Image
from pathlib import Path
import time

# Image folder
image_dir = Path(__file__).parent.parent / "assets" / "images"
image_files = sorted(list(image_dir.glob("*.jpeg")))

# Initialize session state
if "slideshow_active" not in st.session_state:
    st.session_state.slideshow_active = False
if "slideshow_index" not in st.session_state:
    st.session_state.slideshow_index = 0
if "thumbnail_clicked" not in st.session_state:
    st.session_state.thumbnail_clicked = False

# Title
st.set_page_config(page_title="Image Explorer")
st.header("Image Explorer")

# Slideshow Controls (side-by-side)
# st.subheader("Auto-Scroll Preview")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("▶️ Start Slideshow", key="start"):
        st.session_state.slideshow_active = True
        st.session_state.thumbnail_clicked = False
with col2:
    if st.button("🛑 Stop Slideshow", key="stop"):
        st.session_state.slideshow_active = False

# Thumbnails
st.subheader("Choose your color!")
thumb_cols = st.columns(len(image_files))
for i, img_file in enumerate(image_files):
    thumb = Image.open(img_file).resize((100, 60))
    with thumb_cols[i]:
        if st.button("", key=f"thumb_{i}"):
            st.session_state.slideshow_index = i
            st.session_state.slideshow_active = False
            st.session_state.thumbnail_clicked = True
        st.image(thumb, caption=img_file.name)

# Show selected or current slideshow image
current_index = st.session_state.slideshow_index
image_path = image_files[current_index]
image = Image.open(image_path)
st.image(image, caption=image_path.name)

# Handle slideshow
if st.session_state.slideshow_active:
    if not st.session_state.thumbnail_clicked:
        time.sleep(2)  # Delay between slides
        st.session_state.slideshow_index = (current_index + 1) % len(image_files)
        st.rerun()
    else:
        # A thumbnail was just clicked, prevent slideshow from continuing this cycle
        st.session_state.thumbnail_clicked = False