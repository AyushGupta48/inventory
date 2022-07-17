import jwt
import hashlib
import requests
from config import url
import smtplib
import os

# Clears all lists in the data store


def clear_v1():
    store = data_store.get()
    store['id'] = []
    store['name'] = []
    store['description'] = []
    store['note'] = []
