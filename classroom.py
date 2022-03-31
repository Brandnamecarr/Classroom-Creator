class Classroom():

    def __init__(self, course_id : int, course_name : str, students : 'list[str]'):
        self._course_id = course_id
        self._course_name = course_name
        self._students = students
    
    # Getter and Setter Functions for class properties
    @property
    def course_id(self) -> int:
        return self._course_id
    
    @course_id.setter
    def course_id(self, id : int) -> None:
        self._course_id = id
    
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

    # TODO - Identify canvas import stategy