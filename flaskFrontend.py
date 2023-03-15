from flask import Flask, render_template
from threading import Thread
app = Flask('')

@app.route('/')
def home():
  return render_template('McComas.html')

def run():
  app.run(host='0.0.0.0', port=8080)

def frontEndThread():
  t = Thread(target=run)
  t.start()
