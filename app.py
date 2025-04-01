import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import folium
import networkx as nx
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static



# Custom CSS for overlay effect
st.markdown("""
    <style>
    .header-container {
        position: relative;
        text-align: center;
        width: 100%;
    }
    
    .header-container img {
        width: 100%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# Set Image (Replace with your own URL or path)
st.image("Cyber Threat Dashboard.png", use_column_width=True)

# Overlay Title
# st.markdown('<div class="header-title">👾 Cyber Threat Intelligence Dashboard</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Load threat data
df = pd.read_csv("cyber_threats.csv")

# VirusTotal API settings
VIRUSTOTAL_API_KEY = 'c602d6e2c680cb2b8fc504eae3ef64b77176d740e0569ae84ac354de8cca8657'
VT_URL = "https://www.virustotal.com/api/v3/domains/"

def check_domain_vt(domain):
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    response = requests.get(VT_URL + domain, headers=headers)
    if response.status_code == 200:
        data = response.json()
        malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
        return malicious
    return None

# ➤ **Streamlit Sidebar**
st.sidebar.title("👾 Check Website for Malicious Activity")
website_url = st.sidebar.text_input("Enter Website URL")

if st.sidebar.button("🔍 Lookup"):
    if website_url:
        vt_result = check_domain_vt(website_url)
        if vt_result is not None:
            if vt_result > 0:
                st.sidebar.warning(f"⚠️ VirusTotal Reports: {vt_result} malicious detections!")
            else:
                st.sidebar.success("✅ No malicious activity detected.")
        else:
            st.sidebar.error("❌ Could not fetch results. Please try again!")
    else:
        st.sidebar.info("ℹ️ Please enter a website URL to check.")




st.dataframe(df, width=800)

search_term = st.text_input("Search Domain")
if search_term:
    result = df[df["Threat"].str.contains(search_term, na=False)]
    st.dataframe(result)
    vt_result = check_domain_vt(search_term)
    if vt_result is not None:
        st.warning(f"⚠️ VirusTotal Reports: {vt_result} malicious detections!")

# Data visualization

# Set dark mode style
plt.style.use("dark_background")

### ➤ Create Streamlit Columns (2 in a Row)
col1, col2 = st.columns(2)

### **1️⃣ Threat Source Bar Chart**
with col1:
    st.subheader("📊 Threat Source Distribution")
    fig, ax = plt.subplots()
    df["Source"].value_counts().plot(kind="bar", ax=ax, color=["#1f77b4", "#ff7f0e", "#2ca02c"], edgecolor="white")
    ax.set_xlabel("Threat Sources", color="white")
    ax.set_ylabel("Count", color="white")
    ax.set_title("Threat Source Distribution", color="white")
    st.pyplot(fig)

### **2️⃣ Geolocation Map**
with col2:
    st.subheader("🔗 Threat Network")
    
    G = nx.Graph()
    for source, ip in zip(df["Source"], df["Threat"]):
        G.add_edge(source, ip)

    fig_network, ax_network = plt.subplots(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color="cyan", edge_color="white", font_color="white", node_size=2000, ax=ax_network)
    plt.title("Threat Source Network", color="white")
    st.pyplot(fig_network)

    

### **3️⃣ Network Graph**
st.subheader("🌍 Threat Locations (IP Mapping)")

# Function to get location data
def get_location(ip):
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url).json()
    if "loc" in response:
        lat, lon = response["loc"].split(",")
        return float(lat), float(lon)
    return None

# Create Folium Map
map = folium.Map(location=[20,0], zoom_start=2, tiles="CartoDB dark_matter")

# Add Threat IP Locations
for ip in df["Threat"]:
    loc = get_location(ip)
    if loc:
        folium.Marker(loc, popup=ip, icon=folium.Icon(color="red")).add_to(map)

# Display Map in Streamlit
folium_static(map)
