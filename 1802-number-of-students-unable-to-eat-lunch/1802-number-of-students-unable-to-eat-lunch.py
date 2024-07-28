class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        circle sandwich: 0
        square sandwich: 1
        number of sandwiches = number of students
        sandwiches in a stack
        if student at front prefers top sandwich, they take and leave queue
        else, they go to end of queue
        this loops till no queue students want top sandwich
        """
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                if students.count(students[0]) == len(students):
                    break

        return len(students)