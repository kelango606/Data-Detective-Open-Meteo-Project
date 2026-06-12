def fetch_api_data(url, params=None):
    """
    Sends a GET request to the API URL and returns JSON data.
    
    Args:
        url (str): The API endpoint
        params (dict, optional): Query parameters
    
    Returns:
        data (dict or list): Parsed JSON data from the API
    """
    try:
        # TODO: fetch data
        print("Fetching data... (not implemented yet)")
        return None
    except requests.exceptions.RequestException as e:
        # TODO: handle error
        return None
