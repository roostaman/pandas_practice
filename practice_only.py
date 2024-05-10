# with open('./weather_data.csv', mode='r') as weather_file:
#     data = weather_file.readlines()
#
# for line in data:
#     line.strip()
#     print(line)

# import csv
#
# with open('./weather_data.csv', mode='r') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# print(data['temp'])

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
# print(data_dict)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# temp_list = data['temp'].to_list()
#
# av_temp = (sum(temp_list)) / len(temp_list)
# print(av_temp)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# av_temp = data['temp'].mean()  # calculate average of something
# print(av_temp)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# monday_row = data[data.day == "Monday"]
# print(monday_row)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# max_temp = data['temp'].max()
# max_temp_row = data[data.temp == max_temp]
# print(max_temp_row)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# monday_data = data[data.day == 'Monday']
# monday_temp = monday_data.temp[0]
# print(monday_temp)

import pandas

new_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 90, 80]
}

data = pandas.DataFrame(new_dict)
print(data)
data.to_csv('student_scores_data.csv')
