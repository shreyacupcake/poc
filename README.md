# Tool Execution Framework

This project provides a framework for executing security-based use cases defined in a JSON knowledge base. The framework supports the dynamic invocation of tools with user-provided arguments.

## Features

- Load and Print Employee Details: Reads and prints employee details from a JSON file.
- Tool Execution Framework:
- call_tool Function: Simulates calling a tool with a given command and arguments.
- execute_use_case Function:
- Searches for a use case by name provided by the user.
- Prints the use case's name and description if found.
- Calls each tool specified in the use case, prompting the user for required arguments.
- Prints an error message if the use case is not found.
