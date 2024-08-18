# using python-espncricinfo client for ESPNCricinfo's match, summary and player information.
# https://github.com/outside-edge/python-espncricinfo

import pandas as pd


from espncricinfo.series import Series
s = Series('18018')
s.name

# df.to_csv('Espncricinfo.csv')

from espncricinfo.player import Player
p = Player('8608')
# print(p.name)

# filename = p.name.replace(" ", "-",)

# x = p.get_career_summary('c', 1, 'batting')

p.get_data(p.name, 1, 'bowling', 'innings')

p.get_


