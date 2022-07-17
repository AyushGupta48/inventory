from re import A
import sys
import signal
from json import dumps
from _pytest.python_api import ApproxBase
from flask import Flask, request
import requests
from flask_cors import CORS
import threading
import time
import config
from config import url
from data_store import data_store
from inventory import inventory_add

def quit_gracefully(*args):
    '''For coverage'''
    exit(0)


def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)


# Example
# @APP.route("/echo", methods=['GET'])
# def echo():
#     data = request.args.get('data')
#     if data == 'echo':
#    	    raise InputError(description='Cannot echo "echo"')
#     return dumps({
#         'data': data
#     })


@APP.route("/inventory", methods=['POST'])
def update_inventory():
    request_data = request.get_json()
    return dumps(inventory_add(
        request_data["id"],
        request_data["name"],
        request_data["description"],
        request_data["note"]
        )
        )

if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit_gracefully)  # For coverage
    APP.run(port=config.port)  # Do not edit this port