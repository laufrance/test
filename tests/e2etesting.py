import requests
import unittest
from dotenv import load_dotenv
import os
import sys

load_dotenv()

HOST = sys.argv[1] if len(sys.argv) > 1 else os.getenv("HOST", "localhost")
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("PORT", 8080))

class TestClassConnectAPI(unittest.TestCase):
    BASE_URL = f"http://{HOST}:{PORT}/courses"

    def test_create_course(self):
        """
        Test creating a new course with valid data.
        Ensures the course is successfully created with status 201 and returns the course data.
        """
        response = requests.post(
            self.BASE_URL,
            json={
                "title": "Course 1",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("data", response.json())

    def test_get_courses(self):
        """
        Test retrieving all courses.
        Ensures the response returns a list of courses and status 200.
        """
        requests.post(
            self.BASE_URL,
            json={
                "title": "Course 2",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae.",
            },
        )
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json().get("data"), list)

    def test_get_course_by_id(self):
        """
        Test retrieving a specific course by its UUID.
        Ensures the response returns the correct course data and status 200.
        """
        course = requests.post(
            self.BASE_URL,
            json={
                "title": "Course 3",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum.",
            },
        ).json()["data"]
        response = requests.get(f'{self.BASE_URL}/{course["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["title"], "Course 3")

    def test_delete_course_by_id(self):
        """
        Test deleting a course by its UUID.
        Ensures the course is deleted successfully with status 204 and returns 404 when accessed again.
        """
        course = requests.post(
            self.BASE_URL,
            json={
                "title": "Course 4",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel mauris eget risus gravida tincidunt.",
            },
        ).json()["data"]
        delete_response = requests.delete(f'{self.BASE_URL}/{course["id"]}')
        self.assertEqual(delete_response.status_code, 204)
        get_response = requests.get(f'{self.BASE_URL}/{course["id"]}')
        self.assertEqual(get_response.status_code, 404)

    def test_invalid_description_length(self):
        """
        Test creating a course with invalid description length.
        Ensures the API rejects descriptions shorter than 50 characters or longer than 255 characters.
        """
        long_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit."
        response = requests.post(
            self.BASE_URL,
            json={"title": "Invalid Course", "description": long_description},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid Description Length", response.json().get("title"))

        short_description = "Lorem ipsum dolor sit amet, consectet"
        response = requests.post(
            self.BASE_URL,
            json={"title": "Invalid Course", "description": short_description},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid Description Length", response.json().get("title"))

        valid_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        response = requests.post(
            self.BASE_URL,
            json={"title": "Valid Course", "description": valid_description},
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("data", response.json())


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
