from classroom import Classroom
import unittest

class TestClassroom(unittest.TestCase):

    #create classroom object
    test_class1 = Classroom('12345', 'English I', 'jane@gmail.com', ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com'])
    test_class2 = Classroom('12345', 'English I', 'jane@gmail.com', ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com'])

    def test_getter_methods(self):
        # test get methods from classroom
        self.assertEqual(self.test_class1.course_id, '12345')
        self.assertEqual(self.test_class1.course_name, 'English I')
        self.assertEqual(self.test_class1.teacher, 'jane@gmail.com')
        self.assertEqual(self.test_class1.students, ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com'])

    def test_setter_methods(self):
        # set new values
        self.test_class1.course_id = '54321'
        self.test_class1.course_name = 'English II'
        self.test_class1.teacher = 'johnny@gmail.com'
        self.test_class1.students = ['suzy@gmail.com', 'barry@gmail.com']
        # verify new values taken
        self.assertEqual(self.test_class1.course_id, '54321')
        self.assertEqual(self.test_class1.course_name, 'English II')
        self.assertEqual(self.test_class1.teacher, 'johnny@gmail.com')
        self.assertEqual(self.test_class1.students, ['suzy@gmail.com', 'barry@gmail.com'])
    
    def test_add_student(self):
        # add new student
        self.test_class2.addStudent('george@gmail.com')
        # verify additional student
        self.assertEqual(self.test_class2.students, ['bob@gmail.com', 'joe@gmail.com', 'mary@gmail.com', 'george@gmail.com'])


if __name__ == '__main__':
    unittest.main()