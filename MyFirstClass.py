
class Complex:

    printwasused = False

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def printsomething(self, something):
            print('hello: ' + something)
            self.printwasused = True


