import json
import requests
import csv
import gzip
import io
from io import StringIO

# Function to prompt the user for new database information
def prompt_user_for_database():
    db_name = input("Enter the name of the new database: ").strip()
    url = input("Enter the URL of the new database: ").strip()
    format_type = input("Enter the format (json/csv) of the new database: ").strip().lower()
    if format_type not in ["json", "csv"]:
        print("Invalid format type. Please choose 'json' or 'csv'.")
        return None
    return db_name, url, format_type

# Function to save the configuration to a local file
def save_config_file(file_path, config):
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
        print(f"Configuration file saved successfully to {file_path}")
    except IOError as e:
        print(f"Error saving configuration file: {e}")

# Function to load the configuration from a local file
def load_configuration_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error accessing configuration file: {e}")
        return None

# Function to fetch NVD data
def fetch_nvd_data(url_template):
    try:
        year = input("Enter the year (e.g., 2022) for NVD data: ").strip()
        url = url_template.format(year=year)
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gzip_file:
            json_data = json.load(gzip_file)
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Function to fetch CVE data from a CSV or other sources
def fetch_cve_data(url_template):
    try:
        url = url_template
        response = requests.get(url)
        response.raise_for_status()
        csv_data = response.text
        return csv_data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Function to fetch data from the Vulners API
def fetch_vulners_data(vulnerability_id):
    url = f"https://vulners.com/api/v3/search/id/?id={vulnerability_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Function to extract information from Vulners data
def extract_vulnerability_info(data, vulnerability_id):
    if data is not None and data.get('result') == 'OK':
        v1 = data.get('data', {})
        v2 = v1.get('documents', {})
        v3 = v2.get(vulnerability_id, {})
        print(f"ID: {v3.get('id', 'N/A')}")
        print(f"Type: {v3.get('type', 'N/A')}")
        print(f"BulletinFamily: {v3.get('bulletinFamily', 'N/A')}")
        print(f"Title: {v3.get('title', 'N/A')}")
        print(f"Description: {v3.get('description', 'N/A')}")
    else:
        print("No valid data or unsuccessful API response.")

config_file_path = "Configurationfile.json"
config = load_configuration_from_file(config_file_path)
if config is not None:
    databases = config.get('databases', {})
    print("Available Databases:")
    for db_name in databases:
        print(f"- {db_name}")
    selected_db = input("Enter the name of the database to fetch data from: ").strip()
    if selected_db in databases:
        db_info = databases[selected_db]
        url_template = db_info['url']
        format_type = db_info['format']
        if format_type == "json":
            if selected_db == "NVD":
                data = fetch_nvd_data(url_template)
            else:
                data = fetch_cve_data(url_template)
        elif format_type == "csv":
            data = fetch_cve_data(url_template)
        if selected_db == "Vulners":
            vulnerability_id = input("Enter the vulnerability ID (e.g., WOLFI:GHSA-JQ35-85CJ-FJ4P): ").strip()
            data = fetch_vulners_data(vulnerability_id)
            extract_vulnerability_info(data, vulnerability_id)
        elif data is not None:
            if format_type == "json":
                if selected_db == "NVD":
                    num_entries = len(data['CVE_Items'])
                    print(f"Total number of entries for {selected_db} in 2023: {num_entries}")
                    for i, vulnerability in enumerate(data.get('CVE_Items', []), start=1):
                        cve_id = vulnerability['cve']['CVE_data_meta']['ID']
                        description = vulnerability['cve']['description']['description_data'][0]['value']
                        print(f"\nVulnerability {i} (CVE-ID: {cve_id}):")
                        print(f"Description: {description}")
            elif format_type == "csv":
                reader = csv.reader(StringIO(data))
                next(reader)  # Skip header row
                for i, row in enumerate(reader, start=1):
                    cve_id = row[0]
                    description = row[2]
                    print(f"\nVulnerability {i} (CVE-ID: {cve_id}):")
                    print(f"Description: {description}")
        else:
            print(f"No data fetched for {selected_db}")
    else:
        print("Invalid database selected. Please choose from the available options.")
else:
    print("Failed to load configuration from file.")