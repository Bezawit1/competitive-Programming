class Solution(object):
    def countStudents(self, students, sandwiches):
        while students and sandwiches[0] in students:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)

        return len(students)


        
        