import subprocess
import os
import shlex
files=(
    "./find_contest.py",
    "./get_from_posts.py",
    "./merge.py"
)
commit=lambda:subprocess.run(['git', 'commit', '-am', r'"Updated on Raspberry pi"'])
git_control=lambda c:subprocess.run(f"git {c} origin master".split())
pull=lambda:git_control("pull")
push=lambda:git_control("push")

commit()
pull()
commit()
push()

for file in files:
    subprocess.run("python3 " +file,shell=True)
    #os.system("python3 " +file)
    print("Done")

commit()
push()