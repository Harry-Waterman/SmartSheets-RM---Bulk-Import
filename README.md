# SmartSheets Resource Management Bulk Import Historical Data
Python Script to bulk import historical time entry data via the API

### How to use this script 

Download the contents of the repo, create a upload_log.txt file in the same location you have the bulk-import.py script 

run the bulk-import.py script with python > you will be prompted to enter your API key and full filepath for the CSV

You will see a record of what has been uploaded successfully within the command prompt and a more detailed log in upload_log.txt - if it fails to upload a row of the CSV the script will exit so you know where to pick up again once you resolve the issue. 
