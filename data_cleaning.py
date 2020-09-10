# -*- co=ng: utf-8 -*-.,.
"""
Created on Sat Sep  5 13:03:47 2020

@author: melyndabillings
"""

import pandas as pd 

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing 

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ','  in x.lower() else 0)
df = df[df['job_state'] != 0]

#parsing of job descriptions
#python
df['python'] = df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x:1 if 'excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index=False)


pd.read_csv('salary_data_cleaned.csv')
