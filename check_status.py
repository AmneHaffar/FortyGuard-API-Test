
import os
import requests
import time
import json

# Get API key
api_key = os.getenv("FORTYGUARD_API_KEY")

if not api_key:
    raise RuntimeError("API key is missing")

# Your successful Heatmap Activity ID
activity_id = "da59dc40-0cd6-427b-a1fa-e3b650aee349"

# FortyGuard API endpoint
status_url = f"https://api.fortyguard.com/v1/status/{activity_id}"

headers = {
    "api-key": api_key
}

print("Checking FortyGuard Heatmap status...")

try:
    for attempt in range(12):

        response = requests.get(
            status_url,
            headers=headers,
            timeout=30
        )

        print("HTTP Status:", response.status_code)

        if not response.ok:
            print("Request failed.")
            print(response.text[:1000])
            break

        response_data = response.json()
        data = response_data.get("data", {})

        status = str(data.get("status", "unknown")).lower()

        print("Task Status:", status)

        if status in ("completed", "succeeded"):

            print("Task completed successfully!")

            print("Result keys:", list(data.keys()))

            # Extract Heatmap result
            result = data.get("result")

            if result is None:
                print("No result data returned.")
                break

            # Save result as JSON file
            filename = "heatmap_result.json"

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(
                    result,
                    file,
                    indent=2,
                    ensure_ascii=False
                )

            print("Heatmap result saved successfully!")
            print("File:", filename)

            if isinstance(result, dict):
                print("Available result fields:", list(result.keys()))

            break

        elif status in ("failed", "error"):

            print("Task failed.")
            print(data)
            break

        else:

            print("Task is still processing...")
            time.sleep(5)

    else:
        print("Task is still processing. Try again later.")

except requests.RequestException as error:
    print("Request error:", error)

except (ValueError, TypeError) as error:
    print("Data processing error:", error)
