import json
import os
from flask import Flask,jsonify,request,url_for
from flask_cors import CORS,cross_origin
from algo import first_solution
import subprocess
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/output',methods=['GET'])
@cross_origin(origin='*')
def output_json():
    # with open('./iug_output1.json', 'r') as myfile:
    #  data = myfile.read()
    with open('algo/classes/iug_output v6.json', 'r') as myfile:
        data = myfile.read()
    return data

@app.route('/getinput',methods=['GET'])
@cross_origin(origin='*')
def getInput_json():
    # with open('./iug_output1.json', 'r') as myfile:
    #  data = myfile.read()
    with open('algo/classes/1st iug_input v4 grouping_modules.json', 'r') as myfile:
        data = myfile.read()
    return data

@app.route('/generateoutput',methods=['GET'])
@cross_origin(origin='*')
def generateOutput_json():
    subprocess.call(" python algo/first_solution.py ", shell=True)
    return 'done'


@app.route('/input',methods=['POST'])
def input_json():
    request_data = request.data
    request_data = json.loads(request.data.decode('utf-8'))
    return request_data

if __name__ == '__main__':
    app.run()