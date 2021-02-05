# Week03 of GMIT CyberSecurity
# IDR lecturer Seamus Dowling has set us the task of comparing malware on MitreAttackNavigator
# At the same time programming lecturer Andrew Beatty has set us the task of parsing JSON output
# So, I've decided to dowload the output of my IDR mitre navigator comparison as a JSON file
# read it in to a data structure in python and see what I can print out
# That's the theory
# 
# This is very definitely a work in progress

import json

with open("ComparisonLayer.json", "r") as read_file:
    mitreAttackNavigatorData = json.load(read_file)

print ("\n" + mitreAttackNavigatorData["name"] + "\n") # Print the name of the Mitre Navigator Sheet

for techniqueID in mitreAttackNavigatorData["techniques"] :
	print (techniqueID["techniqueID"],techniqueID["tactic"])

