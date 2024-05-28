import pandas as pd
import os
import ApiFetcher

DATABASE_FOLDER = "./DB"


def teamsList(season: int) -> tuple:
    """
    Creates a list with all the participant teams of a season.
    :params season: the numeric year of the season you want to get its teams.
    :Return: The teams that participate in the event.
    :rtype: tuple
    """
    request = ApiFetcher.fetchTeamsFromApi(season=season)
    teams_df = pd.json_normalize(request)

    teams_list = []
    total_pages = teams_df.loc[0, "pageTotal"]

    for i in range(total_pages):
        print("iteration:", f'{i + 1}/{total_pages}')
        request = ApiFetcher.fetchTeamsFromApi(season=season, page=i + 1)
        teams_df = pd.json_normalize(request, record_path="teams")

        for i in range(len(teams_df)):
            teams_list.append(teams_df.loc[i, "teamNumber"])

    return teams_list


def matchesResults(season: int, event_code: str) -> pd.DataFrame:
    """
    Creates a database with all the matches, points and if the robot was in field or not.
    :params season: the numeric year of the season you want yo get its matches results.
    :params event_code: the code of the event you want to get its matches results.
    :Return: The teams that participate in the event.
    :rtype: pd.dataframe
    """

    request = ApiFetcher.fetchMatchFromApi(season=season, event_code=event_code)
    matches_df = pd.json_normalize(request, record_path="matches")
    matches_df.to_csv("test.csv")

    matches_data = {
        "Description": [],
        "Red Alliance pts": [],
        "Blue Alliance pts": [],
        "Red Alliance Teams": [],
        "Blue Alliance Teams": [],
        "Teams On Field": [],
        "Teams Out Of Field": [],
    }
    teams = None
    for i in range(len(matches_df)):
        matches_data["Description"].append(matches_df.loc[i, "description"])
        matches_data["Red Alliance pts"].append(matches_df.loc[i, "scoreRedFinal"])
        matches_data["Blue Alliance pts"].append(matches_df.loc[i, "scoreBlueFinal"])
        teams = matches_df.loc[i, "teams"]

        red_alliance_teams = [
            item["teamNumber"]
            for item in teams
            if item["station"] in ["Red1", "Red2", "Red3"]
        ]
        blue_alliance_teams = [
            item["teamNumber"]
            for item in teams
            if item["station"] in ["Blue1", "Blue2", "Blue3"]
        ]

        matches_data["Red Alliance Teams"].append(red_alliance_teams)
        matches_data["Blue Alliance Teams"].append(blue_alliance_teams)

        teams_on_field = [item["teamNumber"] for item in teams if item["onField"]]
        teams_out_of_field = [
            item["teamNumber"] for item in teams if not item["onField"]
        ]

        matches_data["Teams On Field"].append(teams_on_field)
        matches_data["Teams Out Of Field"].append(teams_out_of_field)

    match_results_df = pd.DataFrame(matches_data)
    return match_results_df


def createEloDatabase(season: int) -> pd.DataFrame:
    """
    Creates a database with all the teams the number of qualification matches played and their ELO.
    :params season: the numeric year of the season you want to generate an ELO database.
    :Return: The teams that participate in the event.
    :rtype: pd.dataframe
    """
    teams_list = teamsList(season)

    data = {
        'team_number': teams_list,
        'ELO': [],
        'Qualification_matches_played': [],
    }

    for i in range(len(teams_list)):
        data["ELO"].append(1500)
        data['Qualification_matches_played'].append(0)

    ELO_df = pd.DataFrame(data)
    ELO_df.to_csv(f'{DATABASE_FOLDER}/ELO/{season}.csv')

    return ELO_df

if __name__ == "__main__":
    print(createEloDatabase(2023))
