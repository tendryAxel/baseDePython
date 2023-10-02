class test:
    def __init__(self):
        # Object variable
        self.variable = 1
    
    # Object method
    def incremente(self):
        self.variable += 1
        print(self.variable)
        return self.variable

# Instantiation
objectTest = test()
objectTest.incremente()