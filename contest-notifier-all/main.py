import subprocess
import os
files=(
    "./find_contest.py",
    "./get_from_posts.py",
    "./merge.py"
)
subprocess.run("git pull origin master")
for file in files:
    subprocess.run("python3 " +file,shell=True)
    #os.system("python3 " +file)
    print("Done")