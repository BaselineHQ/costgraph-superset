import os
import requests

new_zip_file = os.getenv("SUPERSET_DASHBOARD_ZIP", "/app/dashboard.zip")
username = os.getenv("SUPERSET_ADMIN_USERNAME")
password = os.getenv("SUPERSET_ADMIN_PASSWORD")
login_payload = {
    "password": password,
    "provider": "db",
    "refresh":  True,
    "username": username,
}

base_url = 'http://localhost:8088'

while True:
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        break
    except Exception:
        pass

login_url = f"{base_url}/login/"
api_login_url = f"{base_url}/api/v1/security/login"
session = requests.Session()

payload = {}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = session.request("GET", login_url, headers=headers, data=payload)
csrf_token = response.text.split('<input id="csrf_token" name="csrf_token" type="hidden" value="')[1].split('">')[0]

# perform login

payload = f'csrf_token={csrf_token}&username={username}&password={password}'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded'
}

session.request("POST", login_url, headers=headers, data=payload, allow_redirects=False)
cookie = session.cookies.get_dict().get('session')
print(session.cookies.get_dict())

auth_login_headers = {
    'Content-Type': 'application/json',
    "Accept": "application/json",
    "Access-Control-Allow-Credentials": "true"
}
auth_response = requests.post(api_login_url, headers=auth_login_headers, json=login_payload, allow_redirects=False)
token = auth_response.json()['access_token']

# Import dashboards
import_dashboard_url = f"{base_url}/api/v1/dashboard/import/"

with open(new_zip_file, 'rb') as f:
    payload = {
        'passwords': '{"databases/Postgres.yaml": "' + os.getenv("POSTGRES_PASSWORD") + '"}',
        'overwrite': 'true'
    }
    files = [
        ('formData', ('dashboards.zip', f, 'application/zip'))
    ]
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'Cookie': f'session={cookie}',
        'X-CSRFToken': csrf_token
    }

    response = requests.request("POST", import_dashboard_url, headers=headers, data=payload, files=files)

print(response.text)