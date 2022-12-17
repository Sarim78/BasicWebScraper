import requests
import time

print("Welcome to python webscraper!")

time.sleep(1)

url = input("Please enter the url: ")

print("")
print("--" * 10)
print("")

getData = requests.get(url)

print(getData.text)