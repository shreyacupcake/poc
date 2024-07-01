# Tool Execution(POC.py)

This repository contains a Python script designed to execute AI-based security use cases defined in a JSON knowledge base. The script reads the knowledge base, prompts the user to select a use case, and calls the relevant tools associated with the selected use case. This tool is particularly useful for cybersecurity professionals and researchers looking to automate and streamline the execution of security-related tasks using AI and machine learning tools.

## Features

- Reads a JSON file containing AI-based security use cases.
- Prompts the user to select and execute a specific use case.
- Calls tools associated with the selected use case, requiring user input for arguments.
- Supports integration with various AI and ML tools for security applications.


## Usage

1. Place the knowledge base JSON file (e.g., `kb.json`) in the same directory as the script.
2. Run the script:

    ```bash
    python POC.py
    ```

3. When prompted, enter the name of the AI-based security use case you want to execute.
4. Provide values for the required arguments when prompted.

## Example

Assuming the `kb.json` file contains the following data:

```json
{
    "use_cases": [
        {
            "name": "Intrusion Detection",
            "description": "Use AI to detect network intrusions.",
            "tools": [
                {
                    "toolname": "intrusion_detection_tool",
                    "commands": "detect_intrusions",
                    "arguments": ["data_path", "model_path"]
                }
            ]
        }
    ]
}
```


# Another Module #
# Vulnerability Database Plugin (POC1.py)

## Overview

The Vulnerability Database Plugin is designed for integration into a larger vulnerability management system. It provides functionalities for managing database configurations, fetching data from multiple vulnerability databases, and displaying detailed vulnerability information. This plugin is suitable for security professionals and developers who need to interact with various vulnerability data sources in their security tools.

## Features

- **Database Management**: Add new vulnerability databases to a local configuration file.
- **Data Fetching**: Fetch data from different vulnerability databases including NVD and CVE.
- **Data Display**: Display detailed information about vulnerabilities, including CVE IDs and descriptions.
- **Vulners Integration**: Fetch and display specific vulnerability details using the Vulners API.

## Installation

To install the plugin, clone this repository and ensure you have Python 3.x installed. Install the required dependencies using pip:

```bash
git clone https://github.com/your_username/vulnerability-database-plugin.git
cd vulnerability-database-plugin
pip install requests
```

## Configuration
Local Configuration File
Create a configuration file named Configurationfile.json in the root directory of the plugin with the following structure:

```json
{
    "databases": {
        "NVD": {
            "url": "https://nvd.nist.gov/vuln/data-feeds",
            "format": "json"
        },
        "CVE": {
            "url": "https://example.com/cve-data.csv",
            "format": "csv"
        },
        "Vulners": {
            "url": "https://vulners.com/api/v3/search/id/?id={vulnerability_id}",
            "format": "json"
        }
    }
}
```
## Adding New Databases
To add new databases, manually update the Configurationfile.json file with new entries under the databases key.

## Usage
Running the Plugin
To run the plugin, use the following command:
```bash
python plugin.py

```
## You will be prompted to:

* Select a Database: Choose from the available databases defined in Configurationfile.json.
* Enter Additional Information: For NVD: Provide the year for which you want to fetch data; For Vulners: Provide the vulnerability ID to fetch specific details; For CVE: Fetch data from the provided CSV URL.
