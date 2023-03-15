import matplotlib.pyplot as plt, pandas as pd, matplotlib.dates as mpl_dates, pytz, datetime
from matplotlib import ticker

tzEast = pytz.timezone('America/New_York')


def create_graph(currentDate, dayOfTheWeek):
  if int(currentDate.strftime("%w")) >= 1 and int(
      currentDate.strftime("%w")) <= 5:
    openTime = 6
    closeTime = 23
  else:
    openTime = 10
    closeTime = 22

  plt.figure(figsize=(16, 9))
  plt.style.use('seaborn-v0_8')
  df = pd.read_csv(f'static/csv/{dayOfTheWeek}.csv')
  ax = plt.subplot()
  x = mpl_dates.date2num(df['Time'])
  y = df['Occupancy']
  ax.plot_date(x, y, linestyle="solid")
  ax.set_title(f'McComas occupancy on {currentDate.strftime("%A, %m/%d/%y")}',
               fontsize=20)
  ax.set_xlabel("Time", fontsize=20)
  ax.set_ylabel("People in McComas", fontsize=20)
  plt.xticks(fontsize=15)
  plt.yticks(fontsize=18)
  ax.yaxis.set_major_locator(
    ticker.FixedLocator([0, 100, 200, 300, 400, 500, 600, 700, 800]))
  ax.set_ylim(0, 800)
  openDate = tzEast.localize(
    datetime.datetime(currentDate.year,
                      currentDate.month,
                      currentDate.day,
                      hour=openTime))
  closeDate = tzEast.localize(
    datetime.datetime(currentDate.year,
                      currentDate.month,
                      currentDate.day,
                      hour=closeTime,
                      minute=10))
  ax.set_xlim(openDate, closeDate)
  ax.xaxis.set_major_locator(mpl_dates.HourLocator(interval=2))
  plt.tick_params(rotation=45)
  date_format = mpl_dates.DateFormatter('%I:%M %p', tz=tzEast)
  plt.gca().xaxis.set_major_formatter(date_format)
  plt.tight_layout()
  plt.savefig(f'static/img/{dayOfTheWeek}.png', dpi=400)
