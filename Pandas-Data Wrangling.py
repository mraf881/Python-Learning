df.rename(column={"column1":"column_id"}) #renaming the column1 to column_id

df.rename(column={"column1":"column_id","column2":"column_name"}) #to rename multiple column

df.rename(column={"column1":"column_id","column2":"column_name"}, inplace=True) #put inplace=True to show the changes made in the next dataframe.

df.drop(["column1","column2"], axis=1, inplace=True) #drop multiple column

df.duplicate().sum() #to show the duplicate.

df.drop_duplicate(inplac=True) #To remove the duplicate
