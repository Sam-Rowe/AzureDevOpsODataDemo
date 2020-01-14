import os
import requests
import pyodata

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

#session.get("https://analytics.dev.azure.com/samuelrowe-ms/Home%20Improvements/_odata/v2.0/WorkItems/?$Select=WorkItemId")

WORK_ITEM_URL = ( "https://analytics.dev.azure.com/" + org_name + "/" + project + "/_odata/" + version + "/WorkItems/?$Select=WorkItemId" )
r = session.get(WORK_ITEM_URL)
print(r.text)

SERVICE_URL = ( "https://analytics.dev.azure.com/" + org_name + "/" + project + "/_odata/" + version + "/" )

# This falls over ? I think its because it doesn't understand OData v4
devops = pyodata.Client(SERVICE_URL, session)

work_id_list = devops.entity_sets.WorkItems.get_entities()

print(work_id_list)
