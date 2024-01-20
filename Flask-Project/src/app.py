import os

# App Initialization

from src.create_app import create_app  # from __init__ file


# Applications Routes

from src.accounts.urls import accounts_bp


app = create_app(os.getenv("CONFIG_MODE"))

# ----------------------------------------------- #

# Hello World!


@app.route("/")
def hello():
    return "Hello World!"


app.register_blueprint(accounts_bp)
# ----------------------------------------------- #

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()
