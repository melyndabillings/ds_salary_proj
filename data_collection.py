#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:03:47 2020

@author: melyndabillings
"""

import glassdoor_scraper as gs
import pandas as pd


path = '/usr/local/bin/chromedriver'


df = gs.get_jobs('data scientist', 200, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

