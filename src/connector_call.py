""" calling the function user_list and conversation_list"""

from src import connector_info
from configparser import ConfigParser


def start():
    """
    args: none
    returns : response 
    """
    config = ConfigParser()
    config.read('config/connector_config.cfg')

    BASE_URL = config['baseUrl']['base_url']
    CONVERSATIONLIST_ENDPOINT = config['endpoints']['converstion_list']
    USERLIST_ENDPOINT = config['endpoints']['user_list']
    API_KEY = config['credentials']['api_key']

    connector_info.conversation_list(BASE_URL,CONVERSATIONLIST_ENDPOINT,API_KEY)
    connector_info.user_list(BASE_URL,USERLIST_ENDPOINT,API_KEY)


