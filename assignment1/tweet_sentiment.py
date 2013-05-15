import sys
import json 

scores = {} # initialize an empty dictionary
    
def buildDictionary(file):
    global scores
    afinnfile = open(file)
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildDictionary(sys.argv[1])
    # lines(sent_file)
    # lines(tweet_file)
    
    for tweet in tweet_file.readlines():
        parsed_text = json.loads(tweet)
        sum=0
        if parsed_text.has_key("text"):
            tweet_text =  parsed_text["text"].split(" ")
            for word in tweet_text:
                if scores.has_key(word):
                    sum += scores[word]
                else:
                    sum+=0
        print sum
if __name__ == '__main__':
    main()
