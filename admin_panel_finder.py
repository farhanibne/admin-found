#!/usr/bin/env python
# -*- coding: UTF-8 -*-
try:
    import requests
except:
    print("please wait installing 'requests' module... ")
    import subprocess

    subprocess.run("pip install requests")
    print("\n install finished. Re-start this tool.")

import requests


def findAdmin():
    file = open("web.txt", "r");
    link = "http://www." + input("Enter Site Name \n(ex : example.com or www.example.com ): ")
    aa = requests.get(link).status_code

    try:
        print("\n\nAvilable links : \n")
        while True:
            sub_link = file.readline()
            if not sub_link:
                break
            req_link = link + "/" + sub_link
            aa = requests.get(req_link).status_code

            try:
                if aa == 404:
                    print("Trying... " + sub_link)
                elif aa == 200:
                    print("[FOUND] ", req_link, aa)
                    # input("Press enter to continue or press CTRL+C to stop process. ")
            except:
                print("Process stopped. ")
                # input("")
    except:
        print("Invalid url or check your internet connection.")
        # input("Enter to exit ")


def Credit():
    print("#######################################")
    print("#    +++ Admin Panel Finder v1 +++    #")
    print("#            Developed by             #")
    print("#          DZ Hacking Gang            #")
    print("#######################################")


Credit()
findAdmin()
