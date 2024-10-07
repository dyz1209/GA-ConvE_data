import pandas as pd
import itertools

# Read the CSV file
df = pd.read_csv('../data/kg_data.csv',encoding='latin-1')

# Get the last column as the category column
category_column = df.columns[-1]

# Remove rows where the category is 'NULL'
df = df[df[category_column] != 'NULL']

# Store the final results
all_combinations = []

# Group the data based on the last column (category)
grouped = df.groupby(category_column)

# Iterate through each category
for category, group in grouped:
    # Get the elements from the first column for this category
    elements = group.iloc[:, 0].tolist()

    # Generate all pairwise combinations, filtering out pairs with identical elements
    combinations = list(itertools.combinations(elements, 2))

    # Filter out combinations where Element1 and Element2 are the same, and ensure uniqueness within the same category
    unique_combinations = set([comb for comb in combinations if comb[0] != comb[1]])

    # Add the unique combinations to the final result
    all_combinations.extend(list(unique_combinations))

# Convert to a list and create a new DataFrame
output_df = pd.DataFrame(all_combinations, columns=['Element1', 'Element2'])

# Save the result to a new CSV file
output_df.to_csv('../data/Relation_Matrix.csv', index=False)
