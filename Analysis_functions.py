import pandas as pd

all_cases=0
all_deaths=0
maxi_cases=0
maxi_deaths=0
maxi_cases_date=""
maxi_deaths_date=""
avg_cases=0
avg_deaths=0

def average_cases(c_code):
    main(c_code)
    return avg_cases

def average_deaths(c_code):
    main(c_code)
    return avg_deaths
    

def maximum_deaths(c_code):
    main(c_code)
    return (maxi_deaths,maxi_deaths_date)
    

def maximum_cases(c_code):
    main(c_code)
    return (maxi_cases,maxi_cases_date)
    

def total_cases(c_code):
    main(c_code)
    return all_cases
    

def total_deaths(c_code):
    main(c_code)
    return all_deaths
    


def main(c_code):
    global all_cases,all_deaths,maxi_cases,maxi_deaths,avg_cases,avg_deaths,maxi_cases_date,maxi_deaths_date
    with open("Processed_Covid_file.csv") as myfile:
            raw_data=pd.read_csv(myfile)
    dates=list(raw_data['Date_reported'])
    daily_cases=list(raw_data['New_cases'])
    daily_deaths=list(raw_data['New_deaths'])
    country_codes=list(raw_data['Country_code'])
    days=0

    for i in range(1,len(raw_data['Country_code'])):
        if(country_codes[i]==c_code):
            all_cases+=int(daily_cases[i])
            days+=1
            all_deaths+=int(daily_deaths[i])
            if(maxi_cases<int(daily_cases[i])):
                maxi_cases=daily_cases[i]
                maxi_cases_date=dates[i]
            
            if(maxi_deaths<int(daily_deaths[i])):
                maxi_deaths=daily_deaths[i]
                maxi_deaths_date=dates[i]
    
    avg_cases=all_cases/days
    avg_deaths=all_deaths/days


        
                