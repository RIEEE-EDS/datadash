import flask
import components.utils.sqlconnection as dataserver

# INTERFACING WITH SHIBBOLETH SINGLE SIGN-ON AUTHENTICATION
#
# THIS IS USED ONLY IN A REQUESTS CONTEXT.

def userAuthentication():

    # If there is no request context, ignore and return out
    if not flask.has_request_context():
        return None

    # If Remote-User is available in the header 
    if 'Uid' in flask.request.headers:
        
        # Get the username
        UID = flask.request.headers['Uid']

        return [True, UID, dataserver.get_user_role(UID)]
    
    else :

        return [False, None, None]

