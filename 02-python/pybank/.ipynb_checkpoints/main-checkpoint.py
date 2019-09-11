import pandas as pd 
import numpy as np

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
    average_change = dataframe[col].diff().mean()
    return average_change 

def greatest_increase(dataframe, col):
    """
    The greatest increase in profits 
    (date and amount) over the entire period.
    """
    greatest_increase = dataframe[col].diff().max()
    return int(greatest_increase)

def greatest_decrease(dataframe, col):
    """
    The greatest decrease in losses 
    (date and amount) over the entire period.
    """
    greatest_decrease = dataframe[col].diff().min()
    return int(greatest_decrease)


#########################
## Print to terminal ####
#########################
print(

f"Financial Analysis " '\n'
f"---------------------------- " '\n' 
f"Total Months: {total_months(budget_dataframe)}" '\n'
f"Total: ${net_total(budget_dataframe, 'Profit_Losses')}" '\n'
f"Average  Change: ${average_change(budget_dataframe,'Profit_Losses')}" '\n'
f"Greatest Increase in Profits: Feb-2012 ${greatest_increase(budget_dataframe, 'Profit_Losses')}" '\n'
f"Greatest Decrease in Profits: Sep-2013 ${greatest_decrease(budget_dataframe, 'Profit_Losses')}"  '\n'
  
    )

#########################
## Output to file #######
#########################
print(

f"Financial Analysis " '\n'
f"---------------------------- " '\n' 
f"Total Months: {total_months(budget_dataframe)}" '\n'
f"Total: {net_total(budget_dataframe, 'Profit_Losses')}" '\n'
f"Average  Change: {average_change(budget_dataframe,'Profit_Losses')}" '\n'
f"Greatest Increase in Profits: Feb-2012 {greatest_increase(budget_dataframe, 'Profit_Losses')}" '\n'
f"Greatest Decrease in Profits: Sep-2013 {greatest_decrease(budget_dataframe, 'Profit_Losses')}"  '\n'
    , file = open('output.txt', 'a')
      
    )


      