#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv
import math

total = 0
minVal = 0
maxVal = 0
meanVal = 0
medVal = 0
stDev = 0
count = 0

#Array of the contribution amounts
contb_receipt_amt =[]

#candidates
canDidates = []

for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        total += float(row[9])
        count = count +1
        contb_receipt_amt.append(float(row[9]))

        # Store unique candidate values
        if row[2] not in canDidates:
            canDidates.append(str(row[2])) 

        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/
minVal = min(contb_receipt_amt)
maxVal = max(contb_receipt_amt)
meanVal = total / count

contb_receipt_amt.sort()

# Calculates the median value
i = len(contb_receipt_amt)/2
if len(contb_receipt_amt)%2 == 0:
    medVal = (contb_receipt_amt[i-1]+ contb_receipt_amt[i])/2.0
else:
    medVal = contb_receipt_amt[i]

# calculates the variance and standard deviation
v = sum([pow(meanVal - i,2)for i in contb_receipt_amt])
stDev = (v/count)**0.5


###
# TODO: aggregate any stored numbers here
#
##/

##### Print out the stats
print "Total: %s" % total
print "Minimum: %s" % minVal
print "Maximum: %s" % maxVal
print "Mean: %s" % meanVal
print "Median: %s" %medVal
# square root can be calculated with N**0.5
print "Standard Deviation: %s" %stDev

##### Comma separated list of unique candidate names
print "Candidates: %s" %canDidates

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations

    norm = ((value - minVal)/(maxVal - minVal))* ((1-0)+0)

    ###/
    
    return norm

# calculates the z score
def zscore_normalize(value):
    z= ((value - meanVal)/ stDev)
    return z


##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])
print "Z-max score: %r" % map(zscore_normalize, [2500, 50, 250, 35, 8, 100, 19])
