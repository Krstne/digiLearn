import datetime
import pickle
import os
from Auth import AuthenticationManager
from digipackDB import DatabaseManager as dbm
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials




def create_service(user_auth, api_name, api_version, *scopes, user_email):
    _scopes = [scope for scope in scopes[0]]
    
    cred = None
    filePathFlag = False

    #instantiate AuthenticationManager object with path to local client secrets
    am = AuthenticationManager.AuthenticationManager(user_auth)
    
    print("create_service says user_email is " + user_email)
    
    #request user credentials from email
    cred = dbm.getCredentials( user_email )
    
    #check for credentials recieved
    if( cred == 0 ):
        print("Unable to retrieve credentials.")
        return None
    
    #convert cred JSON string to Oauth2 credentials object
    cred = am.getCredentialsFromFileOrString( filePathFlag, fileString=cred )
    

    try:
        service = build(api_name, api_version, credentials=cred)
        return service
    # this needs to be an actual exception, not a "catch all here"
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt
