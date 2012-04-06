# This is statement is required by the build system to query build info
if __name__ == '__build__':
    raise Exception

# Attempt to load numpy
try:
    from numpy import *
    from numpy.random import *
except ImportError, err:
    print "The display system requires numpy"
    import sys
    sys.exit()
    
import string
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

def display(*args):
    # Set the background color ( random for the debug )
    glClearColor(random_sample(), random_sample(), random_sample(), 0.0)
    
    # Clear the window
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Flush the changes to the buffer
    glFlush()
    
    # Swap the background and foreground buffers
    glutSwapBuffers()
    

def setup_viewport():
    # Set the matrix calculation mode to projection
    glMatrixMode(GL_PROJECTION)
    
    # Create the viewport identity
    glLoadIdentity()
    
    # Set the viewport camera angle
    glOrtho(0.0, 1.0, 0.0, 1.0, 0.0, 1.0)

def main():
    
    # Initilize glut
    glutInit(sys.argv)
    
    # Set the display mode to RGB double buffered
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    
    # Set the inital window size
    glutInitWindowSize(300, 300)
    
    # Create the window
    glutCreateWindow("Galaxy Collision")
    
    # Set the viewport
    setup_viewport()
    
    # Set the idle callback
    glutIdleFunc(display)
    
    # Set the display callback
    glutDisplayFunc(display)
    
    # Run Glut
    glutMainLoop()
    

main()
