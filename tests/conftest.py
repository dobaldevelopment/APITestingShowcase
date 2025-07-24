# API Testing Showcase

## Instalación

```sh
pip install -r requirements.txt
```

## Ejecutar tests

```sh
pytest tests/
```

import pytest
import requests
from src.api_client import get_data

@pytest.fixture
def mock_jwt_token():
    # Este token es simulado, no tiene firma real
    return "eyFakeAdriToken.12345.payload.fakeSignature"

def test_get_data_success(mock_jwt_token):
    response = get_data(token=mock_jwt_token)
    assert response is not None
    assert response.status_code == 200
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data
