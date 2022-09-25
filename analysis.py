import pandas as pd

excel_data_df = pd.read_excel('mass_sorted.xlsx')
indep = excel_data_df["Тип"]
dep = excel_data_df["Вес"]
N = 0
group_count = {}
group_result = {}

res = 0
counter = 0
for item in dep:
    counter = counter + 1
    res = res + item

X = res / counter
SST = 0
SSW = 0
SSB = 0

for item in dep:
    prom = (item - X) ** 2
    SST = SST + prom

for item in indep:
    if item not in group_count:
        group_count[item] = 1
    else:
        group_count[item] = group_count[item] + 1


for item in group_count:
    N = N + group_count[item]
    result_item = excel_data_df.loc[excel_data_df["Тип"] == item]
    group_result[item] = sum(result_item["Вес"]) / group_count[item]

for item in group_result:
    result_item = excel_data_df.loc[excel_data_df["Тип"] == item]
    for i in result_item["Вес"]:
        SSW = SSW + ((i - group_result[item]) ** 2)

dFSSW = N - len(group_result)

for item in group_result:
    SSB = SSB + group_count[item] * ((group_result[item] - X) ** 2)

dFSSB = len(group_result) - 1


F = (SSB / dFSSB) / (SSW / dFSSW)

print('SST =',SST)
print('SSB =',SSB)
print('dfSSB =', dFSSB)
print('SSW =',SSW)
print('dfSSW =', dFSSW)
print('F =',F)