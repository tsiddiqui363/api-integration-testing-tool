import requests
import json
import time
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename="reports/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# API endpoints to test
endpoints = [
    "https://fakestoreapi.com/products",
    "https://fakestoreapi.com/users",
    "https://fakestoreapi.com/carts"
]

# Final report
report = {
    "timestamp": datetime.now().isoformat(),
    "results": []
}

logging.info("API test run started")

for url in endpoints:
    endpoint_result = {
        "endpoint": url,
        "success": False,
        "status_code": None,
        "response_time_ms": None,
        "item_count": 0,
        "errors": []
    }

    logging.info(f"Testing endpoint: {url}")

    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        end = time.time()

        endpoint_result["status_code"] = response.status_code
        endpoint_result["response_time_ms"] = round((end - start) * 1000)

        logging.info(f"Received status code: {response.status_code} for {url}")
        logging.info(f"Response time: {endpoint_result['response_time_ms']} ms")

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, list):
                endpoint_result["success"] = True
                endpoint_result["item_count"] = len(data)
                logging.info(f"{url} returned {len(data)} items")

                if len(data) > 0 and isinstance(data[0], dict):
                    first_item = data[0]
                    required_keys = ["id"]

                    for key in required_keys:
                        if key not in first_item:
                            error_message = f"Missing key '{key}' in first item for {url}"
                            endpoint_result["errors"].append(error_message)
                            logging.error(error_message)
            else:
                error_message = f"Response is not a list for {url}"
                endpoint_result["errors"].append(error_message)
                logging.error(error_message)
        else:
            error_message = f"Unexpected status code {response.status_code} for {url}"
            endpoint_result["errors"].append(error_message)
            logging.error(error_message)

    except Exception as e:
        error_message = f"Exception while testing {url}: {str(e)}"
        endpoint_result["errors"].append(error_message)
        logging.exception(error_message)

    report["results"].append(endpoint_result)

# Save the report to a JSON file
with open("reports/report.json", "w") as f:
    json.dump(report, f, indent=2)

logging.info("API test run completed")

# Print result in terminal
print("Done. Report saved to reports/report.json")
print(json.dumps(report, indent=2))