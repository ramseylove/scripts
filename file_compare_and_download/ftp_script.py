import csv
import math
from ftplib import FTP

# ftp credentials
usr = 'username'
pwd = 'P@$$w0rd'
ftp_url = 'ftp.website.com'

# folder in path
folder = 'folder_of_files'

# path on ftp server
path = f'\\site\\wwwroot\\assets\\uploads\\${folder}'

# define the number of filenames listed in each csv, adjust if receiving errors
filenames_per_csv = 40000

dir_list = []

with FTP(ftp_url) as ftp:
    ftp.login( user=usr, passwd=pwd)
    ftp.cwd(path)
    
    ftp.retrlines('NLST', dir_list.append )

dir_list.sort()
count = len(dir_list)
num = filenames_per_csv
iter_num = math.ceil(count / num)

end_num = count
start_num = end_num - num

while(iter_num > 0):
    print(f'{iter_num} Start num: {start_num}, End num: {end_num}')
    output_file = open(f"server_${folder}_{iter_num:02}.csv", "w")
        
    for line in dir_list[start_num:end_num]:
        if line == 'thumbnail':
            pass
        else:
            line_split = line.split()
            line = line_split[-1] + '\n'
            output_file.write(line)

    output_file.close()
    iter_num -= 1
    end_num = start_num
    
    if end_num >= num:
        start_num -= num
    else:
        start_num = 0
