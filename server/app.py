app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

...

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

