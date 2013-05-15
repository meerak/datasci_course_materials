import sys
import json 

dict = {} # initialize an empty dictionary

def main():
    global dict
    
    tweet_file = open(sys.argv[1])
    
    for tweet in tweet_file.readlines():
        parsed_text = json.loads(tweet)
        if parsed_text.get("entities") is not None and parsed_text["entities"].has_key("hashtags"):
            hashtags =  parsed_text["entities"]["hashtags"]
            for item in hashtags:
                tag = item.get("text")
                if tag is not None:
                    if(dict.has_key(tag)):
                        dict[tag] += 1
                    else:
                        dict[tag] = 1
    
    result = sorted(dict.keys(), key = lambda k:dict[k], reverse=True )
    for i in range(10):
        print result[i].encode('utf-8'), float(dict[result[i]])
if __name__ == '__main__':
    main()
