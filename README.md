
# Google Calendar Integration with Django REST API

This is a Django REST API project that implements Google Calendar integration using OAuth2 mechanism to get users calendar access. Below are details of API endpoints and corresponding views that have been implemented.




## API Endpoints and Views


```
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
```

This view starts step 1 of the OAuth. It prompts the user for his/her credentials.

```
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
```

This view does two things:

It handles redirect request sent by Google with code for token. You need to implement the mechanism to get the access_token from the given code.

Once the access_token is obtained, it gets the list of events in the user's calendar.



## Technologies Used

* Django
* Django REST Framework
* Google APIs


## Installation and Setup

To use this project, you need to clone the repository to your local machine and install the required dependencies. You can do this by running the following commands:

```
git clone https://github.com/<username>/<repository>.git
cd <repository>
pip install -r requirements.txt
```

Once you have installed the dependencies, you can run the Django server using the following command:

```
python manage.py runserver
```

You can then access the API endpoints using the URL http://localhost:8000/rest/v1/calendar/


## Dependencies

This project requires the following dependencies:

* Django
* Django REST framework
* google-auth
* google-auth-oauthlib
* google-auth-httplib2
* google-api-python-client

You can install these dependencies using pip. A requirements.txt file is included in the repository.


## Contributors

- Abhilasha  
abhilashapimpalgaonkar18@gmail.com

