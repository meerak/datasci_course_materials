import sys
import json

scores = {} # initialize an empty dictionary
new_words = {}

def buildDictionary(file):
    global scores
    afinnfile = open(file)
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global new_words
    
    tweet_file = open(sys.argv[2])
    buildDictionary(sys.argv[1])
    
    for tweet in tweet_file.readlines():
        parsed_text = json.loads(tweet)
        sum=0
        if parsed_text.has_key("text"):
            tweet_text =  parsed_text["text"].split()
            for word in tweet_text:
                if scores.has_key(word):
                    sum += scores[word]
            for word in tweet_text:
                if not scores.has_key(word):
                    if new_words.has_key(word):
                        tuple = new_words[word][0] + sum, new_words[word][1] +  1 
                        new_words[word] = tuple
                    else:
                        new_words[word] = (sum , 1)
    for key in new_words.keys():
        print key.encode('utf-8'), float(new_words[key][0])/new_words[key][1]

if __name__ == '__main__':
    main()
