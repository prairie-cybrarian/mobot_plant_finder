import re
import os

#here we go through all our scrapped webpages and find what we actually want. In this instance, the code wants information on the following: Attracts, Bloom Description, Bloom Time, Common Name, Culture, Family, Flower, Formal Name, Fruit, Garden Uses, Height, Invasive, Leaf, Maintenance, Native Range, Noteworthy Characteristics, Other, Problems, Spread, Suggested Use, Sun, Tolerate, Type, Water, and Zone

if __name__ == "__main__":

	path = "mobot_entries/scraped_results/"

	g = open("mobot_entries/cleaner_results/plants_mobot.csv", 'w')

	g.write("Attracts,Bloom Description,Bloom Time,Common Name,Culture,Family,Flower,Formal Name,Fruit,Garden Uses,Height,Invasive,Leaf,Maintenance,Native Range,Noteworthy Characteristics,Other,Problems,Spread,Suggested Use,Sun,Tolerate,Type,Water,Zone" + "\n")

	for filename in os.listdir(path):

		with open(path + filename) as f:
			for i, line in enumerate(f):
				cleaner_line = line.strip(", ").strip("  ").strip('<div class="row">').strip("</div>").strip("\n").strip("\t").strip("	 ").strip(" 	").strip("	 	").strip(" ")
				cleaner_line_list = cleaner_line.split("<")
				content = cleaner_line_list[0]

				pattern = re.compile(r"[^A-Za-z0-9 :]+")
				content = pattern.sub("", content)

				if i == 1: formalName = content
				if "Attracts" in line: 
					if ":" in line:
						attractsText_list = content.split(":") 
						attractsText = attractsText_list[1] 
				if "Bloom Description" in line: 
					if ":" in line:
						colorText_list = content.split(":") 
						colorText = colorText_list[1]
					else:
						colorText = str(content)
				if "Bloom Time" in line: 
					if ":" in line:
						bloomTime_list = content.split(":") 
						bloomTime = bloomTime_list[1]
					else:
						bloomTime - str(content)
				if "Common Name" in line:
					if ":" in line:
						commonName_list = content.split(":") 
						commonName = commonName_list[1] 
					else:
						commonName = str(content)
				if "Culture" in line:
					if ":" in line:
						culture_list = content.split(":") 
						culture = culture_list[1] 
					else:
						culture = str(content)
				if "Family" in line: 
					if ":" in line:
						family_list = content.split(":") 
						family = family_list[1]
					else:
						family = str(content)
				if "Flower" in line: 
					if ":" in line:
						flower_list = content.split(":") 
						flower = flower_list[1]
					else:
						flower = str(content)
				if "Fruit" in line: 
					if ":" in line:
						fruit_list = content.split(":") 
						fruit = fruit_list[1]
					else:
						fruit = str(content)
				if "Garden Uses" in line: 
					if ":" in line:
						gardenUses_list = content.split(":") 
						gardenUses = gardenUses_list[1]
					else:
						gardenUses = str(content)
				if "Height" in line: 
					if ":" in line:
						height_list = content.split(":") 
						height = height_list[1]
					else:
						height = str(content)
				if "Invasive" in line: 
					if ":" in line:
						invasive_list = content.split(":") 
						invasive = invasive_list[1]
					else:
						invasive = str(content)
				if "Leaf" in line: 
					if ":" in line:
						leaf_list = content.split(":") 
						leaf = leaf_list[1]
					else:
						leaf = str(content)
				if "Maintenance" in line:
					if ":" in line:
						maintenance_list = content.split(":") 
						maintenance = maintenance_list[1]
					else:
						maintenance = str(content)
				if "Native Range" in line:
					if ":" in line:
						nativeRange_list = content.split(":") 
						nativeRange = nativeRange_list[1]
					else:
						nativeRange = str(content)
				if "Noteworthy Characteristics" in line: 
					if ":" in line:
						noteworthyCharacteristics_list = content.split(":") 
						noteworthyCharacteristics = noteworthyCharacteristics_list[1]
					else:
						noteworthyCharacteristics = str(content)
				if "Other" in line: 
					if ":" in line:
						other_list = content.split(":") 
						other = other_list[1]
					else:
						other = str(content)
				if "Problems" in line: 
					if ":" in line:
						problems_list = content.split(":") 
						problems = problems_list[1]
					else:
						problems = str(content)
				if "Spread" in line: 
					if ":" in line:
						spread_list = content.split(":") 
						spread = spread_list[1]
					else:
						spread = str(content)
				if "Suggested Use" in line:
					if ":" in line:
						suggested_use_list = content.split(":") 
						suggested_use = suggested_use_list[1]
					else:
						suggested_use = str(content)
				if "Sun" in line: 
					if ":" in line:
						sun_list = content.split(":") 
						sun = sun_list[1]
					else:
						sun = str(content)
				if "Tolerate" in line: 
					if ":" in line:
						tolerate_list = content.split(":") 
						tolerate = tolerate_list[1]
					else:
						tolerate = str(content)
				if "Type" in line: 
					if ":" in line:
						type_plant_list = content.split(":") 
						type_plant = type_plant_list[1]
					else:
						type_plant = str(content)
				if "Water" in line: 
					if ":" in line:
						water_list = content.split(":") 
						water = water_list[1]
					else:
						water = str(content)
				if "Zone" in line: 
					if ":" in line:
						zone_list = content.split(":") 
						zone = zone_list[1]
					else:
						zone = str(content)
			
				try:
				    attractsText
				except NameError:
				    attractsText = "NA"
				else:
				    continue
                        
				try:
				    colorText
				except NameError:
				    colorText = "NA"
				else:
				    continue

				try:
				    bloomTime
				except NameError:
				    bloomTime = "NA"
				else:
				    continue

				try:
				    commonName
				except NameError:
				    commonName = "NA"
				else:
				    continue

				try:
				    culture
				except NameError:
				    culture = "NA"
				else:
				    continue

				try:
				    family
				except NameError:
				    family = "NA"
				else:
				    continue

				try:
				    flower
				except NameError:
				    flower = "NA"
				else:
				    continue

				try:
				    fruit
				except NameError:
				    fruit = "NA"
				else:
				    continue

				try:
				    gardenUses
				except NameError:
				    gardenUses = "NA"
				else:
				    continue

				try:
				    height
				except NameError:
				    height = "NA"
				else:
				    continue

				try:
				    invasive
				except NameError:
				    invasive = "NA"
				else:
				    continue

				try:
				    leaf
				except NameError:
				    leaf = "NA"
				else:
				    continue

				try:
				    maintenance
				except NameError:
				    maintenance = "NA"
				else:
				    continue

				try:
				    nativeRange
				except NameError:
				    nativeRange = "NA"
				else:
				    continue

				try:
				    noteworthyCharacteristics
				except NameError:
				    noteworthyCharacteristics = "NA"
				else:
				    continue

				try:
				    other
				except NameError:
				    other = "NA"
				else:
				    continue

				try:
				    problems
				except NameError:
				    problems = "NA"
				else:
				    continue

				try:
				    spread
				except NameError:
				    spread = "NA"
				else:
				    continue

				try:
				    suggested_use
				except NameError:
				    suggested_use = "NA"
				else:
				    continue

				try:
				    sun
				except NameError:
				    sun = "NA"
				else:
				    continue

				try:
				    tolerate
				except NameError:
				    tolerate = "NA"
				else:
				    continue

				try:
				    type_plant
				except NameError:
				    type_plant = "NA"
				else:
				    continue

				try:
				    water
				except NameError:
				    water = "NA"
				else:
				    continue

				try:
				    zone
				except NameError:
				    zone = "NA"
				else:
				    continue

		plant_characteristics = [attractsText,colorText, bloomTime, commonName, culture, family, flower, formalName, fruit, gardenUses, height, invasive, leaf, maintenance, nativeRange, noteworthyCharacteristics, other, problems, spread, suggested_use, sun, tolerate, type_plant, water, zone]
		g.write(",".join(plant_characteristics) + "\n")
		print("Finished up " + formalName)

	g.close()

	print("Done!")



