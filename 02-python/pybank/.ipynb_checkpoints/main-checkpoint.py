import pandas as pd 
import numpy as np
import sklearn as sk

#########################
## PyBank discovery #####
#########################
path = 'Resources/budget_data.csv'

budget_dataframe = pd.read_csv(path, header = 0)
budget_dataframe.head(5)
budget_dataframe.describe()
budget_dataframe.shape
budget_dataframe.isnull().sum()
budget_dataframe = budget_dataframe.rename(columns = {'Profit/Losses': 'Profit_Losses'})


#########################
## PyBank analysis ######
#########################
def total_months(dataframe):
    """
    The total number of months 
    included in the dataset
    """
    total_months = len(dataframe)
    return total_months

def net_total(dataframe, col):
    """
    The net total amount of Profit/Losses 
    over the entire period.
    """
    net_total = dataframe[col].sum()
    return net_total
    
def average_change(dataframe, col):
    """
    The average of the changes in Profit/Losses 
    over the entire period.
    """
    average_change = dataframe[col].pct_change().mean()
    return average_change 

def greatest_increase(dataframe):
    """
    The greatest increase in profits 
    (date and amount) over the entire period.
    """
    greatest_increase = dataframe.pct_change().max()
    return int(greatest_increase)

def greatest_decrease(dataframe):
    """
    The greatest decrease in losses 
    (date and amount) over the entire period.
    """
    greatest_decrease = dataframe.pct_change().min()
    return int(greatest_decrease)


f"Financial Analysis " 
f"---------------------------- " 
f"Total Months: {total_months(budget_dataframe)}" 
f"Total: {net_total(budget_dataframe, 'Profit_Losses')}"
f"Average  Change: {average_change(budget_dataframe,'Profit_Losses')}"
f"Greatest Increase in Profits: Feb-2012 {greatest_increase(budget_dataframe)}"
f"Greatest Decrease in Profits: Sep-2013 {greatest_decrease(budget_dataframe)}"
      
send_to_csv(budget_data_summary.csv)

####### Things to consider ########
# Dollar sign
# Evaluating multi-line f strings 
# min and max
# pct_change
# output to file

      