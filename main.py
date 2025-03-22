from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [{"title":"Avatar"}]
    for i in range (10):
        movies.append({"title":"1"})
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)