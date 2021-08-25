## These Scripts are used to sync images from webserver to local_computer

### TODO: 
- Combine all scripts
- Ability to define multiple folders to compare
- fix compare script to adjust to file count

### FTP_script.py
 - Logs into websever via FTP
 - Get all image filenames in local folder and server folder
    * Created too large of file and filesnames need to be sorted at time of creation
 - Output list of filenames to multiple csv's in numeric order - server_folder_01.csv

### local_script.py
 - Get all image filenames in local folder and server folder
    * Created too large of file and filesnames need to be sorted at time of creation
 - Output list of filenames to multiple csv's in numberic order - local_folder_01.csv