import sqlite3


def init_db():
    """
    Initializes the SQLite database and creates the courses table if it doesn't exist.
    """
    conn = sqlite3.connect("courses.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def save(course):
    """
    Saves a new course to the database.

    Args:
        course (dict): A dictionary containing course data (id, title, description).
    """
    conn = sqlite3.connect("courses.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (id, title, description) VALUES (?, ?, ?)",
        (course["id"], course["title"], course["description"]),
    )
    conn.commit()
    conn.close()


def get_all():
    """
    Retrieves all courses from the database.

    Returns:
        list: A list of dictionaries representing courses.
    """
    conn = sqlite3.connect("courses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM courses")
    courses = [
        {"id": row[0], "title": row[1], "description": row[2]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return courses[::-1]


def get_by_id(course_id):
    """
    Retrieves a specific course by its UUID from the database.

    Args:
        course_id (str): The UUID of the course.

    Returns:
        dict or None: A dictionary with course data if found, otherwise None.
    """
    conn = sqlite3.connect("courses.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, description FROM courses WHERE id = ?", (course_id,)
    )
    course = cursor.fetchone()
    conn.close()
    if course:
        return {"id": course[0], "title": course[1], "description": course[2]}
    return None


def delete(course_id):
    """
    Deletes a course by its UUID from the database.

    Args:
        course_id (str): The UUID of the course.
    """
    conn = sqlite3.connect("courses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
