from EPACalculator import TeamRatingSystem as EPA
import pandas as pd
import ast


class MatchPredictor:
    def __init__(self, season) -> None:
        self.DB_rute = "./DB"
        self.teams_database = pd.read_csv(f"./DB/EPA/{season}.csv")
        self.season = season

    def calculateEPA(self, event_code: str, match_number: int) -> None:
        matches_df = pd.read_csv(
            f"{self.DB_rute}/Matches/{self.season}{event_code}.csv"
        )
        match_row = matches_df.iloc[match_number - 1]
        red_alliance_pts = match_row.iloc[2]
        blue_alliance_pts = match_row.iloc[3]
        red_alliance_teams = ast.literal_eval(match_row.iloc[4])
        blue_alliance_teams = ast.literal_eval(match_row.iloc[5])
        teams_on_field = ast.literal_eval(match_row.iloc[6])
        red_win = red_alliance_pts > blue_alliance_pts
        blue_win = red_alliance_pts < blue_alliance_pts

        epa: EPA
        win: bool
        for team in teams_on_field:
            epa = EPA(team, self.season, self.teams_database)

            if team in red_alliance_teams:
                win = red_win
            else:
                win = blue_win

            epa = epa.updateEPA(
                blue_alliance_pts,
                red_alliance_pts,
                blue_alliance_teams,
                red_alliance_teams,
                win,
            )
            print(f"New EPA: {team}: {epa}")

        self.teams_database = pd.read_csv(f"./DB/EPA/{self.season}.csv")
        self.calculateMatchProbability(event_code)

    def calculateProbability(
        self, blue_alliance_members: list, red_alliance_members: list
    ) -> float:

        red_alliance_EPA = EPA(
            red_alliance_members[0], self.season, self.teams_database
        ).allianceEPA(red_alliance_members)

        blue_alliance_EPA = EPA(
            red_alliance_members[0], self.season, self.teams_database
        ).allianceEPA(blue_alliance_members)

        red_favor = red_alliance_EPA > blue_alliance_EPA

        print(red_favor)

        d = abs(red_alliance_EPA - blue_alliance_EPA)

        exponent_value = pow(10, d / 400) + 1

        p_win = 1 / exponent_value * 100

        p_win = max(p_win, 100 - p_win)

        probability = []

        if red_favor:
            probability = [p_win, 100 - p_win]
        else:
            probability = [100 - p_win, p_win]

        return probability

    def calculateMatchProbability(self, event_code: str) -> pd.DataFrame:
        matches_df = pd.read_csv(
            f"{self.DB_rute}/Matches/{self.season}{event_code}.csv"
        )
        tmp_data = {
            "Match Number": [],
            "Red Alliance Win Probability": [],
            "Blue Alliance Win Probability": [],
        }
        for i in range(len(matches_df) - 7):
            match_row = matches_df.iloc[i]
            red_alliance_teams = ast.literal_eval(match_row.iloc[4])
            blue_alliance_teams = ast.literal_eval(match_row.iloc[5])
            win_probability = self.calculateProbability(
                blue_alliance_teams, red_alliance_teams
            )

            tmp_data["Match Number"].append(match_row[1])
            tmp_data["Red Alliance Win Probability"].append(win_probability[0])
            tmp_data["Blue Alliance Win Probability"].append(win_probability[1])

        tmp_dataframe = pd.DataFrame(tmp_data)

        tmp_dataframe.to_csv(
            f"{self.DB_rute}/Matches/Predictions/{self.season}{event_code}.csv"
        )

        return tmp_dataframe


if __name__ == "__main__":
    Predictor = MatchPredictor(2023)
    for i in range(1, 34):
        print(Predictor.calculateEPA("MXCTQ", i))
    # print(Predictor.calculateMatchProbability("MXCTQ"))
