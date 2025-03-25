# to-do list

## API
- is there coordinates for bus **stops** as well :
  - 3800 of them in `stops_coords.txt` in `stop`, (`lat`, `lon`) format

## backend
- set up search bar for address and make it work with the map to find locations (prob would be best if we can zoom into a bus stop, maybe we have to get coords of bus stops if the api doesnt have them)
- we gotta loop through `stops_coords.txt` and make static markers. dont want to redundantly render bus stops (run the loop) every time we open the app. write loop once, store in dataframe, get markers from there and add to map.

## frontend
- html/css website:
- info/landing page
- page for the map
- maybe a big HST clock on map page to make it seem live and up to date
- make it look cool
