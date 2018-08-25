#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:59:35 2018

@author: lukeiorio
"""

#PyPoll

import os
import csv
from collections import Counter

csv_file_path = os.path.join("election_data.csv")
file_output = "election_summary.txt"




VoterID = []
County = []
Candidate = []

with open(csv_file_path,newline="") as csvfile:
	csvreader = csv.reader(csvfile,delimiter=",")
	next(csvreader,None)
	for row in csvreader:
		VoterID.append(row[0])	
		County.append(row[1])
		Candidate.append(row[2])


totVotes = len(Candidate)
dictCountCand = Counter(Candidate)


with open (file_output, 'w') as file:


    file.write("Election Results")
    file.write("_______________________")
    file.write("Total Votes: "+str(len(Candidate)))
    file.write("_______________________")
    for x in dictCountCand.keys():
        file.write(x+": "+"{:5.2f}".format(100.*dictCountCand[x]/float(totVotes))+"%"+" ("+str(dictCountCand[x])+")" )
    file.write("_______________________")
    file.write("Winner: " + max(dictCountCand,key=dictCountCand.get) )
    file.write("_______________________")


