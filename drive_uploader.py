from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
import pickle
import os

class Uploader:
    """
    Implemenation of Google Drive API V3 used to upload created .csv 
    file to specific Google Drive account
    
    """
    
    #Base address to access Drive API
    SCOPE = ['https://www.googleapis.com/auth/drive']
    
    def credentialVerification(self):
        """Prompt user to verify access to Google Drive account before upload
        
        Return
        ------
        service : Resource
            Object to allowe user to interact with Google Drive upload feature
            
        """
        creds = None
        
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        #Create credential if on has not been created
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPE)
            creds = flow.run_local_server(port=0)
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
            
        service = build('drive', 'v3', credentials=creds)

        return service

    # Uploads the csv file to google sheets
    def upload(self, service, file_name, file_path):
        """Uploads the .csv file at file_path to Google Drive
        
        Parameters
        ----------
        service: Resource
            Object to allowe user to interact with Google Drive upload feature
        file_name : str
            Name to set file to in Google Drive
        file_path : str
            Local path to .csv file
            
        """
        
        file_metadata = {'name': file_name}  #Build metadata for Google Drive to track
        
        #Locate and upload the corresponding csv file at file_path
        media = MediaFileUpload( file_path,
                                mimetype='text/csv')
        file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

        print('File ID: %s' % file.get('id'))


    