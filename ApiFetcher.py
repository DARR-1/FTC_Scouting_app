import requests


USERNAME = "darr21735"
AUTHORIZATION_TOKEN = "29E70DEF-2781-450A-A3CF-54050818BF79"
SERVER = "https://ftc-api.firstinspires.org/v2.0/"


def fetchDataFromApi(path_params=None, query_params=None):
    try:
        response = requests.get(
            SERVER + path_params,
            params=query_params,
            auth=(USERNAME, AUTHORIZATION_TOKEN),
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None


def fetchEventsFromApi(season, team_number=None, event_code=None):
    path_params = f"{season}/events/"
    query_params = {"teamNumber": team_number, "eventCode": event_code}

    return fetchDataFromApi(path_params, query_params)


def fetchTeamFromApi(season, team_number=None, event_code=None, state=None, page=None):
    path_params = f"{season}/teams/"
    query_params = {
        "teamNumber": team_number,
        "eventCode": event_code,
        "state": state,
        "page": page,
    }

    return fetchDataFromApi(path_params, query_params)


def fetchSeasonFromApi(season):
    path_params = f"{season}/"

    return fetchDataFromApi(path_params)


def fetchMatchFromApi(
    season,
    event_code,
    tournament_level=None,
    team_number=None,
    match_number=None,
    start=None,
    end=None,
):
    path_params = f"{season}/matches/{event_code}/"
    query_params = {
        "tournamentLevel": tournament_level,
        "teamNumber": team_number,
        "matchNumber": match_number,
        "start": start,
        "end": end,
    }

    return fetchDataFromApi(path_params, query_params)


def fetchScoreFromApi(
    season,
    event_code,
    tournament_level,
    team_number=None,
    match_number=None,
    start=None,
    end=None,
):
    path_params = f"{season}/scores/{event_code}/{tournament_level}/"

    query_params = {
        "teamNumber": team_number,
        "matchNumber": match_number,
        "start": start,
        "end": end,
    }

    return fetchDataFromApi(path_params, query_params)


def main():
    print(fetchEventsFromApi("223"))
    print(fetchTeamFromApi("2023"))
    print(fetchSeasonFromApi("2023"))
    print(fetchMatchFromApi("2023", "USAKCMP"))
    print(fetchScoreFromApi("2023", "USAKCMP", "qual"))


if __name__ == "__main__":
    main()
