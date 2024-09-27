import csv

def main():
    # Open the CSV file for reading and open the txt file for writing
    with open('../data/kg_data.csv', mode='r', encoding='ISO-8859-1') as csv_file, open('../data/Triplets.txt', mode='w', encoding='ISO-8859-1') as txt_file:
        csv_reader = csv.reader(csv_file)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            A = row[0]
            B = row[1]
            C = row[2]
            D = row[3]
            E = row[4]

            # Skip the row if E is 'NULL'
            if E == 'NULL':
                continue

            # Construct triplet relationships and write to the txt file
            txt_file.write(f"{A} Has {B}\n")
            txt_file.write(f"{B} Related {C}\n")
            txt_file.write(f"{E} Exploits {A}\n")
            txt_file.write(f"{E} Associated {D}\n")

if __name__ == "__main__":
    main()
