from operator import truediv
from pydoc import locate
from sqlite3 import Date
import time
from typing import List
from warnings import catch_warnings
import settings
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from craigslist import CraigslistHousing
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
from util import find_points_of_interest, post_listing_to_slack

engine = create_engine('sqlite:///listings.db', echo = False)
Base = declarative_base()

#Table for storing listing data
class Listing(Base):
    __tablename__ = 'listings'

    id = Column(Integer, primary_key = True)
    link = Column(String, unique = True)
    created = Column(DateTime)
    geotag = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    name = Column(String)
    price = Column(Float)
    location = Column(String)
    cl_id = Column(Integer, unique = True)
    area = Column(String)
    cta_stop = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Scrapes for certain geographic areas and finds the latest listings
#Returns a list of results
def scrape_area(area):
    clh = CraigslistHousing(site = 'chicago', area = 'chc',
                            filters= {'max_price' : settings.MAX_PRICE, 'min_price' : settings.MIN_PRICE})
    
    #results will be returned
    results = [] 
    gen = clh.get_results(sort_by='newest',  geotagged=True, limit=20)
    print

    while True:
        try:
            result = next(gen)
        except StopIteration:
            print('StopIteration occured')
            break
        except Exception:
            continue
        listing = session.query(Listing).filter_by(cl_id=result["id"]).first()    

        if listing is None:
            if result["where"] is None:
                continue
            lat = 0        
            lon = 0
            if result["geotag"] is not None:
                lat = result["geotag"][0]
                lon = result["geotag"][1]

                geo_data = find_points_of_interest(result["geotag"], result["where"])
                result.update(geo_data)
            else:
                result["area"] = ""
                result["cta"] = ""

            # formatting price
            price = 0
            try:
                removeDollar = result['price'].replace('$', '')
                removeComma = removeDollar.replace(',', '')
                price = float(removeComma)
            except Exception:
                pass

            # Creates listing from data and adds to database
            listing = Listing(
                link = result['url'],
                created = parse(result['datetime']),
                lat = lat,
                lon = lon,
                name = result['name'],
                price = price,
                location = result['where'],
                cl_id = result['id'],
                area = result['area'],
                cta_stop = result['cta']
            )
            
            session.add(listing)
            session.commit()
            
            #This is where we filter out the results we want in terms of location
            if len(result["cta"]) > 0 or len(result["area"]) > 0:
                if 'studio' not in result['name'].lower():
                    results.append(result)
    
    return results  

#Driver Function
def do_scrape():

    #Connects to Slack Web Client
    sc = WebClient(settings.SLACK_TOKEN)

    #list of all results continuously added to results
    all_results = []
    all_results += scrape_area(settings.AREAS)
    print("{}: Returned {} results".format(time.ctime(), len(all_results)))

    for result in all_results:
        post_listing_to_slack(sc, result)
        