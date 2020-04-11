from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/search_result')
def search_resut():
   return render_template('search_result.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)