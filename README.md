# Politify

### A tool to determine the political bias among public figures by analyzing their tweets is a truly unbiased way!

Made by: Ashish D'Souza and Sharath Palathingal

### 
Politify is a simple to use service which prevents human bias from determining how skewed tweets are from public figures.
Many public figures have seemingly harmless tweets scrutanized by "mainstream" media hoping to draw attention to their programming.
The root of division is often forces out of the individual's power.
In the hope of delivering power to the people, we created a complex ML algorithm that analyzes a public figure's tweets and determines on net how biased they are with relation to other public figures.
We do this comparision to provide the user context and hence advise them to take "information" provided by these tweets with a pinch of salt.
Now how big should this pinch be?
Glad you asked!
Our Ml system also assigns a Bias score to each public figure which helps users easily identify how skewed their tweets tend to be.

### What we used to implement Politify:

* **ReactJS** for UI/UX
* **Flask** as our back-end application framework
* **PostgreSQL** for database storage
* **Google Cloud**
  * **Natural Language API** for performing sentiment analysis on tweets
  * Also used for preprocessing the tweet datasets with text classification (unsupervised learning) to eliminate extra noise
* **Selenium** for web scraping JavaScript-rendered tweets
* **BeautifulSoup** for other normal webscraping
* **Pandas** for preprocessing datasets
* **Transformers** for implementing the Bidirectional Encoder Representations from Transformers (**BERT**) natural language processing networks
* **PyTorch** for training and testing the machine learning models
* **Nvidia CUDA** for GPU-accelerated computations to faster optimize the machine learning models, running on an Nvidia RTX 2070 Super graphics card


### How It Works:

1. A user submits a public figure's Twitter handle through the UI
2. The back-end Flask framework receives the username and uses Selenium to parse through the account's Tweets until a specified threshold is reached (usually around 200).
3. The trained BERT Natural Language Processing model is loaded into PyTorch and used to classify each Tweet on a political spectrum.
4. The Google Cloud Natural Language Processing API is then used to perform sentiment analysis on each Tweet when political keywords (aka "hot topics") are discovered in the Tweet
5. Ranking and bias scores are then used to determine the overall placement on the political spectrum for each Twitter user.
6. After the asynchronous prediction is completed (via multithreading), the data is then stored in the PostgreSQL database
7. When the political spectrum page is indexed, the updated list of politicians/public figures are displayed on the political spectrum.
8. An additional feature exists to test our machine learning algorithms on any Tweet (where a user can enter a sample Tweet and see whether it is classified to the left or right of the political spectrum)
