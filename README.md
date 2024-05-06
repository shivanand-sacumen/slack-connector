# Test Connector

connector created for training purpose 

# Functionalities 

- Fetch user list from Workspace
- Fetch channel list from workspace 

# Installations

### Packages 
```shell
pip install -r requirements.txt
```
# Configurations

### Logging Configurations

LOG_HANDLER = RotatingFileHandler
LOG_LEVEL = DEBUG
LOG_FILE_NAME = slack_connector.log

# Run unit test cases 

To run unittest cases `pytest` module is required 

To execute unit test cases for slack Connector, perform following steps:

1. Create a virtual environment
2. Enable virtual environment
3. Install required libraries from `requirements.txt`.
4. Execute `pytest`