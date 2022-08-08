# pan-da
This is a movie api, created with django and python webscrapping. It contains two major end points,

SEARCH
The search endpoint /api/search/<search term>
note the angle brackets are not needed in the actual endpoint it is for emphasis
in the search endpoint you enter a movie name and it returns a list of movies or series that are closesly related to the search term
within the response is an identifier which is needed to download that particular movie.

GET
The get endpoint /api/get/<identifier>
note the angle brackets are not needed in the actual endpoint it is for emphasis
in the get endpoint you enter a identifier gotten from the response of the search endpoint(identifier specify the specific movie you wish to download)
it returns the download link for the movie. 
