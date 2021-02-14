def compute_windchill(t, v):

    """
    Compute windchill factor and wind speed
    Note: This computation is valid only for T between -45F and +45F

    Parameters:
       t: The temperature in units of F (float)
       v: The windspeed in m/s (float)
    """

    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v**0.16
    wci = a + (b*t) - (c * v16) + (d*t*v16)
    return wci


def compute_heatindex(t, hum):

    """
    Compute heat index given temperature and humidity
 
    Parameters:
       t: Temperature in degrees F (float)
       hum:  Relative humiityd in % (float)
    """

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

