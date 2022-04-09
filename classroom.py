class Classroom():

    def __init__(self, course_name : str, course_section : str, students : 'list[str]'):
        self._course_section = course_section
        self._course_name = course_name
        self._students = students
    
    # Getter and Setter Functions for class properties
    @property
    def course_section(self) -> str:
        return self._course_section
    
    @course_section.setter
    def course_section(self, id : str) -> None:
        self._course_section = id
    
    @property
    def course_name(self) -> str:
        return self._course_name
    
    @course_name.setter
    def course_name(self, name : str) -> None:
        self._course_name = name
    
    @property
    def students(self) -> 'list[str]':
        return self._students
    
    @students.setter
    def students(self, new_students : 'list[str]') -> None:
        self._students = new_students
    
    # inserts student into list of students
    def addStudent(self, student : str) -> None:
        self._students.append(student)


    # TODO - Create format data for Google classroom in format if needed
    def create_course_format(self):
        course = {
            'name' : self._course_name,
            'section' : self._course_section,
        }

        return course
    
    def enroll_students_format(self):
        students = []

        for s in self._students:
            students.append({
                'userID' : s
            })
        
        return students
