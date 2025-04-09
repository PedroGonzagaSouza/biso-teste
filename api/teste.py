import csv, sqlite3
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# filmes = pd.read_csv('./data/Filmes.csv')
ratings = pd.read_csv('./data/Ratings.csv')
tags = pd.read_csv('./data/Tags.csv')
# print(filmes.head(10))
conn = sqlite3.connect('./filmes.db')
c = conn.cursor()


# c.execute("CREATE TABLE FILMES (MOVIEID INTEGER,TITLE TEXT,GENRES TEXT,YEAR INTEGER)")
# c.execute("CREATE TABLE RATINGS (USERID, MOVIEID, RATING )")
# c.execute("CREATE TABLE TAGS (MOVIEID INTEGER,TAG TEXT)")

# filmes.to_sql('FILMES', conn, if_exists='append', index=False, dtype={'MOVIEID': 'INTEGER', 'TITLE': 'TEXT', 'GENRES': 'TEXT', 'YEAR': 'INTEGER'})
# ratings.to_sql('RATINGS', conn, if_exists='append', index=False, dtype={'USERID': 'INTEGER', 'MOVIEID': 'INTEGER', 'RATING': 'REAL'})
# tags.to_sql('TAGS', conn, if_exists='append', index=False, dtype={'MOVIEID': 'INTEGER', 'TAG': 'TEXT'})
conn.commit()
conn.close()    