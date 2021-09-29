# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze."""

    # Write your Rat methods here.
    def __init__(self, symbol, row, column):
        """
        (Rat, str, int, int) -> NoneType
        
        A rat with symbol and its position in a row and in a column of the maze
        
        >>> rat = Rat(’P’, 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.column
        4
       
        """
        self.symbol = symbol
        self.row = row
        self.column = column
        self.num_sprouts_eaten = 0
    
    
    def set_location(self, row, column):
        """
        (Rat, int, int) -> NoneType
        
        Sets the location of a rat
        
        >>> rat = Rat(’P’, 1, 4)
        >>> rat.set_location(rat.row, rat.column)
        1,4
        """
        self.row, self.column = row, column
        #return self.row, self.column
        
        
    def get_location(self):
        """
        Returns the rat's location
        """
        return (self.row, self.column)
   
   
    def eat_sprout(self):
        """
        (Rat) -> NoneType
        
        Number of sprouts eaten
        >>> rat = Rat(’P’, 1, 4)
        >>> eat_sprout(rat)
        1
        """
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1
        
    def __str__(self):
        """
        (Rat) -> str
        
        Returns a string representation of the rat in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts
        
        >>> rat = Rat(’P’, 1, 4)
        >>> rat.set_location(rat.row, rat.column)
        >>> eat_sprout(rat)
        >>> str(rat)
        ’P at (1, 4) ate 1 sprouts.’
        """
        return self.symbol + ' at (' + str(self.row) + ',' +  str(self.column) + ') ate ' \
            + str(self.num_sprouts_eaten) + ' sprouts.'
    
        
        
   


rat = Rat("P", 1, 4)
rat.set_location(rat.row, rat.column)
rat.eat_sprout()
#print(rat.eat_sprout())
#print(rat.num_sprouts_eaten)
#print(rat.__str__())
#print(rat.row, rat.column)
#print(rat.set_location(rat.row, rat.column))
    
 
    
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    
    def __init__(self, maze_structure, rat_1, rat_2):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType
        
        Initializes a maze object
        
        >>> maze = Maze([['#','#','#','#','#'], \
                         ['#','.','.','@','#'], \
                             ['#','.','#','.','#'], \
                                 ['#','@','.','@','#'], \
                                     ['#','#','#','#','#']],\
                        Rat('P',2,2), 
                        Rat('J',2,3))
        >>> maze.maze_structure
        [['#','#','#','#','#'],
         ['#','.','.','@','#'],
         ['#','.','#','.','#'], 
         ['#','@','.','@','#'], 
         ['#','#','#','#','#']]
        >>> maze.rat_1
        P at (2,2) ate 0 sprouts.
        >>> maze.rat_2
        J at (2,3) ate 0 sprouts.
        """
        
        self.maze_structure = maze_structure
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        count = 0
        
        for i in self.maze_structure:
            for j in i:
                if j == SPROUT:
                    count = count +1
                            
       
        self.num_of_sprouts_left  = count
        
        
   
    def is_wall(self, row, column):
        """
        (Maze, int, int) -> bool
        
        Returns True if in that (row, column) position of the maze 
        there is a wall and False if otherwise.
        
        >>> maze = Maze([['#','#','#','#','#'],
                         ['#','.','.','@','#'],
                         ['#','.','#','.','#'],
                         ['#','@','.','@','#'], 
                         ['#','#','#','#','#']],
                        Rat('P',2,2), 
                        Rat('J',2,3))
        >>> maze.is_wall(0,0)
        True
        >>> maze.is_wall(1,2)
        False
        """
        
        if self.maze_structure[row][column] == WALL:
            return True
        else:
            return False

    def get_character(self, row, column):
        """
        (Maze, int, int) -> str
        
        Return the character in the maze at the given row and column.
        """
        
        element = self.maze_structure[row][column]
        
        if (self.rat_1.row, self.rat_1.column) == (row, column):
            element = self.rat_1.symbol
        if (self.rat_2.row, self.rat_2.column) == (row, column):
            element = self.rat_2.symbol
              
        return element
    
    
    def move(self, rat, v, h):
        """
        (Maze, Rat, int, int) -> bool
        
        Returns True if a rat has eaten a Sprout.
        v = vertical change: v = 1 when UP, v = 0 when NO_CHANGE and v = -1 when DOWN
        h = horizontal change: h = 1 when RIGHT, h = 0 when NO_CHANGE and h = -1 when LEFT
        >>> maze = Maze([['#','#','#','#','#'], \
                         ['#','.','.','@','#'], \
                             ['#','.','#','.','#'], \
                                 ['#','@','.','@','#'], \
                                     ['#','#','#','#','#']],\
                        Rat('P',2,1), 
                        Rat('J',2,3))
        >>> maze.move(Rat('P',2,1), 1, 0)
        True
        >>> maze.move(Rat('P',2,1), -1, 0)
        None
        """
        
        #rat_new_position = rat.get_location(rat.row + v, rat.column + h)
        #if rat_new_position =
        if self.is_wall(rat.row + v , rat.column + h):
            #rat_new_position = 
            rat.get_location()
            #return rat_new_position
        elif maze.maze_structure[rat.row + v][rat.column + h] == HALL:
            #rat_new_position = rat.set_location(rat.row + v, rat.column + h)
            #rat_new_position=
            rat.set_location(rat.row + v, rat.column + h)
        
        else:
            #rat_new_position=rat.set_location(rat.row + v, rat.column + h)
            #rat.num_sprouts_eaten = 
            rat.eat_sprout()
            self.num_of_sprouts_left = self.num_of_sprouts_left - 1
            self.maze_structure[rat.row + v][rat.column + h] = HALL
            return True
            
            
            
    def __str__(self):
        """
        (Maze) -> str
        Return a string representation of the maze
        >>> str(maze)
        """
        
        return str(self.maze_structure)  + "\n" + self.rat_1.__str__()  + "\n" + self.rat_2.__str__()
        
            
    
        
        
#................Main program........................

#rat = Rat("P", 1, 4)
#rat.set_location(rat.row, rat.column)
#rat.eat_sprout()
#print(rat.eat_sprout())
#print(rat.num_sprouts_eaten)
#print(rat.__str__())
#print(rat.row, rat.column)
#print(rat.set_location(rat.row, rat.column))


maze = Maze([['#','#','#','#','#'], \
                         ['#','.','.','@','#'], \
                             ['#','.','#','.','#'], \
                                 ['#','@','.','@','#'], \
                                     ['#','#','#','#','#']],\
                        Rat('P',2,2), 
                        Rat('J',2,3))
    
    
print(maze.maze_structure)
print(maze.rat_1)
print(maze.rat_2)

    


print(maze.num_of_sprouts_left)
print(maze.is_wall(0,0))
print(maze.maze_structure[1][3])
print(maze.get_character(1, 0))

    
maze_1 = Maze([['#','#','#','#','#'], \
                         ['#','.','.','@','#'], \
                             ['#','.','#','.','#'], \
                                 ['#','@','.','@','#'], \
                                     ['#','#','#','#','#']],\
                        Rat('P',2,1), 
                        Rat('J',2,3))
    
    
print(maze_1.get_character(2, 3))

rata = Rat("Y", 2, 1)
#rat_new_position = rata.get_location(rata.row + 2, rata.column + 1)
print('alalalalalla')
#print(rat_new_position)
#print(type(rat_new_position))
rata1 = maze_1.rat_1
print(maze_1.move(rata1, 1, 0))
#print(maze_1.maze_structure)
print(maze_1.num_of_sprouts_left)
print(str(maze_1))