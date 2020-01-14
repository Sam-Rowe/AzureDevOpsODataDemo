#!/bin/ruby
require 'frodata'


# Set the PAT token up as an environment variable DevOpsPAT and it is used with
pat_token = ENV['DevOpsPAT'] || "CREATE_YOUR_OWN_PAT"

# Set the User name up as an environment variable DevOpsUser and it is used with
user_name = ENV['DevOpsUser'] || "user"

orgName="samuelrowe-ms"
project="Home%20Improvements"
version="v2.0"
#https://analytics.dev.azure.com/samuelrowe-ms/Home%20Improvements/_odata/v2.0/WorkItems/?$Select=WorkItemId

endpoint="https://analytics.dev.azure.com/#{orgName}/#{project}/_odata/#{version}/"

devops = FrOData::Service.new(endpoint, {name: 'DevOpsODataDemo'}) do |conn|
    conn.basic_auth(ENV['DevOpsUser'],ENV['DevOpsPAT'])
end

#puts devops.entity_types
#puts devops.entity_sets
work_items = devops["WorkItems"]

#Docs say this should work but bombs out, bug possibly?
#puts("There are #{work_items.count} Work Items")

odata_query = devops['WorkItems'].query
odata_query.select("Title,WorkItemType,State,CreatedDate,WorkItemId")
odata_query.order_by("CreatedDate")
results = odata_query.execute
results.each do | wi |
    puts("#{wi['Title']} (ID\# #{wi['WorkItemId']}) is a #{wi['WorkItemType']} and is #{wi['State']}")
end

