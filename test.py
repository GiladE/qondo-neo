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

# Posting a csv containing tweets (unique-id,tweet-body) to /api/tweets should return http 201

# Posting a csv containing tweets (unique-id,tweet-body) to /api/tweets should create tweets in the db

# Posting a csv containing tweets (unique-id,tweet-body) to /api/tweets should not create duplicates

# Making a get request to /api/tweets should return http 200

# Making a get request to /api/tweets should return an unanswered sentiment

# Posting to /api/answers/<tweet-id> with a correct tweet-id should return 201

# Posting to /api/answers/<tweet-id> with a correct tweet-id should return next sentiment to be answered

if __name__ == '__main__':
  unittest.main()
