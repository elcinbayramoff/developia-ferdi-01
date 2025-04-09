import pandas as pd

#Task1
# def search_malin_adi(dataframe, text):
#     mask = dataframe['Malın adı'].str.contains(text, case=False, na=False)
#     results = dataframe[mask]
#     return results

# df = pd.read_excel('data1.xlsx', sheet_name=0)

# search_text = input('Axtarılacaq sözü daxil edin: ')
# results = search_malin_adi(df, search_text)

# print(results[['Sorgu nömrəsi','Malın adı']])

#Task2
# df = pd.read_excel('data1.xlsx', sheet_name=0)

# conversion_rates = {
#     'USD':1,
#     'EUR':1.121198,
#     'RUB':0.01069,
#     'CNY':0.1381,
#     'TRY':0.03083

# }
# # def func(row):
# #     return round(row['Faktura dəyəri'] * conversion_rates[row['Valyuta']], 2)


# df['Faktura dəyəri (USD)'] = df.apply(
#     lambda row: round(row['Faktura dəyəri'] * conversion_rates[row['Valyuta']], 2),
#     axis=1
# )

# matching_rows = df[df['Faktura dəyəri (USD)'] == round(df['Statistik dəyəri'],2) ]

# print(matching_rows[['Sorgu nömrəsi','Valyuta','Faktura dəyəri','Faktura dəyəri (USD)','Statistik dəyəri']])

#Task3

# df = pd.read_excel('data1.xlsx', sheet_name=0)

# def calculate_emeliyyat_haqqi(gomruk_deyeri):
#     if gomruk_deyeri <= 1000:
#         return 30
#     elif gomruk_deyeri <= 10000:
#         return 120
#     elif gomruk_deyeri <= 50000:
#         return 240
#     elif gomruk_deyeri <= 100000:
#         return 400
#     elif gomruk_deyeri <= 500000:
#         return 600
#     elif gomruk_deyeri <= 1000000:
#         return 1200
#     else:
#         return 2000
    
# df['Əməliyyat yeni'] = df['Gomruk dəyəri'].apply(calculate_emeliyyat_haqqi)
# uygunsuzlar = df[df['Əməliyyat yeni'] != df['Əməliyyat haqqı']]
# print(uygunsuzlar[['Əməliyyat yeni','Əməliyyat haqqı']])

# df = pd.read_excel('data1.xlsx', sheet_name=0)

# df['Uygunsuzluq'] = df.apply(
#     lambda row: True if row['Imtiyaz'] == "210"  and (not row['Tic. edən ölkənin kodu']==row['Mənşə ölkəsinin kodu']==row['Gondərən ölkənin kodu']) else False,
#     axis=1)


# # True if 5 > 4 else False
# print(df[['Uygunsuzluq','Imtiyaz']][df['Uygunsuzluq']==True])


def calculate_emeliyyat_haqqi(gomruk_deyeri):
    if gomruk_deyeri <= 1000:
        return 30
    elif gomruk_deyeri <= 10000:
        return 120
    elif gomruk_deyeri <= 50000:
        return 240
    elif gomruk_deyeri <= 100000:
        return 400
    elif gomruk_deyeri <= 500000:
        return 600
    elif gomruk_deyeri <= 1000000:
        return 1200
    else:
        return 2000
    
# df = pd.read_excel('data1.xlsx', sheet_name=0)

# print(df.head()) # min, max, mean, count
# grouped_df = df.groupby('Sorgu nömrəsi').agg({'Gomruk dəyəri':'sum', 'Əməliyyat haqqı':'sum'}).reset_index()
# grouped_df['Calculated Əməliyyat haqqı'] = grouped_df['Gomruk dəyəri'].apply(calculate_emeliyyat_haqqi)

# grouped_df['Uygunsuqluq'] = grouped_df['Calculated Əməliyyat haqqı'] != grouped_df['Əməliyyat haqqı']

# df = pd.merge(df, grouped_df[['Sorgu nömrəsi','Uygunsuqluq','Calculated Əməliyyat haqqı']], on='Sorgu nömrəsi', how='left')
# print(df)

# df.to_excel('Grouped_data.xlsx')

df = pd.read_excel('data1.xlsx', sheet_name=0)

# grouped_df = df.groupby('Malın kodu').agg({'Gomruk dəyəri':'min'}).reset_index()

# grouped_df['Min Gomruk Deyeri'] = grouped_df['Gomruk dəyəri']
# merged_df = pd.merge(df, grouped_df[['Malın kodu','Min Gomruk Deyeri']], on='Malın kodu', how='left')
# merged_df = merged_df[merged_df['Gomruk dəyəri'] == merged_df['Min Gomruk Deyeri']][['Sorgu nömrəsi','Gomruk dəyəri','Malın kodu', 'Malın adı']]
# print(merged_df.head(25))
# a = int(input('Malın kodunu daxil edin: ')) # 4016995200
# result = merged_df[merged_df['Malın kodu']==a]['Sorgu nömrəsi']
# print(result)

# searching(duyu) -> DataFrame
# Malin koduna uygun filtrleme -> DataFrame

# df['1 cut netto'] = df.apply(
#     lambda row: row['Netto cəkisi'] / row['Malın miqdarı 1'] if row['Ölcu vahidi 1'] == 'cüt' else None,
#     axis=1
# )

# print(df[['Malın adı','Netto cəkisi','Malın miqdarı 1','Ölcu vahidi 1', '1 cut netto']][df['Ölcu vahidi 1'] == 'cüt'])

df['1 cut netto'] = df.apply(
    lambda row: row['Netto cəkisi'] / row['Malın miqdarı 1'],
    axis=1
)

print(df[['Malın adı','Netto cəkisi','Malın miqdarı 1','Ölcu vahidi 1', '1 cut netto']][df['Ölcu vahidi 1'] == 'cüt'])
