class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #Counting Sort
        maxInd = max(max(seats),max(students))+1
        countSeats = [0] * maxInd
        countStudents = [0] * maxInd

        for seat in seats:
            countSeats[seat] +=1
        for student in students:
            countStudents[student] +=1
        
        i,j = 0,0
        remaining = len(students)
        res = 0

        while remaining:
            if countSeats[i] == 0:
                i+=1
            if countStudents[j] == 0:
                j+=1
            if countSeats[i] and countStudents[j]:
                res += abs(i-j)
                countSeats[i]-=1
                countStudents[j]-=1
                remaining -=1
        return res

        # #Sorting algo - O(NLogN)

        # seats.sort()
        # students.sort()
        # #[1,3,5]
        # #[2,4,7]
        # count = 0

        # for i in range(len(seats)):
        #     count += abs(students[i]-seats[i])
        
        # return count