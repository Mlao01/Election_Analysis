# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of election based on popular vote

import csv
import os

# Assign a var for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a var to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # print each row in the CSV file.
    for row in file_reader:
        headers= next(file_reader)
        print(headers)


