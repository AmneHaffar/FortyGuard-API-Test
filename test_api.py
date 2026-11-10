
import os
import requests

api_key = os.getenv("FORTYGUARD_API_KEY")

if not api_key:
    raise RuntimeError("API key is missing")

url = "https://api.fortyguard.com/v1/heatmap"

headers = {
    "api-key": api_key,
    "Content-Type": "application/json"
}

payload = {
    "polygon_aoi": {
        "type": "Polygon",
        "coordinates": [[
            [-74.0170, 40.7051],
            [-74.0031, 40.7051],
            [-74.0031, 40.7180],
            [-74.0170, 40.7180],
            [-74.0170, 40.7051]
        ]]
    },
    "date_time": {
        "start_date": "2024-07-15",
        "start_time": "14:00",
        "filter_type": 1
    },
    "granularity": 100
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("HTTP Status:", response.status_code)
    print("Response:", response.text[:2000])

    if response.ok:
        result = response.json()
        activity_id = result.get("data", {}).get("activity_id")

        if activity_id:
            print("SUCCESS! Activity ID:", activity_id)
        else:
            print("No activity ID returned.")
    else:
        print("Request failed.")

except requests.RequestException as error:
    print("Request error:", error)
