df.rename(column={"column1":"column_id"}) #renaming the column1 to column_id

df.rename(column={"column1":"column_id","column2":"column_name"}) #to rename multiple column

df.rename(column={"column1":"column_id","column2":"column_name"}, inplace=True) #put inplace=True to show the changes made in the next dataframe.


