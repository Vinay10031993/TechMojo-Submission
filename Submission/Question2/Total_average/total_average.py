import os
import pandas as pd
import numpy as np
p=pd.read_csv("testfile.csv",encoding='unicode escape', delimiter=',', header=None)
p.columns=['ID','Date','Time','status']
for i in range(0,p.shape[0]):
     p.Date[i]=p.Date[i].replace('\x96','-').replace(' ','')
p['Date']=pd.to_datetime(p.Date+' ' +p.Time)
p.drop('Time',inplace=True,axis=1)
p.status=p.status.str.replace(' ','')
p1=p.loc[p.status!='End',:]
p2=p.loc[p.status=='End',:]
p3=pd.merge(p1,p2,on='ID')
print((p3.Date_y-p3.Date_x).astype('timedelta64[m]').mean(),'mins')
