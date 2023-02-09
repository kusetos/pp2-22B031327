movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# 1
def above(movies, name):
    for x in movies:
        if x["name"] == name:
            return x["imdb"] > 5.5
print(above(movies, "Dark Knight"))

# 2
def goodMovies(movies):
    MovieList = []
    for x in movies:
        if x["imdb"] > 5.5:
            MovieList.append(x["name"])
    print(*MovieList, sep=", ", end='. \n')
goodMovies(movies)

# 3
def category(movies, typ):
    MovieList = []
    for x in movies:
        if x["category"] == typ:
            MovieList.append(x["name"])
    print(*MovieList, sep=", ", end='.\n')
category(movies, "Romance")

# 4
def avarageScore(movies):
    sum = 0
    for x in movies:
        sum += x["imdb"]
    return sum/len(movies)
print(avarageScore(movies))

# 5
def imdbCategory(movies, cat):
    sum = 0
    i = 0
    MovieList = []
    for x in movies:
        if x["category"] == cat:
            #MovieList.append(x["name"])
            sum += x["imdb"]
            i += 1
    return sum / i
print(imdbCategory(movies, "Romance"))
