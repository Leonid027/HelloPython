from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Ploss, pozdravlyayu ss 5!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
>>> def maxlen(s):
...     return len(max(s.split(), key=len))
...
>>> maxlen("Hello world") == 5
True
>>> maxlen("This is a simple test") == 6
True
>>>
