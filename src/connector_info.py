""" functions to fetch data from the userlist and Conversation list"""

import requests
import json
import logging
logging.basicConfig(filename='slack_connector.log',level=logging.DEBUG, filemode='w')


def conversation_list(base_url:str, end_point:str, apikey:str) ->json :
    """get all conversation list.
        args :
            base_url, endpoint, apikey.
        return : 
            response
    """
    headers = {
        'Authorization': apikey,
    }
    URL = base_url+end_point
    response = requests.get(url=URL,headers=headers)
    logging.debug(response.text)
    return response.json()



def user_list(base_url:str, end_point:str, apikey:str) ->json :
    """ Get all user list. 
        args : 
            base_url, end_point, apikey.
        return : 
            response.
    """
    headers = {
        'Authorization':apikey
    }
    response = requests.get(f"{base_url}{end_point}",headers=headers)
    logging.debug(response.text)
    return response.json()


