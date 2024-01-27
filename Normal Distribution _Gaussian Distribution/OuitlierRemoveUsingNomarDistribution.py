import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the DataFrame
df = pd.read_csv("weight-height.csv")
print(df.head())

# Describe:
print("Describing ")
print(df.Height.describe())

# # Plot with KDE True
# print("When KDE Is True ")
# sns.histplot(df.Height, kde=True)
# # plt.show()  # Display the plot
# plt.savefig("histogramKdeTrue.png")  # Save the plot after displaying

# # Plot with KDE False
# print("When KDE Is False ")
# sns.histplot(df.Height, kde=False)
# # plt.show()  # Display the plot
# plt.savefig("histogramKdeFalse.png")  # Save the plot after displaying

# Finding Mean
# Finding Mean
mean = df.Height.mean()
print("\nMean of Height is:", mean)

# Finding Standard Deviation
std_dev = df.Height.std()
print("Standard Deviation of Height is:", std_dev)

# Print the range for values within 3 standard deviations from the mean
print("Range within 3 standard deviations:")
print("Lower bound:", mean - 3 * std_dev)
print("Upper bound:", mean + 3 * std_dev)

# Identify and print rows with outliers
outliers = df[(df.Height > mean + 3 * std_dev) | (df.Height < mean - 3 * std_dev)]
print("Rows with outliers:")
print(outliers)
print(outliers.shape)

# Filter out rows with outliers
df_no_outliers = df[(df.Height <= mean + 3 * std_dev) & (df.Height >= mean - 3 * std_dev)]
print("\nDataFrame without outliers:")
print(df_no_outliers)
print(df_no_outliers.shape)

# Display histogram with KDE False
# print("Displaying histogram with KDE False")
# sns.histplot(df_no_outliers.Height,kde=True)
# plt.savefig("After Remove_Outliear .png")
df['Zscore']=(df.Height - df.Height.mean())/std_dev
print(df.head())
df_NoOutliers_Zscore=df[(df.Zscore<=3) & (df.Zscore>=-3)]
print(df_NoOutliers_Zscore.shape)
# Outlier is Removed And Sve it in Excel Sheet 
df_NoOutliers_Zscore.to_excel("Filtereddata.xlsx",index=False)