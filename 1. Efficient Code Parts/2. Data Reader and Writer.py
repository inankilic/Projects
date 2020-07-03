 ### ************************
 ### DATA READING AND WRITING
 ### ************************

import pandas as pd 

##################################################
### Reading Excel with Pandas
##################################################

df = pd.read_excel('My_Excel.xlsx')
print(df.shape)
print('-'*25)

## Most commonly used parameters
# sheet_name  = 'col_name'
# index_col   = 'col_name'
# usecols     = ['col_name_1', 'col_name_2'] 
# nrows       = 100
# parse_dates = True


##################################################
### Reading CSV with Pandas
##################################################

df = pd.read_csv('My_Csv.csv')
print(df.shape)
print('-'*25)

## Most commonly used parameters
# sep         = ','
# decimal     = '.'
# index_col   = 'col_name'
# usecols     = ['col_name_1', 'col_name_2'] 
# nrows       = 100
# parse_dates = True


##################################################
### Writing a DataFrame to Excel or CSV
##################################################

df.to_excel('My_Excel.xlsx', index=False)
df.to_csv('My_Csv.csv', index=False)


##################################################
### Writing data to seperate sheets in an Excel
##################################################

writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()


##################################################
### Reading Data with SQL
##################################################

# Suppose you have a valid connection string called conneciton
sql = """
SELECT * 
FROM SCHEME.TABLE
WHERE DATE_COLUMN BETWEEN TO_DATE('20200101','YYYYMMDD') AND TO_DATE('20200101','YYYYMMDD')
"""

df = pd.read_sql(sql, connection)
print(df.shape)
print('-'*25)

df.to_csv('SQL_Data.csv', sep=';', decimal='.', index=False)


##################################################
### Reading Data with SQL - If data is so large
##################################################

# Suppose you have a valid connection string called conneciton
sql = """
SELECT * 
FROM SCHEME.TABLE
WHERE DATE_COLUMN BETWEEN TO_DATE('20200101','YYYYMMDD') AND TO_DATE('20200131','YYYYMMDD')
"""

chunk = 25000
df_chunk = pd.read_sql(sql, connection, chunksize=chunk)

for ind, df in enumerate(df_chunk):
	print((ind+1)*chunk, end='\r')
	df.to_csv('SQL_Data.csv', sep=';', decimal='.', mode='a', header=(ind==0) )


##################################################
### Reading Data with SQL - If IN operator has over 1000 values
##################################################

my_list = df_key['KEY_COLUMN'].drop_duplicates().to_list()
print(len(my_list))

# Suppose len(my_list) is over 1000, then SQL with a regular query will riase an error
# Therefore, we create a for loop for each 1000 value and append the results
df = pd.DataFrame()
for i in range(0, len(my_list), 1000):
	to_search = ','.join([str(e) for e in my_list[i:i+1000]]) # for strings:  str(e)  >>>  "\'" + str(e) + "\'" 
	
	sql = f"""
	SELECT * 
	FROM SCHEME.TABLE
	WHERE THE_COLUMN IN ({to_search})
	"""

	df = df.append( pd.read_sql(sql, connection) )
	print( (i/1000) + 1, df.shape, end='\r' )

print('-'*25)
print(df.shape)
print('-'*25)

