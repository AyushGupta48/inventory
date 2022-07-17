from data_store import data_store
from error import InputError, AccessError
import re
import smtplib



def inventory_add(id, name, description, note):
    '''
    Auth_login_v2 takes in a user's email and their password and returns their user id.

    Arguments:
        email    (string)   - The email of the user
        password (string)   - The password of the user

    Exceptions:
        InputError  -   Occurs when email address is not registered
                    -   Occurs when no email is passed in
                    -   Occurs when password does not match
                    -   Occurs when password is not passed in

    Return Value:
        Returns {'token': token, 'auth_user_id': store['user_emails'].index(email) + 1} on completion of the function.
        The value "store['user_emails'].index(email) + 1" will find the index of the user's email and add 1
        since the user_ids start from 1. Token is a unique JWT.
    '''
    store = data_store.get()


    # Email checks
    if id == None:
        raise InputError(description="Invalid id: no id given")
    
    if name == None:
        raise InputError(description="Invalid name: no name given")
    
    if description == None:
        raise InputError(description="Invalid description: no description given")
    
    if note == None:
        raise InputError(description="Invalid note: no note given")



    store['id'][id].append(id)
    store['name'][id].append(name)
    store['description'][id].append(description)
    store['note'][id].append(note)

    data_store.set(store)

    return {
    }
