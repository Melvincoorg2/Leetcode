 def countStudents(self, students, sandwiches):

        count0 = students.count(0)
        count1 = students.count(1)

        for sandwich in sandwiches:

            if sandwich == 0:
                if count0 == 0:
                    break
                count0 -= 1
            else:
                if count1 == 0:
                    break
                count1 -= 1

        return count0 + count1