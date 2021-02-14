def print_comparison(name, dates, times, original_data, computed_data):
    """
    Print a comparison between original and computed time series

    Parameters:
        name: A string name for data being compared (limited to 9 chars)
        dates: List of strings representing dates for data
        times: List of strings represengint times for data
        original_data: List of orginal data (floats)
        computed_data: List of computed data (floats)
    """

    # Output comparison of data
    print(f' Date    Time  {name.upper():>9} {name.upper():>9} Difference')
    print('               original  compute')
    print('------- ------ --------- --------- ----------')

    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = comp - orig
        print(f'{date} {time:>6} {orig:9.3f} {comp:9.3f} {diff:10.3f}')

