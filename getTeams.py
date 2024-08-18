from cricguru import team

team = team.Team()
query_params = {"template": "results", "class": "2"}
cric_data = team.overall(query_params)

#Returns a pandas dataframe
cric_data.head()