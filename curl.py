#!/usr/bin/python3
import requests

tenantName = "https://atg-mkt-stage2-"
domainName = ".campaign.adobe.com"
rtest = "/r/test"
try:
 for i in range(1, 5):
   finalURL = (tenantName +str(i) +str(domainName) +str(rtest))
   res = requests.get(finalURL)
   print(res.text)
except:
  print('seems no more containers available')
