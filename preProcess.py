import csv
import copy


	# myWriter = csv.writer(csvfile, lineterminator = '\n')

def deleteNoPrevYears(): 
	r = csv.reader(open('clean_course_data.csv')) # Here your csv file
	lines = list(r)

	year = lines[1][9]
	x = 1  #skip header line
	

	while year != "2011":
		while x < len(lines) and (lines[x][9] == year) :  #cycles thru each class in a given year
			takesPlace = False 
			currentRow = lines[x]
			y = copy.deepcopy(x)
			prevYear = copy.deepcopy(int(year) - 1)  #turns year into an int, subtracts 1, makes copy
			prevYear = str(prevYear) 

			while (y < len(lines)) and (lines[y][9] != prevYear) : #takes the y iterator to the first line of the prev year
				y = y + 1

			while y < len(lines) and (lines[y][9] == prevYear) : ##now cycling through each of the courses in the prev year
				if lines[y][0] == currentRow[0] and (lines[y][2] == currentRow[2]) and (lines[y][4] == currentRow[4]) and (lines[y][10] == currentRow[10]): 
					##same subject, tietle, catalog num, quarter
					takesPlace = True 
					break 
					#the course does take place the previous year--don't delete 
				y = y + 1
			if takesPlace == False:

				del lines[x] ##course doesn't take place the prev year --> delete
				x = x - 1 ##decrement x b/c just deleted a row

			x = x + 1
			if x < len(lines):
				break
		
		year = lines[x][9]  #now cycles through for the new year
	

	writer = csv.writer(open('preProcessedData.csv', 'w'), lineterminator = '\n')
	writer.writerows(lines)


def addClass():
	return 

deleteNoPrevYears()

