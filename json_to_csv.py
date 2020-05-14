import csv
import json
import sys

inputFile = open(/Users/Shelomov/PycharmProjects/Plotting Crypto Data/bitmex_xbtusd_orderbook.json) #open json file
outputFile = open(fileOutput, 'w') #load csv file
data = json.load(inputFile) #load json content
inputFile.close() #close the input file
output = csv.writer(outputFile) #create a csv.write
output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row