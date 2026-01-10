
from fastapi.testclient import TestClient
from api.main import app

testcli = TestClient(app)

def test_health():
    response = testcli.get("/")
    print(response)
    assert response.status_code == 200
    assert response.json() == {"status": "Healthy"}

def test_db_fetch():
    response = testcli.get("/dbtables")
    print(response)
    assert response.status_code == 200
    assert response.json() == {"tables": ["users", "books"]}

def test_faulty_fetch():
    response = testcli.get("/dbtables")
    print(response)
    assert response.status_code == 200
    assert response.json() != {"tables": []}
