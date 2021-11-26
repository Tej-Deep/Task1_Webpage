from org.transcrypt.stubs.browser import *
from datetime import *
array = []

def Predict1():
	'''This function is called to take in inputs of indicators and return predicted number of covid deaths'''
	# Getting values from the webpage
	num_cancer = document.getElementsByName("num_cancer")[0].value
	num_cases = document.getElementsByName("num_cases")[0].value
	num_GDP = document.getElementsByName("num_GDP")[0].value
	num_smoker = document.getElementsByName("num_smoker")[0].value


	# Throw alert and stop if nothing in the text input
	if (num_cancer == "") or (num_cases == "") or (num_GDP == "") or (num_smoker == ""):
		window.alert("Your textbox is empty")
		return

	int_cancer = int(num_cancer)
	int_cases = int(num_cases)
	int_GDP = int(num_GDP)
	int_smoker = int(num_smoker)
	beta = [-2366.169597,0.286816327,0.008504693,-13.98936169, 3.305856129]
	pred_value = beta[0] + beta[1]  * int_cancer + beta[2] * int_cases + beta[3]*int_GDP + beta[4]*(int_smoker**0.5)
	
	document.getElementById("predicted").innerHTML = str(pred_value)


def Predict_2():
	
	num_date = document.getElementsByName("num_date")[0].value
	
	if num_date == "":
		window.alert("Your textbox is empty")
		return
	date_list = num_date.split('-')
	date1 = date(int(date_list[0]), int(date_list[1]), int(date_list[2])) 
	date2 = date(2021,2,26) 
	days = date1.toordinal() - date2.toordinal() + 1
	console.log(days)
	
	days_scaled = days/200
	
	beta =  [61.90594471, 8.79796245, -10.43911235, -14.51486364, -10.42213455,-0.81248547,  13.44031826,  32.29907487]
	
	Cases = 0
	for i in range(8):
		Cases += beta[i] * (days_scaled ** i)
		console.log(Cases)
	document.getElementById("prediction").innerHTML = str(Cases)


	

