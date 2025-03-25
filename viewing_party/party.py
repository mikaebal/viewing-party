# ------------- WAVE 1 --------------------
# Testing push - pull
# initial comment 

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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

