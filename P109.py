import pandas as pd
import statistics
import csv

df=pd.read_csv("P109.csv")
gender_list=df["gender"].to_list()
race_list=df["race/ethnicity"].to_list()
ed_list=df["parental level of education"].to_list()
lunch_list=df["lunch"].to_list()
test_list=df["test preparation course"].to_list()
math_list=df["math score"].to_list()
read_list=df["reading score"].to_list()
write_list=df["writing score"].to_list()

#Mean
gender_mean=statistics.mean(gender_list)
race_mean=statistics.mean(race_list)
ed_mean=statistics.mean(ed_list)
lunch_mean=statistics.mean(lunch_list)
test_mean=statistics.mean(test_list)
math_mean=statistics.mean(math_list)
read_mean=statistics.mean(read_list)
write_mean=statistics.mean(write_list)

#Median
gender_med=statistics.median(gender_list)
race_med=statistics.median(race_list)
ed_med=statistics.median(ed_list)
lunch_med=statistics.median(lunch_list)
test_med=statistics.median(test_list)
math_med=statistics.median(math_list)
read_med=statistics.median(read_list)
write_med=statistics.median(write_list)

#Mode
gender_mode=statistics.mode(gender_list)
race_mode=statistics.mode(race_list)
ed_mode=statistics.mode(ed_list)
lunch_mode=statistics.mode(lunch_list)
test_mode=statistics.mode(test_list)
math_mode=statistics.mode(math_list)
read_mode=statistics.mode(read_list)
write_mode=statistics.mode(write_list)

#Standard Deviation
gender_std=statistics.stdev(gender_list)
race_std=statistics.stdev(race_list)
ed_std=statistics.stdev(ed_list)
lunch_std=statistics.stdev(lunch_list)
test_std=statistics.stdev(test_list)
math_std=statistics.stdev(math_list)
read_std=statistics.stdev(read_list)
write_std=statistics.stdev(write_list)

print("Mean,Median and Mode of Gender is {},{}and{}respecively".format(gender_mean,gender_med,gender_mode))
print("Mean,Median and Mode of Race is {},{}and{}respecively".format(race_mean,race_med,race_mode))
print("Mean,Median and Mode of Education is {},{}and{}respecively".format(ed_mean,ed_med,ed_mode))
print("Mean,Median and Mode of Lunch is {},{}and{}respecively".format(lunch_mean,lunch_med,lunch_mode))
print("Mean,Median and Mode of Math is {},{}and{}respecively".format(math_mean,math_med,math_mode))
print("Mean,Median and Mode of Test is {},{}and{}respecively".format(test_mean,test_med,test_mode))
print("Mean,Median and Mode of Read is {},{}and{}respecively".format(read_mean,read_med,read_mode))
print("Mean,Median and Mode of Write is {},{}and{}respecively".format(write_mean,write_med,write_mode))
#Finding Start and End
gender_first_std_dev_start,gender_first_std_dev_end=gender_mean-gender_std,gender_mean+gender_std
gender_second_std_dev_start,gender_second_std_dev_end=gender_mean-(2*gender_std),gender_mean+(2*gender_std)
gender_third_std_dev_start,gender_third_std_dev_end=gender_mean-(3*gender_std),gender_mean+(3*gender_std)

race_first_std_dev_start,race_first_std_dev_end=race_mean-race_std,race_mean+race_std
race_second_std_dev_start,race_second_std_dev_end=race_mean-(2*race_std),race_mean+(2*race_std)
race_third_std_dev_start,race_third_std_dev_end=race_mean-(3*race_std),race_mean+(3*race_std)

ed_first_std_dev_start,ed_first_std_dev_end=ed_mean-ed_std,ed_mean+ed_std
ed_second_std_dev_start,ed_second_std_dev_end=ed_mean-(2*ed_std),ed_mean+(2*ed_std)
ed_third_std_dev_start,ed_third_std_dev_end=ed_mean-(3*ed_std),ed_mean+(3*ed_std)

math_first_std_dev_start,math_first_std_dev_end=math_mean-math_std,math_mean+math_std
math_second_std_dev_start,math_second_std_dev_end=math_mean-(2*math_std),math_mean+(2*math_std)
math_third_std_dev_start,math_third_std_dev_end=math_mean-(3*math_std),math_mean+(3*math_std)

test_first_std_dev_start,test_first_std_dev_end=test_mean-test_std,test_mean+test_std
test_second_std_dev_start,test_second_std_dev_end=test_mean-(2*test_std),test_mean+(2*test_std)
test_third_std_dev_start,test_third_std_dev_end=test_mean-(3*test_std),test_mean+(3*test_std)

read_first_std_dev_start,read_first_std_dev_end=read_mean-read_std,read_mean+read_std
read_second_std_dev_start,read_second_std_dev_end=read_mean-(2*read_std),read_mean+(2*read_std)
read_third_std_dev_start,read_third_std_dev_end=read_mean-(3*read_std),read_mean+(3*read_std)

write_first_std_dev_start,write_first_std_dev_end=write_mean-write_std,write_mean+write_std
write_second_std_dev_start,write_second_std_dev_end=write_mean-(2*write_std),write_mean+(2*write_std)
write_third_std_dev_start,write_third_std_dev_end=write_mean-(3*write_std),write_mean+(3*write_std)

lunch_first_std_dev_start,lunch_first_std_dev_end=lunch_mean-lunch_std,lunch_mean+lunch_std
lunch_second_std_dev_start,lunch_second_std_dev_end=lunch_mean-(2*lunch_std),lunch_mean+(2*lunch_std)
lunch_third_std_dev_start,lunch_third_std_dev_end=lunch_mean-(3*lunch_std),lunch_mean+(3*lunch_std)
#Calculating Percentage
gender_list_of_data_within_1_std_deviation=[result for result in gender_list if result > gender_first_std_dev_start and result < gender_first_std_dev_end ]
gender_list_of_data_within_2_std_deviation=[result for result in gender_list if result > gender_second_std_dev_start and result < gender_second_std_dev_end ]
gender_list_of_data_within_3_std_deviation=[result for result in gender_list if result > gender_third_std_dev_start and result < gender_third_std_dev_end ]

race_list_of_data_within_1_std_deviation=[result for result in race_list if result > race_first_std_dev_start and result < race_first_std_dev_end ]
race_list_of_data_within_2_std_deviation=[result for result in race_list if result > race_second_std_dev_start and result < race_second_std_dev_end ]
race_list_of_data_within_3_std_deviation=[result for result in race_list if result > race_third_std_dev_start and result < race_third_std_dev_end ]

ed_list_of_data_within_1_std_deviation=[result for result in ed_list if result > ed_first_std_dev_start and result < ed_first_std_dev_end ]
ed_list_of_data_within_2_std_deviation=[result for result in ed_list if result > ed_second_std_dev_start and result < ed_second_std_dev_end ]
ed_list_of_data_within_3_std_deviation=[result for result in ed_list if result > ed_third_std_dev_start and result < ed_third_std_dev_end ]

math_list_of_data_within_1_std_deviation=[result for result in math_list if result > math_first_std_dev_start and result < math_first_std_dev_end ]
math_list_of_data_within_2_std_deviation=[result for result in math_list if result > math_second_std_dev_start and result < math_second_std_dev_end ]
math_list_of_data_within_3_std_deviation=[result for result in math_list if result > math_third_std_dev_start and result < math_third_std_dev_end ]

test_list_of_data_within_1_std_deviation=[result for result in test_list if result > test_first_std_dev_start and result < test_first_std_dev_end ]
test_list_of_data_within_2_std_deviation=[result for result in test_list if result > test_second_std_dev_start and result < test_second_std_dev_end ]
test_list_of_data_within_3_std_deviation=[result for result in test_list if result > test_third_std_dev_start and result < test_third_std_dev_end ]

read_list_of_data_within_1_std_deviation=[result for result in read_list if result > read_first_std_dev_start and result < read_first_std_dev_end ]
read_list_of_data_within_2_std_deviation=[result for result in read_list if result > read_second_std_dev_start and result < read_second_std_dev_end ]
read_list_of_data_within_3_std_deviation=[result for result in read_list if result > read_third_std_dev_start and result < read_third_std_dev_end ]

write_list_of_data_within_1_std_deviation=[result for result in write_list if result > write_first_std_dev_start and result < write_first_std_dev_end ]
write_list_of_data_within_2_std_deviation=[result for result in write_list if result > write_second_std_dev_start and result < write_second_std_dev_end ]
write_list_of_data_within_3_std_deviation=[result for result in write_list if result > write_third_std_dev_start and result < write_third_std_dev_end ]

lunch_list_of_data_within_1_std_deviation=[result for result in lunch_list if result > lunch_first_std_dev_start and result < lunch_first_std_dev_end ]
lunch_list_of_data_within_2_std_deviation=[result for result in lunch_list if result > lunch_second_std_dev_start and result < lunch_second_std_dev_end ]
lunch_list_of_data_within_3_std_deviation=[result for result in lunch_list if result > lunch_third_std_dev_start and result < lunch_third_std_dev_end ]

#Result
print("{}% of data for gender lies within 1 standard deviation".format(len(gender_list_of_data_within_1_std_deviation)*100/len(gender_list)))
print("{}% of data for gender lies within 2 standard deviations".format(len(gender_list_of_data_within_2_std_deviation)*100/len(gender_list)))
print("{}% of data for gender lies within 3 standard deviations".format(len(gender_list_of_data_within_3_std_deviation)*100/len(gender_list)))

print("{}% of data for race lies within 1 standard deviation".format(len(race_list_of_data_within_1_std_deviation)*100/len(race_list)))
print("{}% of data for race lies within 2 standard deviations".format(len(race_list_of_data_within_2_std_deviation)*100/len(race_list)))
print("{}% of data for race lies within 3 standard deviations".format(len(race_list_of_data_within_3_std_deviation)*100/len(race_list)))

print("{}% of data for education lies within 1 standard deviation".format(len(ed_list_of_data_within_1_std_deviation)*100/len(ed_list)))
print("{}% of data for education lies within 2 standard deviations".format(len(ed_list_of_data_within_2_std_deviation)*100/len(ed_list)))
print("{}% of data for education lies within 3 standard deviations".format(len(ed_list_of_data_within_3_std_deviation)*100/len(ed_list)))

print("{}% of data for lunch lies within 1 standard deviation".format(len(lunch_list_of_data_within_1_std_deviation)*100/len(lunch_list)))
print("{}% of data for lunch lies within 2 standard deviations".format(len(lunch_list_of_data_within_2_std_deviation)*100/len(lunch_list)))
print("{}% of data for lunch lies within 3 standard deviations".format(len(lunch_list_of_data_within_3_std_deviation)*100/len(lunch_list)))

print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100/len(math_list)))

print("{}% of data for test lies within 1 standard deviation".format(len(test_list_of_data_within_1_std_deviation)*100/len(test_list)))
print("{}% of data for test lies within 2 standard deviations".format(len(test_list_of_data_within_2_std_deviation)*100/len(test_list)))
print("{}% of data for test lies within 3 standard deviations".format(len(test_list_of_data_within_3_std_deviation)*100/len(test_list)))

print("{}% of data for read lies within 1 standard deviation".format(len(read_list_of_data_within_1_std_deviation)*100/len(read_list)))
print("{}% of data for read lies within 2 standard deviations".format(len(read_list_of_data_within_2_std_deviation)*100/len(read_list)))
print("{}% of data for read lies within 3 standard deviations".format(len(read_list_of_data_within_3_std_deviation)*100/len(read_list)))

print("{}% of data for write lies within 1 standard deviation".format(len(write_list_of_data_within_1_std_deviation)*100/len(write_list)))
print("{}% of data for write lies within 2 standard deviations".format(len(write_list_of_data_within_2_std_deviation)*100/len(write_list)))
print("{}% of data for write lies within 3 standard deviations".format(len(write_list_of_data_within_3_std_deviation)*100/len(write_list)))
























