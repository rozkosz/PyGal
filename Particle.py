import numpy
# Contains mass, position, velocity, and accleration information

class Particle(object):
    
    # Function: Constructor
    # Description: Creates a new particle
    # Arguments:
    #   mass, The mass of the object
    #   posX, The position of this object on the X axis
    #   posY, The position of this object on the Y axis
    #   posZ, The position of this object on the Z axis
    #   velX, The velocity of this object on the X axis
    #   velY, The velocity of this object on the Y axis
    #   velZ, The velocity of this object on the Z axis
    # Returns: Particle
    def __init__( self , mass , posX , posY , posZ , velX , velY , velZ ):
        
        # Set the mass
        self.mass = mass
        
        # Set the position
        self.position = numpy.array( [ posX , posY, posZ ] )
        
        # Set the velocity
        self.velocity = numpy.array( [ velX , velY, velZ ] )
        
        # Create the accleration array
        self.accleration = numpy.array( [ [ 0.0 , 0.0 , 0.0 ] , [ 0.0 , 0.0 , 0.0 ] ] )
    
    # Computed Property: ke
    # Description: Returns this particles kinetic energy
    # Arguments: N/A
    # Returns: number
    @property
    def ke( self ):
        
        # Kinetic energy = .5 * mass * velocity**2
        return ( 0.5 * self.mass ) * ( numpy.sum( v**2 for v in self.velocity ) ) )
    
