import os
import requests
from tqdm import tqdm
import math
import time

url=input("Enter the url of the file you want to download: ")

r=requests.get(url)


file_size=int(r.headers['Content-Length'])
chunk_size=256

r=requests.get(url,stream=True)


extension=(os.path.splitext(url))[-1]
file="file"+extension

iterations=math.ceil(file_size/chunk_size)

with open(file, "wb") as file:
	for chunk in tqdm(r.iter_content(chunk_size=chunk_size),total=iterations):
		time.sleep(0.5)
		file.write(chunk)
