from classroom import Classroom
import unittest

class TestClassroom(unittest.TestCase):

    # sample classroom values
    course_id = 12345
    course_name = 'English I'
    students = ['Bob Jones', 'Ashley Moore', 'Julie Smith']
    students2 = ['Bob Jones', 'Ashley Moore', 'Julie Smith']
    
    #create classroom object
    test_class1 = Classroom(course_id, course_name, students)
    test_class2 = Classroom(course_id, course_name, students2)

    def test_getter_methods(self):
        # test get methods from classroom
        self.assertEqual(self.test_class1.course_id, 12345)
        self.assertEqual(self.test_class1.course_name, 'English I')
        self.assertEqual(self.test_class1.students, ['Bob Jones', 'Ashley Moore', 'Julie Smith'])

    def test_setter_methods(self):
        # set new values
        self.test_class1.course_id = 54321
        self.test_class1.course_name = 'English II'
        self.test_class1.students = ['John Doe', 'Jane Doe']
        # verify new values taken
        self.assertEqual(self.test_class1.course_id, 54321)
        self.assertEqual(self.test_class1.course_name, 'English II')
        self.assertEqual(self.test_class1.students, ['John Doe', 'Jane Doe'])
    
    def test_add_student(self):
        # add new student
        self.test_class2.addStudent('Joe Cool')
        # verify additional student
        self.assertEqual(self.test_class2.students, ['Bob Jones', 'Ashley Moore', 'Julie Smith', 'Joe Cool'])


if __name__ == '__main__':
    unittest.main()