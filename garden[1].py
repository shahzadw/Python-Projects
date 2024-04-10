import spacy 
nlp = spacy.load("en_core_web_sm") #the Doc object for processed text, the "" contains the lanugage model instance
gardenpathSentences = ["We painted the wall with cracks", "I convinced her childern are noisy"]#my sentences
gardenpathSentences_add= ["Mary gave the child a Band-Aid", "That Jill never here hurts", "The cotton clothing is made of grows in Mississipppi"]
my_list= gardenpathSentences + gardenpathSentences_add
# print(len(my_list))

#tokenising and named entity recognition
doc =nlp(my_list[0])
a= doc.text.split() #assigning a variable to print item to check
print(a)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

doc1 =nlp(my_list[1])
b= doc1.text.split()
print(b)
for ent in doc1.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

doc2 =nlp(my_list[2])
c= doc2.text.split() 
print(c)
for ent in doc2.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

doc3 =nlp(my_list[3])
d= doc3.text.split() 
print(d)
for ent in doc3.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

doc4 =nlp(my_list[4])
e= doc4.text.split() 
print(e)
for ent in doc4.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

#What was the Entity and its explaination that you looked up?
#Sentence 3, Mary was recognised as a person 
#Sentence 4 Jill was recognised as a person 
#Did the entity make sense in terms of the word assosiated with it?
#For both entities, spacy.explain() managed to identify names as a Person. It makes sense
#as I would identify them the same way 

#General Comments about the solution
#I have used a sequential method to solve the above problem. This is the first iteration 
#of my solution. Upon further thinking aware that I can use a for loop and nest another loop 
#within it to run through sentences and words respectively. If I was to do this exercise again
#I would look to use for loops instead. 

















