from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/factorial/<numb>')
def calculate_factorial(numb):
    num = int(numb)
    factorial = 1    
    if num < 0:    
       return 'Factorial does not exist for negative numbers'    
    elif num == 0:    
       return 'The factorial of 0 is 1'    
    else:    
       for i in range(1,num + 1):    
           factorial = factorial*i    
       return f'The factorial of {num} is {factorial}'

@app.route('/feature')
def hello_feature():
    return 'Hello, new feature!'


if __name__ == "__main__":
    app.run()
