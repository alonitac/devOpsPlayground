from datetime import datetime

infile = open('C:/Users/log.txt', 'r')
FMT = '%H:%M:%S.%f'
id
first_line = infile.readline()
spFirst_line = first_line.split()
min = (datetime.strptime(spFirst_line[2], FMT) - datetime.strptime(spFirst_line[1], FMT)).total_seconds()
file_lines = infile.readlines()
for line in file_lines:
    spline = line.split()
    tdelta = (datetime.strptime(spline[2], FMT) - datetime.strptime(spline[1], FMT)).total_seconds()
    if tdelta < min:
        min = tdelta
        id = spline[3]
print(id)




# count = 0
# for line in file_lines:
#     spline = line.split()
#     for word in spline:
#         if word == 'INFO':
#             count += 1
# print(count)

# infile = open('C:/Users/log.txt', 'r')
# FMT = '%H:%M:%S'
# count = 0
# sum = 0
# file_lines = infile.readlines()
# for line in file_lines:
#     count += 1
#     spline = line.split()
#     tdelta = (datetime.strptime(spline[2], FMT) - datetime.strptime(spline[1], FMT)).total_seconds()
#     print(tdelta)
#     sum = sum + int(tdelta)
# print(sum/count)
