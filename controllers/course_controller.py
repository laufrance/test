from flask import request, jsonify
from services import course_service
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def create():
    """
    Handles the creation of a new course. Validates the input data, ensuring
    the title and description are provided and the description length is between 50 and 255 characters.

    Returns:
        Response (Flask): JSON response with the created course data or an error message.
    """
    data = request.get_json()
    if not data.get("title") or not data.get("description"):
        logging.warning("Failed to create course: missing title or description")
        return (
            jsonify(
                {
                    "type": "about:blank",
                    "title": "Bad Request",
                    "status": 400,
                    "detail": "Title and description are required",
                }
            ),
            400,
        )

    if len(data["description"]) < 50 or len(data["description"]) > 255:
        logging.warning(
            "Failed to create course: description must be between 50 and 255 characters"
        )
        return (
            jsonify(
                {
                    "type": "about:blank",
                    "title": "Invalid Description Length",
                    "status": 400,
                    "detail": "Description must be between 50 and 255 characters",
                }
            ),
            400,
        )

    course = course_service.create_course(data["title"], data["description"])
    logging.info(f"Course created: {course['title']}")
    return jsonify({"data": course}), 201


def get_all():
    """
    Retrieves all courses from the service layer.

    Returns:
        Response (Flask): JSON response with the list of courses.
    """
    logging.info("Fetching all courses")
    courses = course_service.get_all_courses()
    return jsonify({"data": courses}), 200


def get_by_id(course_id):
    """
    Retrieves a specific course by its UUID.

    Args:
        course_id (str): The UUID of the course to retrieve.

    Returns:
        Response (Flask): JSON response with the course data or an error message.
    """
    logging.info(f"Fetching course with ID: {course_id}")
    course = course_service.get_course_by_id(course_id)
    if not course:
        logging.warning(f"Course not found: ID {id}")
        return (
            jsonify(
                {
                    "type": "about:blank",
                    "title": "Course Not Found",
                    "status": 404,
                    "detail": f"The course with ID {course_id} was not found.",
                }
            ),
            404,
        )

    return jsonify({"data": course}), 200


def delete(course_id):
    """
    Deletes a course by its UUID.

    Args:
        course_id (str): The UUID of the course to delete.

    Returns:
        Response (Flask): Empty response with status 204 if successful, or 404 if not found.
    """
    logging.info(f"Deleting course with ID: {course_id}")
    if not course_service.delete_course(course_id):
        logging.warning(f"Failed to delete: Course not found with ID {course_id}")
        return (
            jsonify(
                {
                    "type": "about:blank",
                    "title": "Course Not Found",
                    "status": 404,
                    "detail": f"The course with ID {course_id} was not found.",
                }
            ),
            404,
        )
    logging.info(f"Course deleted: ID {id}")
    return "", 204
