import numpy as np
import pandas as pd
from flask import Flask, render_template, request, json
import requests

from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = 'YOUR_API_KEY'

from tmdbv3api import Movie

data = pd.read_csv("dataset and scores\main_data.csv")
score_overall = pd.read_csv("dataset and scores\score_overall.csv")
score_genre = pd.read_csv("dataset and scores\score_genre.csv")
score_cast = pd.read_csv("dataset and scores\score_cast.csv")


def k_nearest(m,n):

    if m not in np.array(data['movie_title']):

        return('string')

    elif (n == 1):

        row = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(np.array(score_overall.iloc[row])))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[:22]
        l = []
        for i in range(22):
            a = lst[i][0]
            if ((data['movie_title'][a]) == m):
                continue
            l.append(data['movie_title'][a])
        return l[:20]

    elif (n == 2):

        row = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(np.array(score_genre.iloc[row])))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[:22]
        l = []
        for i in range(22):
            a = lst[i][0]
            if ((data['movie_title'][a]) == m):
                continue
            l.append(data['movie_title'][a])
        return l[:20]

    elif (n == 3):

        row = data.loc[data['movie_title']==m].index[0]
        lst = list(enumerate(np.array(score_cast.iloc[row])))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[:22]
        l = []
        for i in range(22):
            a = lst[i][0]
            if ((data['movie_title'][a]) == m):
                continue
            l.append(data['movie_title'][a])
        return l[:20]

def ListOfGenres(genre_json):
    if genre_json:
        genres = []
        genre_str = ", " 
        for i in range(0,len(genre_json)):
            genres.append(genre_json[i]['name'])
        return genre_str.join(genres)

def date_convert(s):

    MONTHS = ['January', 'February', 'Match', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    y = s[:4]
    m = int(s[5:-3])
    d = s[8:]

    result = d + ' ' + MONTHS[m-1] + ' '  + y
    return result

def MinsToHours(duration):

    if duration%60==0:
        return "{:.0f} hours".format(duration/60)

    else:
        return "{:.0f} hours {} minutes".format(duration/60,duration%60)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    classifier = request.args.get('classifier')
    r = k_nearest(movie.lower(),int(classifier))
    movie = movie.upper()

    if type(r)==type('string'):

        return render_template('recommend.html',movie=movie,r=r,t='s')

    else:

        tmdb_movie = Movie()
        result = tmdb_movie.search(movie)
        movie_id = result[0].id
        
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
        data_json = response.json()
        poster = data_json['poster_path']
        img_path = 'https://image.tmdb.org/t/p/original{}'.format(poster)

        genre = ListOfGenres(data_json['genres'])
        
        rd = date_convert(result[0].release_date)

        status = data_json['status']

        runtime = MinsToHours(data_json['runtime'])

        poster = []
        movie_title_list = []
        for movie_title in r:
            list_result = tmdb_movie.search(movie_title)
            if (list_result == []):
                continue
            movie_title_list.append(movie_title)
            movie_id = list_result[0].id
            response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
            data_json = response.json()
            poster.append('https://image.tmdb.org/t/p/original{}'.format(data_json['poster_path']))
            if (len(movie_title_list) == 10):
                break

        movie_cards = {poster[i]: movie_title_list[i] for i in range(len(movie_title_list))}
        
        return render_template('recommend.html',movie=movie,mtitle=movie_title_list,t='l',cards=movie_cards,
            result=result[0],img_path=img_path,genres=genre,
            release_date=rd,status=status,runtime=runtime,classifier=classifier)

if __name__ == '__main__':
    app.run(debug=True)
