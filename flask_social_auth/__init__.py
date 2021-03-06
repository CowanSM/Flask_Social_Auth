from flask import Flask
from oauth import OAuth
from os import environ

# Create application object
app = Flask(__name__)
app.config.from_object('flask_social_auth.default')
app.config.from_envvar('APPLICATION_SETTINGS', silent=True)

oauth = OAuth()
if app.config.get('DEBUG') == True:
    fb_key = environ.get('FACEBOOK_LOCAL_APP_ID')
    fb_secret = environ.get('FACEBOOK_LOCAL_APP_SECRET')
else:
    fb_secret = environ.get('FACEBOOK_APP_SECRET')
    fb_key = environ.get('FACEBOOK_APP_ID')
    
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=fb_key,
    consumer_secret=fb_secret,
    request_token_params={'scope': 'email'}
)
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=environ.get('TWITTER_CONSUMER_KEY'),
    consumer_secret=environ.get('TWITTER_CONSUMER_SECRET')
)
google = oauth.remote_app('google',
    base_url=None,
    request_token_url=None, #this should only exist for OAuth1.0
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    consumer_key=environ.get('GOOGLE_CLIENT_ID'),
    consumer_secret=environ.get('GOOGLE_CLIENT_SECRET'),
    access_token_method='POST',
    request_token_params={'response_type':'code','scope':'https://www.googleapis.com/auth/userinfo.email','grant_type':'authorization_code'}
)

# Import everything
import flask_social_auth.views
