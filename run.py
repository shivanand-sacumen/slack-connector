"""start the slack connector"""
from src.connector_call import start

try:
    start()
except Exception as e:
    raise e