class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives,tens=0,0
        for i,n in enumerate(bills):            
            if n==5:
                fives+=1
            elif n==10:
                if fives>=1:
                    tens+=1
                    fives-=1   
                else:
                    return False
                               
            else:
                if tens>=1 and fives>=1:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
            print((n,i,fives,tens))

        return True
        