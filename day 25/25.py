import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempertur = []
    for temp in data:
        data[2] 
    # for row in data :
    #     print(row)