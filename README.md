##Program 1:
# POS Tagging Program

This Python program performs Part-of-Speech (POS) tagging on a given sentence using the Natural Language Toolkit (NLTK).

## Overview

The program tokenizes an input sentence into words and punctuation and then tags each token with its part of speech. It uses NLTK's `word_tokenize` for tokenization and `pos_tag` for POS tagging.

## Prerequisites

To run this program, you need Python and the NLTK library installed. You can install NLTK using pip if you haven't already:

```bash
pip install nltk

## code explaination:

1) Imports and Downloads:

Imports necessary functions from NLTK.
Downloads required NLTK resources (punkt and averaged_perceptron_tagger).

2)Functions:

 pos_tagging(sentence):

 Takes a sentence as input, tokenizes it, and returns POS-tagged tokens.

 print_pos_tags(tagged):
 Prints each word and its corresponding POS tag.

3) Main Execution:

Defines an example sentence.
Calls pos_tagging to get the POS tags.
Prints the tagged tokens using print_pos_tags.

## Example

For the example sentence "Im student of Artificial Inteligence", the output will be:

Im: VB
student: NN
of: IN
Artificial: JJ
Inteligence: NN.


## Program 2:

# Simple Chatbot Program

This Python program demonstrates a basic chatbot that can respond to predefined patterns and questions. It uses the Natural Language Toolkit (NLTK) library to handle pattern matching and responses.

## Overview

The chatbot is designed to respond to a few specific questions and patterns. It uses the `nltk.chat.util.Chat` class to match user input with predefined responses.

## Prerequisites

To run this program, you need Python and the NLTK library installed. You can install NLTK using pip if you haven't already:

```bash
pip install nltk


Code Explanation:

Imports and Definitions:

Imports necessary modules from NLTK.
Defines pairs, a list of tuples where each tuple contains a pattern and a list of responses.

Chatbot Function:

chatbot(): Creates a Chat instance with the defined patterns and responses.
Starts a loop where it takes user input, responds using the chatbot, and ends if the user types 'Quit', 'Bye', or 'Exit'.
Main Execution:

Calls the chatbot() function if the script is run as the main module.

Example Interaction:

Hello! I am your chatbot. Type 'Quit', 'Bye', or 'Exit' to end the conversation.
Enter your Question : Hi
Chatbot: Hello! How can I assist you today?
Enter your Question : What can you do?
Chatbot: I can answer a few predefined questions. Try asking me something!
Enter your Question : Quit
Chatbot: Goodbye! Have a nice day!


