from webtest import TestApp
import bottleapp

def test_bottleapp_view():
    app = TestApp(bottleapp.app)
    response = app.get('/view/1001001')
    assert response.status == '200 OK'
    assert response.json['_id'] == '1001001'

