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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

