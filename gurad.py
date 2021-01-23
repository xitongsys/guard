from flask import Flask, request, send_from_directory, render_template
import xuexi_login as xl

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route("/")
def main():
    return app.send_static_file('index.html')

@app.route("/login")
def login():
    return app.send_static_file('login.html')

@app.route("/api/xuexi_login")
def xuexi_login():
    return "hehe"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)