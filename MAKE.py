APIKey = "05ff55684cb55f443d41d5558c15d6bb"

import json, requests, pprint as pr, time, pandas as pd, numpy as np

genre = 'Comedy Thriller Drama Musical Horror Documentary Sci-fi Adventure Crime Animation Romance'.split()

def get_API():
    print('Please get your API key from https://developers.themoviedb.org/3/getting-started/introduction')
    print('Please enter your API key from TMDB: ', end = '')
    API = input()
    return API


def get_MovieList():
# This function will ask recent movies/TV shows users watched and liked.
# Users will provide title of the movies/TV shows, and provide rating to them.

    print('> To recommend you movies, I need to know list of films and TV shows you recently enjoyed!')
    #time.sleep(1)
    print('> More films you tell me, the better recommendation is going to be.''')
    #time.sleep(1)
    print('> How many favorite films do you want to tell me:' ,end='')
    numberofObjects = input()
    numberofObjects = int(numberofObjects)

    # Taking keywords user want to look for
    print('> Please enter the title of your favorite film one by one!')
    user_response = []
    for i in range(numberofObjects):
        print('Name of the film (with spaces between words): ', end='')
        user_response.append(input().lower())
        print('> Movies you\'re searching for: %s' % user_response)

    return user_response

def get_MovieRating(movie_list):
    print('Now, can you please give rating for the movies you mentioned?')
    user_rating = []
    for i in range(len(movie_list)):
        print('What is your rating for the film %s: ' %(movie_list[i]), end = '')
        user_rating.append(input())
    print(user_rating)





def test(API):
    url = 'https://api.themoviedb.org/3/movie/550?api_key=' + str(API)
    response = requests.get(url)
    response.raise_for_status()
    jsonData = json.loads(response.text)
    pr.pprint(jsonData)


    language = jsonData['original_language']
    title = jsonData['original_title']
    plot = jsonData['overview']
    rating = jsonData['vote_average']

    pr.pprint(plot)
    print(type(plot))


movie_list = get_MovieList()
user_rating = get_MovieRating(movie_list)
API = get_API()
test(API)

# Create_Matrix() <- We need a function to combine name of the films and the ratings into one matrix
