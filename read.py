import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_top_goalscorers"


table = pd.read_html(url,match='Notes')[0]

print(table.columns)
# table.to_csv('data/top_goalscorers.csv', index=False)
