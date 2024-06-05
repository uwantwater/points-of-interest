from OSMPythonTools.overpass import Overpass
import json

result = []

def points_of_interest(x_coord: float, y_coord: float):
    rect = [x_coord - 0.04, y_coord - 0.04, x_coord + 0.04, y_coord + 0.04]
    bounds = [round(coord, 5) for coord in rect]
    overpass = Overpass()
    try:
        response = overpass.query(f"(nwr[amenity=place_of_worship][wikipedia~'.*']({bounds[0]}, {bounds[1]}, {bounds[2]}, {bounds[3]});nwr[tourism=attraction][wikipedia~'.*']({bounds[0]}, {bounds[1]}, {bounds[2]}, {bounds[3]});); out body;")
    except:
        return(None)
    response = response.toJSON()
    # print(json.dumps(response["elements"], indent=4))
    for i in range(len(response["elements"])):
        d = {}
        for key, value in response["elements"][i].items():
            match(key):
                case "type":
                    d["type"] = value
                case "id":
                    d["id"] = value
                case "lat":
                    d["lat"] = value
                case "lon":
                    d["lon"] = value
                case "tags":
                    for k, v in value.items():
                        try:
                            d["name"] = response["elements"][i]["tags"]["name:en"]
                        except KeyError:
                            d["name"] = response["elements"][i]["tags"]["name"]
            result.append(d)

        # print("\n")
    print(result)


points_of_interest(27.69474, 85.31902)