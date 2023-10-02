import requests

def fetch_and_show_data():
    url = 'https://5d63-2405-201-2009-905b-51c-228c-dff9-4ec1.ngrok-free.app/users/v1/profile'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status code indicates an error

        data = response.json()

        for item in data:
            print(item['name'])  # Assuming the API returns a list of dictionaries with a 'name' key

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_and_show_data()




