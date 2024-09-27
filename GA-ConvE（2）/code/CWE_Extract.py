import csv
import string

# Define the words to be excluded
excludes = {'a', 'an', 'also', 'and', 'in', 'more',
            'on', 'the', 'to', 'or', 'of', 'not', 'are', 'is', 'it', 'does', 'as', 'for', 'be', 'from', 'can', 'by',
            'has', 'with',
            'been', 'that', 'this', 'but', 'when', 'which', 'within', 'properly', 'such', 'other', 'may', 'was', 'if',
            'its', 'all',
            'have'
            }

def main():
    # Create a dictionary to store word frequencies
    word_counts = {}

    # Read the CSV file
    with open('../data/cwe_data.csv', 'r', encoding='latin-1') as file:
        reader = csv.reader(file)

        # Skip the header row of the CSV file
        next(reader)

        # Process each row of data
        for row in reader:
            # Get the second column, convert to lowercase, and remove punctuation
            words = row[1].lower().translate(str.maketrans('', '', string.punctuation)).split()

            # Count word frequencies, excluding specified words
            for word in words:
                if word not in excludes:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

    # Sort the words by frequency in descending order and get the top 50 frequent words
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:50]

    # Create a new dictionary to store the top frequent words
    top_words_dict = {}

    # Store the top frequent words in the new dictionary
    for word, count in top_words:
        top_words_dict[word] = count

    # Process the second column of the CSV file and compare it with the dictionary data
    with open('../data/cwe_data.csv', 'r', encoding='latin-1') as file:
        reader = csv.reader(file)

        # Create a list to store the output data
        output_data = []

        # Process each row of data
        for row in reader:
            # Get the second column, convert to lowercase, and remove punctuation
            words = row[1].lower().translate(str.maketrans('', '', string.punctuation)).split()

            # Get the first element of each row as the prefix
            prefix = row[0]

            # Compare with the words in the dictionary
            output_row = [prefix]  # Add prefix

            for word, _ in top_words:
                if word in words:
                    output_row.append('1')
                else:
                    output_row.append('0')

            # Add the processed row to the output list
            output_data.append(output_row)

    # Write the output data to a new CSV file
    with open('../data/CWE_Matrix.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(output_data)

if __name__ == "__main__":
    main()
