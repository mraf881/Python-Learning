#Renaming and dropping column

df.rename(column={"column1":"column_id"}) #renaming the column1 to column_id

df.rename(column={"column1":"column_id","column2":"column_name"}) #to rename multiple column

df.rename(column={"column1":"column_id","column2":"column_name"}, inplace=True) #put inplace=True to show the changes made in the next dataframe.

df.drop(["column1","column2"], axis=1, inplace=True) #drop multiple column

#Duplicate

df.duplicate().sum() #to show the duplicate.

df.drop_duplicate(inplac=True) #To remove the duplicate

#To check and remove missing value.

df.isna() #check missing value. True is the missing value.

df.isna().sum() #to show missing value in column.

df.isna().sum().sum() #to show overall missing value.

(df.isna().sum()/df.shape[0])*100 #to show percentage of missing value.

df.fillna(0) #fill the entire row with 0 for null value.

df.column1.fillna(0) #fill the specifi row with 0 for null value.

df.column1.fillna(0,inplace=True) #to show the changes in the next dataframe.

df.["New_Column1"]=0 #Create new column with 0 value in it.

df.["is missing"] = df.column1.isna() #create new column with name "is missing" and show the null value is present acording to column1 as value.

#To Change Data Type

df.column1.dtype #To show data type for column1.

df.column1.astype("object") #Change the data type to object.






