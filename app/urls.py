from django.urls import path
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('calendar/init/', GoogleCalendarInitView.as_view()),
    path('calendar/redirect/', GoogleCalendarRedirectView.as_view()),
]