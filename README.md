# API-Test
This Python script allows you to test APIs by sending HTTP requests, handling authentication using an API key, specifying custom headers, and printing the JSON response data from the API. It provides flexibility for different HTTP methods, making it suitable for various API testing scenarios.

1. Importing the necessary module:
The script begins by importing the requests library, which allows us to send HTTP requests and handle responses from APIs.

2. Defining the test_api function:
This function is responsible for testing the API and handling different HTTP methods (GET and POST). It takes the following parameters:

* endpoint_url: The URL of the API endpoint to test.
* http_method: The HTTP method to use for the request. The default is "GET".
* headers: Any additional headers to include in the request. It defaults to None.
* api_key: The API key used for authentication. It defaults to None.
* data: The JSON data to send with the POST request. It defaults to None.

3. Making the API request:
The function then tries to make an API request based on the provided http_method, headers, api_key, and data.

4. Handling GET and POST requests:
* If the http_method is "GET", the function sends a GET request with the specified headers and includes the API key as a query parameter in the URL.
* If the http_method is "POST", the function sends a POST request with the specified headers, includes the API key as a query parameter in the URL, and sends the data as JSON in the request body.

5. Processing the API response:
After sending the request, the function checks if the response is successful (non-empty). If so, it prints the status code, parses the JSON response, and prints the JSON data.

6. Returning JSON data:
The function returns the JSON data received from the API response if the request was successful. Otherwise, it returns None.

Example usage:
The script provides an example of how to use the test_api function. In the example, you need to replace the api_endpoint, api_key, request_headers, and request_data variables with appropriate values specific to your API.

Overall, the script is a reusable function to test APIs using different HTTP methods, handle authentication with an API key, and print the JSON data from the API response.
