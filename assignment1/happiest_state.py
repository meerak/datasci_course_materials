import sys
import json 

scores = {} # initialize an empty dictionary
state_score =  {}
def buildDictionary(file):
    global scores
    afinnfile = open(file)
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def lines(fp):
    print str(len(fp.readlines()))

def main():
    global state_score
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildDictionary(sys.argv[1])
    # lines(sent_file)
    # lines(tweet_file)
    
    for tweet in tweet_file.readlines():
        parsed_text = json.loads(tweet)
        sum=0
        place = parsed_text.get("place")  
        if  place is not None and place.get("country") == "United States":
            state = place.get("full_name")[-2:]
            if parsed_text.has_key("text"):
                tweet_text =  parsed_text["text"].split()
                for word in tweet_text:
                    if scores.has_key(word):
                        sum += scores[word]
                    else:
                        sum+=0
            if state_score.has_key(state):
                state_score[state] = state_score[state][0] + sum, state_score[state][1] +  1 
            else:
                state_score[state] = (sum , 1)
   
    result = sorted(state_score.keys(), key=lambda x:float(state_score[x][0])/state_score[x][1], reverse = True)
    print result[0]
    # for key in  sorted(state_score.keys(), key=lambda x:float(state_score[x][0])/state_score[x][1], reverse = True):
        # print key.encode('utf-8'), float(state_score[key][0])/state_score[key][1]
if __name__ == '__main__':
    main()
