import os
from bs4 import BeautifulSoup

file_path = "output.json"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        # file is a filehandle of the markup I want parsed
        soup = BeautifulSoup(file, 'html.parser')
        myfile = open("formattedData.txt", 'w')
        for line in soup.find_all('p'):
            myfile.write(line.get_text() + "\n")

    

