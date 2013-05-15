import urllib
import json

# responseURL = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=1")
# response =  json.load(responseURL)

# print type(response)

# print response.keys()

#print response["results"]

#print type(response["results"])

#print response["results"][0]

#print type(response["results"][0])

#print response["results"][0].keys()

url = "http://search.twitter.com/search.json?q=microsoft&page="
for i in range(1,11):
    print "\nPage " + str(i)
    responseURL = urllib.urlopen(url + str(i))
    response =  json.load(responseURL)
    results = response["results"]
    for tweet in results:
        unicode_string = tweet["text"]
        encoded_string = unicode_string.encode('utf-8')
        print "\n" + encoded_string
