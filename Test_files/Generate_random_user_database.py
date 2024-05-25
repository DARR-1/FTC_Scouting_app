import pandas as pd
import random

ROWS_LIMIT = 40

data = {"Team_number": ["DARR"], "EPA": [78], "Qualification_matches_played": [5]}

for i in range(ROWS_LIMIT):
    data["Team_number"].append(random.randint(1,10000))
    data["EPA"].append(random.randint(0,85))
    data["Qualification_matches_played"].append(random.randint(0, 68))

df = pd.DataFrame(data)

df.to_csv("./DB/Users.csv")
print(df)
