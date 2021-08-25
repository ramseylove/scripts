import csv
import glob
import math

folder = 'folder_to_compare'

path = 'path_to_folder'

# define the number of filenames listed in each csv, adjust if receiving errors
# must be the same as the ftp_script
filenames_per_csv = 40000

file_list = glob.glob(f'${path}/{folder}/*', recursive=False)
file_list.sort()
count = len(file_list)
num = filenames_per_csv
iter_num = math.ceil(count / num)

end_num = count
start_num = end_num - num

while(iter_num > 0):
    print(f'{iter_num} Start num: {start_num}, End num: {end_num}')
    output_file = open(f"local_flower_images{iter_num:02}.csv", "w")
        
    for line in file_list[start_num:end_num]:
        line_split = line.split('/')
        line = line_split[-1] + '\n'
        output_file.write(line)

    output_file.close()
    iter_num -= 1
    end_num = start_num
    
    if end_num >= num:
        start_num -= num
    else:
        start_num = 0
        
    