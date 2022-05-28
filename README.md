
# Movie Recommender

![Python](https://img.shields.io/badge/Python-3.9.7-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

Content based recommender system which recommends movies similar to the input movie based on cosine similarity distance for scoring movies and sorting the most closesly related ones while also considering the three different types of recommendations (overall , genre based and cast based).

Check out the live demo: [movie-recommender](https://movie-recommender0291.herokuapp.com/)

## Basic working of the system

 ![image](static\Flowchart.png)

### a.) Data Preprocessing

I imported raw data of American movies from 2015 - 2021, preprocessed them separately, and then merged them back to obtain a dataset with utilitarian information such as title, cast details and genres.

### b.) Sorting movies based on similarity scores

I count vectorized the above mentioned obtained data and then extracted a sparse matrix from the same using the cosine similarity score. This was then used to rank the movies on the basis of similarity in a descending order and the top 10 movies were selected to complete the k nearest implementation for the recommendation purpose.

### c.) TMDB API calls

API requests are then made to TMDB to extract relevant features for the recommended movies like title, genre, runtime, rating, poster, etc. which are passed on to the front end and displayed under the banner of "Movies Recommended For You".

## How to get the API key?

Create an account in <https://www.themoviedb.org/>, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?

1. Clone this repository in your local system.
2. Install all the libraries mentioned in the [requirements.txt](https://github.com/lunaticAJ/Movie_Recommender/blob/main/requirements.txt) file.
3. Replace YOUR_API_KEY in the `main.py` file.
4. Open the command prompt from your project directory and run the command `python main.py`.
5. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
6. Hurray! That's it.

### Sources of the datasets

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
6. [List of movies in 2021](https://en.wikipedia.org/wiki/List_of_American_films_of_2021)
