import time
from flask import Flask, render_template, request
import csv
import os
import sys

app = Flask(__name__)

# Check to see if a file exists
inputFile = "./data/richathletes.csv"

if not os.path.exists(inputFile):
    sys.exit("File not found")



@app.route('/', methods=['GET'])
def index():
    return render_template('database.html')

@app.route('/', methods=['POST'])
def form():
    
    athletes()

    return render_template('form.html', output = data)


data = []

def athletes():
    # open the file and then auto close it when done
    with open('./data/richathletes.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        counter = 0
        for row in reader:
            # do stuff here
            if (counter == 0):
                header = row        
            else:
                data.append(row)
    
            counter += 1

    athletes = len(data)

    # print(f"There are {counter} rows")
    # print(f"There are {athletes} data rows")
    # print(header)
    # print(data[34])



if __name__ == '__main__':
    app.run(debug=True)




