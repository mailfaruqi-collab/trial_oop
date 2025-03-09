import streamlit as st
import pandas as pd
import libs
from streamlit_folium import st_folium
import folium

# Initialize database
if "database" not in st.session_state:
    st.session_state.database = libs.UserDatabase()

st.title("User Management System")

# map
def display_map():
    m = folium.Map(
        location=[-6.21, 106.81], 
        zoom_start=11,
        tiles="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        attr="Google Maps"
    )
    for user in st.session_state.database.get_users():
        folium.Marker(
            location=[user["latitude"], user["longitude"]],
            popup=f"{user['name']} ({user['vehicle_type']})",
        ).add_to(m)
    return m

# Sidebar 
st.sidebar.header("Add New User")
name = st.sidebar.text_input("Name")
vehicle_type = st.sidebar.selectbox("Vehicle Type", ["2W", "4W"])

st.sidebar.write("Click on the map to set location")
map_data = st_folium(display_map(), height=500, width=700) 

if map_data and map_data.get("last_clicked"):
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    if st.sidebar.button("Add User"):
        st.session_state.database.add_user(name, lat, lon, vehicle_type)
        st.sidebar.success(f"Added {name} successfully!")
        st.rerun()

# Display user data
st.subheader("User List")
user_data = st.session_state.database.get_users()
df = pd.DataFrame(user_data)
st.dataframe(df)

# Delete user
st.sidebar.header("Remove User")
user_id = st.sidebar.text_input("Enter User ID")
if st.sidebar.button("Delete User"):
    st.session_state.database.remove_user(int(user_id))
    st.sidebar.success(f"User {user_id} removed!")
    st.rerun()