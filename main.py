import datetime, time, pytz, logging
from flaskFrontend import frontEndThread
from scraper import scrape
from plotting import create_graph

tzEast = pytz.timezone('America/New_York')
frontEndThread()

#Logging setup
logger = logging.getLogger('mcComasLogger')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#Stream Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
#Error Log
error_handler = logging.FileHandler("static//logs//errorLog.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
logger.addHandler(error_handler)

#Main loop
while True:
  currentDate = datetime.datetime.now(tzEast)
  dayOfTheWeek = currentDate.strftime("%A")
  try:
    scrape(currentDate, dayOfTheWeek)
  except:
    logger.error("Scrape Failed")
  try:
    create_graph(currentDate, dayOfTheWeek)
  except:
    logger.error("Graph Falied")
  time.sleep(300)
