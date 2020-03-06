import pytest
import bottleapp
from webtest import TestApp

@pytest.fixture
def webapp():
    return TestApp(bottleapp.app)

def test_index(webapp):
    response = webapp.get('/', expect_errors=True)
    assert response.status == '200 OK'
    assert response.html.get_text() == 'Hello'

def test_create(webapp):
    response = webapp.get('/create/1001001', expect_errors=True)
    assert response.status == '200 OK'
    assert response.json['_id'] == '1001001'

def test_view(webapp):
    response = webapp.get('/view/1001001', expect_errors=True)
    assert response.status == '200 OK'
    assert response.json['_id'] == '1001001'

