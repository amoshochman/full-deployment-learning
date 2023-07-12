from main import app
from unittest.mock import patch

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8').find("<!DOCTYPE html>") == 0

