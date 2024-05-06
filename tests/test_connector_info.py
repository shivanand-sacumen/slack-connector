""" mock testing of user_list and conversation_list """
import pytest
import responses
from src import connector_info
# from config.connector_config import config_dict

@responses.activate
def test_conversation_list():
    """
    Test case for conversation_list 
        args :
            mocker : none
        returns :
            success msg 
    """

    data = {'ok':True,'channels':[{'id':'1234','name':'random'}]}
    responses.add('GET',url =f"https://abcd.com/books" ,json = data, status=200)
    BASE_URL = "https://abcd.com"
    END_POINT = '/books'
    API_KEY = '12345678'

    result = connector_info.conversation_list(BASE_URL,END_POINT,API_KEY)
    assert result == data


@responses.activate
def test_user_list():
    """
    Test case for user_list 
        args :
            mocker : none
        returns :
            success msg
    """
    data = {'ok':True,'members':[{'id':'1234','teamid':'Abcd123','name':'slackbot'}]}
    responses.add('GET',url =f"https://abcd.com/books" ,json = data, status=200)
    BASE_URL = "https://abcd.com"
    END_POINT = '/books'
    API_KEY = '12345678'

    result = connector_info.user_list(BASE_URL,END_POINT,API_KEY)
    assert result == data   



