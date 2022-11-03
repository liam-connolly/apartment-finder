
##PRICE
MIN_PRICE = 500
MAX_PRICE = 1250

#LOCATION PREFERENCES
CRAIGSLIST_CITY = 'chicago'
AREAS = 'chc'

#COORDINATES OF DESIRED AREAS
BOXES = {
    'old_town': [   
            [-87.643959,41.895964], 
            [-87.625514,41.911295]
                ],

    'lincoln_park' : [
            [-87.667219,41.910619],
            [-87.631513,41.925628]        
                ],
    
    'lakeview' : [
            [-87.688119,41.925021],
            [-87.631213,41.954358]
            ],

    'uptown' : [
            [-87.690865,41.953672],
            [-87.642371,41.99105]           
    ],

    'rogers_park' : [
        [-87.711851,41.990157],
        [-87.648637,42.041044]
    ]
}

#FAILSAFE FOR DESIRED NEIGHBORHOODS WITH NO LOCATION LISTING
NEIGHBORHOODS = ['old town', 'lincoln park', 'wrigleyville', 'lake view', 'lake view east', 'roscoe village', 'uptown', 'andsersonville', 'buena park']

#MAX DISTANCE WILLING TO WALK FOR TRANSIT
MAX_L_DIST = 2 #kilometers

#COORDINATES OF DESIRED L STATIONS
L_STATIONS = {
    'clark/division' : [41.90498136473898, -87.6323562411854],
    'sedgwick' : [41.91074894317455, -87.63864063457204],
    'north/clybourn' : [41.91115318667504, -87.64896150618155],
    'armitage' : [41.91895458473454, -87.65270961218712],
    'fullerton' : [41.925946737939306, -87.65249233155835],
    'diversey' : [41.93293812423488, -87.65298121495039],
    'wellington' : [41.93693863064373, -87.65325281683484],
    'belmont' : [41.940332802935714, -87.65325281683484],
    'southport' : [41.94409042581892, -87.66346504769058],
    'paulina' : [41.944130829162695, -87.67123286158618],
    'addison-b' : [41.947605420944896, -87.67487232683796],
    'addison-r' : [41.94792862915813, -87.6536330594731],
    'sheridan' : [41.954190464847954, -87.65461082625714],
    'irving park' : [41.9546752264718, -87.67503528796863],
    'montrose' : [41.9624854594689, -87.67538197215102],
    'damen' : [41.96684158997151, -87.67874266177795],
    'western' : [41.96694289178825, -87.6885522423106],
    'wilson' : [41.965205603392704, -87.65767674963772],
    'argyle' : [41.9740416942623, -87.6585428237428],
    'bryn mawr': [41.983842239624195, -87.65883151511117],
    'thorndale' : [41.990458543154936, -87.65931266739179]

}

SLEEP_INTERVAL = 2*60 #20 minutes

#SLACK CREDENTIALS
SLACK_TOKEN = 'xoxb-4218791331425-4300119512213-MwvVP0Bp6Bwj37klcd5uHtYm'
SLACK_CHANNEL = '#housing'