import numpy as np
import pandas

def cost_function(data,theta_0,theta_1,no_instances):
	totalError = 0
	for i in range(no_instances):
		x = data["Distance"][i]
		y = data["Calories"][i]
		totalError += (y - ( theta_1* x + theta_0)) ** 2
	return totalError / float(no_instances)

def best_fit_line(data,theta_0,theta_1,no_instances):
	error = cost_function(data,theta_0,theta_1,no_instances)
	print "After {0} iterations b = {1}, m = {2}, error = {3}".format(1000, theta_0, theta_1,error)
  
def apply_gradient_descent(data,alpha,theta_0,theta_1,no_instances):
	count = 0
	while(count<1001):
		count+=1
		sum_theta_0 = 0
		sum_theta_1 = 0
		for i in range(no_instances):
			sum_theta_0 += (theta_0 + theta_1*data["Distance"][i]) - data["Calories"][i]
			sum_theta_1 += ((theta_0 + theta_1*data["Distance"][i]) - data["Calories"][i])*(data["Distance"][i])
		prev_theta_0 = theta_0
		prev_theta_1 = theta_1
		theta_0 -= (alpha/no_instances) * sum_theta_0
		theta_1 -= (alpha/no_instances) * sum_theta_1

	best_fit_line(data,theta_0,theta_1,no_instances)

def load_data(filename):
	data = pandas.read_csv(filename,header=None)
	data.columns = ["Distance","Calories"]
	alpha = 0.0001
	theta_0 = 0
	theta_1 = 0
	no_instances = data.shape[0] 
	apply_gradient_descent(data,alpha,theta_0,theta_1,no_instances)

if __name__ == '__main__':
	load_data('/Users/svdj16/Downloads/Intro_to_the_Math_of_intelligence-master/data.csv')
