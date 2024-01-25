import pandas as pd
import numpy as np

# Read the Excel file
df = pd.read_excel("Accounting Dataset.xlsx", names=["Name", "Monthly Income ($)"], thousands=',')
print(df)
# Display summary statistics
print(df.describe())

# Calculate the 25th percentile (Q1)
q1 = df['Monthly Income ($)'].quantile(0.25,interpolation='lower')
print(f"The 25th percentile of Monthly Income is: {q1}")
# Minimum Quantile 0th
print(df['Monthly Income ($)'].quantile(0))
 # Maxmum Quantile 1th
print(df['Monthly Income ($)'].quantile(1))
print('Use quantile To Remove the Outliear')

percentile_99=df['Monthly Income ($)'].quantile(0.99)
print(f"The 99th Percentile Value Is :{percentile_99}")
# Here tht Outliner Is Removed 
df_no_outliner=df[df['Monthly Income ($)']>percentile_99]
print(df_no_outliner)
# Valid Value Which is Less than the outliner 
def_Valid_Outliner=df[df['Monthly Income ($)']<=percentile_99]
print("Valid Outliner ",def_Valid_Outliner)


# Fill Out The missing Value
print("Filling Out THe rMissing Value :")
print(df)
df['Monthly Income ($)'][3]=np.NaN
print(df)
df_new=df.fillna(df['Monthly Income ($)'].mean())
# It will Take Very Big Value 
print(df_new)
# Instead We Will Do Meadian for Geting Aprox Value 
df_new=df.fillna(df['Monthly Income ($)'].median())
print(df_new)
