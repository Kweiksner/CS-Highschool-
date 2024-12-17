'''
FlowerBox 
Name: Kaki Weiksner 
Description: Creates a pie chart of the frequently used words 
Bugs: None that I have found
Feautures: Sorts the data I used Plotly 
Logs: 1.0 intial release 1150 
Sources:I got the spllitting lines to words part from the textbook. I found my csv writing and sorting a dictionary on Geeks for geeks. Lastly I got the plotly chart information from Matplotlib.com.  
'''

#imports files from my computer 
import string 
import csv
import pandas as pd
from matplotlib.pyplot import pie, axis, show

#list of the words do not add value to the speach 
bad_words= ["for", "to", "as","my", "you", "being", "an", "me", "and", "so", "very", "when", "about", "the", "we", "have", "am", "with", "your", "is", "will", "who", "are", "going", "be", "who", "has","put", "in", "that", "here", "was", "but", "im", "had", "one", "of", "her", "own", "every", "our", "a", "i", "this", "it", "on", "their", "not", "country", "by", "they", "from", "been", "all", "them", "at", "more", "she", "new", "no", "were", "ever", "or", "can", "its", "these", "make", "other", "now", "what", "because", "out", "never", "us", "also", "great", "than", "most", "any", "way", "up", "into", "which", "years", "back", "just" ]

  

def frequency_piechart(csvname, fhand): 
        #allows each word to be seen as different words
        counts = dict()
        for line in fhand:
            line = line.rstrip()                                                                                                                    
            line = line.translate(line.maketrans("", "", string.punctuation))               
            line = line.lower()                     
            words = line.split()                                    
            
            #counts the amount of times a word appears and disregards any word in the list bad words 
            for word in words:                                          #goes through each word
                if word not in bad_words:                               # if the word is not in bad words
                    if word not in counts:                              #if the word has not been counted yet
                        counts[word] = 1                                # adds words to counts and sets it to 1 
                    else:
                        counts[word] += 1                               #adds one to counts

        #sorts the dictionary 
        sorted_words = dict(sorted(counts.items(), key=lambda item: -item[1]))

        #puts the top 10 frequently occuring words into a new count 
        sorted_dict = dict()                                        #creates a new dictionary 
        count = 0
        for i in sorted_words:                                      # loop for the number of sorted words                  
            if count < 10:                                          # when count is less than ten
                sorted_dict[i] = sorted_words[i]                    #sets sorted dictionary to the same as the sorted words
                count += 1                                          #adds one to count
            else:
                break
        print(sorted_dict)                              


        # writing to csv file
        with open(csvname, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)                                  # creating a csv writer object
            fields = ['word', 'count']                                       #creates the two headers 
            csvwriter.writerow(fields)                                      #writes the rows for the fields 
            for word in sorted_dict:
                csvwriter.writerow([word, sorted_dict[word]])                #writes the rows for the words

       #creates the plotly chart 
        axis('equal')
        pie(sorted_dict.values(), labels=sorted_dict.keys(), autopct='%1.1f%%')
        show()
    

fhand = open('kamala_new.txt')                                  #opens the Kamala text file    
kamala_csv = "kamala_speech.csv"                                #opens the csv file
frequency_piechart(kamala_csv, fhand)                           #calls the function with 2 parameters
fhand = open('cleaned_trump_speech_transcript.txt')             #opens the Trump text file 
trump_name = "cleaned_trump_speech_transcript.csv"              #opens the Trump csv file 
frequency_piechart(trump_name, fhand)                            #calls the function with 2 parameters                        