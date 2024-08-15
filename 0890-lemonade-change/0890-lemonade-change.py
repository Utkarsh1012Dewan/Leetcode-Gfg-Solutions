class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives,tens = 0,0
#more clean code
        for i in bills:
            if i == 5:
                fives +=1
            
            if i == 10:
                if fives > 0:
                    tens +=1
                    fives -=1
                else:
                    return False
            
            if i == 20:
                if tens > 0 and fives > 0:
                    tens -=1
                    fives -=1
                elif fives >= 3:
                    fives -=3
                else:
                    return False
        return True



# #my code (badly written)
#         for i in bills:
#             if i == 5:
#                 fives +=1
#             elif i == 10:
#                 if fives == 0:
#                     return False
#                 else:
#                     tens +=1
#                     fives -=1
#             elif i == 20:
#                 if fives == 0:
#                     return False
#                 elif tens == 0: 
#                     if fives < 3:
#                         return False
#                     else:
#                         fives -= 3
#                 elif tens > 0 and fives > 0:
#                     tens -=1
#                     fives -=1
#         return True