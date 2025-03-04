# to-do list

## API
- mess with [oahu bus api](https://hea.thebus.org/api_info.asp) (json format) to see what it returns (hopefully coordinates that are constantly updating)
- function to store and update these coordinates as they are recieved
- there is **vehicle** api, **arrivals** api, and **route** api. figure out what each does and what we need/dont need
- is there coordinates for bus **stops** as well as buses themselves

## backend
- set up [folium](https://pypi.org/project/folium/) map of oahu in python
- set up routes.py for getting coordinate from api to the map
- set up all the other py files, app.py etc so we can run something
- set up search bar for address and make it work with the map to find locations (prob would be best if we can zoom into a bus stop, maybe we have to get coords of bus stops if the api doesnt have them)

## frontend
- html/css website:
- info/landing page
- page for the map
- maybe a big HST clock on map page to make it seem live and up to date
- make it look cool
