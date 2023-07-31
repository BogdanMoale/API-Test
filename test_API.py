import requests

def test_api(endpoint_url, http_method="GET", headers=None, api_key=None, data=None):
    try:
        response = None
        if http_method == "GET":
            response = requests.get(endpoint_url, headers=headers, params={"api_key": api_key})
        elif http_method == "POST":
            response = requests.post(endpoint_url, headers=headers, params={"api_key": api_key}, json=data)
        # Add support for other HTTP methods like PUT, DELETE, etc. as needed.

        if response:
            print(f"API Test using {http_method} method for URL: {endpoint_url}")
            print(f"Response Status Code: {response.status_code}")
            json_data = response.json()
            print("Response Body (JSON):")
            print(json_data)
            return json_data
        else:
            print(f"HTTP method {http_method} is not supported or invalid.")
            return None
    except requests.RequestException as e:
        print(f"API Test Failed: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    api_endpoint = "https://api.example.com/data"  # Replace with your API endpoint URL
    api_key = "your_api_key_here"  # Replace with your actual API key
    request_headers = {"Content-Type": "application/json"}  # Replace with any required headers
    request_data = {"key": "value"}  # Replace with any JSON data for POST requests

    json_response_get = test_api(api_endpoint, http_method="GET", headers=request_headers, api_key=api_key)
    json_response_post = test_api(api_endpoint, http_method="POST", headers=request_headers, api_key=api_key, data=request_data)

