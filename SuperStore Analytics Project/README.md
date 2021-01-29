# SuperStore
The explosive growth of online content and services has provided a myriad of choices for users. Therefore, personalized recommendations are necessary to improve user experience and ensure retention.\
The corollary of pleasant and convenient user experience is augmented profits for businesses. Before curating a set of products for different users, it is imperative to understand them better. Every customer is unique. Hence, if you treat them the same way with the same content, same channel, same importance, they will find another option which understands them better.\
We segment the users based on RFM Modelling and create personalised Recommender System models based on Collaborative filtering.\
In order to tackle the cold-start problem i.e. when new user opens the app we recommend popular items\n
Users can search for products and with product similarity search we display similar products to product that user searched for 

# Project Proposal
CLAAT: https://codelabs-preview.appspot.com/?file_id=1v93fwAPwqChS22TUFjwjyT-RNtvWgNpaRr53NvFMF3U#0

# Report
CLAAT: https://codelabs-preview.appspot.com/?file_id=1Sw4fG-F6BLDCx5oMwuYoyhWEHMqgGy9IXSjnGi7SklY#0

# Application URL
Heroku: https://superstoreapp.herokuapp.com/

# Dashboard
   https://datastudio.google.com/u/0/reporting/8fe1e49e-78be-4b1b-b2b5-94ad5d9db854/page/UIhtB \
   https://datastudio.google.com/u/0/reporting/8fe1e49e-78be-4b1b-b2b5-94ad5d9db854/page/ypstB

![image](https://user-images.githubusercontent.com/73679593/102679947-f318af80-4181-11eb-9f7d-2f4f5cea63e4.png)
![image](https://user-images.githubusercontent.com/73679593/102679964-26f3d500-4182-11eb-98fb-7a2608d01120.png)

# Approach
1. We performed EDA and analyzed customer behavior trends to better understand our customer's data 
2. We segmented the customers using RFM Modelling based on their purchasing history. Also, calculated the CLV to understand the importance of each customer.
3. We provided personalised recommendations to users by predicting their ratings based on collaborative filtering
4. We excecuted 4 collaborative models and compared its evaluation metrics to chose the model most ideal model for our prediction
5. For new users we recommend products based on popularity
6. The users have an option to search for products and get a list of products similar to their search
7. We created an interactive dashboard to analyze the sales based on customer segments.

# Customer Segmentation
1. We cannot treat every customer with the same importance.They will find another option which understands them better.
2. Each customer has a different profile and we need to tailor our recommendations based on their profiles. 
3. In order to better understand our customers we segment our customers based on their RFM values.
4. By using the RFM score we segment our customers into Top,Lost and Regular customers

# Recommendation
1. A recommender system predicts the rating value of a user-item combination with an assumption that the training data available indicates a user’s preference for other items.
2. We use the user-item Interaction Data, such as ratings and apply various modelling techniques that uses collaborative filtering to predict user’s preference.
3. We executed 4 collaborative modelling techniques :
   1. FastAI    
   2. Alternating Least Square (ALS)  
   3. Simple Algorithm for Recommendation (SAR)  
   4. Surprise Singular Value Decomposition (SVD)
4. We compared the evaluation metrics and chose SVD as most ideal for our dataset 
5. Based on the predicted ratings we recommended top-k items to a particular user.
6. For new users as we do not have their preferences we recommend most popular products.
7. We check for products which are most purchased and are highly rated to recommend those for new users


# Search 
1. Users can find the products they are looking for using the Search feature
2. The search feature also lists the products similar to the items being searched
3. We used text processing to find similar products.
4. We created a Document Term Matrix using TF-IDF to extract vectors
5. Using cosine similarity we calculated proximity between strings
6. Based on similarity values we created product groups
  

# Application Navigation
### 1. Welcome Page
Superstore home page

### 2. Login 
When a user login using their credentials, personalised recommendations are provided 

### 3. Search
When a customer searches a product,the app displays the product searched and also the similar products to the search

### 4. New Customer
When a new customer opens the app,product recommendations are provided based on popularity

#### Test Cases
##### Login
1. User Name(Top): 25, 33, 43, 46, 49, 58, 62, 65, 74, 80
2. User Name(Regular): 200, 202, 204, 206, 207, 210, 211, 212, 213, 215
3. User Name(Lost): 100, 104, 108, 109, 121, 128, 135, 139, 141, 144
4. Password: SuperStore

##### 2. Search
Product Name:
1. Tenex Lockers, Blue
2. Memorex Memory Card, USB
3. Fellowes File Cart, Industrial
4. Konica Printer, White
5. Stanley Canvas, Blue





