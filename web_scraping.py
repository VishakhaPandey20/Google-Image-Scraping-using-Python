import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os

# Import required libraries
save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Set a fake User-Agent to avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Define the search query
query = "Virat Kohli"
response = requests.get(
    f"https://www.google.co.in/search?q={query}&tbm=isch",
    headers=headers
)

print(response)  # Check the response status

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
images_tags = soup.find_all("img")

# Remove the first tag (usually the logo or unwanted)
del images_tags[0]

# Download and save images
img_data_mongo = []
for i in images_tags:
    image_url = i["src"]
    image_data = requests.get(image_url).content
    mydict = {"index": image_url, "image": image_data}
    img_data_mongo.append(mydict)

    with open(os.path.join(save_dir, f"{query}_{images_tags.index(i)}.jpg"), "wb") as f:
        f.write(image_data)
