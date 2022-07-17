import pytest

from inventory import inventory_add
from error import InputError
import requests
from config import url

# no id
def test_no_id(clear_data):    
    with pytest.raises(InputError):
        inventory_add(None, "Vikram", "valid", "valid")

# no name
def test_no_name(clear_data):    
    with pytest.raises(InputError):
        inventory_add(1, None, "valid", "valid")

# no description
def test_no_des(clear_data):    
    with pytest.raises(InputError):
        inventory_add(1, "Vikram", None, "valid")

# no note
def test_no_note(clear_data):    
    with pytest.raises(InputError):
        inventory_add(1, "Vikram", "valid", None)

def test_http_valid(clear_data):
    payload_inventory = {
        "id": 1,
        "name": "Vikram",
        "description": "valid",
        "note": "valid"
    }
    response_user = requests.post(
        f"{url}/inventory", json=payload_register_user)
    response_user_data = response_user.json()

    payload_create_channel = {
        "token": response_user_data.get('token'),
        "name": "coolkidsclub",
        "is_public": True
    }
    response_channel = requests.post(
        f"{url}channels/create/v2", json=payload_create_channel)
    response_channel_data = response_channel.json()
    
    assert response_user_data.get('name') == "Vikram"