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


