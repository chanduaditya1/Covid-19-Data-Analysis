import pandas as pd
import csv
def handle_Null_Value(df,string):
    n = len(df[string])
    for i in range(n):
        if(df[string][i]=='' or int(df[string][i])<0):
            df[string][i]=0


with open("WHO-COVID-19-global-data.csv") as myfile:
    raw_data = list(csv.reader(myfile))

newData = dict()
headers = list(raw_data[0])
for i in range(0,len(headers)):
    k=list()
    for j in range(1,len(raw_data)):
        k.append(raw_data[j][i])
    newData[headers[i]]=list(k)

df = pd.DataFrame(newData)
handle_Null_Value(df,'New_cases')
handle_Null_Value(df,'Cumulative_cases')
handle_Null_Value(df,'New_deaths')
handle_Null_Value(df,'Cumulative_deaths')
df.to_csv("Processed_Covid_file.csv",index=False)

