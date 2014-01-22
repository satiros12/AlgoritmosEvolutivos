import AlgoritmoGenetico.Mutacion as Mutation
print "Mutacion"

class TestMutacion:
    mutacion = Mutation.GeneticMutations()
    
    #print "Se inicializa"
    def prueba0(self):
        first = bin(200)[2:]
        second = bin (150)[2:]    
        print "First:",first,"Second:",second
        print self.mutacion.crossingOnePart(first,second)
        print self.mutacion.crossingOnePart(first,second)
        print self.mutacion.crossingOnePart(first,second)
        print self.mutacion.crossingOnePart(first,second)