

import glassdoor_scraper as gs
import pandas as pd

path = '/usr/local/bin/chromedriver'


df = gs.get_jobs('data scientist', 100, False, path, 15)

df
