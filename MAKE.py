import json, requests, pprint as pr, time, pandas as pd, numpy as np

APIKey = "05ff55684cb55f443d41d5558c15d6bb"

def get_API():
    print('Please get your API key from https://developers.themoviedb.org/3/getting-started/introduction')
    print('Please enter your API key from TMDB: ', end='')
    API = input()
    return API


def get_MovieList(API):
    # This function will ask recent movies/TV shows users watched and liked.
    # Users will provide title of the movies/TV shows, and provide rating to them.

    print('> To recommend you movies, I need to know list of films and TV shows you recently enjoyed!')
    # time.sleep(1)
    print('> More films you tell me, the better recommendation is going to be.''')
    # time.sleep(1)
    print('> How many favorite films do you want to tell me: ', end='')
    while True:
        try:
            numberofObjects = input()
            numberofObjects = int(numberofObjects)
        except ValueError:
            print('Please enter number.')
            continue
        else:
            break

    # Taking keywords user want to look for
    print('> Please enter the title of your favorite film one by one!')
    user_movieList = []
    user_movieID = []
    for i in range(numberofObjects):
        print('Name of the film (with spaces between words): ', end='')
        title_search = input()
        url = 'https://api.themoviedb.org/3/search/movie?api_key=%s&language=en-US&query=%s&page=1&include_adult=true' % (
        API, title_search)
        response = requests.get(url)
        response.raise_for_status()
        jsonData = json.loads(response.text)
        if jsonData['total_results'] > 1:
            print("There are multiple films that matches your search which is the one...")
            title = []
            release_date = []
            overview = []  # plot
            movie_ID = []  # Unique number for a film

            for t in jsonData['results']:
                title.append(t['title'])
                try:
                    release_date.append(str(t['release_date']))
                except:
                    release_date.append('NA')
                overview.append(t['overview'])
                try:
                    movie_ID.append(t['id'])
                except:
                    movie_ID.append('NA')

            userDF = pd.DataFrame({'title': title,
                                   'release_date': release_date, 'movie_ID': movie_ID})
            pd.set_option("display.max_rows", None, "display.max_columns", None)

            # Verify_list is a Dataframe that contains the title and the release date of films that users selected
            verify_list = pd.DataFrame({'title': title,
                                        'release_date': release_date})
            # 'overview': overview})
            print(verify_list)
            print('Please enter the ID number of a film you\'re looking for: ', end='')

            idNumber = int(input())
            title_df = userDF.get('title')
            id_df = userDF.get('movie_ID')
            user_movieList.append(title_df[idNumber])
            user_movieID.append(id_df[idNumber])

            # Creating a DataFrame that contains the titles and IDs for films
            user_response = pd.DataFrame({'Title': user_movieList, 'Movie ID': user_movieID})

        print('> Movies you\'re searching for: %s' % user_movieList)
    print(user_response)

    return user_response


def get_MovieRating(movie_DF):
    print('Now, please give rating for the movies you mentioned with digits between 1 to 10 (1-bad, 10-great)')
    user_rating = []
    movie_titles = movie_DF.get('Title')

    for i in range(len(movie_titles)):
        print('What is your rating for the film %s: ' % (movie_titles[i]), end='')
        user_rating.append(input())
    rating_DF = pd.DataFrame({'User Rating': user_rating})
    DF = pd.concat([movie_DF, rating_DF], axis=1)

    return DF


def get_recommendation(API, userDF):
    ID_series = userDF.get('Movie ID')
    rating_series = userDF.get('User Rating')
    recommended_titles = []
    release_dates = []
    vote_average = []
    weighted_rating = []

    for i in range(len(ID_series)):
        url = 'https://api.themoviedb.org/3/movie/%s/recommendations?api_key=%s&language=en-US&page=1' %(ID_series[i],API)
        response = requests.get(url)
        response.raise_for_status()
        jsonData = json.loads(response.text)

        for t in jsonData['results']:
            recommended_titles.append(t['original_title'])
            release_dates.append(t['release_date'])
            vote_average.append(t['vote_average'])
            weighted_rating.append((float(t['vote_average'])+float(rating_series[i]))/2)

        recommended_DF = pd.DataFrame({'Title': recommended_titles,
                                       'Release date': release_dates,
                                       'Vote average': vote_average,
                                       'weighted rating': weighted_rating})

    return recommended_DF


def eliminate(DF, rating_DF):
    newdata = DF.drop(DF[int(rating_DF) < 6]).ind
    print (newdata)

    return newdata



def get_averageRating(userDF):
    rating = userDF.get('User Rating')
    total_rating = 0

    for i in range(len(rating)):
        total_rating += float(rating[i])
    rating_average = total_rating / len(rating)

    return rating_average


API = get_API()
movie_DF = get_MovieList(API)
userDF = get_MovieRating(movie_DF)
rating_average = get_averageRating(userDF) # Determine pass/fail line
print(rating_average)
r_DF = get_recommendation(API, userDF)
print(r_DF)
