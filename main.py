import pandas

# squirrel_data = pandas.read_csv('./2018_Squirrel_Data.csv')
#
# by_color = squirrel_data['Primary Fur Color']
#
# grey = 0
# red = 0
# black = 0
# for color in by_color:
#     if color == 'Gray':
#         grey += 1
#     elif color == 'Cinnamon':
#         red += 1
#     elif color == 'Black':
#         black += 1
#
# count_dict = {
#     'Fur color': ['grey', 'red', 'black'],
#     'Count': [grey, red, black]
# }
#
# new_data = pandas.DataFrame(count_dict)
# print(new_data)
#
# new_data.to_csv('squirrel_count_color.csv')

squirrel_data = pandas.read_csv('./2018_Squirrel_Data.csv')

grey = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
red = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

count_dict = {
    'Fur color': ['grey', 'red', 'black'],
    'Count': [grey, red, black]
}

new_data = pandas.DataFrame(count_dict)
print(new_data)

new_data.to_csv('squirrel_count_color_way2.csv')
