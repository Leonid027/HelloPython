from flask import Flask
app = Flask(__name__)

@app.route("/")
#def hello();
#eturn "Hello Ploss, pozdravlyayu ss 5!"
def func(string):
  maxlen = 0
  for x in string.split('Hello Ploss, pozdravlyayu ss 5!'):
    if len(x)> maxlen:
      maxlen = len(x)
      word = x
  print (string +'\n','Самое длинное слово - ', word, ',', maxlen, ' символов')
 
# func(string = input ('Введите строку: '))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

