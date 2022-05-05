import pandas as pd
import matplotlib.pyplot as plt, mpld3
from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')


# I couln't get the data to get into a readable array, instead of having a length of 7 it only had a length of one making one massive index
# I spent a lot of time trying to figure it out, I just dont want you to think I didn't care, and I know my grade will reflect 


@app.route('/')
def index_page():
    return render_template('index.html', title="Home page")

@app.route('/sport')
def sport_page(): 
    sport_graph()
    return render_template('sport.html', title="Sports page")

@app.route('/money')
def money_page():
    money_graph()
    return render_template('money.html', title="Money page")

@app.route('/current_rank')
def currentrank_page():
    current_rank()
    return render_template('current_rank.html', title="Current Rank page")
  
def sport_graph():
    x = []
    y = []

    with open('./static/data/richathletes.csv', newline='') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',', quotechar='|')
        # print(plots)

        for row in plots:
            fixed_file = ', '.join(row)
         
        for item in fixed_file:
            
            if len(item) > 5:
                x.append(item[0])
                y.append(item[2])

    plt.bar(x, y, color = 'g', width = 0.72, label = "Sport")
    plt.xlabel('Names')
    plt.ylabel('Sports')
    plt.title('Sports Played')
    plt.legend()
    plt.show()

    file_exists = os.path.exists("./static/sport.png")

    if file_exists == False:
        plt.savefig('./static/sport.png')


def money_graph():

    x = []
    y = []

    with open('./static/data/richathletes.csv', newline='') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',', quotechar='|')
        # print(plots)

        for row in plots:
            fixed_file = ', '.join(row)
         
        for item in fixed_file:
            
            if len(item) > 5:
                x.append(item[0])
                y.append(item[2])

    plt.bar(x, y, color = 'g', width = 0.72, label = "Money Made")
    plt.xlabel('Names')
    plt.ylabel('Dollars')
    plt.title('Money Made')
    plt.legend()
    plt.show()
   
    file_exists = os.path.exists("./static/money.png")

    if file_exists == False:
        plt.savefig('./static/money.png')



def current_rank():
    x = []
    y = []

    with open('./static/data/richathletes.csv', newline='') as csvfile:
        try:
            plots = csv.reader(csvfile, delimiter = ',', quotechar='|')
        

            for row in plots:
                fixed_file = ', '.join(row)
         
        # I could not get the data to read into a readable array, It only had a length of 1
            for item in fixed_file:
            
                if len(item) > 5:
                    x.append(item[0])
                    y.append(item[2])

            plt.bar(x, y, color = 'g', width = 0.72, label = "Current Rank")
            plt.xlabel('Names')
            plt.ylabel('Rank')
            plt.title('Current Rank')
            plt.legend()
            plt.show()

        finally:
            # plots.close()
    
   
            file_exists = os.path.exists("./static/rank.png")

            if file_exists == False:
                plt.savefig('./static/rank.png')




if __name__ == '__main__':
    app.run(debug=True)