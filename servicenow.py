import requests
import config

def create_ticket(short_desc, long_desc):

    url = f"{config.SERVICENOW_URL}/api/now/table/incident"

    payload = {
        "short_description": short_desc,
        "description": long_desc
    }

    response = requests.post(
        url,
        auth=(config.SERVICENOW_USER, config.SERVICENOW_PASSWORD),
        json=payload
    )

    return response.json()