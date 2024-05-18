import requests

USERNAME = 'darr21735'
AUTHORIZATION_TOKEN = '29E70DEF-2781-450A-A3CF-54050818BF79'
SERVER = 'https://ftc-api.firstinspires.org/v2.0/'

def fetchDataFromApi(path_params = None, query_params = None):
    try:
        response = requests.get(SERVER + path_params, params=query_params, auth=(USERNAME, AUTHORIZATION_TOKEN))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data from API: {e}')
        return None

def fetchEventsFromApi(season, team_number = None, event_code = None):
    path_params = f'{season}/events/'
    query_params = {
        'teamNumber': team_number,
        'eventCode': event_code
    }

    return fetchDataFromApi(path_params, query_params)

if __name__ == "__main__":
    print(fetchEventsFromApi('2023', event_code='USAKCMP'))

