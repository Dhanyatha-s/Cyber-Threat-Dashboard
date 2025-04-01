# Cyber Threat Intelligence Dashboard 🚀

## Overview 📌
The Cyber Threat Intelligence Dashboard is a security-focused application designed to track, analyze, and visualize cybersecurity threats in real-time. It integrates multiple threat intelligence sources and provides security professionals with actionable insights to mitigate risks.

## Key Features 🔥
### 🔍 Malicious Website Detection
- ✅ **VirusTotal API Integration**: Checks for malicious activity associated with entered website domains.
- ⚠️ **Threat Level Indicators**: Displays the number of malicious detections.
- 🔗 **User Input for URL Lookup**: Users can manually enter a website to check for cyber threats.

### 📊 Threat Data Visualization
- 📈 **Threat Source Distribution Bar Chart**: Identifies the most common sources of cyber threats.
- 🌐 **Network Graph Representation**: Shows relationships between threat sources and affected domains.
- 🗺️ **Interactive Threat Map**: Uses geolocation data to map IP addresses linked to cyber threats.

### 🗂️ Threat Data Management
- 📥 **CSV-Based Threat Data Loading**: Processes cybersecurity threat records from a CSV file.
- 🔎 **Search Functionality**: Users can search for specific threats within the dataset.
- 🔄 **Real-Time Updates**: The dashboard can be modified to integrate live threat feeds.
![Screenshot 2025-04-01 175005](https://github.com/user-attachments/assets/88a8cad1-7aa6-4b29-ac52-bb0a6f07077d)
![Screenshot 2025-04-01 175026](https://github.com/user-attachments/assets/3e9fc490-1ca2-4c5d-9ba1-d232a4bc3115)
![Screenshot 2025-04-01 175049](https://github.com/user-attachments/assets/e1d088b1-a635-47a3-bd9a-935615dad217)

## Technology Stack 🛠️
### 📝 Programming Languages & Libraries
- **Python** 🐍: Core programming language for data processing and API integration.
- **Streamlit** 🎨: Framework for building the interactive dashboard.
- **Pandas** 📊: Used for data manipulation and analysis.
- **Matplotlib** 📉: Generates visualizations of threat data.
- **Folium** 🗺️: Maps threat locations using geospatial data.
- **NetworkX** 🔗: Constructs and visualizes threat-related network graphs.
- **Geopy & IPInfo API** 🌍: Retrieves geolocation data for IP addresses.
- **Requests** 🌐: Fetches data from external threat intelligence sources.

### 🌎 APIs & External Services
- **VirusTotal API** 🦠: Scans and analyzes domains for cybersecurity threats.
- **IPInfo API** 📌: Provides geolocation data for detected threat IPs.
- **CartoDB Tiles** 🗺️: Used for rendering dark-themed threat maps.
## 🐳 Dockerization

### 📦 Why Docker?
- 🚀 **Portability**: Run the application across different environments without setup conflicts.
- 📌 **Consistency**: Ensures the application runs identically in development and production.
- 🔄 **Scalability**: Easily deployable in cloud environments using containers.

### 🛠️ How to Run with Docker
#### Clone the Repository:
```bash
git clone https://github.com/yourrepo/cyber-threat-dashboard.git
cd cyber-threat-dashboard
```
### Build the Docker Image:
```bash
docker build -t cyber-threat-dashboard .
```
### Run the Container:
```bash
docker run -p 8501:8501 cyber-threat-dashboard
```
### Access the Application:
#### Open your browser and go to: http://localhost:8501

## Industry Applications 🏢
### 🔐 Cybersecurity Operations Centers (CSOCs)
- 🛡️ **Threat Monitoring**: Identifies malicious entities targeting enterprise systems.
- 🏃 **Incident Response**: Helps security analysts react to potential cyber-attacks.
- 🔗 **Threat Intelligence Sharing**: Enables real-time data exchange with industry security groups.

### 🏦 Financial Institutions & Banks
- 💰 **Fraud Prevention**: Detects phishing websites and malicious domains targeting customers.
- 📉 **Risk Management**: Identifies compromised financial systems or user credentials.
- 📜 **Regulatory Compliance**: Supports compliance with cybersecurity frameworks like GDPR and PCI-DSS.

### 🏛️ Government & Defense Organizations
- 🏴‍☠️ **National Cyber Threat Intelligence**: Maps out cyber threats to national infrastructure.
- ⚠️ **Advanced Persistent Threat (APT) Detection**: Tracks sophisticated cyber-attacks.
- 🌍 **Cross-Border Threat Analysis**: Monitors global cyber-attack trends.

### ☁️ IT & Cloud Service Providers
- ☁️ **Cloud Security**: Detects and mitigates security risks in cloud environments.
- 🔐 **Enterprise Network Protection**: Identifies internal network vulnerabilities.
- 🚀 **Zero Trust Security Implementation**: Provides real-time security insights to enforce Zero Trust models.

## Future Enhancements 🔮
### 🤖 AI-Powered Threat Prediction
- 🔍 Implementing machine learning to predict emerging cyber threats based on past trends.
- 🚀 Automating threat classification using AI-driven models.

### 📡 Real-Time Threat Intelligence Feeds
- 🔗 Integrating live feeds from cybersecurity platforms like IBM X-Force, FireEye, and Open Threat Exchange.
- ⚡ Implementing WebSocket-based updates for continuous monitoring.

### 🎨 Advanced Visualization & Custom Dashboards
- 📊 Enhancing data visualization using D3.js for interactive threat mapping.
- 🎛️ Allowing customizable widgets for personalized cybersecurity insights.

### 🔄 API-Based Threat Mitigation
- 🔥 Integrating with firewall and endpoint security solutions for automated threat blocking.
- 🛡️ Developing response automation to quarantine infected assets.

## Conclusion 🎯
The Cyber Threat Intelligence Dashboard provides security professionals with actionable insights into cyber threats. By integrating multiple data sources, advanced visualizations, and real-time analytics, organizations can proactively mitigate cyber risks and enhance their security posture.

💡 Contributions and feedback are welcome!

## License 📜
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Author 👨‍💻
Developed by **Dhanyatha S** 🚀 | Feel free to connect on [GitHub](https://github.com/Dhanyatha-s)!


