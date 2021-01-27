import pandas as pd
#import math
import requests

#Step 1 Data Collection
url = 'https://en.wikipedia.org/wiki/List_of_current_boxing_rankings'
req = requests.get(url)
data_list = pd.read_html(req.text)
heavyWeight_df = data_list[2]
lHeavyWeight_df = data_list[4]
sMiddleWeight_df = data_list[5]
middleWeight_df = data_list[6]
lMiddleWeight_df = data_list[7]

#Step 2 Data Cleaning

#Issue 1 Column Names
heavyWeight_df.columns = ['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO','NA']
lHeavyWeight_df.columns = ['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO','NA']
sMiddleWeight_df.columns = ['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO','NA']
middleWeight_df.columns = ['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO','NA']
lMiddleWeight_df.columns = ['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO','NA']

#Issue 2 Extra Columns
heavyWeight_df = heavyWeight_df[['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO']]
lHeavyWeight_df = lHeavyWeight_df[['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO']]
sMiddleWeight_df = sMiddleWeight_df[['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO']]
middleWeight_df = middleWeight_df[['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO']]
lMiddleWeight_df = lMiddleWeight_df[['Rank','BoxRec','TBRB','The Ring','WBA','WBC','IBF','WBO','IBO']]

#Issue 3 dropping empty rows
heavyWeight_df = heavyWeight_df.dropna(how='all')
lHeavyWeight_df = lHeavyWeight_df.dropna(how='all')
sMiddleWeight_df = sMiddleWeight_df.dropna(how='all')
middleWeight_df = middleWeight_df.dropna(how='all')
lMiddleWeight_df = lMiddleWeight_df.dropna(how='all')

#Issue 4 iterating rows and creating dictionary to assign points

#for Heavy Weight division
columns = list(heavyWeight_df)
hW_dict = {}

for i in columns:
    for j in range (11,22):
        points = 22 - j
        if heavyWeight_df[i][j] in hW_dict.keys():
            prev_points = hW_dict[heavyWeight_df[i][j]]
            hW_dict[heavyWeight_df[i][j]] = points + prev_points
        else:
            hW_dict[heavyWeight_df[i][j]] = points

#for light Heavy Weight division
columns = list(lHeavyWeight_df)
lHW_dict = {}


for i in columns:
    for j in range (11,22):
        points = 22 - j
        if lHeavyWeight_df[i][j] in lHW_dict.keys():
            prev_points = lHW_dict[lHeavyWeight_df[i][j]]
            lHW_dict[lHeavyWeight_df[i][j]] = points + prev_points
        else:
            lHW_dict[lHeavyWeight_df[i][j]] = points

#for Super Middle Weight division
columns = list(sMiddleWeight_df)
sMW_dict = {}


for i in columns:
    for j in range (11,22):
        points = 22 - j
        if sMiddleWeight_df[i][j] in sMW_dict.keys():
            prev_points = sMW_dict[sMiddleWeight_df[i][j]]
            sMW_dict[sMiddleWeight_df[i][j]] = points + prev_points
        else:
            sMW_dict[sMiddleWeight_df[i][j]] = points
            
#for Middle Weight division
columns = list(middleWeight_df)
mW_dict = {}


for i in columns:
    for j in range (11,22):
        points = 22 - j
        if middleWeight_df[i][j] in mW_dict.keys():
            prev_points = mW_dict[middleWeight_df[i][j]]
            mW_dict[middleWeight_df[i][j]] = points + prev_points
        else:
            mW_dict[middleWeight_df[i][j]] = points


#for light Middle Weight division
columns = list(lMiddleWeight_df)
lMW_dict = {}


for i in columns:
    for j in range (11,22):
        points = 22 - j 
        if lMiddleWeight_df[i][j] in lMW_dict.keys():
            prev_points = lMW_dict[lMiddleWeight_df[i][j]]
            lMW_dict[lMiddleWeight_df[i][j]] = points + prev_points
        else:
            lMW_dict[lMiddleWeight_df[i][j]] = points
            

#Issue 4 Introducing points column to the dataframe
#points = [11,10,9,8,7,6,5,4,3,2,1]
#heavyWeight_df['Points'] = points



#Issue 3 Extra Rows
#last_idx = target_df.index[-1]
#target_df = target_df.drop([last_idx, last_idx-1])