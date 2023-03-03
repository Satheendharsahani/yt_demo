import os
import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
import googleapiclient.errors
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import httplib2

# Read the credentials from the environment variables
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
refresh_token = os.environ.get('REFRESH_TOKEN')

# Set up the Google API client
creds = google.oauth2.credentials.Credentials.from_authorized_user_info(info=None, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)
service = build('youtube', 'v3', credentials=creds)

# Define the video file to upload
video_file = 'video.mp4'

# Define the metadata for the video
request_body = {
    'snippet': {
        'title': 'My cool video',
        'description': 'Check out my cool video',
        'tags': ['cool', 'video']
    },
    'status': {
        'privacyStatus': 'public'
    }
}

# Upload the video file and metadata
try:
    # Upload the video file
    media = MediaFileUpload(video_file)
    video_response = service.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()

    # Print the response
    print('Video ID:', video_response['id'])

except googleapiclient.errors.HttpError as error:
    print(f'An error occurred: {error}')
    video_response = None

# Define the requirements file to upload
requirements_file = 'requirements.txt'

# Upload the requirements file
try:
    # Upload the requirements file
    media = MediaFileUpload(requirements_file)
    requirements_response = service.files().create(media_body=media, body={'name': requirements_file}).execute()

    # Print the response
    print('Requirements file ID:', requirements_response['id'])

except googleapiclient.errors.HttpError as error:
    print(f'An error occurred: {error}')
    requirements_response = None
