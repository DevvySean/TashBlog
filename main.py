from flask import Flask, render_template, request, flash


# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key"


@app.route('/', methods=['GET', 'POST'])
def index():

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.index.html')
    elif "android" in user_agent:
        return render_template('mobile.index.html')
    else:
        return render_template('desktop.index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


@app.route('/blog',  methods=['GET', 'POST'])
def blog():

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.blog.html')
    elif "android" in user_agent:
        return render_template('mobile.blog.html')
    else:
        return render_template('desktop.blog.html')


@app.route('/my-journey')
def my_journey():

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.myDiabetesjourney.html')
    elif "android" in user_agent:
        return render_template('mobile.myDiabetesjourney.html')
    else:
        return render_template('desktop.myDiabetesjourney.html')


if __name__ == '__main__':
    app.run(debug=True)

