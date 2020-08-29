import requests

# Here we define our query as a multi-line string
query = '''
query ($page: Int, $perPage: Int, $search: String, $averageScore: Int, $genre: String, $seasonYear: Int, $season: MediaSeason) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
        media (search: $search, averageScore: $averageScore, genre: $genre, seasonYear: $seasonYear, season: $season) {
            
            title {
                romaji
                english
            }
            averageScore
            genres
            seasonYear
            season
        }
    }
}
'''
variables = {
    'search': str(input('Please enter an anime: ')),
    'page': 1,
    'perPage': int(input('How many results would you like to see? (Only Page 1): '))
}
url = 'https://graphql.anilist.co'

try:
    response = requests.post(url, json={'query': query, 'variables': variables})
except:
    response = None
    print("An Error has occured.")
    quit()

print('Here are some results: ' + '\n' + 
'Page Information:', response.json()['data']['Page']['pageInfo'], '\n' + 
'Animes Found: \n')

for anime in response.json()['data']['Page']['media']:
    print('Title:', anime['title'], '\n' +
    'Average Score:', anime['averageScore'], '\n' +
    'Genres:', anime['genres'], '\n' +
    'Year:', anime['seasonYear'], '\n' +
    'Season:', anime['season'], '\n' +
    '------------------------------------------------------------------------------------'
    )

