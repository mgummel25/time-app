# This is a simple Flask app to display the current epoch time
import os
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    epoch_time = time.time()
    return f"This is the epoch time: {int(epoch_time)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
