# AI-Based Security Use Case Executor

This repository contains a Python script designed to execute AI-based security use cases defined in a JSON knowledge base. The script reads the knowledge base, prompts the user to select a use case, and calls the relevant tools associated with the selected use case. This tool is particularly useful for cybersecurity professionals and researchers looking to automate and streamline the execution of security-related tasks using AI and machine learning tools.

## Features

- Reads a JSON file containing AI-based security use cases.
- Prompts the user to select and execute a specific use case.
- Calls tools associated with the selected use case, requiring user input for arguments.
- Supports integration with various AI and ML tools for security applications.

## Requirements

- Python 3.x

## Usage

1. Place your knowledge base JSON file (e.g., `kb.json`) in the same directory as the script.
2. Run the script:

    ```bash
    python use_case_executor.py
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
