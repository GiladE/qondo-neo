from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

# Visiting / should return http 200
  def test_web_get_index_200(self):
    tester = app.test_client(self)
    response = tester.get('/')
    self.assertEqual(response.status_code, 200)

# Visiting /api should return http 200
  def test_api_get_index_200(self):
    tester = app.test_client(self)
    response = tester.get('/api/')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()
