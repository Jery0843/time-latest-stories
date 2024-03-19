# Time-latest-stories

This project contains a simple web server written in Python that fetches and serves the latest stories from TIME.com.

## Features

- Fetches the latest stories from TIME.com using a GET request.
- Parses the HTML content to extract story titles and links.
- Serves the extracted stories as a JSON response.

## Requirements

- Python 3
- `re` module for regular expressions
- `json` module for JSON manipulation
- `http.server` module for HTTP server functionality
- `urllib.request` module for URL handling

## Usage

1. Run the server script:
   ```shell
   python3 server.py

2. Access the latest stories in JSON format:
   ```shell
   curl http://localhost:8000/latest-stories

