# Simple parse of the 'games.json' file.
import os
import json
import numpy as np
import pandas as pd









if os.path.exists('games.json'):
  # read the json file ,you can check the raw file by yourself
  df = pd.read_json('games.json',orient='index')
  # choose the column that we need
  df_selected = df[['name', 'release_date', 'required_age', 'price','dlc_count','windows', 'mac', 'linux','metacritic_score', 'achievements', 'supported_languages', 'full_audio_languages', 'developers', 'publishers', 'categories', 'genres', 'positive', 'negative', 'estimated_owners', 'average_playtime_forever','average_playtime_2weeks','median_playtime_forever','median_playtime_2weeks','peak_ccu','tags']]
  df_selected['app_id'] = df_selected.index  # put the df index into column
  print(df_selected.head()) # print the first 5 rows to take a look
  df_selected.to_excel('games_data1.xlsx', index=False) # output the data to a modern excel file
  print("data has been output to games_data.xlsx")
