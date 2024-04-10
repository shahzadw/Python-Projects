import spacy
nlp = spacy.load('en_core_web_md')

word1= nlp("cat")
word2= nlp("monkey")
word3= nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word2))


# example from lecture notes using for loops

tokens= nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# example from lecture notes using for loops to get similarity between sentences

sentence_to_compare = "why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car"
"I/'ve lost my car in my car"
"I/'d like my boat back"
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence)
    print(similarity)

#observations Practical Task 1
#I have picked a few examples from the output to explain the question, Il call semantic similarity as SS
#cat and cat have SS of 1 as both animal and the same animal
#cat and apple have very little SS as one is animal and other is fruits. Cats are carnivors 
#monkey and banana have 0.4 SS becuse monkies eat bananas
#banana and apple have 0.66 SS as both are fruits