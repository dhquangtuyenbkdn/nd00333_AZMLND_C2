import urllib.request
import requests
import json
import os
import ssl

#def allowSelfSignedHttps(allowed):
#    bypass the server certificate verification on client side
#   if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
#       ssl._create_default_https_context = ssl._create_unverified_context
#
#allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.


# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://5f6b1d29-4398-4cca-9e39-e0cdabd75873.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '5NZCIOeyAA4e8eFszibS7gXKwmN0beo1'

# Two sets of data to score, so we get two results back
data =  {
  "Inputs": {"data":
        [
          {
            "age": 17,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 971,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
          {
            "age": 87,
            "campaign": 1,
            "cons.conf.idx": -46.2,
            "cons.price.idx": 92.893,
            "contact": "cellular",
            "day_of_week": "mon",
            "default": "no",
            "duration": 471,
            "education": "university.degree",
            "emp.var.rate": -1.8,
            "euribor3m": 1.299,
            "housing": "yes",
            "job": "blue-collar",
            "loan": "yes",
            "marital": "married",
            "month": "may",
            "nr.employed": 5099.1,
            "pdays": 999,
            "poutcome": "failure",
            "previous": 1
          },
      ]
    }
}

#data =  {"data":
#        [
#          {
#            "age": 17,
#            "campaign": 1,
#            "cons.conf.idx": -46.2,
#            "cons.price.idx": 92.893,
#            "contact": "cellular",
#            "day_of_week": "mon",
#            "default": "no",
#            "duration": 971,
#            "education": "university.degree",
#            "emp.var.rate": -1.8,
#            "euribor3m": 1.299,
#            "housing": "yes",
#            "job": "blue-collar",
#            "loan": "yes",
#            "marital": "married",
#            "month": "may",
#            "nr.employed": 5099.1,
#            "pdays": 999,
#            "poutcome": "failure",
#            "previous": 1
#          },
#          {
#            "age": 87,
#            "campaign": 1,
#            "cons.conf.idx": -46.2,
#            "cons.price.idx": 92.893,
#            "contact": "cellular",
#            "day_of_week": "mon",
#            "default": "no",
#            "duration": 471,
#            "education": "university.degree",
#            "emp.var.rate": -1.8,
#            "euribor3m": 1.299,
#            "housing": "yes",
#            "job": "blue-collar",
#            "loan": "yes",
#            "marital": "married",
#            "month": "may",
#            "nr.employed": 5099.1,
#            "pdays": 999,
#            "poutcome": "failure",
#            "previous": 1
#          },
#      ]
#    }
#

#body = str.encode(json.dumps(data))
#headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}
#req = urllib.request.Request(scoring_uri, body, headers)
#
#try:
#   response = urllib.request.urlopen(req)
#
#   result = response.read()
#   print(result)
#except urllib.error.HTTPError as error:
#   print("The request failed with status code: " + str(error.code))
#
#   # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
#   print(error.info())
#
# Convert to JSON string
input_data = json.dumps(data) 
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


