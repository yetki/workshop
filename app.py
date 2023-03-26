from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'test'
    return render_template('index.html', name=name)


@app.route('/atolye/<name>')
def user(name):
    return "<h1>Hells {}</h1>".format(name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500



#* 
#def index():
#    name = 'John'
#    return render_template('index.html', name=name)
 #






if __name__ == '__main__':
    app.run(debug=True)
