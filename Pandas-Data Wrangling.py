#Renaming and dropping column

df.rename(columns={"column1":"column_id"}) #renaming the column1 to column_id

df.rename(columns={"column1":"column_id","column2":"column_name"}) #to rename multiple column

df.rename(columns={"column1":"column_id","column2":"column_name"}, inplace=True) #put inplace=True to show the changes made in the next dataframe.

df.drop(["column1","column2"], axis=1, inplace=True) #drop multiple column

#Duplicate

df.duplicated().sum() #to show the duplicate.

df.drop_duplicated(inplac=True) #To remove the duplicate

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

#Formating Text

df.column1 = df.column1.str.capitalize() #capatilise the value in the selected column

df.column1 = df.column1.str.upper() #uppercase the value in the selected column

df.column1 = df.column1.str.lower() #lowercase the value in the selected column

df.column1 = df.column1.str.strip() #remove whitespace in selected column

df.column.str.lstrip("leftstripstr") #to remove character from left 

df.column.str.rstrip("rightstripstr") #to remove character from right

df["col1_and_col2"] = df.col1 + df.col2 #concatenate between two column.

df["col1_and_col2"] = df.col1 + " " + df.col2 #to add whitespace between concatenated value.

#let say the following situation below
#the col1 have dtype as float64 and the value is 2022.0
#and we want to make it 2022. So,

df["col1"]=df["col1"].astype(str) #to convert the float64 to str

df["col1"]=df.col1.str(:4) #to get result as intended (2022).

#sorting

df.sort_values(by="col1",ascending=True,inplace=True) #to sort the dataframe to ascending order

df.sort_values(by=["col1","col2","col3"],ascending=True,inplace=True) #to sort the dataframe to ascending order

df.sort_values(by=["col1","col2","col3"],ascending=False,inplace=True) #to display highest value first.

####

df["new_col1"] = df.col1 + df.col2
