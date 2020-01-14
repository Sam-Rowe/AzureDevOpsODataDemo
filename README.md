# AzureDevOpsODataDemo
Odata example for Azure DevOps using Python and Ruby. I am not a full time developer be kind and offer improvements :)


## References
[Authentication for OData](https://docs.microsoft.com/en-us/azure/devops/report/powerbi/client-authentication-options?view=azure-devops)

[OData VS Code extension](https://docs.microsoft.com/en-us/azure/devops/report/powerbi/odataquery-connect?view=azure-devops)

## Python Libraries tried :(
* [SAP python-pyodata](https://github.com/SAP/python-pyodata) Doesn't support OData v4 so no JSON responses
* [tuomur python-odata](https://github.com/tuomur/python-odata) Should work but can't get it to install on WSL or Windows

## Ruby libraries
* [wrstudios frodata](https://github.com/wrstudios/frodata) Only one I got working. I have an example using a query to select a couple of properties from each work item.