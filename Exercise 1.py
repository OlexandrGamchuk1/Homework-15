class GroupException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class Group:
    def __init__(self, students=None):
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        if len(self.students) == 10:
            raise GroupException('There can be no more than 10 people in a group.')
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_a_student(self, surname):
        for student in self.students:
            if student == surname:
                return f'{student}\n'

    def __str__(self):
        return '\n'.join(self.students) + '\n'

    def __iter__(self):
        return GroupIterator(self.students)


class GroupIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


harris = 'Harris Jessica'
ivanov = 'Ivanov Ivan'
adamson = 'Adamson Samuel'
evans = 'Evans Joseph'
smith = 'Smith Olivia'
walker = 'Walker Emily'
davies = 'Davies Thomas'
wilson = 'Wilson George'
king = 'King Lily'

groups = [harris, ivanov, adamson, evans, smith, walker, davies, wilson, king]
groups = Group(groups)
for group in groups:
    print(group)