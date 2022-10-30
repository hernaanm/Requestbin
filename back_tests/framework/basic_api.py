import requests
import logging
import json
from jsonschema import validate

BASE_URL = "http://127.0.0.1:8000"
JSON_STORE_PATH = "back_tests/json_store/"

log = logging.getLogger("BASIC_API")


class Basic_API:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            log.info("Creating API object")
            cls._instance = super(Basic_API, cls).__new__(cls)
            # Initializing variables
            cls._instance.base_url = BASE_URL
            cls._instance.json_store = JSON_STORE_PATH
            cls._instance.response = None
        return cls._instance

    def validate_schema(self, schema):
        log.info(f'Validating schema against ${schema}')
        with open(f"{self.json_store}/{schema}", "r") as reference_file:
            validate(instance=self.response, schema=json.load(reference_file))

    def create_bin(self, form=None):
        url = self.base_url + "/api/v1/bins"

        log.info(f'Creating bin on with {form}')

        response = requests.post(url=url, data=form)
        return response

    def send_webhook_to_bin(self, bin_id, parameters=None):
        if parameters is None:
            parameters = {}

        url = self.base_url + "/" + bin_id

        log.info(f'Sending webhook to bin ${bin_id} with {parameters}')

        response = requests.post(url=url, json=parameters)
        return response

    def get_all_bin_requests(self, bin_id):

        url = self.base_url + "/api/v1/bins/" + bin_id + "/requests"

        log.info(f'Getting all requests attached to bin ${bin_id}')

        response = requests.get(url=url)
        return response

    def get_bin_request(self, bin_id, request_id):

        url = self.base_url + "/api/v1/bins/" + bin_id + "/requests/" + request_id

        log.info(f'Getting requestes ${request_id} attached to bin ${bin_id}')

        response = requests.get(url=url)
        self.response = json.loads(response.json()["body"])
        return response
