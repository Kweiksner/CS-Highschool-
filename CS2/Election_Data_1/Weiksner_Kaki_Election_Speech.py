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
    """
    Args: 
        cvsname(str): The name of the csv file 
        fhand(str): The name of the file that the user wants the data from 
    Void: 
        Returns Nothing 
        
    """
     #allows each word to be seen as different words
    counts = dict()                                                                     #creates new dictionary
    for line in fhand:
        line = line.rstrip()                                                            #splits each line                                                    
        line = line.translate(line.maketrans("", "", string.punctuation))               #removes punctuation for the string           
        line = line.lower()                                                             #makes everything lowercase        
        words = line.split()                                                            #splits all of the lins into individual words
   
        #counts the amount of times a word appears and disregards any word in the list of bad words 
        for word in words:
            if word not in bad_words:                                                   #if words not in bad words
                if word not in counts:                                                  #if word has not already been added, it adds it to the list
                    counts[word] = 1
                else:                                                                   #if the word is already in counts than adds one to it's counter
                    counts[word] += 1
    #sorts the dictionary 
    sorted_words = dict(sorted(counts.items(), key=lambda item: -item[1]))

    #puts the top 10 frequently occuring words into a new dictionary 
    sorted_dict = dict()                                                             #creates a dictionary for the sorted words
    count = 0
    for i in sorted_words:                                                          #goes through each word
        if count < 10:                                                              #only goes through the first 10 
            sorted_dict[i] = sorted_words[i]                                        #put each word into the sorted dictionary
            count += 1
        else:
            break

    '''
    # writing to csv file
    with open(csvname, 'w',newline="") as csvfile:
        csvwriter = csv.writer(csvfile)                                  # creating a csv writer object
        fields = ['word', 'count']                                       #creates the two headers 
        csvwriter.writerow(fields)                                      #writes the rows for the fields 
        for word in sorted_dict:
            csvwriter.writerow([word, sorted_dict[word]])                #writes the rows for the words
        '''
#creates the plotly chart 
    axis('equal')
    pie(sorted_dict.values(), labels=sorted_dict.keys())
    show()
    

fhand = open('kamala_new.txt', "r")                                              #opens the Kamala text file    
kamala_csv = "kamala_speech.csv"                                            #opens the csv file
frequency_piechart(kamala_csv, fhand)                                       #calls the function with 2 parameters
fhand = open('cleaned_trump_speech_transcript.txt')                         #opens the Trump text file 
trump_name = "cleaned_trump_speech_transcript.csv"                          #opens the Trump csv file 
frequency_piechart(trump_name, fhand)                                        #calls the function with 2 parameters                        