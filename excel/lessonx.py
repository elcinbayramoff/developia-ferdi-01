import pandas as pd

df = pd.read_excel('sales.xlsx',sheet_name=0)
# # print(df.head(10))
# # print(df.sort_values(by='Units', ascending=False).head(5))

# # print(df.sort_values(by='Units', ascending=False)['Total'].sum())
# total_by_region = df.groupby("Region")['Total'].sum().reset_index()
# print(total_by_region['Total'].sum())

# pivot_table = df.pivot_table(values='Units',index='Rep',columns='Region',aggfunc='sum',fill_value=0)
# print(pivot_table)

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

df['Month'] = df['OrderDate'].dt.month
df['Year'] = df['OrderDate'].dt.year
df['Day'] = df['OrderDate'].dt.day

# print(df[['OrderDate','Month','Year']])
# print(df)
# monthly_total = df.groupby('Month')['Total'].sum().reset_index()
# print(monthly_total)
# best_month = monthly_total.loc[monthly_total['Total'].idxmax()]
# print(f'Best month: {int(best_month['Month'])} with the total of {round(best_month['Total'])}$')

# quarter1_2024 = df[
#     (df['Year']==2025) 
#         & 
#     (df['Month'].isin([1,2,3,4,5,6]))
#     ]
# print(quarter1_2024)

