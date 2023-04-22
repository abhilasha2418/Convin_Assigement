from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow


CLIENT_SECRETS_FILE = '/home/katniss/convin/GcalenderIntegration/app/credentials.json'

# Define redirect URI for OAuth2
REDIRECT_URI = 'http://localhost:3000/rest/v1/calendar/redirect/'



class GoogleCalendarInitView(APIView):
    """
    View to start step 1 of OAuth2 process to get user's calendar access.
    """

    def get(self, request):
        # Flow object to handle OAuth2 flow
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=['https://www.googleapis.com/auth/calendar.events.readonly'],
            redirect_uri=REDIRECT_URI
        )


        # Generate the authorization URL and redirect user to Google authorization URL
        authorization_url, _ = flow.authorization_url(prompt='consent')
        return redirect(authorization_url)
       


class GoogleCalendarRedirectView(APIView):
    """
    View to handle redirect request from Google with code for token and get list of events in user's calendar.
    """

    def get(self, request):
        # Get the authorization code from the redirect URL
        code = request.GET.get('code')

        # Create a Flow object to handle OAuth2 flow
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=['https://www.googleapis.com/auth/calendar.events.readonly'],
            redirect_uri=REDIRECT_URI
        )

        # Exchange the authorization code for access token
        flow.fetch_token(code=code)
        credentials = flow.credentials

        # Build the Google Calendar API service
        service = build('calendar', 'v3', credentials=credentials)

        # Get list of events from user's primary calendar
        events = service.events().list(calendarId='primary', timeMin='2023-01-01T00:00:00Z', timeMax='2023-12-31T23:59:59Z').execute()

        # Return the list of events in the response
        return Response(events)