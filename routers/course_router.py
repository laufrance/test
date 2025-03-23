from flask import Blueprint
from controllers import course_controller

"""
Defines and registers the routes.
"""

course_router = Blueprint("course_router", __name__)

course_router.route("/courses", methods=["POST"])(course_controller.create)
course_router.route("/courses", methods=["GET"])(course_controller.get_all)
course_router.route("/courses/<string:course_id>", methods=["GET"])(
    course_controller.get_by_id
)
course_router.route("/courses/<string:course_id>", methods=["DELETE"])(
    course_controller.delete
)
