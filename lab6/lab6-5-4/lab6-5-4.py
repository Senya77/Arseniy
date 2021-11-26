import datetime

from Dots import dots

start_time = datetime.datetime.now()
current_date = str(datetime.datetime.now())

input_file = open('input(6-5-4).txt', 'r')
output_file = open('output(6-5-4).txt', 'w')

values = input_file.readline().split()
r = int(values[0])

output_file.write(current_date + '\n')
output_file.write(str(dots(r)) + '\n')
output_file.write("%s" % (datetime.datetime.now() - start_time))

input_file.close()
output_file.close()
