import os
import requests
import json

# Set the PAT token up as an environment variable DevOpsPAT and it is used with
# os.environ["DevOpsPAT"]

# Set the User name up as an environment variable DevOpsUser and it is used with
# os.environ["DevOpsUser"]

# For now I have hard coded with my org
org_name="samuelrowe-ms"
project="Home%20Improvements"
version="v2.0"

session = requests.Session()
session.auth = (os.environ["DevOpsUser"],os.environ["DevOpsPAT"])

raw_work_items = session.get("https://analytics.dev.azure.com/samuelrowe-ms/Home%20Improvements/_odata/v2.0/WorkItems/$Select=WorkItemId,Title,WorkItemType,State,CreatedDate&").text

work_items = json.loads(raw_work_items)

print(work_items)