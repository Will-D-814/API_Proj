import requests
import json
from flask import Flask,request,render_template,url_for
from server_functions.function_list import get_API_data,category_count,output_of_category

URL='https://api.publicapis.org/entries'
API_dict = get_API_data(URL)

app = Flask(__name__)

@app.route("/")
def index():
    return 'So it is working'

@app.route("/echo")
def default_output():
    return get_API_data(URL)


#route for counting the number within a given category.
@app.route("/will",methods=['POST','GET'])
def category_counter():
    if request.method =='POST':
        category = request.form['content']
        output =  "There are: "+ str(category_count(category,API_dict))+" APIs in the "+ str(category)+' category'
        return render_template('category.html', output=output)
    else:
        return render_template('category.html')

@app.route('/category', methods =["POST","GET"])
def category_list():
    if request.method =='POST':
        category = request.form['content']
        temp =  output_of_category(category,API_dict) 
        output = ''
        for api in temp:
            output = output + ' ,' + api
        return render_template('category.html', output=output)
    else:
        return render_template('category.html')


    
if __name__ == '__main__':
    app.run(host='127.0.01', port =8080,debug = True)
