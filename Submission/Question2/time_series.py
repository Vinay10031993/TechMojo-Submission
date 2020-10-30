import pandas as pd
import numpy as np


df = pd.read_csv('testfile.csv')
df['date'] = df['date'].astype(str)
df['datetime'] = df['date'] + ' '+ df['time']
df['datetime']=pd.to_datetime(df['datetime'], format='%Y/%m/%d %H:%M')
print( "-------------------------------------------------------------------------------------------------------------------------")
print( "############################### Average time taken for the task to complete in minutes. ###############################")
## Average time taken for the task to complete in minutes.
print (df.groupby('taskid').agg({
        'datetime': lambda x: x.diff().astype('timedelta64[s]').sum()//60}))
print( "-------------------------------------------------------------------------------------------------------------------------")
print( "-------------------------------------------------------------------------------------------------------------------------")

## Average datetime to complete a task

print( "############################### Average datetime to complete a task. ###############################")
print(df.groupby('taskid')['datetime'].agg(lambda x: x.mean(numeric_only=False)))


print( "-------------------------------------------------------------------------------------------------------------------------")
