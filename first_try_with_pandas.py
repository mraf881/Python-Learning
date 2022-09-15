import pandas as pd #importing the pandas

#df = dataframe
df=pd.read_csv("location.csv") #read the csv files

df.head() #show the table

df.column_1 #show the series of value available at the selected column

df.head(10) # to display only 10 row

df.columns # to show column in the dataframe

df.total_rooms[0] #display the value for assigned position in [] according defined column

df.iloc[0,0] #select value using index based selection

df.loc[0:5,["total_rooms","total_bedrooms"]] #selectiing the six row of defined column df.loc[<initial num row>:<final num row>,["column_name1", "column_name2"]]

#please note the return value of row of iloc and loc is not the same

df.describe() #give quick summary of the table

df.info() #another quick overview with different perspective

df.shape # return the (value of row, column)

df.column1.max # return max value of selected column

df.column1.min # return min value of selected column

df.column1 == 'value' # conditional selection

df[df.column1 == 'value'] # it show the result in form of table

df.loc[(df.column1 == 'value') | (df.column1 == 'value2')]

df.[df.column1.isin(["value1","value2"])


