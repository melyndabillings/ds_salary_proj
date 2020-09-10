"""
@author: melyndabillings
"""

import pandas as pd 

df = pd.read_csv('glassdoor_jobs.csv')

#parsing of salary 

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_dollar_sign = salary.apply(lambda x: x.replace('K','').replace('$',''))

del_salary = minus_dollar_sign.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = del_salary.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = del_salary.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['company_names'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#delete unused columns
df = df.drop(columns='Headquarters')
df = df.drop(columns='Competitors')
df = df.drop(columns='Type of ownership')
df = df.drop(columns='Size')



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