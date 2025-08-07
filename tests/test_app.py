import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        TimelinePost.delete().execute()  # Clear the database before each test


    def tearDown(self):
        TimelinePost.delete().execute()  # Clear the database after each test

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('<h1>Armando Mac Beath</h1>', html)
        self.assertIn('<h1>Fiona Laygo</h1>', html)
    
    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        self.assertEqual(response.status_code, 200)
        assert response.is_json
        json = response.get_json()
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 0

        request = self.client.post('/api/timeline_post', data={
            'name': 'John Doe',
            'email': 'john21@gmail.com',
            'content': 'Hello World!'
        })
        self.assertEqual(request.status_code, 200)
        post_json = request.get_json()
        self.assertEqual(post_json['name'], 'John Doe')
        self.assertEqual(post_json['email'], 'john21@gmail.com')
        self.assertEqual(post_json['content'], 'Hello World!')

    def test_malformed_timeline_post(self):
        response = self.client.post('/api/timeline_post', data=
        { 'name': '', 'email': 'john@example.com', 'content': "Hello World, I'm john!" })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid name' in html

        response = self.client.post('/api/timeline_post', data=
        { 'email': 'john@example.com', 'name': "John Doe", 'content': '' })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid content' in html

        response = self.client.post('/api/timeline_post', data=
        { 'email': 'notanemail', 'content': "Hello World, I'm john!", 'name': 'John Doe' })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert 'Invalid email' in html