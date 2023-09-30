import pandas as pd
import re
# Function to extract numerical part from price
def extract_numeric_price(price_str):
    numeric_part = re.search(r'[\d.]+', price_str)
    if numeric_part:
        return float(numeric_part.group())
    return None

# Merging the three csv files into one dataframe
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')
df = pd.concat([df1, df2, df3])

# Filtering out the rows where product is not pink morsel
df = df[df['product'] == 'pink morsel']

# merging quantity and price columns into sales column by multiplying them

# Apply the function to extract numeric prices and perform multiplication
df['sales'] = df.apply(lambda row: extract_numeric_price(row['price']) * row['quantity'] if isinstance(row['quantity'], int) else row['price'], axis=1)

# Dropping the quantity and price columns
df = df.drop(['quantity', 'price'], axis=1)

# dropping the product column as there is only one product
df = df.drop(['product'], axis=1)

# converting dataframe into csv file
df.to_csv('data/pink_morsel_sales.csv', index=False)
