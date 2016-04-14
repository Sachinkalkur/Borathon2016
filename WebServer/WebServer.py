from flask import Flask, redirect, request, url_for, render_template, Response

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


if __name__ == "__main__":
    app.debug = True
    app.Thread = True
    app.run('172.31.28.150', 80)
