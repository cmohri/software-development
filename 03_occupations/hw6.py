#Team Yellow
#Clara Mohri, Daniel Keriazis
#SoftDev1 pd07
#K06 --StI/O: Divine your Destiny!
#2018-09-14

from random import random

# Returns the contents of the file with name `file`
def read_file(file):
    with open(file) as f:
        return f.read()

# Parse a CSV row with contents `csv_row`
def parse_csv_row(csv_row):
    row = []
    cell = ''
    in_quotes = False
    for i in csv_row:
        if i == '"':
            in_quotes = not in_quotes
        elif i == ',' and not in_quotes:
            row.append(cell)
            cell = ''
        else:
            cell += i
    row.append(cell)
    return row

# Adds the csv row `row` into `weights`
# using entry 1 as a weight and entry 0 as a value
def add_weight(weights, row):
    weights[float(row[1])] = row[0]

# Has an `n` chance of returning True, where `n` is a float
def chance(n):
    return random() < n

# Returns a value of `weights`
# using its corresponding key as a percentage
def weighted_choice(weights): # THIS CODE WILL NOT WORK (I think)
    max_weight = 100
    for weight in weights:
        if chance(weight / max_weight):
            return weights[weight]
        else:
            max_weight -= weight
    return None # If percentages don't add up to 100

# Converts `csv` to a weighted list
def csv_to_weighted_list(csv):
    lines = csv.split('\n')
    # Remove the first and last lines,
    # which are a header and total, respectively
    lines = lines[1:-2]
    weights = {}
    for line in lines:
        row = parse_csv_row(line)
        add_weight(weights, row)
    return weights

# Read 'occupations.csv' and return an occupation based on its weight
def main():
    
    occupations = read_file("occupations.csv")
    print(weighted_choice(csv_to_weighted_list(occupations)))

main()
