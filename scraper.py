import pandas as pd, os, requests
from bs4 import BeautifulSoup as bs


def scrape(currentDate, dayOfTheWeek):
  url = "https://connect.recsports.vt.edu/facilityoccupancy"
  #Website Scraping
  page = requests.get(url)
  result = bs(page.content, "html.parser").find(
    id="occupancyChart-da73849e-434d-415f-975a-4f9e799b9c39")
  #Create pandas data-frame
  mcComasData = pd.DataFrame(
    [[currentDate, int(result["data-occupancy"])]],
    columns=['Time', 'Occupancy'])
  #Saving data results
  if os.path.exists(f'static/csv/{dayOfTheWeek}.csv') and pd.read_csv(
      f'static/csv/{dayOfTheWeek}.csv'
  )['Time'][0][0:10] == currentDate.strftime('%F'):
    mcComasData.to_csv(f'static/csv/{dayOfTheWeek}.csv',
                       mode='a',
                       index=False,
                       header=False)
  else:
    mcComasData.to_csv(f'static/csv/{dayOfTheWeek}.csv',
                       index=False,
                       header=True)
