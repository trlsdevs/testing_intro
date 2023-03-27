# contents of conftest.py
import pytest
import requests


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def mock_post(*args, **kwargs):
    return MockResponse()


@pytest.fixture(autouse=True)
def custom_requests(monkeypatch):
    monkeypatch.setattr(requests, "post", mock_post)
