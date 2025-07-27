import csv
import os
import sys
import json
sys.path.append(r'D:\DE ITI\python\py_tasks')
from email_validation import email_valid
# Dummy data for testing
dummy_data = [
    {"Name": "Manar Mosa", "Email": "manar.mosa@gmail.com"},
    {"Name": "Ali Salem", "Email": "ali@@gmail..com"},
    {"Name": "Aya Nabil", "Email": "aya.nabil@outlook.com"},
    {"Name": "Omar Fathi", "Email": "omarfathi.gmail.com"},
    {"Name": "Reem Adel", "Email": "reem_adel@ymail"},
    {"Name": "Sara Helmy", "Email": "sara.helmy@yahoo.com"},
    {"Name": "Tamer Youssef", "Email": "tamer#outlook.com"},
    {"Name": "Mona Hossam", "Email": "mona.hossam@hotmail.com"},
    {"Name": "Khaled Rami", "Email": "khaled.rami@icloud.com"},
    {"Name": "Nour Ashraf", "Email": "@icloud.com"}
]

# Save dummy data to CSV
os.makedirs("check_dummy_data", exist_ok=True)
with open("check_dummy_data/tdummy_data.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Email"])
    writer.writeheader()
    writer.writerows(dummy_data)

# Load CSV data
with open("check_dummy_data/tdummy_data.csv", 'r', newline='') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Get valid emails
def valid_email_list(data):
    valid_emails = []
    for row in data:
        email = row["Email"]
        if email_valid(email):
            valid_emails.append(email)
    return valid_emails

# Convert to set
def unique_email_set(valid_emails):
    return set(valid_emails)

# Save to JSON
def save_to_json(email_set, path):
    with open(path, 'w') as f:
        json.dump(list(email_set), f, indent=2)

# Run script
if __name__ == "__main__":
    valid_emails = valid_email_list(data)
    print("Valid Emails List:", valid_emails)

    unique_emails = unique_email_set(valid_emails)
    print("Unique Valid Emails Set:", unique_emails)

    save_to_json(unique_emails, "check_dummy_data/valid_emails.json")
    print("JSON file saved at 'check_dummy_data/valid_emails.json'")
