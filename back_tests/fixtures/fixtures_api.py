import pytest

from framework.basic_api import Basic_API


@pytest.fixture
def form_new_bin_invalid_name():
    form = dict(name="invalid")
    return form


@pytest.fixture
def form_new_bin():
    form = dict(name="Test1237")
    return form


@pytest.fixture
def create_bin(form_new_bin):
    api = Basic_API()
    resp = api.create_bin(form_new_bin)
    response = resp.json()

    bin_key = response["name"]

    yield api, bin_key

    # api.delete_bin(bin_key)


@pytest.fixture
def payload_package_created():
    payload = {
        "data": {
            "schedulePackage": {
                "success": True,
                "error": None,
                "package": {
                    "id": "12345",
                    "deliveries": [
                        {
                            "tasks": [
                                {
                                    "type": "PICKUP",
                                    "address": {
                                        "geocoded": "Carrer de Pau Claris 130, 08009, Barcelona, Spain",
                                        "location": {
                                            "lat": "41.39317",
                                            "long": "2.16699"
                                        }
                                    }
                                },
                                {
                                    "type": "DROPOFF",
                                    "address": {
                                        "geocoded": "Carrer de Pau Claris 170, 08037, Barcelona, Spain",
                                        "location": {
                                            "lat": "41.39546",
                                            "long": "2.16385"
                                        }
                                    }
                                }
                            ]
                        }
                    ],
                    "status": "NOT_ASSIGNED",
                    "createdAt": "2022-03-23T15:06:09+01:00",
                    "ref": "67890"
                }
            }
        }
    }
    return payload
