def main():
    import platform
    if platform.system()!="Linux":
        exit()
    import psutil
    for proc in psutil.process_iter(['pid', 'name', 'username',"cmdline"]):
        if proc.info["cmdline"]==['/usr/bin/python3', 'atcoderbot_discord.py']:
            proc.kill()