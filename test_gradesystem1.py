import pytest
import gradesystem1

def test_calcavrg():
	assert gradesystem1.calcavrg(300,5) == 60.0
	assert gradesystem1.calcavrg(200,2) == 100.0  
	assert gradesystem1.calcavrg(500,5) == 100.0
	assert gradesystem1.calcavrg(120,3) == 40.0
	assert gradesystem1.calcavrg(360,4) == 90.0
	assert gradesystem1.calcavrg(240,4) == 60.0
	assert gradesystem1.calcavrg(302,4) == 75.5  
	assert gradesystem1.calcavrg(332,4) == 83.0
	assert gradesystem1.calcavrg(251,4) == 62.8
	assert gradesystem1.calcavrg(159,4) == 39.8
	assert gradesystem1.calcavrg(267,4) == 66.8
	assert gradesystem1.calcavrg(240,4) == 60.0



def test_determineGrade():
	assert gradesystem1.determineGrade(85) == 'A'
	assert gradesystem1.determineGrade(75) == 'B'
	assert gradesystem1.determineGrade(65) == 'C'
	assert gradesystem1.determineGrade(55) == 'D'
	assert gradesystem1.determineGrade(45) == 'E'
	assert gradesystem1.determineGrade(35) == 'F'
	assert gradesystem1.determineGrade(0) == 'F'
	assert gradesystem1.determineGrade(1000) == '-'
	assert gradesystem1.determineGrade(79.9) == 'B'
	assert gradesystem1.determineGrade(69.9) == 'C'
	assert gradesystem1.determineGrade(59.9) == 'D'
	assert gradesystem1.determineGrade(49.9) == 'E'
	assert gradesystem1.determineGrade(39.9) == 'F'
	assert gradesystem1.determineGrade(20) == 'F'
	assert gradesystem1.determineGrade(99.9) == 'A'
	assert gradesystem1.determineGrade(10) == 'F'
	assert gradesystem1.determineGrade(1200) == '-'
