import csv
import requests
import logging
import sys

api_key = input("Please enter your Resource Management API key: ")
# Configure the logging settings
logging.basicConfig(filename='upload_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Path to your CSV file
csv_file_path = input("Please enter your full CSV file path (e.g. C:\Users\username\Desktop\file.csv):")

# Define headers for your API request
headers = {
    "Content-Type": "application/json",
    "auth": api_key,
    # Add more headers as needed
}

# Read CSV file and send data to API
with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        # Build JSON Data per row
        json_data = {
            "user_id": row["user_id"],
            "assignable_id": row["project_id"],
            "date": row["date"],
            "hours": row["hours"],
            "notes": row["notes"],
            #"task": row["task"] only required if you have tasks set to mandatory within RM
            # Add more fields as needed
        }
        # Your API endpoint URL
        api_url = "https://api.rm.smartsheet.eu/api/v1/projects/{row['project_id']}/time_entries"
        # Make a POST request to the API endpoint with headers
        response = requests.post(api_url, json=json_data, headers=headers)

        # Print the full response
        logging.info("Full Response:")
        logging.info(f"Status Code: {response.status_code}")
        logging.info("Headers:")
        for key, value in response.headers.items():
            logging.info(f"{key}: {value}")
        logging.info("Body:")
        logging.info(response.text)

        # Check if the request was successful
        if response.status_code == 200:
            logging.info(f"Data for row ID {row['row_id']} uploaded successfully")
            print(f"Data for row ID {row['row_id']} uploaded successfully")
        else:
            logging.info(f"Failed to upload data for row ID {row['row_id']}.")
            print(f"Failed to upload data for row ID {row['row_id']}.")
            sys.exit(1)
