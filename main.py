from flask import Flask
app = Flask(__name__)

@app.route("/")


f = open("lesson.txt")
r = f.read()
 
# данный код определяет сколько раз встречается самое длинное слово в файле.
s = max(map(lambda x: (len(x), x), r.replace(',','').replace('.','').split(" ")))
 
print(r,'\n','Самое длинное слово:"',s[1],'" встречается:',r.count(s[1]), 'раз(а)')

#def hello();
#eturn "Hello Ploss, pozdravlyayu ss 5!"
#def func(string):
 # maxlen = 0
 # for x in string.split('Hello Ploss, pozdravlyayu ss 5!'):
 #   if len(x)> maxlen:
   #   maxlen = len(x)
   #   word = x
 # print (string +'\n','Самое длинное слово - ', word, ',', maxlen, ' символов')
 
# func(string = input ('Введите строку: '))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

