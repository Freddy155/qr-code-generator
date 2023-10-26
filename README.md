# Advanced QR Code Generator

## Project Description
This Python application allows users to generate QR codes for various types, including URLs, WiFi credentials, and vCard information. Users can input the required data, and the application will create and display the QR code on the screen. This README provides an overview of how to use the application and its dependencies.

## Installation
1. Clone the repository from GitHub: [GitHub Repository](https://github.com/Freddy155/qr-code-generator)
   ```bash
   git clone https://github.com/Freddy155/qr-code-generator.git
   ```
2. Create a virtual environment (recommended) to isolate the project dependencies:
   ```bash
   python -m venv venv &&
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install the project dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

Usage
-----

1.  Run the `app.py` script to start the application:
   ```bash
   python app.py
   ```

2.  Follow the on-screen prompts to choose the type of QR code and input the required information. The QR code will be generated and displayed on the screen.

Supported QR Code Types
-----------------------

-   URL: Encode a URL in a QR code.
-   WiFi: Encode WiFi credentials (SSID, password, security type) in a QR code.
-   vCard: Encode contact information (name, phone number, email) in a QR code.

Dependencies
------------

-   `qrcode` (v7.3)
-   `Pillow` (v8.3.1)

Contributing
------------

Contributions to the project are welcome. If you would like to contribute, please follow these steps:

1.  Fork the repository on GitHub.
2.  Clone the forked repository to your local machine.
3.  Create a new branch for your feature or bug fix.
4.  Make your changes and test them thoroughly.
5.  Commit your changes and push them to your fork on GitHub.
6.  Create a pull request to the original repository.