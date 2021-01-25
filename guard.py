from flask import Flask, request, send_from_directory, render_template
import xuexi_login as xl
import os, datetime

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, template_folder='./static')

users = ['baba', 'kk', 'kk2']
def getQrcodeInfo():
    res = []
    for user in users:
        it = {
            'user': user,
            'date': None
        }
        path = os.path.join('static', user + '.png')
        if os.path.exists(path):
            it['date'] = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
        res.append(it)
    return res


@app.route("/")
def main():
    users = getQrcodeInfo()
    return render_template('index.html', users=users)

@app.route("/api/xuexi_reloadqrcode/<user>")
def xuexi_reloadqrcode(user):
    return xl.updateQrcode(user, 'static')

@app.route("/api/xuexi_updatecookie/<user>/<qr>")
def xuexi_updatecookie(user, qr):
    return xl.updateCookie(qr, os.path.join('static', user + "_cookies.json"));

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
