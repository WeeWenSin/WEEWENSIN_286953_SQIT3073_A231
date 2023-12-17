import os
os.system('cls')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

adequacy = pd.read_excel(io= '4.4.xlsx', engine="openpyxl", sheet_name='4.4', skiprows=3)
adequacy.replace('nan',np.nan,inplace=True)
adequacy_clean = adequacy.drop(1)
adequacy_clean['Akhir tempoh/End of period'] = adequacy_clean['Akhir tempoh/End of period'].replace('nan',pd.NA).ffill()
adequacy_clean = adequacy_clean.rename(columns={"Unnamed: 1":"Period"})

# Life Insurance Company
unwanted_columns = [
    ('Penanggung Insurans Am/General Insurance Companies'),
    ('Unnamed: 6'),
    ('Unnamed: 7'),
    ("Penanggung Insurans Komposit2/Composite2 Insurance Companies"),
    ("Unnamed: 9"),
    ("Unnamed: 10"),
    ("Keseluruhan Industri/Consolidated Industry"),
    ("Unnamed: 12"),
    ("Unnamed: 13")
]

# Drop unwanted columns
adequacy_LIC = adequacy_clean.drop(columns=unwanted_columns)
adequacy_LIC = adequacy_LIC.dropna()
adequacy_LIC = adequacy_LIC.rename(columns={"Penanggung Insurans Hayat/Life Insurance Companies":"Jumlah Modal Sedia Ada3/Total Capital Available3"})
adequacy_LIC = adequacy_LIC.rename(columns={"Unnamed: 3":"Jumlah Modal Dikehendaki3/Total Capital Required3"})
adequacy_LIC = adequacy_LIC.rename(columns={"Unnamed: 4":"Nisbah Kecukupan Modal/Capital Adequacy Ratio (%)"})
print("Life Insurance Company:")

# Filter data
LIC_2023 = adequacy_LIC[adequacy_LIC['Akhir tempoh/End of period'] == 2023.0]

# Print Life Insurance Companies 
print(LIC_2023)
print("\n\n")

# Plot grouped barchart
width = 0.4
x_ca=[x-width for x in range(len(LIC_2023['Jumlah Modal Sedia Ada3/Total Capital Available3']))]
x_cp=[x for x in range(len(LIC_2023['Jumlah Modal Dikehendaki3/Total Capital Required3']))]
fig,ax = plt.subplots(figsize=(10,6))
bar1 = ax.bar(x_ca,LIC_2023['Jumlah Modal Sedia Ada3/Total Capital Available3'],width,color='plum',label='Total Capital Available')
bar2 = ax.bar(x_cp,LIC_2023['Jumlah Modal Dikehendaki3/Total Capital Required3'],width,color='purple',label='Total Capital Required')
for bar, value in zip(bar1, LIC_2023['Jumlah Modal Sedia Ada3/Total Capital Available3']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{value:.2f}', ha='center', va='center', color='white')
for bar, value in zip(bar2, LIC_2023['Jumlah Modal Dikehendaki3/Total Capital Required3']):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{value:.2f}', ha='center', va='center', color='white')

# Plot line graph
ax2 = ax.twinx()
ax2.plot(LIC_2023["Period"],LIC_2023['Nisbah Kecukupan Modal/Capital Adequacy Ratio (%)'],'o-',color='palevioletred',linewidth=3,label='Capital Adequacy Ratio')
for i, val in enumerate(LIC_2023['Nisbah Kecukupan Modal/Capital Adequacy Ratio (%)']):
    ax2.annotate(f'{val:.2f}', (LIC_2023["Period"].iloc[i], val), textcoords="offset points", xytext=(0, 10), ha='center',color='darkgrey',fontweight='bold')

plt.title('Capital Adequacy Ratio of Life Insurance Company in Year 2023')
plt.xlabel('Quarter')
ax.set_ylabel('RM million')
ax2.set_ylabel('Ratio(%)')
ax.legend(loc='upper left', bbox_to_anchor=(0.85, 1.0))
ax2.legend(loc='upper left', bbox_to_anchor=(0.85, 0.9)) 
plt.show()

# General Insurance Company
unwanted_columns = [
    ('Penanggung Insurans Hayat/Life Insurance Companies'),
    ('Unnamed: 3'),
    ('Unnamed: 4'),
    ("Penanggung Insurans Komposit2/Composite2 Insurance Companies"),
    ("Unnamed: 9"),
    ("Unnamed: 10"),
    ("Keseluruhan Industri/Consolidated Industry"),
    ("Unnamed: 12"),
    ("Unnamed: 13")
]

# Drop unwanted columns
adequacy_GIC = adequacy_clean.drop(columns=unwanted_columns)
adequacy_GIC = adequacy_GIC.dropna()
adequacy_GIC = adequacy_GIC.rename(columns={"Penanggung Insurans Am/General Insurance Companies":"Jumlah Modal Sedia Ada3/Total Capital Available3"})
adequacy_GIC = adequacy_GIC.rename(columns={"Unnamed: 6":"Jumlah Modal Dikehendaki3/Total Capital Required3"})
adequacy_GIC = adequacy_GIC.rename(columns={"Unnamed: 7":"Nisbah Kecukupan Modal/Capital Adequacy Ratio (%)"})

# Print General Insurance Companies
print("General Insurance Company:")
GIC_2023 = adequacy_GIC[adequacy_GIC['Akhir tempoh/End of period'] == 2023.0]
print(GIC_2023)
print("\n\n")

# plot pyramid graph
lefth=GIC_2023["Jumlah Modal Dikehendaki3/Total Capital Required3"]*-1
fig2 = plt.figure(figsize=(10,6))
GIC_2023["Capital Available(left)"] = 0
GIC_2023["Capital Available Width"] = GIC_2023["Jumlah Modal Sedia Ada3/Total Capital Available3"]
GIC_2023["Capital Required(left)"] = -GIC_2023["Jumlah Modal Dikehendaki3/Total Capital Required3"]
GIC_2023["Capital Required Width"] = GIC_2023["Jumlah Modal Dikehendaki3/Total Capital Required3"]
plt.barh(y=GIC_2023["Period"],width=GIC_2023["Capital Available Width"],color="cadetblue",label="Total Capital Available")
plt.barh(y=GIC_2023["Period"],width=GIC_2023["Capital Required Width"],left=GIC_2023["Capital Required(left)"],color="mediumaquamarine",label="Total Capital Required")
for index, value in enumerate(GIC_2023["Capital Required Width"]):
    plt.text(-value / 2, index, f'{value:.2f}', ha='center', va='center', color='black', fontsize=14)
for index, value in enumerate(GIC_2023["Capital Available Width"]):
    plt.text(value / 2, index, f'{value:.2f}', ha='center', va='center', color='black', fontsize=14)
plt.xlim(-25000,25000)
plt.xlabel('RM million')
plt.ylabel('Quarter')
plt.title('Total Capital Available and Required of General Insurance Company in Year 2023')
plt.legend()
plt.show()

# plot donut chart
plt.pie(x=GIC_2023['Nisbah Kecukupan Modal/Capital Adequacy Ratio (%)'],explode=[0.05,0.05,0.05],labels=['Q1','Q2','Q3'],autopct='%3.2f%%',shadow=True,startangle=90,colors=['rosybrown','lightcoral','indianred'])
plt.axis('equal')
plt.legend()
plt.title('Capital Adequacy Ratio of General Insurance Company in Year 2023')
donut_chart = plt.Circle(xy=(0,0),radius=.65,facecolor='white')
plt.gca().add_artist(donut_chart)
plt.show()

print("\n-------------------------------------------------------------------------------------------------")
print("Hopefully the presented visualizations does shows a clear and concise representation of the data.")
print("-------------------------------------------------------------------------------------------------")