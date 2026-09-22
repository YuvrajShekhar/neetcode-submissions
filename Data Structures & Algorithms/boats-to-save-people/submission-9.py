class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        output = 0
        for i in range(r+1):
            while l<=r:
                if people[l]+people[r]<=limit :
                    output+=1
                    l+=1
                    r-=1
                if people[l]+people[r]>limit and people[r]<=limit:
                    output+=1
                    r-=1
                

        return output
                
        