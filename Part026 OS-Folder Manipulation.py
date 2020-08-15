#OS-Folder Manipulation
import os
from datetime import datetime

#os.mkdir("student")
#os.makedirs('student/Grade/ninthGrade/student.txt')
#os.rmdir("student")
#os.rmdir('student/Grade/ninthGrade/student.txt')
      #to gete " st_atime ""
#print(os.stat("student"))
#print(os.stat("student").st_atime)
#os.chdir("Url with forward slash")
#print(get.cwd())

# modified_time = os.stat("student").st_atime
# print(datetime.timestamp(modified_time))

current_dir=os.getcwd()
for dirpath,drinames,filenames in os.walk(current_dir):
    print(drinames)
    print(filenames)