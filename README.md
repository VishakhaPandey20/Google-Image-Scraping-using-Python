# 🖼️ Google Image Scraping using Python

## 📌 Project Overview

This project demonstrates how to perform image scraping from **Google Images** using Python.  
The main objective was to gain hands-on experience with web scraping techniques and automate the process of collecting images from the web.

---

## 📷 Use Case

For this project, the search query used was **"Virat Kohli"**, and the goal was to extract and store multiple images from Google Images search results.

---

## 🔧 Technologies & Libraries Used

- **Python**
- `urllib.request` – For opening and reading URLs
- `requests` – For making HTTP requests
- `BeautifulSoup` – For parsing HTML content
- `os` – For handling directories and file paths

---

## 🧠 Key Steps Performed

1. **Directory Setup:**  
   Created an `images/` folder using the `os` module to store the scraped images.

2. **Sending HTTP Requests:**  
   Sent a GET request to Google Images with a custom **User-Agent** header to prevent blocks.

3. **HTML Parsing:**  
   Parsed the returned HTML using **BeautifulSoup** to find image tags.

4. **Image Extraction:**  
   Located image sources (`src` or `data-src`) and downloaded them.

5. **Saving Images:**  
   Saved the images into the created folder using a loop with proper filenames.

---

## ✅ Output

- Successfully retrieved and saved images related to the search keyword.
- Images are stored in the local `images/` directory.

---

## 🚧 Challenges Faced

- Google blocking automated scraping requests.
- Solved by setting a custom `User-Agent` header to mimic browser behavior.

---

## 🎯 Conclusion

This project showcases how web scraping tools like **BeautifulSoup**, **urllib**, and **requests** can be combined effectively to extract visual data from the web and organize it efficiently.

---

## 👤 Author

**Manish Divekar**

---

## 📝 Disclaimer

This project is for educational purposes only. Scraping Google Images may violate their terms of service. Please use responsibly and avoid overloading servers.

