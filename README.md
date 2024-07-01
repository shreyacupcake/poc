# Tool Execution

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





# Vulnerability Database Management and Fetching Tool

## Overview

This tool helps manage and fetch data from different vulnerability databases. It supports adding new databases to a local configuration file and fetching vulnerability data from selected sources.

## Features

- Add new databases to a local configuration file.
- Fetch NVD (National Vulnerability Database) data for a given year.
- Fetch CVE data from a CSV source.
- Fetch and display vulnerability details from the Vulners API.

## Prerequisites

- Python 3.x
- `requests` library (install via `pip install requests`)

## Getting Started

### 1. Configuration File

Create a local configuration file with the following format:

```json
{
    "databases": {
        "NVD": {
            "url": "https://nvd.nist.gov/vuln/data-feeds",
            "format": "json"
        },
        "SomeOtherDB": {
            "url": "https://example.com/someotherdb.csv",
            "format": "csv"
        }
    }
}
