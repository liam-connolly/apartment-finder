
##PRICE
MIN_PRICE = 500
MAX_PRICE = 5000

#LOCATION PREFERENCES
CRAIGSLIST_CITY = 'chicago'
AREAS = 'chc'

#COORDINATES OF DESIRED AREAS
BOXES = {
    'west_town': [   
            [-87.707154,41.889194],
            [-87.639872,41.914059]
                ],

    'logan_square': [   
            [-87.731664,41.913575],
            [-87.66202,41.932388]
                ],

    'lincoln_park' : [
            [-87.682501,41.910861],
            [-87.626196,41.933045]
                ],
    
    'lakeview' : [
            [-87.674261,41.932343],
            [-87.635208,41.954751]
            ]

}

#FAILSAFE FOR DESIRED NEIGHBORHOODS WITH NO LOCATION LISTING
NEIGHBORHOODS = ['lakeview', 'lake view', 'lincoln park', 'logan square', 'bucktown', 'wicker park', 'wrigleyville', 'ukrainian village']

#MAX DISTANCE WILLING TO WALK FOR TRANSIT
MAX_L_DIST = 2 #kilometers

#COORDINATES OF DESIRED L STATIONS
L_STATIONS = {
    #brown/red
    'fullerton' : [41.925946737939306, -87.65249233155835],
    'belmont' : [41.940332802935714, -87.65325281683484],
    #brown
    'southport' : [41.94409042581892, -87.66346504769058],
    'paulina' : [41.944130829162695, -87.67123286158618],
    'addison-brown' : [41.947605420944896, -87.67487232683796],
    'diversey' : [41.93293812423488, -87.65298121495039],
    'wellington' : [41.93693863064373, -87.65325281683484],
    'armitage' : [41.91895458473454, -87.65270961218712],
    'sedgwick' : [41.91074894317455, -87.63864063457204],
    #red
    'north/clybourn' : [41.91115318667504, -87.64896150618155],
    'clark/division' : [41.90498136473898, -87.6323562411854],
    'addison-red': [41.947494921335576, -87.65364452193835],
    'sheridan': [41.953771007352614, -87.65473133231862],
    #blue
    'chicago-blue': [41.89619560287934, -87.65549091917651],
    'division': [41.90356410305652, -87.66731037318343],
    'damen': [41.90981125270273, -87.67777473080255],
    'western-blue': [41.916029781025294, -87.6871098412632],
    'california': [41.921995637323434, -87.69712249992425],
    'logan-square': [41.92969401063697, -87.70773965044285]

}

SLEEP_INTERVAL = 2*60 #20 minutes

#SLACK CREDENTIALS
SLACK_TOKEN = 'xoxb-4218791331425-4300119512213-MwvVP0Bp6Bwj37klcd5uHtYm'
SLACK_CHANNEL = '#two-bed-chicago'