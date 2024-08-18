# using cricguru: https://github.com/puppetmaster12/cricguru
# instal: pip install cricguru

from cricguru import player

player = player.Player(8608)
query_params = {
    'class' : '1',
    'type' : 'bowling',
    'view' : 'innings'
}

cric_data = player.career_summary(query_params)
# print(cric_data.head())