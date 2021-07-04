#!/usr/bin/env python

import requests

def download(url):
    get_request = requests.get(url)
    # print(get_request.content)
    file_name = url.split("/")[-1]  # we use this to get the last content of url so that could be used as file_name 
    # or also we can specify our own file name with proper file extension
    with open(file_name,"wb") as out_file:
    	out_file.write(get_request.content)

    # print("File Downloaded")


download("http://localhost/Nope.exe")

