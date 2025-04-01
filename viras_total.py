import requests


VIRUSTOTAL_API_KEY = 'c602d6e2c680cb2b8fc504eae3ef64b77176d740e0569ae84ac354de8cca8657'
VT_URL = "https://www.virustotal.com/api/v3/domains/"

def check_domain_vt(domain):
    headers = {'x-apikey': VIRUSTOTAL_API_KEY}
    response = requests.get(VT_URL + domain, headers=headers)

    if response.status_code == 200:
        data = response.json()
        malicious = data['data']['attributes']['last_analysis_status']['malicious']
        return malicious
    return None

domain ="https://www.malwaredomainlist.com/mdlcsv.php"
result = check_domain_vt(domain)
print(f"Malicious reports: {result}")
    
