import sys
import json

frequency_dict = {}

def buildDictionary(file):
    global scores
    afinnfile = open(file)
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global frequency_dict
    
    tweet_file = open(sys.argv[1])
    count = 0
    for tweet in tweet_file.readlines():
        parsed_text = json.loads(tweet)
        if parsed_text.has_key("text"):
            tweet_text =  parsed_text["text"].split()
            for word in tweet_text:
                if frequency_dict.has_key(word):
                    frequency_dict[word] += 1
                else:
                    frequency_dict[word] = 1
                count += 1
    
    word_frequency = float(1) / count 
    for key in frequency_dict.keys():
        print key.encode('utf-8'), frequency_dict[key] * word_frequency

if __name__ == '__main__':
    main()
