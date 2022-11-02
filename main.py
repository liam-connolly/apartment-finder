from inspect import trace
from scraper import do_scrape
import settings
import time
import sys
import traceback

if __name__ == '__main__':
    while True:
        print("{}: starting scrape".format(time.ctime()))
        try:
            do_scrape()
        except KeyboardInterrupt:
            print("exiting!")
        except Exception as exc:
            print("Error with scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully scraped!".format(time.ctime()))
        time.sleep(settings.SLEEP_INTERVAL)