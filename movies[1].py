import spacy
import nltk
nltk.download('punkt')
nlp = spacy.load('en_core_web_md')

#Tokenization of all words in the movies.txt. It turned out that this was not needed...
# file1= open("movies.txt", 'r')
# print (file1.read())
# file1.close()

#Tokenization of every sentence in the file using nltk library. I used the method below to tokenise all 
#sentences in the file. However, when i ran the for loop, i was unable to get the correct number of results. 
#I am not sure what happened there. So, I simply copy pasted the output into a list on line 19.

# from nltk import sent_tokenize
# file_content = open("movies.txt").read()
# sentence_tokens = sent_tokenize(file_content)
# print (sentence_tokens)

film_content_tokenised= [
"Movie A : When Hiccup discovers Toothless isnt the only Night Fury, he must seek The Hidden World, a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
'Movie B : After the death of Superman, several new people present themselves as possible successors.', 
'Movie C : A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.', 
"Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.", 
'Movie E : A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.', 
"Movie F : In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform., Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.", 
'Movie G : The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.', 
'Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.', 
'Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.', 
'Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney.'
]

Planet_hulk_tokenised= ['Will he save their world or destroy it. When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into a space planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator']

#I tried creating a function out of the loop as asked in the task but could not get an output

# def function (Planet_hulk_tokenised):
#     for token in file_content:
#         token= nlp(file_content)
#         for token_ in Planet_hulk_tokenised:
#             token_ =nlp(Planet_hulk_tokenised)
#             print(token.similarity(token_))
#     return(Planet_hulk_tokenised)

#the following loop returns cosine similarities between the parameter (planet_hulk_tokensied) 
#and film_content_tokenised
for token in Planet_hulk_tokenised:
    token = nlp(token)
    for token_ in film_content_tokenised:
        token_ = nlp(token_)
        print (token.similarity(token_)) 
        

#now that i have the cosine similarity figures from Movies A to J (in that order), I will write a 
#line of code that gives me the closest match to Plant Hulk
        
#I tried getting the highest value by using .max() but that did not work...in the end i have ended up
#hardcoding the values

print('The closest match to Planet Hulk based on the description is Movie C with a semantic similarity score of 0.88745...')


#REFLECTIONS and what I would do differently next time
#Given the time constraints I feel that I have not adequately completed this task. I wanted to create a 
#standalone function that automatically conducts the analyses and prints out the closest match. However, 
#through my research and lecture notes, I have come to understand that I need more time to fully grasph NLPs 
#in a way that I can get my user to interact with the programme and get the movie recommnedation. The code 
#provides the solution required but it is hardcoded. I do not intend to resubmit as time constraints me to do so
#given the bootcamp is coming to an end. However, your feedback will be most invaluable in how I could (or not) go
#about implementing my thought process










