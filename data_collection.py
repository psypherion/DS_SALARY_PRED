# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:17:04 2021

@author: Sayan
"""

import glassdoor_scraper as gs
import pandas as pd

path = "E:/END to END PROJECTS/DS_SALARY_PRED/chromedriver"
df = gs.get_jobs('data scientist', 1000, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)