# Column naems and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# Datatypes for each column
types = {'tempout': float, 'humout':float, 'heatindex':float}

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

# Compute heatindex 
def compute_heatindex(t, hum):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = hum / 100
    hi = (a + (b * t) + (c * rh) + (d * t *rh) - (e * t ** 2) + 
          (f * rh ** 2) + (g * rh * t ** 2) + (h * t * rh ** 2) +
          (i * t ** 2 * rh ** 2))

    return hi


# Running function to compute heatindex
heatindex = []
for temp, humout in zip(data['tempout'],data['humout']):
    heatindex.append(compute_heatindex(temp, humout))

# Output comparison of data
print(' Date    Time  Heatindex Heatindex Difference')
print('               original  compute')
print('------- ------ --------- --------- ----------')

zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_orig, hi_comp in zip_data:
    hi_diff = hi_comp - hi_orig
    print(f'{date} {time:>6} {hi_orig:9.3f} {hi_comp:9.3f} {hi_diff:10.3f}')

# DEBUG
#for windchill_data, windchill_comp in zip(data['windchill'],windchill):
#    print(f'{windchill_data:.5f} {windchill_comp:.5f} {windchill_data-windchill_comp:.5f}')
