# import pandas as pd
# import os


# df = pd.read_excel('sales.xlsx', sheet_name=0, usecols=[0,1, 3])

# df - > DataFrame
# df = pd.read_excel('sales.xlsx', sheet_name='Satis')
# print(df.head())


#.to_excel(file_name, index=False, sheet_name='Satis')

# data1 = {'Name':['Ali','Vali'], 'Age':[25, 30]}
# data2 = {'Name':['Sakit','Osman'], 'Age':[25, 30]}

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# with pd.ExcelWriter('data.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='Sheet 1', index=False)
#     df2.to_excel(writer, sheet_name='Sheet 2', index=False)

# df = pd.read_excel('sales.xlsx',sheet_name=0)
# high_sales = df[df['Total'] >= 1000]
# print(high_sales)

# high_unitcost = df[(df['UnitCost'] == 1.99) | (df['Total'] > 200)]
# high_unitcost = df[(df['UnitCost'] == 1.99) & (df['Total'] > 200)]

# print(high_unitcost)


# df = pd.read_excel('sales_updated.xlsx',sheet_name=0)
# print(df.head(10))
# # df['Profit'] = df['Total'] - df['Units'] * df['UnitCost']
# # df.to_excel('sales_updated.xlsx', sheet_name='Satis', index=False)

# #.sum() - Cem
# sum_total = df['Total'].sum()

# #.mean() - Ededi orta
# mean_total = df['Total'].mean()
# # print(mean_total)

# #.sort_values() - Sortlamaq ucun. ascending = True -> Artan sira, deyilse azalan sira
# # print(df.sort_values(by='Units', ascending=False))
# df_clean = df.dropna() # N/A -> None
# print(df_clean)

#excel faylini oxumaq +
#Profit sutunu yaratmaq
# sortlamaq(Profit) azalan
# top 10 data (.head(10))
#Excel faylina elave etmek