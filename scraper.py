# Web scraping from a static page

import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL) # HTTP get request to given URL

# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, "html.parser")

# Find the html element with id
results = soup.find(id="ResultsContainer")

# This returns an iterable containing all the job postings on the page
job_elements = results.find_all("div", class_="card-content")

key = input("What job are you looking for: ")

# Now find all the jobs that contain the key
key_jobs = results.find_all(
    "h2", string=lambda text: key in text.lower()
)

# Use .parent attribute to select the parent element of the element specified
# We can also use .child and .sibling
key_job_elements = [
    h2_element.parent.parent.parent for h2_element in key_jobs
]

# Find the job title, company name and location based on the key
for job_element in key_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    
    # Show the link for the job application
    links = job_element.find_all("a")
    link_url = links[1]["href"]
    print(f"Apply here: {link_url}")
    print()

print(len(key_job_elements), "matches found.")