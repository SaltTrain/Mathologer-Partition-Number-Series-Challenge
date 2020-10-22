from csv import writer
from csv import reader
from A000041_sequence import pattern

# adds new row of data
def append_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerows(list_of_elem)
        
# creates new csv file
def new_csv(file_name):
	with open(file_name, 'w') as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(['index','result'])
		
# read csv
def read_csv(file_name):
	data = {}
	with open(file_name, 'r') as file:
		read = reader(file)
		
		for row in read:
			if row[0] != 'index':
				data[int(row[0])] = int(row[1])
	return data




x = 'data.csv'
data = read_csv(x)


da = []
for i in range(1,701):
	if i not in data:
		da.append([i, pattern(i, data)])
		append_row('data.csv', da)
		print(da[0])
		data = read_csv(x)
		da = []
	else:
		print("next...")




