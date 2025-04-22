import streamlit as st

st.set_page_config(
    page_title="Data Analyst Project",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Data Analyst Project")

st.markdown("### Project Purpose")
st.markdown("""
This Streamlit application may appear to be a simple showcase of trucks I find interesting, 
but its true purpose is to serve as a hands-on environment for mastering full-stack data analytics workflows. 
The project bridges frontend interactivity with backend data control, helping to solidify key concepts in modular application design.
""")

st.markdown("---")

st.markdown("### Project Objectives")

st.markdown("""
- Streamlit for a responsive, modular frontend  
- FastAPI to power backend CRUD operations  
- SQLite as the database for storing and querying user data  
- Image Carousel with main preview and clickable thumbnails  
- Certification CRUD for data such as Name, Email, and more  
- Modular Design — core app logic under 20 lines in `app.py`  
- Dockerized Services using `docker-compose.yaml`:
    - Streamlit  
    - FastAPI  
    - SQLite  
- Requirements tracked in `requirements.txt`  
- Deployment-ready for Posit Connect Cloud
""")

st.markdown("---")

st.caption("This project was built as part of a self-directed learning series to develop scalable, cloud-deployable data applications using open-source tools.")