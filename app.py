from flask import Flask, jsonify, request 
import json

app = Flask(__name__) 

with open('resume.json', 'r') as file:
    resume_data = json.load(file)

@app.route('/resume', methods = ['GET', 'POST']) 
def home(): 
    if request.method == 'GET': 
        return jsonify(resume_data) 

@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
    return jsonify({'data': num**2}) 

# driver function 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug = True)
