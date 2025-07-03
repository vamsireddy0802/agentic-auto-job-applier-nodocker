import requests
from bs4 import BeautifulSoup

def fetch_indeed_jobs(query, location):
    query = query.replace(" ", "+")
    location = location.replace(" ", "+")
    url = f"https://www.indeed.com/jobs?q={query}&l={location}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = []
    for div in soup.find_all("div", class_="job_seen_beacon"):
        try:
            title = div.find("h2").text.strip()
            desc = div.get_text().strip()
            link = "https://www.indeed.com" + div.find("a")["href"]
            jobs.append({"title": title, "description": desc, "url": link})
        except:
            continue
    return jobs