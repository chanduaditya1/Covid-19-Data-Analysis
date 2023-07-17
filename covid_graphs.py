from matplotlib import pyplot as plt    
import pandas as pd

def cases_graph(c_code):
    with open("Processed_Covid_file.csv") as myfile:
        raw_data=pd.read_csv(myfile)

    dates=list(raw_data['Date_reported'])
    daily_cases=list(raw_data['New_cases'])
    country_codes=list(raw_data['Country_code'])
    country=list(raw_data['Country'])

    input_code=c_code
    country_name=""

    x=list()
    y=list()
    for i in range(1,len(raw_data['Country_code'])):
        if(country_codes[i]==input_code):
            x.append(dates[i])
            y.append(daily_cases[i])
            country_name=country[i]
            

    plt.plot(x,y)    
        
    plt.title(f"Covid Cases In {country_name}({input_code})")   
    plt.ylabel('Number of Cases')    
    plt.xlabel(f'Dates({dates[0]} to {dates[-1]})')    
    plt.xticks([])
    plt.show()    


def death_graph(c_code):
    with open("Processed_Covid_file.csv") as myfile:
        raw_data=pd.read_csv(myfile)

    dates=list(raw_data['Date_reported'])
    daily_deaths=list(raw_data['New_deaths'])
    country_codes=list(raw_data['Country_code'])
    country=list(raw_data['Country'])

    input_code=c_code
    country_name=""

    x=list()
    y=list()
    for i in range(1,len(raw_data['Country_code'])):
        if(country_codes[i]==input_code):
            x.append(dates[i])
            y.append(daily_deaths[i])
            country_name=country[i]
            

    plt.plot(x,y)    
        
    plt.title(f"Covid Deaths In {country_name}({input_code})")   
    plt.ylabel('Number of Deaths')    
    plt.xlabel(f'Dates({dates[0]} to {dates[-1]})')    
    plt.xticks([])
    plt.show()    

