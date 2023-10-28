#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# =============================================================================
#Anaconda Prompt: conda install -c conda-forge wordcloud
#Created on Sat Apr 11 14:35:48 2020

#@author: Jaya Sindhura
#Need to run with python3:  python3 Image_Desc_Keywords_Extraction.py

#Required installations :
#pip3 install -U numpy
#pip3 install -U nltk
#python3
#>>>import nltk
#>>>nltk.download('popular')  #downloads all popular & required nltk packages
#pip3 install -U numpy
#pip3 install -U pandas
#pip3 install -U scikit-learn
#pip3 install -U wordcloud

#Purpose of the script
#1. This script identifies & extracts the key words in each figure description through on Natural Language Processing & Cleansing Steps.(using NLTK libraries) and loads into a text file individually for each paper.
#2. Counts the occurrence of each word in the paper and stores it in a data frame,which can be loaded into a text file
#3. Extracts top 30 key words from each paper
#4. Generates wordclouds of top 30 words for each paper.

#5. This Script also identifies & extracts top 10 Keywords from all the papers put together and generates wordcloud for those 1o keywords.
#6. These 10 Key words can be used as 10 classes for model classfication.

# =============================================================================
import io
import os
import sys
import re
from collections import defaultdict
import numpy as np

in_path =  '/home/jpailla/Images_Desc_Split_Join_allpapers'  #image description split join path
out_path_Key_words = '/home/jpailla/Image_Desc_Keywords' #keywords from images descriptions
out_path_Key_word_counts = '/home/jpailla/Image_Desc_Keyword_Counts' # count of each key word from the paper

#data frame to store top n keywords.This data frame is loaded after cleansing and count vectorizer part is done
import pandas as pd
pd.set_option('max_colwidth',150)
pd.set_option('display.max_rows', 1000)
top_keywords_df = pd.DataFrame(columns=['Paper', 'Top_Words'])

#intializing dataframes to get top 10 keywords from all papers together,so that all all keywords from individual papers can be concatented into a single data frame and extract top 10 keywords from that data frame.
top_keywords_all_papers_df = pd.DataFrame()

#main code
for filename in os.listdir(in_path):
    full_file = os.path.join(in_path, filename)
    imagedesc_key_word_file = os.path.join(out_path_Key_words, filename)
    key_word_count_file = os.path.join(out_path_Key_word_counts, filename)
    with io.open(full_file, 'r',encoding='Latin-1') as infile, io.open(imagedesc_key_word_file, 'w',encoding='Latin-1') as out_key_words_file, io.open(key_word_count_file, 'w',encoding='Latin-1') as out_key_word_counts_file:
        lines = infile.read().splitlines()
        lists = [[" ".join(tag.split(" ")[:2]) , " ".join(tag.split(" ")[2:])] for tag in lines] 
        data = defaultdict(list) # to retain duplicate keys in dictionary
        for item in lists:
            key = item[0]
            value = item[1]
            data[key].append(value) # this will print all the duplicate occurences under single key,like if there are multiple valules for Figure 1(a),everything will be printed under single key Figure 1(a)
        #print(data)
        
        #Converting above Dictionary "data" to dataframe with 2 columns
        import pandas as pd
        pd.set_option('max_colwidth',150)
        pd.set_option('display.max_rows', 1000)
        data_df = pd.DataFrame(data.items(),columns=['Figure', 'Description'])
              
        #converting list of elements in Description column to regular line of strings
        data_df['Description']=data_df.Description.apply(''.join)   
        #display(data_df) 
        
        
        #splitting the each description line to multiple words
        def clean_text_round1(text):  
            text= text.split()
            return text
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round1))
                
        
        #lemmatization
        from nltk.stem import WordNetLemmatizer
        
        def clean_text_round2(text):  
            lemmatized_list=[]
            for ele in text:
                lemmatized = WordNetLemmatizer().lemmatize(ele.lower())
                if re.match(r"[0-9].*", ele): #to get 1T / 2T as it is instead of 1t/2t
                    lem_word = ele
                elif ele.istitle(): #to lemmatize Crystal without converting to small letters
                    lem_word = lemmatized.capitalize()
                elif ele.upper()==ele:
                    lem_word = lemmatized.upper()
        
                elif ele.lower()==ele : # to lemmatize all smmall ltters like structures to structure
                    lem_word = lemmatized.lower()
                else: # to preserve ZnSe or KCa2Nb3O10 formuleas
                    lem_word = ele
            
                lemmatized_list.append(lem_word)
            
            return lemmatized_list
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round2))
        
                
        #Punctuations Removal
        def clean_text_round3(text): 
           punctuation = re.compile(r'[.,?!:;]')#digit or sepcial charater
           post_punctuation = []
           for words in text:
                word=punctuation.sub("",words)
                if len(word)>0:
                    post_punctuation.append(word)
           return post_punctuation
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round3))
        
        
        
        #code to give priority to capital lettered words over small lettered at the same time duplicates are removed from each sentence
        #eg: Crystal is picked over crystal,
         
        from collections import OrderedDict
        def clean_text_round4(text): 
             wordset = OrderedDict()
             wordset = OrderedDict.fromkeys(text)
             nodup_list = [sentnce for sentnce in wordset if sentnce.istitle() or sentnce.title() not in wordset or sentnce.isdigit()] 
             return nodup_list
         
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round4))
        
         
        
        #Stop Words Removal
        from nltk.corpus import stopwords
        def clean_text_round5(text): 
            stop_words = set(stopwords.words('english'))
            without_stopwords = [x for x in text if x not in stop_words]
            return without_stopwords
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round5))
        
        
        
        #To eliminate the strings completely having "=" in between like (x=yellow) or (calcium=yellowgermanium=purplehydrogen=black) etc
        #To eliminate strings with in the brackets like (orange) but not Znse(butylamine)
        def clean_text_round6(text):
            new_tokens = []
            for token in text:
                if not (token.find("=")!=-1 or re.match('\(.*?\)',token)):
                    new_tokens.append(token)
            return new_tokens
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round6))
        
        
        #commenting this cleanisng part as there words like 5 s,250 s which are bigrams that needs to ba handled
        #If we cleanse the data by removing numbers alone,then we are loosing important data.
        #Removing only digits like 19,201 etc

 
        def clean_text_round7(text):
             new_tokens = []
             for token in text:
                 if not token.isdigit():
                     new_tokens.append(token)
             return new_tokens
         
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round7))
 
        
        #adding few more stopwords,which are in description but not required for us.
        from nltk.corpus import stopwords
        stopwords = stopwords.words('english')
        newStopWords = ['Copyright','Publishing','Reprinted','permission','image','ref','K','min']
        stop_words = stopwords + newStopWords
        
        def clean_text_round8(text): 
            without_stopwords = [x for x in text if x not in stop_words]
            return without_stopwords
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round8))
        
        
        #Removing some unecessary words with certain patter like right98(i.e right +pagenumber),field etc
        def clean_text_round9(text):
            new_tokens = []
            for token in text:
                if not (token.find("ﬁeld")!=-1 or re.match('right*',token)):   #the word is not exactly field,character f is written differently
                    new_tokens.append(token)
            return new_tokens
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round9))
        
        
        
        from nltk import pos_tag
        
        def clean_text_round10(text):
            tags = pos_tag(text) 
            filterd_tags=[t for t in tags if t[1] == 'JJ' or t[1] == 'CD' or t[1] == 'NN' or t[1] == 'NNP']
            top_key_words=[] 
            for i in filterd_tags:
                top_key_words.append(i[0])
            return top_key_words
        
        data_df['Description'] = pd.DataFrame(data_df.Description.apply(clean_text_round10))
        
        
        #converting list of elements in Description column to regular line of strings otherwise CountVectorizer wont work
        data_df['Description']=data_df.Description.apply(','.join)  
        #display(data_df)
        
        #saving the dataframe to a text file(keywords of each paper individually)
        data_df.to_csv(out_key_words_file, mode='a',sep='\t')
        
        #dropping rows having blanks in descriptions otherwise it is also counted as seperate word.Converting blanks to NaN that's how pandas recognize it as blank lines
        data_df['Description'].replace('', np.NaN, inplace=True)
        data_df.dropna(subset=['Description'], inplace=True)
        
        #append all the individual data frames of all papers to a single dataframe,inorder to find out top 10 keywords among all the research papers
        top_keywords_all_papers_df = top_keywords_all_papers_df.append(data_df)

###################   Building Document-Term matrix   ############################################


        #Custom tokenizer to split based on a custom delimeter and
        def my_tokenizer(text):
            return re.split(",",text)
        
        # create a Document-Term matrix using CountVectorizer
        from sklearn.feature_extraction.text import CountVectorizer
        
        cv = CountVectorizer(tokenizer=my_tokenizer,lowercase=False)#to retain capital letters
        data_cv = cv.fit_transform(data_df.Description)
        #print(cv.get_feature_names()) #gives all the list of words 
        data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
        data_dtm.index = data_df.Figure
        data_dtm = data_dtm.transpose()
        #data_dtm.head()
        
        #print(data_cv.toarray().sum(axis=1)) #gives the sum of occrences of words figure wise (or) 
        #print(data_cv.toarray().sum(axis=0)) #gives the total word count of that particular word across the file
        
        #Adding a new column into the dataframe to hold sum of occurences of each word across all the Figure Descriptions
        data_dtm.insert(0, 'Counts',data_cv.toarray().sum(axis=0))
        
        #Final data frame sorted in descending order based on counts column to see the words with highest number of occurences
        final_df = data_dtm.sort_values(by=['Counts'], ascending=False)
        #final_df.to_pickle("final.pkl")
        
        #save the data frame
        final_df.to_csv(out_key_word_counts_file, mode='a',sep='\t')
        
###################   Fetching Top n Keywords   ############################################        
        
        #picking top 30 key words in each paper and storing it in a dataframe
        top_dict = {}
        top = final_df.Counts.head(30)
        #top_dict[filename]= list(zip(top.index, top.values)) #to store index and append all values
        top_dict[filename]= list(top.index)
        
        #creating a temporary data frame to hold top n keywords for each file seperately,and later appending it to the original data frame "top_keywords" 
        pd.set_option('max_colwidth',150)
        pd.set_option('display.max_rows', 1000)
        temp_top_keywords_df = pd.DataFrame(top_dict.items(),columns=['Paper', 'Top_Words'])
        temp_top_keywords_df['Top_Words'] = temp_top_keywords_df.Top_Words.apply(' '.join) #converting list of values in "Top_words" column to just stream of values

        top_keywords_df = top_keywords_df.append(temp_top_keywords_df)

print("Keywords & Wordcounts of all Papers extracted:successfully")       
# just giving the index with paper numbers other wise everything in index is appearing as 0
full_names = ['Paper 1','Paper 3','Paper 4','Paper 6','Paper 7','Paper 9','Paper 10','Paper 11','Paper 12','Paper 13','Paper 14','Paper 15','Paper 16','Paper 17','Paper 19','Paper 20','Paper 21','Paper 22','Paper 23','Paper 24']
top_keywords_df.index = full_names 
# =============================================================================
#         # Find the top 10 words for each figure
#         top_dict = {}
#         for c in data_dtm.columns:
#             top = data_dtm[c].sort_values(ascending=False).head(30)
#             top_dict[c]= list(zip(top.index, top.values))
#         top_dict
#         
#         
#         # Print the top 10 words for each figure
#         for Figure, top_words in top_dict.items():
#             print(Figure)
#             print(', '.join([word for word, count in top_words[0:15]]))
#             print('---')
#         
#         
#         #import numpy  # need to check this way as well to save the data
#         #numpy.savetxt(r'example.txt', final_df, fmt='%d')
# =============================================================================

###################   Generating Word clouds   ############################################ 
# Anaconda Prompt: conda install -c conda-forge wordcloud
 
from wordcloud import WordCloud        
#wc = WordCloud(background_color="white", colormap="Dark2",max_font_size=150, random_state=42)
wc = WordCloud()

# Reset the output dimensions
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 6]
#to get the titles for each wordcloud
full_names = ['Paper 1','Paper 3','Paper 4','Paper 6','Paper 7','Paper 9','Paper 10','Paper 11','Paper 12','Paper 13',
              'Paper 14','Paper 15','Paper 16','Paper 17','Paper 19','Paper 20','Paper 21','Paper 22','Paper 23','Paper 24']

# Create subplots for each paper
i=0
for row in top_keywords_df.iterrows():
    if top_keywords_df.index[i] == full_names[i]: #if df.index=Paper 1 and Fullnames= Paper 1 then fetch the Top_keywords from the dataframe and generate wordcolud
        wc.generate(top_keywords_df.loc[full_names[i]].Top_Words) #loc[] is to get the row corresponding to Paper 1 in the dataframe and extract Top_keywords from that row
        plt.subplot(4, 5, i+1) #dimensions of the subplot 4 rows ,5 columns
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title(full_names[i])
    i=i+1 #to iterate over each value in Full_names and check the equallity in if condition
plt.show()

############################################################################################################
################### Fetching Top 10 keywords from all papers together ###########################
###################   Building Document-Term matrix   ############################################
top_keywords_all_papers_df.to_csv("/home/jpailla/Image_Desc_Keywords/Keywords_all_papers.txt", mode='a',sep='\t')
#Custom tokenizer to split based on a custom delimeter and
def my_tokenizer(text):
    return re.split(",",text)

# create a Document-Term matrix using CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(tokenizer=my_tokenizer,lowercase=False)#to retain capital letters
data_all_papers_cv = cv.fit_transform(top_keywords_all_papers_df.Description)
#print(cv.get_feature_names()) #gives all the list of words 
data_all_papers_dtm = pd.DataFrame(data_all_papers_cv.toarray(), columns=cv.get_feature_names())
data_all_papers_dtm.index = top_keywords_all_papers_df.Figure
data_all_papers_dtm = data_all_papers_dtm.transpose()

#Adding a new column into the dataframe to hold sum of occurences of each word across all the Figure Descriptions
data_all_papers_dtm.insert(0, 'Counts',data_all_papers_cv.toarray().sum(axis=0))

#Final data frame sorted in descending order based on counts column to see the words with highest number of occurences
final_all_papers_df = data_all_papers_dtm.sort_values(by=['Counts'], ascending=False)
#final_df.to_pickle("final.pkl")

#save the data frame
final_all_papers_df.to_csv("/home/jpailla/Image_Desc_Keyword_Counts/Keyword_counts_all_papers.txt", mode='a',sep='\t')


        
###################   Fetching Top 10 Keywords   ############################################        
        
#picking top 10 key words among all papers together and storing it in a dataframe
top_dict_all = {}
top_all = final_all_papers_df.Counts.head(10)
#top_dict[filename]= list(zip(top.index, top.values)) #to store index and append all values
filenm = "keyword_counts_all_papers.txt"
top_dict_all[filenm]= list(top_all.index)

#creating a data frame to hold top n keywords 
pd.set_option('max_colwidth',150)
pd.set_option('display.max_rows', 1000)
top_keywords_all_papers_df = pd.DataFrame(top_dict_all.items(),columns=['Paper', 'Top_Words'])
top_keywords_all_papers_df['Top_Words'] = top_keywords_all_papers_df.Top_Words.apply(' '.join) #converting list of values in "Top_words" column to just stream of values
top_keywords_all_papers_df.to_csv("/home/jpailla/Image_Desc_Keywords/Top_10_keywords_all_papers.txt", mode='a',sep='\t')
###################   Generating Word clouds   ############################################ 
# Anaconda Prompt: conda install -c conda-forge wordcloud
 
from wordcloud import WordCloud        
wc = WordCloud(background_color="white", colormap="Dark2",regexp=u"[a-zA-Z0-9()']+",
               max_font_size=150, random_state=42,)

# Reset the output dimensions
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [14, 3]
#to get the titles for each wordcloud
#full_names = ['All Papers Top Keywords']


# Create wordcloud
wc.generate(top_keywords_all_papers_df.Top_Words[0])
plt.subplot(1, 1, 1)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad = 0)
#plt.title(full_names[index])
plt.show()















       
        
        
      
        
        
        
        
        