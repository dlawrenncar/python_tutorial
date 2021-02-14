from mysci.readdata import read_data
from mysci.printdata import print_comparison
from mysci.computation import compute_heatindex

# Column naems and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# Datatypes for each column
types = {'tempout': float, 'humout':float, 'heatindex':float}

# Read data
data = read_data(columns, types=types)

# Running function to compute heatindex
heatindex = []
for temp, humout in zip(data['tempout'],data['humout']):
    heatindex.append(compute_heatindex(temp, humout))

print_comparison('Heatindex', data['date'], data['time'], data['heatindex'],
    heatindex)
# DEBUG
#for windchill_data, windchill_comp in zip(data['windchill'],windchill):
#    print(f'{windchill_data:.5f} {windchill_comp:.5f} {windchill_data-windchill_comp:.5f}')
