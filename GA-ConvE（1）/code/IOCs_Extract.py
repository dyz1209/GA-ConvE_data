import csv

# Build feature dictionary
def build_feature_dict():

    feature_dict = [
        'md5: 0839b3f0a4b28111efc94942436041cb',
        'domain: office-rb-support.com',
        'domain: video.cnhardware.info',
        'md5: 6c5c2692597b5bb0f2ecee9c9f667134',
        'ipv4: 81.95.7.12',
        'url: www.hkbytes.info/logo.gif',
        'sha1: f96bcd875836da89800912de1e557891697c7cf4',
        'domain: reg.flnet.org',
        'sha256: 834600ec1f01a039d502a5c3f315d7aac4d95554327b19da17fda30b1d57995a',
        'md5: 067681b79756156ba26c12bc36bf835c',
        'uri: /admin/form_doc/image/down/down.php',
        'domain: 126mailservice.myvnc.com',
        'md5: 0595f5005f237967dcfda517b26497d6',
        'md5: 852a9411a949add69386a72805c8cb05',
        'domain: alphacranes.com',
        'domain: updateservice.redirectme.net',
        'url: khurram.com.pk/js/drv',
        'md5: 2b07e054a1abb2941e5e70fba652a211',
        'sha256: 169f68ba605ae82cdfe11a293fe3ffd59b97e05e301096188e241ca6af3cef2c',
        'md5: 1d303d1948c59348d0352bd730ede33c',
        'url: s2.cdn-edge.net/cart.php',
        'domain: s1.cdn-edge.net',
        'sha256: 8c16ebad57e0288077ae58607b2967bf7b40761b20d783814d655280e9779e99',
        'md5: 16860f5e222ab53f52a3abfd0cb7f890',
        'domain: mmksba.simple-url.com',
        'md5: 0d195b660596810172bb3874bebcd470',
        'ipv4: 185.109.144.102',
        'url: my-homework.890m.com/bbs/data/board.php?v=a',
        'domain: www.wcomputer.org',
        'sha256: 2a25d42130837560fcff1e1e19264f05784bf9e9db6464afb15d7e26f7f4a433',
        'sha256: 9cb4b0f1330478d7748fc1f92e3150dfcb7cf958dce302e9224c235d4b6f19ed',
        'url: scan8t.com/silo/strength.php',
        'domain: saicgovcn.xyz',
        'ipv4: 209.58.185.36'
    ]
    return feature_dict

# Read CSV file row by row and compare with feature dictionary, save the results to a new CSV file
def compare_and_output(csv_filename, feature_dict, output_filename):
    """
    Read each row of the CSV file, compare the second column element with each value in the feature dictionary,
    and write the results to a new CSV file.
    """
    with open(csv_filename, mode='r', encoding='ISO-8859-1') as csv_file, open(output_filename, mode='w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(csv_file)
        writer = csv.writer(output_file)

        # Skip the header of the input file
        next(reader)

        # Process CSV row by row
        for row in reader:
            if len(row) > 1:  # Ensure the row has at least two columns
                first_element = row[0].strip()  # Read the first column element
                second_element = row[1].strip()  # Read the second column element
                output_row = [first_element]  # Initialize the output row with the first column element

                # Compare each value in the feature dictionary with the second column element
                for feature in feature_dict:
                    if feature == second_element:
                        output_row.append('1')  # Output '1' if matched
                    else:
                        output_row.append('0')  # Output '0' if not matched

                # Write the result to the output file
                writer.writerow(output_row)

# Main function
def main():
    csv_filename = '../data/IOCs_data.csv'  # Replace with the actual path to your CSV file
    output_filename = '../data/IOCs_Matrix.csv'  # Output file path

    # 1. Build the feature dictionary
    feature_dict = build_feature_dict()

    # 2. Read the CSV row by row, compare with the feature dictionary, and save the results to the output CSV
    compare_and_output(csv_filename, feature_dict, output_filename)

if __name__ == "__main__":
    main()
