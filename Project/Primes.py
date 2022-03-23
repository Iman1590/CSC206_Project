import time
from flask import Flask, render_template, request

app = Flask(__name__)


prime_list = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form():
    
    user_input = int(request.form.get("num"))

    prime(user_input)

    return render_template('form.html', output = prime_list)

def prime(num_input):
    start = time.time()

    # num_input = int(input("Enter a number: "))

    num_input = int(request.form.get("num"))

  

    for num in range(1, num_input + 1):
   
        if num > 1:

            for i in range(2, num):

                if (num % i) == 0:

                    break
            else:
    
                prime_list.append(num)


    # output_page = request.form.get("output")
  
    

    

    output_num = print(prime_list)

  


    # print("--- %s seconds ---" % (time.time() - start))

    


if __name__ == '__main__':
    app.run(debug=True)
