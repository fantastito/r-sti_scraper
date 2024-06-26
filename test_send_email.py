import unittest
from unittest.mock import patch, Mock
from lambda_function import send_email

class TestSendEmail(unittest.TestCase):

    @patch('lambda_function.boto3.client')
    def test_send_email_success(self, mock_boto_client):
        # Mock the SES client and its send_email method
        mock_client = Mock()
        mock_boto_client.return_value = mock_client
        mock_client.send_email.return_value = {'MessageId': '12345'}

        # Call send_email function
        send_email("Test Subject", "Test Body")

        # Assert that send_email method was called with the correct parameters
        mock_client.send_email.assert_called_once_with(
            Source='simon.budden@gmail.com',
            Destination={'ToAddresses': ['simon.budden@gmail.com']},
            Message={
                'Subject': {'Data': 'Test Subject'},
                'Body': {'Html': {'Data': 'Test Body'}}
            }
        )

    #Unhappy - email fails
if __name__ == '__main__':
    unittest.main()
