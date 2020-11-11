# Column naems and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Datatypes for each column
types = {'tempout': float, 'windspeed':float, 'windchill':float}

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

# Compute windchill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275
    
    v16 = v**0.16
    wci = a + (b*t) - (c * v16) + (d*t*v16)
    return wci

# Running function to compute windchill index
windchill = []
for temp, windspeed in zip(data['tempout'],data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))


# DEBUG
for windchill_data, windchill_comp in zip(data['windchill'],windchill):
    print(f'{windchill_data:.5f} {windchill_comp:.5f} {windchill_data-windchill_comp:.5f}')
