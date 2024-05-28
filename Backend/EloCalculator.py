import pandas as pd


class TeamRatingSystem:

    def __init__(self, team_number: str, event_code: str) -> None:
        """
        Initialize TeamRatingSystem object with the provided team number.
        :param team_number: Team number to initialize the object.
        :params event_code: The code of the event you want to get its participants teams.
        :rtype: None
        """
        self.team_number = team_number
        self.TEAM_DATAFRAME = pd.read_csv(f"./DB/{event_code}")
        self.user_row = self.TEAM_DATAFRAME.loc[
            self.TEAM_DATAFRAME["Team_number"] == self.team_number
        ]

    def EPA(self) -> int:
        """
        Get the Expected Points Added (EPA) for the team.
        :Return: The EPA score of the team.
        :rtype: int
        """
        self.user_row = self.TEAM_DATAFRAME.loc[
            self.TEAM_DATAFRAME["Team_number"] == self.team_number
        ]

        user_EPA = self.user_row.iloc[0]["EPA"]

        return user_EPA

    def allianceEPA(self, alliance_members: list) -> int:
        """
        Get the total Expected Points Added (EPA) for the alliance.
        :param alliance_members: List of team numbers in the alliance.
        :Return: The total EPA score of the alliance.
        :rtype: int
        """
        EPA = 0
        for members in alliance_members:
            member_row = self.TEAM_DATAFRAME.loc[
                self.TEAM_DATAFRAME["Team_number"] == members
            ]
            member_EPA = member_row.iloc[0]["EPA"]

            EPA += member_EPA

        return EPA

    def updateK(self, qualification_matches_played) -> int:
        """
        Update the K parameter based on the number of qualification matches played.
        :param qualification_matches_played: Number of qualification matches played.
        :Return: The updated K parameter.
        :rtype: int
        """
        if qualification_matches_played <= 6:
            K = 0.5
        elif 6 < qualification_matches_played <= 12:
            K = 0.5 - 1 / 30 * (qualification_matches_played - 6)
        else:
            K = 0.3

        return K

    def updateM(self, qualification_matches_played) -> float:
        """
        Update the M parameter based on the number of qualification matches played.
        :param qualification_matches_played: Number of qualification matches played.
        :Return: The updated M parameter.
        :rtype: float
        """
        if qualification_matches_played <= 12:
            M = 0
        elif 12 < qualification_matches_played <= 36:
            M = 1 / 24 * (qualification_matches_played - 12)
        else:
            M = 1

        return M

    def updateEPA(
        self,
        blue_alliance_score: int,
        red_alliance_score: int,
        blue_alliance_members: list,
        red_alliance_members: list,
        win: bool,
    ) -> int:
        """
        Update the team's EPA based on match results.
        :param blue_alliance_score: Score of the blue alliance.
        :param red_alliance_score: Score of the red alliance.
        :param blue_alliance_members: List of team numbers in the blue alliance.
        :param red_alliance_members: List of team numbers in the red alliance.
        :param win: Boolean indicating if the team won the match.
        :Return: The updated EPA score of the team.
        :rtype: int
        """
        qualification_matches_played = self.user_row.iloc[0]["EPA"]

        K = self.updateK(qualification_matches_played)

        M = self.updateM(qualification_matches_played)

        EPA = self.EPA()
        red_alliance_EPA = self.allianceEPA(red_alliance_members)
        blue_alliance_EPA = self.allianceEPA(blue_alliance_members)

        delta_of_EPA = red_alliance_score - red_alliance_EPA
        delta_of_EPA -= M * (blue_alliance_score - blue_alliance_EPA)
        delta_of_EPA = K * 1 / (1 + M) * abs(delta_of_EPA)

        if win:
            EPA += delta_of_EPA
        elif not win:
            EPA -= delta_of_EPA

        self.TEAM_DATAFRAME.loc[
            self.TEAM_DATAFRAME["Team_number"] == self.team_number, "EPA"
        ] = float(EPA)

        self.TEAM_DATAFRAME.to_csv("./DB/Users.csv", index=False)

        return EPA


if __name__ == "__main__":
    user_EPA_class = TeamRatingSystem("DARR")
    print(user_EPA_class.EPA())
    user_EPA_class.updateEPA(
        125, 200, ["DARR", "4206", "4389"], ["4492", "1491", "219"], True
    )
    print(user_EPA_class.EPA())
