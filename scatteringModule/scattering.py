#scattering module
from statistics import mean
from math import sqrt

def Avg(data):
    avg = mean(data)
    return avg

def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg)**2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd