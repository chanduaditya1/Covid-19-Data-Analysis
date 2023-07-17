from tkinter import *
from covid_graphs import cases_graph
from covid_graphs import death_graph
import Analysis_functions as af

BACKGROUND_COLOR = "#B1DDC6"
def bt1_clicked():
    cases_graph(my_input.get())
    response_label=Label(text="Button Got Clicked")
    response_label.grid(column=0,row=2) 

def bt2_clicked():
    death_graph(my_input.get())
    response_label=Label(text="Button Got Clicked")
    response_label.grid(column=1,row=2) 

def bt3_clicked():
    avg_cases=af.average_cases(my_input.get())
    total_cases=af.total_cases(my_input.get())
    max_cases=af.maximum_cases(my_input.get())
    newLabel=Label(text=f'Average Cases : {avg_cases}\nTotal Cases : {total_cases}\nMax Cases : {max_cases[0]} On {max_cases[1]}')
    newLabel.grid(column=3,row=3)

def bt4_clicked():
    avg_deaths=af.average_deaths(my_input.get())
    total_deaths=af.total_deaths(my_input.get())
    max_deaths=af.maximum_deaths(my_input.get())
    newLabel=Label(text=f'Average Deaths : {avg_deaths}\nTotal Death : {total_deaths}\nMax Deaths : {max_deaths[0]} On {max_deaths[1]}')
    newLabel.grid(column=3,row=4)

my_window=Tk()
my_window.minsize(width=600,height=300)
my_window.title("Covid Data Analysis")
my_window.config(padx=20,pady=20)

my_label=Label(text="Enter Country Code: ",font=("Arial",10,"bold"))
my_label.grid(column=0,row=0)

my_input=Entry(width=40)
my_input.grid(column=1,row=0)

  
bt1=Button(text="Number of Cases Graph",command=bt1_clicked)
bt1.grid(column=0,row=1)

bt2=Button(text="Number of Deaths Graph",command=bt2_clicked)
bt2.grid(column=1,row=1)

bt3=Button(text="Cases Information",command=bt3_clicked)
bt3.grid(column=2,row=1)

bt4=Button(text="Deaths Information",command=bt4_clicked)
bt4.grid(column=3,row=1)

my_window.config(bg=BACKGROUND_COLOR)

my_window.mainloop()