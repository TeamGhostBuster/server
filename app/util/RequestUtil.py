from flask import request
from app.config import *
from app.util.MongoUtil import *
from app import app
import requests


def get_auth_info():
    """
    Get user's identity

    Verify the interity of token from the OAuth provider,
    then look up the database check if user exist or not.
    If the user does not exist, create a new user instead.

    :return: user instance
    """
    if 'Access-Token' not in request.headers:
        return None

    access_token = request.headers['Access-Token']
    if access_token is not None:
        # Check that the Access Token is valid.
        url = ('https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=%s'
               % access_token)
        result = requests.get(url).json()
        if result.get('error_description') is not None:
            return None
        elif result['aud'] != BaseConfig.CONFIG['google']['client_key']:
            return None

    user = find_user(result['email'])
    if user is None:
        # if user does not exist, create a new user instead
        app.logger.info('Create User: {}'.format(user))
        user = create_user(result['email'])

    return user
