# Column naems and column indices to read
columns = {'date':0, 'time':1, 'tempout':2}

# Datatypes for each column
types = {'tempout': float}

# Initialize my data variable
data = {}
for column in columns:
    data[column] = []

# Read the data fiel
filename = "data/wxobs20180821.txt"

with open(filename, 'r') as datafile:

    # read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    # Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

# Debug
print(data['tempout'])
