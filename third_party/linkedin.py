import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """ scrape information from linkedin profiles,
    Manually scrape the information from linkedin profile
    :param linkedin_profile_url:
    :return:
    """
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dict = {'Authorization': f'Bearer {os.environ.get("PROXY_CURL_KEY")}'}
    params = {
        'linkedin_profile_url': linkedin_profile_url,
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dict)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications", "groups", "recommendations"]
    }
    return data


def mock_linkedin_request():
    mock_response = requests.get(
        'https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json')

    return mock_response