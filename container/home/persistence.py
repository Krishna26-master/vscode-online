import time
import os
from datetime import datetime
import pytz
def print(log):
    tz_india = pytz.timezone('Asia/Kolkata')
    datetime_india = datetime.now(tz_india)
    india=datetime_india.strftime("%D=>%H:%M:%S")
    with open('/app/logger','a') as logger:
        logger.write(log+'==>'+india+'\n')
data=os.getenv("RCLONE_DATA")
app_name=os.getenv("APP_NAME")
remote=os.getenv("RCLONE_REMOTE")
#Config File
os.system(f'mkdir -p /.config/rclone/')
os.system(f'touch /.config/rclone/rclone.conf')
os.system(f'echo {data} | base64 -d > /.config/rclone/rclone.conf')
print('config File Created')
#Download
os.system(f'rclone sync {remote}:{app_name} /app/WORKSPACE')
print('files Synced')
os.system('pip install -r /app/WORKSPACE/.pip')
print('Installed Python Packages in .pip File')
#upload Every 1 min
while True:
    os.system(f'rclone sync  /app/WORKSPACE {remote}:{app_name}')
    print('Files Uploaded')
    time.sleep(60)
