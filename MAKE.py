import pandas as pd

print('Please enter your preferences with digits between 0 to 10.')

comedy = input('Comedy ')
action = input('Action ')
thriller = input('Thriller ')
romance = input('Romance ')
scifi = input('Sci-fi ')
reality = input('Reality ')
documentary = input('Documentary ')
kids = input('Kids ')
animation = input('Animation ')
horror = input('Horror ')
drama = input('Drama ')

genres = pd.Series({'Comedy': comedy,
                    'Action': action,
                    'Thriller': thriller,
                    'Romance': romance,
                    'Sci-fi': scifi,
                    'Reality': reality,
                    'Documentary': documentary,
                    'Kids': kids,
                    'Animation': animation,
                    'Horror': horror,
                    'Drama': drama})

print(genres.head(11))
