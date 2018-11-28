from flask import Flask, request, render_template
ma ='asd'
app = Flask(__name__)
@app.route('/index', methods=['GET', 'POST'])
def index() :
    return render_template('index.html',ma=ma)
if __name__ =='__main__':
    app.run()
