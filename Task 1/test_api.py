import unittest
import requests

class TestAPIResponse(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """ Setup before all tests, executes the request once """
        cls.url = 'https://jsonplaceholder.typicode.com/posts/1'
        cls.invalid_url = 'https://jsonplaceholder.typicode.com/posts/invalid'  # URL to test errors
        try:
            cls.response = requests.get(cls.url)
            cls.response.raise_for_status()  # Checks for HTTP errors
            cls.response_data = cls.response.json()
        except requests.exceptions.RequestException as e:
            cls.fail(f"Failed to connect to {cls.url}: {e}")
        except ValueError:
            cls.fail(f"Response is not valid JSON")

    def test_status_code(self):
        """ Verifies that the HTTP status code is 200 """
        self.assertEqual(self.response.status_code, 200, "Expected status code 200 but got a different response")

    def test_response_time(self):
        """ Verifies that the response time is less than 1000 ms """
        self.assertLess(self.response.elapsed.total_seconds() * 1000, 1000, "Response time exceeds 300 ms")

    def test_required_fields(self):
        """ Verifies that the required fields are present in the JSON response """
        required_fields = ['userId', 'id', 'title', 'body']
        for field in required_fields:
            with self.subTest(field=field):
                self.assertIn(field, self.response_data, f"'{field}' is missing in the response")

    def test_field_types(self):
        """ Verifies that the fields have the correct data type """
        self.assertIsInstance(self.response_data.get('userId'), int, "userId should be an integer")
        self.assertIsInstance(self.response_data.get('id'), int, "id should be an integer")
        self.assertIsInstance(self.response_data.get('title'), str, "title should be a string")
        self.assertIsInstance(self.response_data.get('body'), str, "body should be a string")

    def test_non_empty_strings(self):
        """ Verifies that the string fields are not empty """
        self.assertGreater(len(self.response_data.get('title')), 0, "Title should not be empty")
        self.assertGreater(len(self.response_data.get('body')), 0, "Body should not be empty")

    def test_non_negative_integers(self):
        """ Verifies that the userId and id fields are non-negative integers """
        self.assertGreaterEqual(self.response_data.get('userId'), 0, "userId should not be negative")
        self.assertGreaterEqual(self.response_data.get('id'), 0, "id should not be negative")

    def test_error_handling_404(self):
        """ Verifies error handling for a 404 (not found) """
        response = requests.get(self.invalid_url)
        self.assertEqual(response.status_code, 404, "Expected status code 404 for invalid URL")
    
    def test_boundary_condition_min_id(self):
        """ Verifies a boundary condition: minimum valid id """
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        data = response.json()
        self.assertGreaterEqual(data['id'], 1, "ID should be greater than or equal to 1")

    @classmethod
    def tearDownClass(cls):
        """ Cleanup after all tests have finished """
        pass

if __name__ == '__main__':
    unittest.main()
