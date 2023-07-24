import unittest
import requests

class TestEmailService(unittest.TestCase):

    def test_create_email_api(self):
        url = 'http://localhost:5000/emails'
        data = {
            'event_id': 1,
            'email_subject': 'PyCon Indonesia 2023 - Bandung',
            'email_content': 'Hi Everyone PyCon Indonesia Is Here 🔥 Register Now 🤙 ',
            'email_send_at': '2023-07-31 12:00',
        }

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(response_data['code'], 200)
        self.assertEqual(response_data['message'], 'Email saved and scheduled successfully')
        self.assertIn('result', response_data)

        email_id = response_data['result']
        self.assertIsInstance(email_id, int)


    def test_create_email_api_bad_request(self):
        url = 'http://localhost:5000/emails'
        data = {
            'event_id': 1,
            'email_subject': 'Test Subject',
            'email_content': 'Test Content',
            'email_send_at': '2023-07-31 12:00:00:00',  # Invalid format with extra ':00'
        }

        response = requests.post(url, json=data)
        response_data = response.json()

        self.assertEqual(response_data['code'], 400)
        self.assertIsInstance(response_data['message'], dict)
        self.assertIsNone(response_data['result'])


    def test_get_email_list_api(self):
        url = 'http://localhost:5000/emails'
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(response_data['code'], 200)
        self.assertEqual(response_data['message'], 'OK')
        self.assertIn('result', response_data)

        email_list = response_data['result']
        self.assertIsInstance(email_list, list)

        if email_list:
            first_email = email_list[0]
            expected_keys = [
                'event_id',
                'email_subject',
                'email_content',
                'email_send_at',
                'email_sent_at',
                'created_at'
            ]
            for key in expected_keys:
                self.assertIn(key, first_email)

            self.assertIsInstance(first_email['event_id'], int)
            self.assertIsInstance(first_email['email_subject'], str)
            self.assertIsInstance(first_email['email_content'], str)
            self.assertIsInstance(first_email['email_send_at'], str)


if __name__ == '__main__':
    unittest.main()
