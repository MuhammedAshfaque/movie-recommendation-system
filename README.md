The Movie Recommendation System is an interactive, content-based recommendation web application designed to help users discover new films based on their current favorites. Instead of suggesting popular or trending items globally, this system provides personalized recommendations by analyzing the metadata of movies.

How it Works
The application leverages Natural Language Processing (NLP) to inspect the descriptive attributes of each film—including its genres, plot summary (overview), cast, director, and keywords.

Text Normalization: Using the Natural Language Toolkit (NLTK), the text is cleaned and words are stemmed to their base forms (e.g., "actor", "acting" → "act") to improve accuracy.
Vector Space Representation: The combined metadata tags are converted into numerical vectors using Scikit-Learn’s CountVectorizer (Bag of Words).
Similarity Calculation: The system computes the Cosine Similarity between the target movie's vector and all other vectors in the TMDB 5,000 dataset to locate the 5 closest matches.
