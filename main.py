from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Ploss, pozdravlyayu ss 5!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
string = hello()
 
words = string.split()
 
shortest = words[0]
 
for i in words[1:]:
    if len(i) < len(shortest):
        shortest = i
 
print(shortest)
print(len(shortest))
