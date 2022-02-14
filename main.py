from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('car_check_tokyomk.html')
    

if __name__ == "__main__":
    app.run(port=3000, debug=True)