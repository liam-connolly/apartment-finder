import settings
import math

def coord_distance(lat1, lon1, lat2, lon2):

    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = 6367 * c
    return km


def in_box(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False


def post_listing_to_slack(sc, listing):
    desc = "Area: {0} \nPrice: {1} \n Distance to nearest L Stop: {2} \nName: {3} \nLink: <{4}>".format(listing["area"], listing["price"], listing["cta_dist"], listing["name"], listing["url"])
    sc.api_call(
        "chat.postMessage",
        json = {
            'channel': settings.SLACK_CHANNEL, 
            'text' : desc,
            'username' : 'pybot',
            'icon_emoji' : ':robot_face:'
        }
    )

def find_points_of_interest(geotag, location):

    area_found = False
    area = ""
    min_dist = None
    near_cta = False
    cta_dist = "N/A"
    cta = ""
    # Look to see if the listing is in any of the neighborhood boxes we defined.
    for a, coords in settings.BOXES.items():
        if in_box(geotag, coords):
            area = a
            area_found = True

    # Check to see if the listing is near any transit stations.
    for station, coords in settings.L_STATIONS.items():
        dist = coord_distance(coords[0], coords[1], geotag[0], geotag[1])
        if (min_dist is None or dist < min_dist) and dist < settings.MAX_L_DIST:
            cta = station
            near_cta = True

        if (min_dist is None or dist < min_dist):
            cta_dist = dist

    # If the listing isn't in any of the boxes we defined, check to see if the string description of the neighborhood
    # matches anything in our list of neighborhoods.
    if len(area) == 0:
        for hood in settings.NEIGHBORHOODS:
            if hood in location.lower():
                area = hood

    return {
        "area_found": area_found,
        "area": area,
        "near_cta": near_cta,
        "cta_dist": cta_dist,
        "cta": cta
    }