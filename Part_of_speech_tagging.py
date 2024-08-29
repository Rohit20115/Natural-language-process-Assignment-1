import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Ensure that necessary resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Perform POS tagging
    tagged = pos_tag(tokens)
    
    return tagged

def print_pos_tags(tagged):
    for word, tag in tagged:
        print(f'{word}: {tag}')

if __name__ == "__main__":
    # Example sentence
    sentence = "Im student of Artificial Inteligence"
    
    # Get POS tags
    tagged = pos_tagging(sentence)
    
    # Print the sentence with its POS tags
    print_pos_tags(tagged)
