import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('assignment data.csv')

# Calculate the average price
average_price = df['price'].mean()

# Filter the DataFrame to include only properties sold for less than the average price
filtered_df = df[df['price'] < average_price]

# Write the filtered data to a new CSV file
filtered_df.to_csv('filtered-sales-data.csv', index=False)

print(f"Filtered data saved to 'filtered-sales-data.csv'.")
