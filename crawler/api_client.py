import json

import requests
from requests.exceptions import ConnectionError


def try_connection(access):
    def wrapper(*args, **kwargs):
        try:
            return access(*args, **kwargs)
        except ConnectionError as conn_error:
            return (
                conn_error.request.text,
                conn_error.request.status_code,
            )

    return wrapper


class APIClient:
    headers = {"content-type": "application/json"}

    def __init__(self, connection_class, conn_timeout=60):
        self.connection_class = connection_class
        self.conn_timeout = conn_timeout

    @try_connection
    def http_request(self, url, method_http, request_data={}):
        response_data = requests.request(
            method=method_http,
            url=url,
            data=json.dumps(request_data),
            headers=self.headers,
            timeout=self.conn_timeout,
        )

        return response_data.json()
