from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['POST']) 

def hello():
   return "Helllllo World!"
print(hello())
listWords = hello().split()
idLongestWord = 0
for i in range(1,len(listWords)):
    if len(listWords[idLongestWord]) < len(listWords[i]):
        idLongestWord = i
print(listWords[idLongestWord])

    return hello
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

