from fastapi.testclient import TestClient
import main
client = TestClient(main.app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Home": "Creado"}

# def test_restaurants():
#     response = client.get("/restaurants")
#     assert response.status_code == 200
    
