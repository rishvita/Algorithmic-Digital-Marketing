### CLAAT Document: https://codelabs-preview.appspot.com/?file_id=15TzOvW4CdU35qpk2XLzej47dlCY8Ha-T-Qovonv99fY#0

### Heroku App: https://searchheroku.herokuapp.com/

# Search 
In this assignment, we are trying to implement visual search based on the input image we have given. We also tried to create app using Streamlit/ Flask 

Data: We are using Cdiscount's Image Classification Challenge dataset from Kaggle. It consists of bson files

## Process
## 1. Ingestion and Pre-Processing:
We have decoded the bson file using bson package and worked on creating key value pairs for the image pairs for our purpose
Sampled the data fro 100 products each in 100 categories, and appending these images to the images file in local

## 2. Search Algorithms
We have applied three different Search algorithms 

### 1. Image Search By an Artistic Style
Here we used the Brute method for similarity search, using the cosine similarity concept

The vectors/embeddings having closer cosine distance are more similar to each other

The algorithm has used convolution neural network and VGG to extract granular pattern/data from the images for further cosine distance analysis, i.e similarity search

### 2.FAISS (Facebook AI Similarity Search)
FAISS (Facebook AI Similarity Search) is a library that allows developers to quickly search for embeddings of multimedia documents that are similar to each other

With FAISS, developers can search multimedia documents in ways that are inefficient or impossible with standard database engines (SQL). It includes nearest-neighbor search implementations for million-to-billion-scale datasets that optimize the memory-speed-accuracy tradeoff. FAISS aims to offer state-of-the-art performance for all operating points.

### 3.Spotify-Annoy Method
Annoy(Approximate Nearest Neighbor Oh Yeah), is an open-sourced library for approximate nearest neighbor implementation

An image feature vector is a list of numbers that represents a whole image, typically used for image similarity calculations or image classification tasks.

We use this Spotify/annoy library and image feature vectors to calculate the image similarity scores which helps us determine the similar images

We store the output in a json file which consists information about the similarity scores and the product information

## 3.ElasticSearch:
Elasticsearch is a highly scalable open-source full-text search and analytics engine. It allows you to store, search, and analyze big volumes of data quickly and in near real time.

We used the output json file of the Spotify-Annoy Method

We indexed the json file using POST with the name "series". We used bulk API to index the data

## 4. Application
Heroku App: https://searchheroku.herokuapp.com/ 




