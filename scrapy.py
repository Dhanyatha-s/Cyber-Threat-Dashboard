import requests
import pandas as pd
# from bs4 import BeautifulSoup

# List of sources
SOURCES = {
    "Abuse.ch": "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"
}

threat_data = []

for source, url in SOURCES.items():
    response = requests.get(url)
    data = response.text.split("\n")

    for line in data:
        if not line.startswith("#") and line.strip():
            threat_data.append({"Source": source, "Threat": line.strip()})

df = pd.DataFrame(threat_data)
df.to_csv("cyber_threats.csv", index=False)
print("Threat data saved.")
