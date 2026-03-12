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

# API endpoint we want to test
url = "https://fakestoreapi.com/products"

# Create a report dictionary to store results
report = {
    "timestamp": datetime.now().isoformat(),
    "endpoint": url,
    "success": False,
    "status_code": None,
    "response_time_ms": None,
    "item_count": 0,
    "errors": []
}

logging.info("API test started")

try:
    # Measure response time
    start = time.time()
    response = requests.get(url, timeout=10)
    end = time.time()

    # Save status and timing
    report["status_code"] = response.status_code
    report["response_time_ms"] = round((end - start) * 1000)

    logging.info(f"Received status code: {response.status_code}")
    logging.info(f"Response time: {report['response_time_ms']} ms")

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if response is a list
        if isinstance(data, list):
            report["success"] = True
            report["item_count"] = len(data)
            logging.info(f"Response contains {len(data)} items")

            # Validate the first item in the list
            if len(data) > 0:
                first_item = data[0]
                required_keys = ["id", "title", "price", "category"]

                for key in required_keys:
                    if key not in first_item:
                        error_message = f"Missing key: {key}"
                        report["errors"].append(error_message)
                        logging.error(error_message)
        else:
            error_message = "Response is not a list"
            report["errors"].append(error_message)
            logging.error(error_message)
    else:
        error_message = f"Unexpected status code: {response.status_code}"
        report["errors"].append(error_message)
        logging.error(error_message)

except Exception as e:
    report["errors"].append(str(e))
    logging.exception("An exception occurred during API testing")

# Save the report to a JSON file
with open("reports/report.json", "w") as f:
    json.dump(report, f, indent=2)

logging.info("API test completed")

# Print result in terminal
print("Done. Report saved to reports/report.json")
print(json.dumps(report, indent=2))