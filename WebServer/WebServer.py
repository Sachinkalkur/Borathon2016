from flask import Flask, redirect, request, url_for, render_template, Response
import urllib2

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('home_page.html')


@app.route("/Login", methods=["POST"])
def login_page():
    if request.method == "POST":
        login_data = request.form
        # if(verify_user(login_data))
        if login_data['userType'] == '1':
            return redirect(url_for('administrator_page'))
        if login_data['userType'] == '0':
            return redirect(url_for('user_page'))
        return "Please enter the type of the user"


@app.route("/Administrator", methods=["GET", "POST"])
def administrator_page():
    return render_template('administrator_page.html')


@app.route("/User", methods=["GET", "POST"])
def user_page():
    return "hello User"


@app.route("/Demo", methods=["GET"])
def demo_page():
    try:
        response = urllib2.urlopen('http://10.172.31.28.150/')
        return response.read()
    except urllib2.HTTPError, e:
        return e.fp.read()


if __name__ == "__main__":
    app.debug = True
    app.Thread = True
    app.run('172.31.28.150', 80)
