def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Station data file

    Parameters:
        columns: A dictionary of cooumn names mnapping to clumn indices
        types: A dictionary of columnn names mapping to the types to which to 
               convert each column of data
        filename: A string pth pointing to the CU Boulder Weather Station data file
    """
    
    # Initialize my data variable
    data = {}
    for column in columns:
        data[column] = []

    # Read the data fiel

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

    return data
