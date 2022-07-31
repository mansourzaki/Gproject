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
    with open('algo/classes/iug_output.json', 'r') as myfile:
        data = myfile.read()
    return data

#get the first input
@app.route('/getinput1',methods=['GET'])
@cross_origin(origin='*')
def getInput_json1():

    with open('algo/classes/iug_input1.json', 'r') as myfile:
        data = myfile.read()
    return data


#get the second input
@app.route('/getinput2',methods=['GET'])
@cross_origin(origin='*')
def getInput_json2():
    # with open('./iug_output1.json', 'r') as myfile:
    #  data = myfile.read()
    with open('algo/classes/iug_input2.json', 'r') as myfile:
        data = myfile.read()
    return data

#run the the grouping and get the first output
@app.route('/generatefirstoutput',methods=['GET'])
@cross_origin(origin='*')
def generateFirstOutput_json():
    subprocess.call(" python algo/groupingmodules2.py ", shell=True)
    # subprocess.call(" python algo/groupingmodules.py ", shell=True)
    return 'done'

#run the initialsolution that produce the final output
@app.route('/generatefinaloutput',methods=['GET'])
@cross_origin(origin='*')
def generateFinalOutputjson():
    print('hii')
    subprocess.call(" python algo/first_solution2.py ", shell=True)
    # subprocess.call(" python algo/first_solution.py ", shell=True)
    return 'done'

#uploads input2 file to algorithim
@app.route('/loadinput2',methods=['POST'])
def inputLoad2_json():
    request_data = request.data
    request_data = json.loads(request.data.decode('utf-8'))
    with open('algo/classes/iug_input2.json', 'w') as write_file:
       json.dump(request_data, write_file, indent=4)
    return request_data

#uploads input1 file to algorithim
##check return invalid
@app.route('/loadinput1',methods=['POST'])
def inputLoad1_json():
    request_data = request.data
    request_data = json.loads(request.data.decode('utf-8'))
    with open('algo/classes/iug_input1.json', 'w') as write_file:
       json.dump(request_data, write_file, indent=4)
    return request_data

if __name__ == '__main__':
    app.run()