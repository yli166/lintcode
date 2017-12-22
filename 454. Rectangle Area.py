class Rectangle:
    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''

    # write your code here
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        goal = self.x * self.y

        return goal