import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """scraping information based on LinkedIn profiles, Scrape the information manually"""
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Seal5/146ded8f4e8e1bc4a2f47b1d7acbf05d/raw/76311f37f89db643a901ba0d1bfb46773c7aee8c/gistfile1.txt"
        response = requests.get(linkedin_profile_url, timeout= 10)
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/seanshin5/"
        )
    )
