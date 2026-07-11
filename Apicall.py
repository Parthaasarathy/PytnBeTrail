import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
#print(response.json())

pretty = response.json()
for result in pretty["results"]:
    print(result['artistName'])

"""first print response: 
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python Apicall.py "Icarus falls"
{'resultCount': 1, 'results': [{'wrapperType': 'track', 'kind': 'song', 'artistId': 973181994, 'collectionId': 1531015419, 
'trackId': 1531015433, 'artistName': 'ZAYN', 'collectionName': 'Icarus Falls', 'trackName': 'Back To Life', 
'collectionCensoredName': 'Icarus Falls', 'trackCensoredName': 'Back To Life', 'artistViewUrl': 'https://music.apple.com/us/artist/zayn/973181994?uo=4', 
'collectionViewUrl': 'https://music.apple.com/us/album/back-to-life/1531015419?i=1531015433&uo=4', 
'trackViewUrl': 'https://music.apple.com/us/album/back-to-life/1531015419?i=1531015433&uo=4', 
'previewUrl': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview115/v4/1e/8f/20/1e8f204d-860a-4cab-4287-7ba850a5c227/mzaf_11951654510067714081.plus.aac.p.m4a', 
'artworkUrl30': 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/03/fe/dc/03fedc98-83cf-8e0c-76c8-1a97799b7b63/886448747352.jpg/30x30bb.jpg', 
'artworkUrl60': 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/03/fe/dc/03fedc98-83cf-8e0c-76c8-1a97799b7b63/886448747352.jpg/60x60bb.jpg', 
'artworkUrl100': 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/03/fe/dc/03fedc98-83cf-8e0c-76c8-1a97799b7b63/886448747352.jpg/100x100bb.jpg', 
'collectionPrice': 14.99, 'trackPrice': 1.29, 'releaseDate': '2018-12-13T12:00:00Z', 'collectionExplicitness': 'explicit', 
'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 29, 'trackNumber': 3, 'trackTimeMillis': 195467, 
'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'Pop', 'isStreamable': True}]}

Second print respomse:
(base) parthasarathysethuraman@Parthasarathys-MacBook-Air PythonTrail % python Apicall.py "Icarus falls"
ZAYN
"""