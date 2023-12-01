from flask import Flask, jsonify, request, render_template

from script import scrape_website
from script import ask_question

from flask_cors import CORS


app = Flask(__name__) 

CORS(app)

@app.route("/") 
def hello(): 
    return render_template('bot.html') 

@app.route('/scrape_website', methods = ['GET', 'POST',]) 
def scrape_website_1():
    url = request.json['url']
    data = scrape_website(url)
    return jsonify({'data': data}) 

@app.route('/ask_question', methods = ['GET', 'POST']) 
def ask_question_1(): 
    prompt = request.json['prompt']
    context = request.json['context']
    data = ask_question(prompt, context)
    return jsonify({'data': data}) 

# if __name__ == '__main__': 

# 	app.run(debug = True, port=8080)
