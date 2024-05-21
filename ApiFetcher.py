import requests


USERNAME = "darr21735"
AUTHORIZATION_TOKEN = "29E70DEF-2781-450A-A3CF-54050818BF79"
SERVER = "https://ftc-api.firstinspires.org/v2.0/"


def fetchDataFromApi(path_params="", query_params="") -> requests.Response.json:
    """
    Fetches data from the FTC API using the provided path and query parameters.
    :Return: The JSON response from the API.
    :rtype: requests.Response.json
    """

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


def fetchEventsFromApi(
    *, season: str, team_number="", event_code=""
) -> requests.Response.json:
    """
    Fetches events from the FTC API based on the provided season, team number, and event code.
    :Return: The JSON response from the API.
    :rtype: requests.Response.json
    """
    path_params = f"{season}/events/"
    query_params = {"teamNumber": team_number, "eventCode": event_code}

    return fetchDataFromApi(path_params, query_params)


def fetchTeamFromApi(
    *, season: str, team_number="", event_code="", state="", page=""
) -> requests.Response.json:
    """
    Fetches teams from the FTC API based on the provided season, team number, event code, state and page.
    :Return: The JSON response from the API.
    :rtype: requests.Response.json
    """
    path_params = f"{season}/teams/"
    query_params = {
        "teamNumber": team_number,
        "eventCode": event_code,
        "state": state,
        "page": page,
    }

    return fetchDataFromApi(path_params, query_params)


def fetchSeasonFromApi(*, season: str) -> requests.Response.json:
    """
    Fetches seasons from the FTC API based on the provided season.
    :Return: The JSON response from the API.
    :rtype: requests.Response.json
    """
    path_params = f"{season}/"

    return fetchDataFromApi(path_params)


def fetchMatchFromApi(
    *,
    season: str,
    event_code: str,
    tournament_level="",
    team_number="",
    match_number="",
    start="",
    end="",
) -> requests.Response.json:
    """
    Fetches matches from the FTC API based on the provided season, event code, tournament level, team number, match number, start and end.
    :Return: The JSON response from the API.
    :rtype: requests.Response.json
    """
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
    *,
    season: str,
    event_code: str,
    tournament_level: str,
    team_number="",
    match_number="",
    start="",
    end="",
) -> requests.Response.json:
    """
    Fetches scores from the FTC API based on the provided season, event code, tournament level, team number, match number, start and end.
    :Return: The JSON response from the API.
    :rtype: requests.Response.json
    """
    path_params = f"{season}/scores/{event_code}/{tournament_level}/"

    query_params = {
        "teamNumber": team_number,
        "matchNumber": match_number,
        "start": start,
        "end": end,
    }

    return fetchDataFromApi(path_params, query_params)


def main() -> None:
    print(
        fetchScoreFromApi(
            season="2023",
            event_code="MXCTQ",
            tournament_level="qual",
            team_number="21735",
        )
    )


if __name__ == "__main__":
    main()
