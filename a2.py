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
    def __init__(self, symbol, row, col):
        """
        (Rat, str, int, int) -> NoneType
        
        A rat with symbol and its position in a row and in a col of the maze
        
        >>> rat = Rat(’P’, 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
       
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
    
    
    def set_location(self, row, col):
        """
        (Rat, int, int) -> NoneType
        
        Sets the location of a rat
        
        >>> rat = Rat(’P’, 1, 4)
        >>> rat.set_location(rat.row, rat.col)
        1,4
        """
        self.row, self.col = row, col
        
        
    def get_location(self):
        """
        Returns the rat's location
        """
        return (self.row, self.col)
   
   
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
        >>> rat.set_location(rat.row, rat.col)
        >>> eat_sprout(rat)
        >>> str(rat)
        ’P at (1, 4) ate 1 sprouts.’
        """
        return self.symbol + ' at (' + str(self.row) + ', ' +  str(self.col) + ') ate ' \
            + str(self.num_sprouts_eaten) + ' sprouts.'
    
        
        
   
    
 
    
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    
    def __init__(self, maze, rat_1, rat_2):
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
        >>> maze.maze
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
        
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        count = 0
        
        for i in self.maze:
            for j in i:
                if j == SPROUT:
                    count = count +1
                            
       
        self.num_sprouts_left  = count
        
        
   
    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool
        
        Returns True if in that (row, col) position of the maze 
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
        
        if self.maze[row][col] == WALL:
            return True
        else:
            return False

    def get_character(self, row, col):
        """
        (Maze, int, int) -> str
        
        Return the character in the maze at the given row and col.
        """
        
        element = self.maze[row][col]
        
        if (self.rat_1.row, self.rat_1.col) == (row, col):
            element = self.rat_1.symbol
        if (self.rat_2.row, self.rat_2.col) == (row, col):
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
        
        if self.is_wall(rat.row + v , rat.col + h):
            rat.get_location()
        elif self.maze[rat.row + v][rat.col + h] == HALL:
            rat.set_location(rat.row + v, rat.col + h)
        
        else:
            rat.eat_sprout()
            self.num_sprouts_left = self.num_sprouts_left - 1
            self.maze[rat.row + v][rat.col + h] = HALL
            return True
            
            
            
    def __str__(self):
        """
        (Maze) -> str
        Return a string representation of the maze
        >>> str(maze)
        """
        
        res = ''
        for i in self.maze:
            for j in i:
                res = res + j
            res = res + "\n"
        res = res + self.rat_1.__str__() + "\n"
        res = res + self.rat_2.__str__()
        return res
            
        
            
    
        
        
