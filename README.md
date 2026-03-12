API Integration Testing Tool

A lightweight Python tool that tests REST API endpoints, validates JSON response structures, 
and generates logs and JSON reports to help diagnose integration issues.

This project simulates troubleshooting workflows commonly used in technical support,
implementation engineering, and API integration roles in fintech and SaaS environments.

Features:
• Tests multiple REST API endpoints
• Validates JSON response structure
• Measures API response time
• Logs troubleshooting information
• Generates structured JSON reports
• Supports multi-endpoint integration testing
Tech Stack
• Python 3
• Requests library
• JSON
• Logging

Project Structure:
api-integration-testing-tool/
│
├── src/
│   └── tester.py      # Main script for API testing
│
├── reports/
│   ├── report.json    # Generated result report
│   └── test.log       # Execution logs
│
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

How It Works:
1. The script sends requests to several API endpoints.
2. Each endpoint response is validated.
3. Response time and status codes are recorded.
4. JSON data structure is inspected.
5. Logs and reports are generated for troubleshooting.
   
Installation:

Clone the repository:
git clone https://github.com/YOUR_USERNAME/api-integration-testing-tool.git

Navigate into the project folder:
cd api-integration-testing-tool

Install dependencies:
python3 -m pip install -r requirements.txt
Run the Tool
python3 src/tester.py

After running the script, a report will be generated in:
reports/report.json

Logs will be written to:
reports/test.log
Purpose of This Project
This project was created to practice:
• API troubleshooting
• JSON validation
• logging and diagnostics
• building developer utilities in Python

It demonstrates practical skills used in technical support, implementation,
and API integration roles.

