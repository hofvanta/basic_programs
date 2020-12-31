import requests
import json


def get_token():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"

    payload = {"username": "devnetuser",
               "password": "Cisco123!"}
    headers = {
        'content-type': 'application/json',
    }

    r = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
    token = r["response"]["serviceTicket"]
    return token


def get_network_config(token):
    url = "https://sandboxapicem.cisco.com/api/v1/network-device/config"

    headers = {
        'X-AUTH-TOKEN': token
    }

    response = requests.request("GET", url, headers=headers).json()

    return response


def main():
    token = get_token()
    network_config = get_network_config(token)
    print(network_config)


if __name__ == "__main__":
    main()