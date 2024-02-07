# AntiVirus for Flash Drive

## Overview

This Python-based AntiVirus for Flash Drives is a lightweight yet effective tool designed to enhance the security of flash drives by scanning for and removing potential threats.
The project uses platform-specific methods to detect flash drives and provides a simple user interface for scanning and handling threats.

## Features

- Cross-platform support (Windows and Linux).
- Automatic detection of connected flash drives.
- Scan flash drives for potential threats such as executable files and suspicious endings.
- Integration with VirusTotal for additional threat analysis.
- User-friendly menu interface for managing and removing threats.

## Usage

1. Clone the repository to your local machine:

2. Navigate to the av directory and run pip install -r requirements.txt in the terminal (installs requests module).

3. Run the Anti-Virus by using:
   - Windows: python av OR python __main__.py (depends on whether you are in the project directory or one layer above it).
   - Linux: python3 av OR python3 __main__.py (depends on whether you are in the project directory or one layer above it).

4. Follow on-screen instructions to scan and manage threats.

## Prerequisites
- Python 3.x installed on your system.

## Project Structure
- __main__.py: Entry point for the antivirus application.
- antivirus.py: Core implementation of the antivirus logic.
- ui.py: User interface module for popups and menu display.
- utils.py: Utility module containing the scanner and drive classes.
- virustotalhandler.py: Integration with VirusTotal for additional threat analysis.

## Contributing
If you would like to contribute to the development of this antivirus tool, feel free to fork the repository, make your changes, and submit a pull request.

## Note: Ensure you have proper permissions to access and modify files on your system and that you understand the potential risks associated with scanning and removing files.
