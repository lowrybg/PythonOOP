from unittest import TestCase, main

from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Joe', {})
        self.student2 = Student('Bob', {'Physic': ['first', 'second']})

    def test_init_creates_all_attributes(self):
        self.assertEqual('Joe', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enrol_if_course_name_exists(self):
        res = self.student2.enroll('Medic',['bla'], 'n')
        self.assertEqual("Course has been added.", res)
        res = self.student.enroll('OOP', ['abv'])
        self.assertEqual("Course and course notes have been added.", res)
        res2 = self.student.enroll('OOP', ['asd'])
        self.assertEqual("Course already added. Notes have been updated.", res2)

    def test_add_notes__when_course_name_exists(self):
        result = self.student2.add_notes("Physic", 'aha')
        self.assertEqual("Notes have been updated", result)

    def test_add_notes__when_course_name_not_exists_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("Blabla", 'aha')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course__when_course_name_exists(self):
        result = self.student2.leave_course("Physic")
        self.assertEqual("Course has been removed", result)

    def test_leave_course__when_course_name_not_exists_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("Blabla")
        self.assertEqual("Cannot remove course. Course not found.",  str(ex.exception))


if __name__ == '__main__':
    main()