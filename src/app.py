import Flask
from flask import Request, Response, render_template
from src.db import db
from src.models.user import User

# App Initialization
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fanzone.db"
# initialize the app with the extension
db.init_app(app)
# migrate.init_app(app, db)


@app.route("/users", methods=["POST"])
def user_create(request: Request):
    user = User(
        username=request.form["username"],
        email=request.form["email"],
    )
    db.session.add(user)
    db.session.commit()
    return Response(response={"message": "OK"}, status=201)


@app.route("/users/create")
def user_create_render():
    return render_template("user/create.html")


@app.route("/users", methods=["GET"])
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return Response(response={"users": users}, status=200)
    # return render_template("user/list.html", users=users)


@app.route("/user/<int:user_id>", methods=["GET"])
def user_detail(user_id: int):
    user = db.get_or_404(User, user_id)
    return Response(response={"user": user}, status=200)


@app.route("/user/<int:user_id>/detail", methods=["GET"])
def render_user_detail(user_id: int):
    user = db.get_or_404(User, user_id)
    return render_template("user/detail.html", user=user)


@app.route("/user/<int:user_id>", methods=["PUT"])
def user_update(user_id: int, request: Request):
    user = db.get_or_404(User, user_id)
    if user:
        user.email = request.form["email"]
        user.username = request.form["username"]
        db.session.add(user)
        db.session.commit()
        return Response(response={"user": user}, status=200)


@app.route("/user/<int:id>", methods=["DELETE"])
def user_delete(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return Response(response={"message": "DELETED"}, status=200)
    # return render_template("user/delete.html", user=user)


if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    app.run()
