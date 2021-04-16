from flask_bootstrap import Bootstrap
from sleep_disorders import app


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=False)
    