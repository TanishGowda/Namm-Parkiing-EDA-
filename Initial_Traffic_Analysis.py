# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 08:51:41 2025

@author: tanis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

df = pd.read_csv('Bengaluru_Traffic.csv')
a = df.head()

imp_stats = df.describe()
df.info()

df.isna()
clean_data = df.dropna()

df.duplicated()
df.duplicated().sum()

final_data = df.drop_duplicates()

# Some Important Initial Visualizations

print(final_data['Date'].dtype)
final_data['Date'] = pd.to_datetime(final_data['Date'])
print(final_data['Date'].dtype)

final_data['Year'] = final_data['Date'].dt.year
grouped_data = final_data.groupby('Year')['Traffic Volume'].sum().reset_index()


# Traffic Volume by Year

plt.bar(grouped_data['Year'],grouped_data['Traffic Volume'])
plt.xlabel('Year')
plt.ylabel('Volume of Traffic')
plt.title('Traffic Volume by Year')
plt.show()


# Traffic Volume by Area

grouped_data_area = final_data.groupby('Area Name')['Traffic Volume'].sum().reset_index()
plt.bar(grouped_data_area['Area Name'], grouped_data_area['Traffic Volume'])
plt.xlabel('Area')
plt.ylabel('Volume of Traffic')
plt.title('Traffic Volume by Area')
plt.xticks(rotation=90)
plt.show()


# Traffic Volume by Weather

grouped_data_weather = final_data.groupby('Weather Conditions')['Traffic Volume'].sum().reset_index()
plt.bar(grouped_data_weather['Weather Conditions'], grouped_data_weather['Traffic Volume'])
plt.xlabel('Weather')
plt.ylabel('Volume of Traffic')
plt.title('Traffic Volume by Weather Condition')
plt.show()

plt.figure(figsize=(7,7))
plt.pie(grouped_data_weather['Traffic Volume'], labels=grouped_data_weather['Weather Conditions'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title('Traffic Volume by Weather')
plt.axis('equal')
plt.show()


# Parking Usage by Area

data_on_parking = final_data.groupby('Area Name')['Parking Usage'].sum().reset_index()
plt.bar(data_on_parking['Area Name'], data_on_parking['Parking Usage'])
plt.xlabel('Area')
plt.ylabel('Parking Usage')
plt.title('Parking Usage by Area')
plt.xticks(rotation=90)
plt.show()

data_on_parking_mean = final_data.groupby('Area Name')['Parking Usage'].mean().reset_index()
plt.bar(data_on_parking_mean['Area Name'], data_on_parking_mean['Parking Usage'])
plt.xlabel('Area')
plt.ylabel('Average Parking Usage')
plt.title('Parking Usage by Area')
plt.xticks(rotation=90)
plt.show()


# Parking Usage by Area (Detailed)

data_on_parking_detailed = final_data.groupby(['Area Name','Road/Intersection Name'])['Parking Usage'].mean().reset_index()
data_on_parking_detailed_sum = final_data.groupby(['Area Name','Road/Intersection Name'])['Parking Usage'].sum().reset_index()

data_on_parking_detailed_sum.to_csv('Areawise_Parking_Usage.csv', index=False)
final_data.to_csv('Final_Dataset.csv', index=False)
