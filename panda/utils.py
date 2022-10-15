import re

def GetMovieInfo(MovieDetails):
    rspec = r'[0-9]+p.*'
    rtitle = r'.*?[0-9]\s'
    movie_details = re.search(rspec, MovieDetails).group()
    title = re.search(rtitle, MovieDetails).group()
    return [title, movie_details]

def GetDescription(description):
    rdescript = r"[A-Z].*"

    result = re.findall(rdescript, description, re.MULTILINE)
    if result:
        result = result[len(result)-1]
        return result
    else:
        return description
