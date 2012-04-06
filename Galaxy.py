import numpy
from itertools import combinations
from Particle import Particle
# Contains a list of particles and methods for manipulating them

class Galaxy( list ):
    
    # Computed Property: ke
    # Description: Returns this galaxies kinetic energy
    # Arguments: N/A
    # Returns: number
    @property
    def ke( self ):
        
        # Return the summation of all particles kinetic energy
        return numpy.sum( particle.ke for particle in self )
    
    # Computed Property: energy
    # Description: Returns this galaxies total energy
    # Arguments: N/A
    # Returns: number
    @property
    def energy( self ):
        
        # Return the kinetic energy + potential energy
        return ( self.ke + self.pe )
    
    # Sub: Step
    # Description: Steps the simulation
    # Arguments: deltaTime, How far to step the simulation by
    # Returns: N/A
    def step( self , deltaTime ):
        
        # Calculate the acclerations
        self.__accelerate()
        
        # Calculate the positions
        
        # Calculate the accelerations
        
        # Calculate the velocities
        
    
    # Sub: Accelerate
    # Description: Calculates the accleration of all particles
    # Arguments: N/A
    # Returns: N/A
    def __accelerate( self ):
        
        # For each particle the galaxy
        for particle in self:
            
            # Swap acceleration states
            particle.accleration[ 1 ] = particle.accleration[ 0 ]
            
            # Set the current accleration to 0
            particle.accleration[ 0 ] = 0.0
            
            # Set the galaxies potential energy to 0
            self.pe = 0
            
            # Loop over all combinations of particles
            for p1, p2 in combinations( self , 2 ):
                
                # Calculate the vector
                vector = numpy.subtract( p1.position , p2.position )
                
                # Calculate the distance
                distance = numpy.sqrt( numpy.sum( vector**2 ) )
                
                # Calculate the current acceleration of particle 1
                p1.acceleration[ 0 ] = p1.acceleration[ 0 ] - ( ( p2.mass / ( distance**3 ) ) * vector )
                
                # Calculate the current acceleration of particle 2
                p2.acceleration[ 0 ] = p2.acceleration[ 0 ] + ( ( p1.mass / ( distance**3 ) ) * vector )
                
                # Adjust the galaxies potential energy
                self.pe -= ( ( p1.mass * p2.mass ) / distance )
                
            
        
    
    # Sub: Step Positions
    # Description: Moves the particles
    # Arguments: deltaTime, How far to step the positions by
    # Returns: N/A
    def __step_positions( self , deltaTime ):
        
        # For each particle the galaxy
        for particle in self:
            
            # Chance: This line's order of operations could be wrong, please check the placement of the parens
            particle.position = particle.position + ( particle.velocity * deltaTime ) + ( 0.5 * ( deltaTime**2 ) * particle.acceleration[0] )
                
            
        
    
    # Sub: Step Velocities
    # Description: Calculates the velocity of all particles
    # Arguments: deltaTime, How far to step the velocities by
    # Returns: N/A
    def __step_velocities( self , deltaTime ):
        
        # For each particle in the galaxy
        for particle in self:
            
            particle.velocity = particle.velocity + ( 0.5 * ( particle.accleration[ 0 ] + particle.accleration[ 1 ] ) * deltaTime )
                
            
        
    
