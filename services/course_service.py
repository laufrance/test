import uuid
from repositories import course_repository


def create_course(title, description):
    """
    Creates a new course with a unique UUID and saves it to the repository.

    Args:
        title (str): The title of the course.
        description (str): The description of the course.

    Returns:
        dict: A dictionary representing the newly created course with id, title, and description.
    """
    course = {"id": str(uuid.uuid4()), "title": title, "description": description}
    course_repository.save(course)
    return course


def get_all_courses():
    """
    Fetches all courses from the repository.

    Returns:
        list: A list of all courses, sorted in reverse chronological order.
    """
    return course_repository.get_all()


def get_course_by_id(course_id):
    """
    Retrieves a course by its UUID.

    Args:
        course_id (str): The UUID of the course.

    Returns:
        dict or None: A dictionary representing the course if found, otherwise None.
    """
    return course_repository.get_by_id(course_id)


def delete_course(course_id):
    """
    Deletes a course by its UUID if it exists.

    Args:
        course_id (str): The UUID of the course.

    Returns:
        bool: True if the course was deleted, False if not found.
    """
    course = course_repository.get_by_id(course_id)
    if course:
        course_repository.delete(course_id)
        return True
    return False
