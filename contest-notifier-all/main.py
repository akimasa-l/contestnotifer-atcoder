import subprocess
import os
import shlex
import platform
files=(
    "./find_contest.py",
    "./get_from_posts.py",
    "./merge.py"
)
p="python3 " if platform.system()=="Linux" else "python "
commit=lambda:subprocess.run(['git', 'commit', '-am', "Updated on Raspberry pi"])
git_control=lambda c:subprocess.run(['git', c, 'origin', 'master'])
pull=lambda:git_control("pull")
push=lambda:git_control("push")

pull()
commit()
push()

for file in files:
    subprocess.run(p +file,shell=True)
    #os.system(p +file)
    print("Done")

commit()
push()