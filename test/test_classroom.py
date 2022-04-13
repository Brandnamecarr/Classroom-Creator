from classroom import Classroom
import unittest

class TestClassroom(unittest.TestCase):

    #create classroom object
    test_class1 = Classroom('English I', 'Period 1', ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com'])
    test_class2 = Classroom('English I', 'Period 2', ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com'])

    def test_getter_methods(self):
        # test get methods from classroom
        self.assertEqual(self.test_class1.course_section, 'Period 1')
        self.assertEqual(self.test_class1.course_name, 'English I')
        self.assertEqual(self.test_class1.students, ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com'])

    def test_setter_methods(self):
        # set new values
        self.test_class1.course_section = 'Period 2'
        self.test_class1.course_name = 'English II'
        self.test_class1.students = ['suzy@gmail.com', 'barry@gmail.com']
        # verify new values taken
        self.assertEqual(self.test_class1.course_section, 'Period 2')
        self.assertEqual(self.test_class1.course_name, 'English II')
        self.assertEqual(self.test_class1.students, ['suzy@gmail.com', 'barry@gmail.com'])
    
    def test_add_student(self):
        # add new student
        self.test_class2.addStudent('george@gmail.com')
        # verify additional student
        self.assertEqual(self.test_class2.students, ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com', 'george@gmail.com'])


if __name__ == '__main__':
    unittest.main()