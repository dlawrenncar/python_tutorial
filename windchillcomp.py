from readdata import read_data
from printdata import print_comparison
from computation import compute_windchill

# Column naems and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Datatypes for each column
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Read data from file
data = read_data(columns, types=types)

# Running function to compute windchill index
windchill = []
for temp, windspeed in zip(data['tempout'],data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

print_comparison('Windchill', data['date'], data['time'], data['windchill'], windchill)
# DEBUG
#for windchill_data, windchill_comp in zip(data['windchill'],windchill):
#    print(f'{windchill_data:.5f} {windchill_comp:.5f} {windchill_data-windchill_comp:.5f}')
