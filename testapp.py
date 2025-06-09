from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data

    









