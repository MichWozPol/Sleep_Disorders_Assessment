from sleep_disorders import app
from flask_bootstrap import Bootstrap


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)
    