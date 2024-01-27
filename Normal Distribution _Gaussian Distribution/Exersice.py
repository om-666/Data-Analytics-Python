# Remove outliers using percentile technique first. Use [0.001, 0.999] for lower and upper bound percentiles
# After removing outliers in step 1, you get a new dataframe.
# On step(2) dataframe, use 4 standard deviation to remove outliers
# Plot histogram for new dataframe that is generated after step (3). Also plot bell curve on same histogram
# On step(2) dataframe, use zscore of 4 to remove outliers. This is quite similar to step (3) and you will get exact same result
import pandas as pd
import numpy as num
import seaborn as sns
import matplotlib.pyplot as pt
# Read The Data
df=pd.read_csv("bhp.csv")
# print(df.head())
print("Describing ")
print(df.describe())
#  Using Percentle Remove Outliers 
PriceTrim=df.price.quantile(0.99)
print(PriceTrim)
print("Percentile  outliar: \n -----------------------------------------------------")
df_Valid_Percentile_Outliear=df[df.price<=PriceTrim]
print(df_Valid_Percentile_Outliear.shape)
print("UpperBound And Lower outliar: \n -----------------------------------------------------")
df_Upper_and_LowerBound = df_Valid_Percentile_Outliear[(df_Valid_Percentile_Outliear.price <= 0.999) & (df_Valid_Percentile_Outliear.price >= 0.001)]
print(df_Upper_and_LowerBound.shape)
print("Strandard Deviation outliar: \n -----------------------------------------------------")
df_Stranded_Deviation=df_Upper_and_LowerBound[(df_Upper_and_LowerBound.price <= (df_Upper_and_LowerBound.price.mean() + 3* df_Upper_and_LowerBound .price .std()) ) & (df_Upper_and_LowerBound.price >= (df_Upper_and_LowerBound.price.mean() - 3* df_Upper_and_LowerBound .price .std()))]
print(df_Stranded_Deviation.shape)
print("Histogram \n-------------------------------------")
# sns.histplot(df.price,kde=True)
# pt.show()
# sns.histplot(df_Upper_and_LowerBound.price, kde = True , bins=50)
# pt.show()
# sns.histplot(df_Stranded_Deviation.price,kde=False)
# pt.show()
print("ZScore\n -----------------------------------------------------") 
df['Zscore']=(df.price-df.price.mean())/df.price.std()
df_Outlier_Zscore=df[(df.Zscore<=4) & (df.Zscore>=-4)]
print(df_Outlier_Zscore.shape)
sns.histplot(df_Outlier_Zscore,kde=True)
pt.show()




