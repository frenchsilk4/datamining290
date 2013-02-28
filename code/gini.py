#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import collections
import csv

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures

############### Read through files
pcnt = Counter()
zipcnt = Counter()
temp2 = 0.0
zipDict = Collections.defaultdict(Counter)
 ###
# TODO: calculate the values below:
gini = 0  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        # Gini Index

        row[cand_nm], row[contbr_zip]
        candidate = row[cand_nm]

        pcnt[candidate] = +1
        zipDict['contbr_zip'] += Counter([row[cand_nm]])

        ##/
# sum of all the candidates in the Data set
sumOfCandidates = sum(pcnt.values())

# Calculating current Gini Index using candidate name as the class
for val in pcnt.values:
	 temp += val/float(sumOfCandidates))**2
gini = 1 - temp2

# Calculating the weighted average of the Gini Indexes using candidate names, split up by zip codes
for eachZip in zipDict.values():
	candsVistByzip = sum(eachZip.values())
	for eachCand in eachZip.values():
		sumOfCandVist += (eachCand/ float candVistByzip)**2
	split_gini += (candsVistByzip/sumOfCandidates)*(1-sumOfCandVist)

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
