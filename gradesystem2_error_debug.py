#Professional Practices Short Course – Assignment 6
#Author: Jadine Meghrajh

#An example of setting a log level to ERROR

#start

import csv 											 #importing a built in module to enable reading/manipulating/writing of csv files
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('gradesystem2_errorlogfile.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')


def main():
	df = pd.read_csv("input_altered.csv")						 
	
	totrows=len(df.axes[0])								 #gets the total number of rows in csv file
	totcol=len(df.axes[1])								 #gets the total number of columns in csv file

	num_of_subjects = totcol-2							 #gets the total number of subjects

	inputfile = open('input_altered.csv')						 #tells the csv module to open the given "input.csv" file and assigns this file to an object (inputfile)
	csv_inputfile = csv.reader(inputfile) 				 #pass the inputfile object to the csv module to create a csv file object
	next(csv_inputfile)									 #tells the program to skip the first row as this data is not useful for further operation

	
	header = ['Firstname', 'Surname','Average', 'Grade'] #assigning the headings that needs to be written to the new "output.csv" file

	createfile = open('output.csv', 'w', newline="") 	 #open a new file for writing, with each information to be stored on the next line with no spaces
	writer = csv.writer(createfile)						 #using the csv writer to write to the file
	

	writer.writerow(header)						 		 #writes the respective header to the newly created "output.csv" file

	for row in csv_inputfile:					 		 #iterate over the csv file object by looping over every row, using a for loop
		
		firstname = (row[0]) 					 		 #extracting the firstname in position 0 from the specific row as a string
		surname = (row[1]) 						 		 #extracting the surname in position 1 from the specific row as a string
		#algebraperc = float(row[2]) 			 		 #extracting the algebra percentage in position 2 from the specific row and converting it to a float 
		#calculusperc = float(row[3]) 			 		 #extracting the calculus percentage in position 3 from the specific row and converting it to a float 
		#programmingperc = float(row[4]) 		 		 #extracting the programming percentage in position 4 from the specific row and converting it to a float 
		#databasesperc = float(row[5]) 			 		 #extracting the databases percentage in position 5 from the specific row and converting it to a float 

		total_subject_percentage = 0
		for i in range(2,totcol):
			total_subject_percentage = float(row[i]) + total_subject_percentage	#calculating each students total percentage over all modules using a nested for loop
		
		avrg = calcavrg(total_subject_percentage,num_of_subjects)
		logger.debug('Average: (( {} ) / {}) = {}'.format(total_subject_percentage, num_of_subjects, avrg))

		grade = determineGrade(avrg);
		logger.debug('Symbol for average: {} = {}'.format(avrg, grade))

		data = [firstname, surname, avrg, grade];
		logger.info('Writing to output csv file: {},{},{},{}'.format(firstname, surname, avrg, grade))

		writer.writerow(data)					  		 #write the respective data to the newly created "output.csv" file


	inputfile.close() 							 		 #calling a method on the file object in order to close the file

#calculating the average percentage per learner by using the total percentage divided by the number of subjects. Rounded off to 1 decimal as required 
def calcavrg(total_subject_percentage,num_of_subjects):
	#ave = float(round(((total_subject_percentage)/(num_of_subjects)),1)) 
	#return ave;

	try:
		
		ave = float(round(((total_subject_percentage)/(num_of_subjects)),1)) 
	except ZeroDivisionError:
		logger.error('Tried to divide by 0')
	else: 
		return ave;

def determineGrade(average):
	if( 80 <= average <= 100): 	
		average = 'A'			   
		return average;
	elif( 70 <= average <= 79.9):					
		average = 'B'			   
		return average;
	elif( 60 <= average <= 69.9):
		average = 'C'			   
		return average;
	elif( 50 <= average <= 59.9):
		average = 'D'			   
		return average;	
	elif( 40 <= average <= 49.9):
		average = 'E'			   
		return average;
	elif( 0 <= average <= 39.9):
		average = 'F'			   
		return average;
	else:
		logger.error('Input value out of bounds which caused an undesired average and no symbol to be created, check input values in csv file')
		

main();
#end