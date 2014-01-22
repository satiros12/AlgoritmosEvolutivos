""" Here i put some  mutation functions"""
import random
class GeneticMutations:
    """With binary strings of equal long int 1 with long 3 is 001"""
    def crossingOnePart(self,  first,  second):
        if(len(first) != len(second)):
             raise NameError("They must have the same long")
        else:
             result = ''
             position = random.randint(0, len(first) - 1) #They must have the same lenght
             index = 0
             while (index < len(first)):
                 if(index >= position):
                    result = result + second[index]
                 else:                 
                    result = result + first[index]
                 index = index + 1
             return result
             
    def bitMutation(self,  first):
        result = ''
        position = random.randint(0, len(first)) 
        idex = 0
        while (index < len(first)):
                result = result + first[index]
                if(index == position):
                    result = result + str((int(first[index]) + 1)  % 2)
                index = index + 1                
        return result
