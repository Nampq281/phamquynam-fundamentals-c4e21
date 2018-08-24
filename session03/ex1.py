fav_movie = ["shawshank", "breakingbad", "gameofthrone"]
fav_size = len(fav_movie)

print(fav_movie[0])
print(fav_movie[1])
print(fav_movie[2])

new_movie = input("new favorite movie? ")
fav_movie.append(new_movie)
print(*fav_movie, sep = ", ")

