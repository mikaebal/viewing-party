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

