import glassdoor_scraper as gs
import pandas as pd

path = "chromedriver.exe"

df = gs.get_jobs('data scientist', 50, False, path, 15)

df.to_csv('datacollection_of_jobs.csv', index = False)

#path = 'glassdoor_jobs.csv'
#df  = pd.read_csv(path)
#print(df)
