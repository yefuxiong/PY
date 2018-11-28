from flask import Flask, request, render_template
name ='asd'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html',name=name)


if __name__ == '__main__':
    app.run()