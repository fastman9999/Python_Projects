import time
from datetime import datetime as dt

hosts_temp=r"C:\Users\admin\Python_Projects\Website Blocker\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=["facebook.com","www.facebook.com","pronews.gr","www.pronews.gr"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "\t \t" + website + "\n")
        print("Working hours...")
    else :
        with open(hosts_path , "r+") as file :
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Relaxing Time...")

    time.sleep(300)