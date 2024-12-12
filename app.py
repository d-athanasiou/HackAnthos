import streamlit as st
import pandas as pd
import geopandas as gpd

# Set the page title and layout
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Header
st.title("Welcome to My Streamlit App!")

# Sidebar
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose a feature", ["Home", "Show Map", "Upload File"])

if option == "Home":
    st.subheader("This is the Home Page")
    st.write("Use the sidebar to navigate!")

elif option == "Show Map":
    st.subheader("Map Example")

    # Example of map data (change this to your geospatial data)
    data = pd.DataFrame({
        'lat': [37.7749, 34.0522, 40.7128],
        'lon': [-122.4194, -118.2437, -74.0060],
        'city': ['San Francisco', 'Los Angeles', 'New York']
    })
    st.map(data)

elif option == "Upload File":
    st.subheader("Upload a GeoJSON or Shapefile")

    uploaded_file = st.file_uploader("Choose a file", type=["geojson", "shp"])
    if uploaded_file is not None:
        try:
            # Read the uploaded file into a GeoDataFrame
            if uploaded_file.name.endswith(".geojson"):
                gdf = gpd.read_file(uploaded_file)
            else:
                gdf = gpd.read_file(uploaded_file)

            # Display data
            st.write(gdf)
            st.map(gdf)
        except Exception as e:
            st.error(f"An error occurred: {e}")
