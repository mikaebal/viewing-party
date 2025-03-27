# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title, 
            "genre": genre, 
            "rating": rating
            }
    return None

def add_to_watched(user_data, movie):
    if "watched" in user_data:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = [movie]

    return user_data

def add_to_watchlist(user_data, movie):
    if "watchlist" in user_data:
        user_data["watchlist"].append(movie)

    else:
        user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break  # Stop looping after finding and moving the movie
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if not user_data["watched"]:
        return 0.0

    total_rating = 0
    count = 0

    # loop through watched movies
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
        count += 1
        # calculate average rating
        average_rating = total_rating / count

    return average_rating

def get_most_watched_genre(user_data):

    if not user_data["watched"]:
        return None

    genre_count = {}

    # count how many times each genre appears
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

    # find the most watched genre
    most_watched_genre = None
    highest_count = 0

    for genre, count in genre_count.items():
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # Get the list of movies the user watched
    user_watched = user_data["watched"]
    
    # Get movies watched by friends
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)  

    # Find movies the user watched but none of friends watched
    user_unique_watched = []
    for movie in user_watched:
        if movie not in friends_watched: 
            user_unique_watched.append(movie)

    return user_unique_watched
    
def get_friends_unique_watched(user_data):
    # Get the list of movies the user watched
    user_watched = user_data["watched"]
    
    # Get movies watched by friends
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)  

    # Find movies the user watched but none of friends watched
    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in user_watched and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    user_watched_titles = []
    unique_recommendations = []

    # store titles of movies user has watched
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])

    # check each friend's watched list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # make sure user hasn't watched it and it's on a subscribed service
            if (
                movie["title"] not in user_watched_titles
                and movie["host"] in user_data["subscriptions"]
                and movie["title"] not in unique_recommendations  # avoid duplicates
            ):
                recommended_movies.append(movie)
                unique_recommendations.append(movie["title"])  # track added movies

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # Step 1: Count genres
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

    # Step 2: Find the most watched genre    
    most_watched_genre = None
    highest_count = 0
    
    for genre, count in genre_count.items():
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre

    # Step 3: Find recommended movies
    user_watched_titles = []
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])

    friend_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_watched_movies:  # Avoid duplicates
                friend_watched_movies.append(movie)

    recommended_movies = []
    for movie in friend_watched_movies:
        if (movie["title"] not in user_watched_titles 
                and movie["genre"] == most_watched_genre):  
            recommended_movies.append(movie)

    return recommended_movies

# wave 5.2 

def get_rec_from_favorites(user_data):

    recommended_movies = []
    
    for movie in user_data["favorites"]:
        movie_watched_by_friend = False

        for friend in user_data["friends"]:
            for watched_movie in friend["watched"]:
                    if movie["title"] == watched_movie["title"]:
                        movie_watched_by_friend = True
                        break
                        
            if not movie_watched_by_friend:
                    recommended_movies.append(movie)

    return recommended_movies