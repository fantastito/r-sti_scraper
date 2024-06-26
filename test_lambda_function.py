import unittest
from unittest.mock import patch, Mock
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    
    #Happy path
    @patch('lambda_function.requests.get')
    @patch('lambda_function.send_email')
    def test_lambda_handler_alpen_fest(self, mock_send_email, mock_requests_get):
        # Mocking the requests.get method
        mock_response = Mock()
        mock_response.status_code = 200
        mock_html_content = """
        <html>
            <body>
                <div title="This Week's Offers">
                    <h3>Flavour of the Week: Alpen Fest</h3>
                </div>
            </body>
        </html>
        """
        mock_response.content = mock_html_content.encode('utf-8')
        mock_requests_get.return_value = mock_response
        
        # Call lambda_handler
        lambda_handler({}, {})
        
        # Assert that send_email was called with the correct parameters
        mock_send_email.assert_called_once_with(
            "Get ready for rösti",
            "It looks like it is Alpen Fest week at Lidl. Go grab some rösti"
        )

    #Unhappy - not Alpen Fest
    @patch('lambda_function.requests.get')
    @patch('lambda_function.send_email')
    def test_lambda_handler_no_alpen_fest(self, mock_send_email, mock_requests_get):
        # Mocking the requests.get method
        mock_response = Mock()
        mock_response.status_code = 200
        mock_html_content = """
        <html>
            <body>
                <div title="This Week's Offers">
                    <h3>Flavour of the Week: Sol Y Mar</h3>
                </div>
            </body>
        </html>
        """
        mock_response.content = mock_html_content.encode('utf-8')
        mock_requests_get.return_value = mock_response
        
        # Call lambda_handler
        lambda_handler({}, {})
        
        # Assert that send_email was called with the correct parameters
        mock_send_email.assert_called_once_with(
            "No rösti this week",
            "No rösti in Lidl this week, you'll have to cook something else"
        )
    
    #Unhappy - Flavour of week not found
    @patch('lambda_function.requests.get')
    @patch('lambda_function.send_email')
    def test_lambda_handler_no_flavour_of_week(self, mock_send_email, mock_requests_get):
        # Mocking the requests.get method
        mock_response = Mock()
        mock_response.status_code = 200
        mock_html_content = """
        <html>
            <body>
                <div title="This Week's Offers">
                    <h3>This is pick of the week</h3>
                </div>
            </body>
        </html>
        """
        mock_response.content = mock_html_content.encode('utf-8')
        mock_requests_get.return_value = mock_response
        
        # Call lambda_handler
        lambda_handler({}, {})
        
        # Assert that send_email was called with the correct parameters
        mock_send_email.assert_called_once_with(
            "No Flavour of the Week",
            "Unable to find 'Flavour of the Week' in Lidl offers this week"
        )

    #Unhappy - Offers section not found
    #Unhappy - Unexpected status code
    #Unhappy - General request exceptions
    #Unhappy - Any unexpected exceptions

if __name__ == '__main__':
    unittest.main()
