#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import random

import warnings
warnings.filterwarnings('ignore')

initiatives = pd.read_csv(r'C:\Users\Harish\OneDrive\Desktop\policy\initiatives.csv', sep = ',') #file with the actions to be taken
#print(initiatives.info())
# print(initiatives.head())

#print(initiatives.section.unique())

# policies = initiatives.groupby('section')
# food = policies.get_group('Food')
# waste = policies.get_group('Waste')
# energy = policies.get_group('Energy')
# water = policies.get_group('Water')
# climate = policies.get_group('Climate')
# trans = policies.get_group('Transportation')
# land = policies.get_group('Land Use')

#print(climate)

issues = pd.read_csv(r'C:\Users\Harish\OneDrive\Desktop\policy\user_data.csv', sep = ',') #file with the user replies
#print(issues.head())
rows = issues.count() #no of rows
print('Number of respondents: ', rows)


group_issues = issues.groupby('issues_faced_in') #groups data based on same values in issues_faced_in
issue_counts = group_issues.size() #size (no of entries) of each group
issue_counts = issue_counts.reset_index() #indexing resets from 0
issue_counts.columns = ['issues_faced_in', 'count'] #name of columns
# print(issue_counts.head())

max_num = issue_counts['count'].idxmax() #max count
priority = issue_counts.loc[max_num, 'issues_faced_in'] #most voted issue
print("Most Prevelant Issue:", priority) #if max count by two, alphabetically first

#ploting bar graph
plt.figure(figsize=(10,6))
plt.bar(issue_counts['issues_faced_in'], issue_counts['count'])  
plt.xlabel('Issue Faced')  
plt.ylabel('Number of People')  
plt.title('Issues Faced By Youth')
plt.show()

policy = initiatives[initiatives['section']==priority].reset_index() #all those rows where section matches with priority
# print(policy)

if not policy.empty: #if atleast 1 row found with section = priority
    recommendation = random.choice(policy['priority_action'].values)
    print('Recommended Policy for', priority, ':', recommendation)