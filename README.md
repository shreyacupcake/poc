# Tool Execution Framework

This repository contains a Python script to execute security-based use cases defined in a JSON knowledge base. The script reads the knowledge base, prompts the user to select a use case, and calls the relevant tools associated with the selected use case.

## Features

- Reads a JSON file containing use cases.
- Prompts the user to select and execute a use case.
- Calls tools associated with the use case, requiring user input for arguments.

## Usage

1. Place your knowledge base JSON file (e.g., `kb.json`) in the same directory as the script.
2. Run the script:

    ```bash
    python POC.py
    ```

3. When prompted, enter the name of the security-based use case you want to execute.
4. Provide values for the required arguments when prompted.

## Example

Assuming the `kb.json` file contains the following data:

```json
{
    "use_cases": [
        {
            "name": "Example Use Case",
            "description": "This is an example use case.",
            "tools": [
                {
                    "toolname": "example_tool",
                    "commands": "example_command",
                    "arguments": ["arg1", "arg2"]
                }
            ]
        }
    ]
}
