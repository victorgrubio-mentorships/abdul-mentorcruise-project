from flask import request, Blueprint

from src.accounts.controllers import (
    list_all_accounts_controller,
    create_account_controller,
    retrieve_account_controller,
    update_account_controller,
    delete_account_controller,
)

accounts_bp = Blueprint("accounts", __name__, url_prefix="accounts")


@accounts_bp.route("/", methods=["GET", "POST"])
def list_create_accounts():
    if request.method == "GET":
        return list_all_accounts_controller()
    if request.method == "POST":
        return create_account_controller()
    else:
        return "Method is Not Allowed"


@accounts_bp.route("/<account_id>", methods=["GET", "PUT", "DELETE"])
def retrieve_update_destroy_accounts(account_id):
    if request.method == "GET":
        return retrieve_account_controller(account_id)
    if request.method == "PUT":
        return update_account_controller(account_id)
    if request.method == "DELETE":
        return delete_account_controller(account_id)
    else:
        return "Method is Not Allowed"
