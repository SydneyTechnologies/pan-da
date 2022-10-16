import re
import random
import string

def GetMovieInfo(MovieDetails):
    # Gets the movie details be running pattern matches with regex
    rspec = r'[0-9]+p.*'
    rtitle = r'.*?[0-9]\s'
    print("These are the movie details:", MovieDetails)
    movie_details = re.search(rspec, MovieDetails).group() if re.search(rspec, MovieDetails) is not None else MovieDetails
    title = re.search(rtitle, MovieDetails).group() if re.search(rtitle, MovieDetails) is not None else MovieDetails
    return [title, movie_details]

def GetDescription(description):
    rdescript = r"[A-Z].*"

    result = re.findall(rdescript, description, re.MULTILINE)
    if result:
        result = result[len(result)-1]
        return result
    else:
        return description



SAFELOCK = "https://b1.safelock.pw:183/d/"

def generateHash():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase  
    numbers = "".join(str(i) for i in list(range(0, 10)))
    final_list = lowercase + uppercase + numbers
    hash = [ random.choice(final_list) for sel in range(7)]
    print("".join(hash))

