# WhatsApp Automation

This script automates the process of sending messages on WhatsApp. It reads phone numbers and messages from a CSV file and sends each message to the corresponding phone number using WhatsApp Web.

## Requirements

- Python 3
- pywhatkit
- Chrome or Firefox browser

## Usage

1. Install the required Python libraries with `pip install -r requirements.txt`.
2. Download the appropriate WebDriver for your browser and add it to your system's PATH.
3. Run the script with `python app.py`.
4. The first time you run the script, you'll need to log into WhatsApp Web by scanning the QR code.

## CSV File Format
You have to create a CSV file for this 
The CSV file should have two columns. The first column should be the phone number (with country code), and the second column should be the message. The first row (header) of the CSV file is ignored.

## Limitations

- The script needs to be run on a machine where you can log into WhatsApp Web.
- The machine must not be locked, as the script automates keyboard and mouse actions.
- The script does not handle CAPTCHAs or other types of verification.