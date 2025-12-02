from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))


# fetch linkedin jobs based on search query and location
def fetch_linkedin_jobs(search_query, location="india", rows=60):
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy":{
			"useApifyProxy":True,
			"apifyProxyGroups":["RESIDENTIAL"]
		}
        
    }

    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)

    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


# fetch naukri jobs based on search query and location
def fetch_naukri_jobs(search_query,location= 'india',rows=60):
    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy":{
			"useApifyProxy":True,
			"apifyProxyGroups":["RESIDENTIAL"]
		}
        
    }

    run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)

    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs