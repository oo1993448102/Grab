import os
import time

source = '/Users/scott_he/Documents/zip/origin'
target_dir = '/Users/scott_he/Documents/zip/zip_one'
target_name = target_dir+os.sep+time.strftime('%d%h%m%s')+'.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {} {}'.format(target_name,source)

# zip -r /Users/scott_he/Documents/zip/zip_one/15Feb021487149803.zip /Users/scott_he/Documents/zip/origin
print(zip_command)
if os.system(zip_command) == 0:
    print('success')
else:
    print('fail')

