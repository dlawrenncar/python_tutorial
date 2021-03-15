from mysci.readdata import read_data
from mysci.printdata import print_comparison
from mysci.computation import compute_dewpoint

# Column naems and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'dewpt':6}

# Datatypes for each column
types = {'tempout': float, 'humout':float, 'dewpt':float}

# Read data
data = read_data(columns, types=types)

# Running function to compute dewpoint temperature
dewpointtemp = [compute_dewpoint(t,h) for t, h in zip(data['tempout'], data['humout'])]

print_comparison('Dewpoint', data['date'], data['time'], data['dewpt'],
    dewpointtemp)
