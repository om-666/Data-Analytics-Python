import pandas as pd

# Read the CSV file with header and specify data types
df = pd.read_csv("AB_NYC_2019.csv", names=['id', 'name', 'host_id', 'host_name', 'neighbourhood_group', 'neighbourhood', 'latitude', 'longitude', 'room_type', 'price', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365'], dtype={'name': str, 'price': str})

# Convert "price" column to numeric, ignoring errors
df['price'] = pd.to_numeric(df['price'], errors='coerce')


# Display summary statistics
print(df.describe())

# Inspect the first few rows of the DataFrame
print(df.head())

# Remove Quantile value
PriceTrim = df["price"].quantile(0.99)
print("99% of the Value is", PriceTrim)

# Filter the DataFrame based on the quantile value
df_Valid_Outliner = df[df['price'] <= PriceTrim]
print(df_Valid_Outliner)

# Export the filtered DataFrame to an Excel file
df_Valid_Outliner.to_excel("filtered_data.xlsx", index=False)
