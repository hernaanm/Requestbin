import json
import pytest
from pytest_lazyfixture import lazy_fixture
from fixtures.fixtures_api import *

from framework.basic_api import Basic_API


def test_create_bin_invalid_name(form_new_bin_invalid_name):
    api = Basic_API()
    response = api.create_bin(form_new_bin_invalid_name)

    assert response.status_code == 422
    assert response.json()["error"] == "Invalid bin name"


@pytest.mark.parametrize(
    "new_bin,webhook_payload,json_schema",
    [
        (
            lazy_fixture("create_bin"),
            lazy_fixture("payload_package_created"),
            "package_created_schema.json",
        ),
    ],
)
def test_package_created_succesfully(new_bin, json_schema, webhook_payload):

    """Create new bin"""
    api, bin_id = new_bin

    """Sending webhook to the bin created"""
    response = api.send_webhook_to_bin(bin_id, webhook_payload)
    assert response.status_code == 200

    """Retrieving all requests linked to that bin"""
    response = api.get_all_bin_requests(bin_id)
    assert response.status_code == 200

    """Retreiving request info -> validating schema and information"""
    for request in response.json():
        response = api.get_bin_request(bin_id, request["id"])
        assert response.status_code == 200
        api.validate_schema(json_schema)

        request_body = json.loads(response.json()["body"])

        assert request_body['data']['schedulePackage']['success'] == True
        assert request_body['data']['schedulePackage']['error'] == None
