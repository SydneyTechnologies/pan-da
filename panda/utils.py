import re

def GetMovieInfo(MovieDetails):
    result = {}
    rspec = r'[0-9]+p.*'
    rtitle = r'.*?[0-9]\s'
    movie_details = re.search(rspec, MovieDetails).group()
    title = re.search(rtitle, MovieDetails).group()
    return [title, movie_details]