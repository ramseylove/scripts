import csv

count = 0

with open('local_flower_images08.csv', 'r') as csv1:
    with open('server_flower_images08.csv', 'r') as csv2:
        csv_reader1 = list(csv.reader(csv1))
        csv_reader2 = list(csv.reader(csv2))


        for local in csv_reader1:
            local_filename = local[0]
            for server in csv_reader2:
                server_filename = server[0]
                if local_filename not in server_filename:
                    count += 1
    
    print(count)