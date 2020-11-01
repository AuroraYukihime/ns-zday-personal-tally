# Filename:    tally.py
# Author:      Aurora Yukihime of Albrook (AuroraYukhime)
# Date:        1 November 2020
# Version:     1.0
# Description: Caveman's first N-Day personal tally. Valid for about 5 days after N-Day before your national happenings disappear.
#              SEE COMMENT BLOCK BEGINNING WITH "Edit these fields" FOR PROPER OPERATION

import re

# Edit these fields
# For nation: Enter your nation name with exact capitalization. I made this at 1am before a workday, sorry! ^^
# For data: See cureData1.txt and cureData2.txt for samples of acceptable National Happenings (page=activity) snips
nation = "Albrook"
data = open("cureData1.txt")

lines = data.read().splitlines()

findMe = "from " + nation
kills = 0
cures = 0
infes = 0
for line in lines:
        if findMe in line:
                if "killing" in line:
                        check= re.search('killing (.+?) million', line)
                        if check:
                                found = check.group(1)
                                addMe = int(found)
                                kills += addMe
                elif "curing" in line:
                        check= re.search('curing (.+?) million', line)
                        if check:
                                found = check.group(1)
                                addMe = int(found)
                                cures += addMe
                elif "infecting" in line:
                        check= re.search('infecting (.+?) million', line)
                        if check:
                                found = check.group(1)
                                addMe = int(found)
                                infes += addMe
totKills = kills/1000
totCures = cures/1000
totInfes = infes/1000

print("Z-Day stats for " + nation)
if totKills>1:
        print("Killed " + str(totKills) + " billion")
else:
        print("Killed " + str(kills) + " million")
        
if totCures>1:
        print("Cured " + str(totCures) + " billion")
else:
        print("Cured " + str(curess) + " million")
        
if totInfes>1:
        print("Infected " + str(totInfes) + " billion")
else:
        print("Infected " + str(infes) + " million")
