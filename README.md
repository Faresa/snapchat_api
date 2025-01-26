# Snapchat Ads Automation

This repository contains a Python script for automating the management of Snapchat Ads campaigns by pausing those with a Return on Ad Spend (ROAS) below a threshold of £1 over the past 30 days. Configuration is done via console input for ease of use.

## Overview

- **Fetch**: Retrieve performance data for campaigns from the last 30 days.
- **Analyze**: Calculate ROAS for each campaign.
- **Act**: Pause campaigns that do not meet the ROAS threshold.

## Prerequisites

- **Python 3.8+**
- Access to the [Snapchat Marketing API](https://developers.snap.com/api/marketing-api/Ads-API/introduction)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Faresa/snapchat_api
   cd snapchat_api
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```bash
python main.py
```

When you run the script, you'll be prompted to enter:

- Your Snapchat Ads API Access Token
- Your Snapchat Account ID

**Note**: The script will not accept empty inputs, so you must provide valid information for each prompt. Once entered, the script will:

- Fetch campaign data
- Calculate ROAS
- Pause underperforming campaigns

## Code Structure

- `main.py`: Coordinates the execution of the automation script, now with console input for configuration.
- `snapchat_api.py`: Handles all interactions with the Snapchat API.
- `campaign_management.py`: Contains the logic to decide and act on campaign performance.
- `utils.py`: Utility functions for date manipulation and ROAS calculation.
- `tests/`: Contains tests for the modules.
- `requirements.txt`: Lists the Python packages required.

## Testing

To run the tests:

```bash
pytest tests/
```

## Notes

- **Error Handling**: Basic error handling is in place for console inputs and API calls. For production, consider more robust error management.
- **Security**: While using console input for credentials, be aware that this method is less secure as credentials will be visible in the console. For production, consider more secure methods like environment variables or configuration files.
- **API Stability**: This code is built on current API specifications; updates to the API might require code changes.

## License

This project is licensed under the MIT License

## Acknowledgments

- **Snapchat** for their API which this project is built upon.
- **Open-source community** for tools like `requests` and `pytest`.
