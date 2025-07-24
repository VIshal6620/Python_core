# numbers = [100, 10, 11, 5, 13,88, 17, 88]
#
# highest = 0
# second_highest = 0
#
# for num in numbers:
#     if num > highest:
#         second_highest = highest
#         highest = num
#     elif num > second_highest and num != highest:
#         second_highest = num
#
# print("Highest number is:", highest)
# print("Second highest number is:", second_highest)


import datetime

today = datetime.date.today()
future = today + datetime.timedelta(days=7)
past = today - datetime.timedelta(days=7)

print("7 days later:", future)
print("7 days ago:", past)