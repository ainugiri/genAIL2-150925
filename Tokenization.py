import nltk

#  nltk - natural language toolkit
#  function defined in nltk
#  helpful for text processing
#  tokenization, removing stop words, stemming, lemmatization, pos tagging, ner etc.


from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
# stop_words : is, the, a, in, of, and, to, etc, from, to be, that, it, on, for, as, with, by, at, this, an, or
user = input("Enter your text: ")
user_tokens = word_tokenize(user)
print("Word Tokens:", user_tokens)

after_rm_stopwords = [word for word in user_tokens if word.lower() not in stopwords.words('english')]
print("After removing stop words:", after_rm_stopwords)

# intent extraction process: 
# Here you can implement your intent extraction logic using the processed tokens

ps = PorterStemmer()
lm = WordNetLemmatizer()


print(ps.stem("writing"))  # run
print(lm.lemmatize("running", pos='v'))  # run

# pos tagging
nltk.download('averaged_perceptron_tagger')
words = word_tokenize("The quick brown fox jumps over the lazy dog")
pos_tags = nltk.pos_tag(words)
print(pos_tags)


# text processing in python - NLTK NlTK - Natural Language Toolkit

# NER - identifies city, organization, person name, date, time, money etc.
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk
import random
# ner 
word = word_tokenize("Microsoft is looking at buying U.K. startup for $1 billion")
pos_tags = nltk.pos_tag(word)
ner1 = ne_chunk(pos_tags)
print(ner1)

# NLP - NLU - Natural Language Processing - Natural Language Understanding
# take input from user
# identifying the intent by using NER, POS tagging, tokenization, removing stop words, stemming, lemmatization etc.
# intent - book a flight, book a hotel, order food, play music, set an alarm, etc.
# entity - location, date, time, number of people, cuisine, song name, alarm time etc.
# action - book a flight, book a hotel, order food, play music, set an alarm etc.


# information pass to model -> model process the data -> result 
# ticket booked
# order placed
# music played
# alarm set

#  nl as input -> nlp -> process the data -> system -> process instruction -> result


# Salesdata  of last 3 years (Raw data -> date, billno, pno, qty, price, loss/gain)
# system have ability to identify the pattern/trend in the data
#  generate report - monthly, quarterly, yearly
#  NLG - Natural Language Generation
#  generate text report - summary of sales, top selling products, low selling products, profit

#  DL - Neural Network - BigData
#  train the model - large corpus of data
#  predict

#  LLM - is deep learning model, which uses NLP techniques to understand the context of the text and generate human like text

# Specific domain - language - train a model with large corpus of data of language processing  - LLM



# LLM - Large Language Model
# categories 
# 1. Text generation - GPT
# 2. Summarization - BERT 
#      without loosing intent / meaning of the text, shorter version of the text

# Pattern
#  GPT: Create a story
#  follow structure - beginning, middle, end
#  Who, What, When, Where, Why, How
#  Cat and Rat -> whisker and squeak

# summarization
# image generation: prompt -> image - diffusion model: 
# i want to create a image cat sitting on the moon 
# diffusion model - DALL.E, Stable Diffusion, MidJourney etc.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def generate_random_prime(start=2, end=1000):
    primes = [x for x in range(start, end+1) if is_prime(x)]
    if not primes:
        return None
    return random.choice(primes)

# Example usage:
print("Random Prime Number:", generate_random_prime(100, 500))

# t5 text to text transfer transformer
# language translation
