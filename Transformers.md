# Transformers

## Language Models
Chatgpt, powered by a model called GPT is based on a deep learning architecture called Transformers. Transformers have sparked a major boom in modern AI because of their capability to understand and generate human-like text. 

## What is a Language Model?
Language models are machine learning models designed to predict the next word in a sentence, given a sequence of previous words. Examples: Gmail's auto-complete, Google's BERT (Bidrectional Encoder Representations from Transformers), and OpenAI's GPT (Generative Pretrained Transformer). GPT is a large language model due to its billions of parameters and massive training dataset, making it more powerful than models like BERT. Fundamentally, GPT and similar models operate by predicting one word at a time, iterating until a complete and coherent answer or sentence is produced. This next-word prediction ability is at the core of language models.

## Understanding Word Embeddings

Machine learning models don’t understand text directly; they understand numbers (vectors).
Words can be represented numerically using word embeddings, vectors that encode semantic meaning.
Example: “King” represented as a vector with features that correspond to concepts like authority, gender, richness.
Embeddings capture relationships: King - Man + Woman ≈ Queen.
Real embeddings have hundreds (e.g., 300 in Google’s Word2Vec) or thousands (e.g., 12,000 in GPT) of dimensions.
Meaningful relationships exist in vector space, such as gender or country-capital vectors.

## Static VS Contextual Embeddings

Static embeddings: One fixed vector per word regardless of context (e.g., Word2Vec, GloVe).
Static embeddings can’t differentiate word meanings in different contexts (e.g., “track” as a railway vs. “track” as to follow).
Contextual embeddings: Word vectors change based on sentence context.
Example of contextual embedding: The word “dish” changes meaning in “rice dish” vs. “cheese dish.”
Contextual embeddings improve next-word prediction by adjusting based on nearby words and sentence context.