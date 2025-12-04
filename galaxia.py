import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random
import math

class Estrela():
   def __init__(self, x, y, cor, raio):
      self.x = x
      self.y = y
      self.cor = cor
      self.raio = raio

estrelas = [
   Estrela(-0.6, 0.7, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
   Estrela(-0.4, 0.3, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
   Estrela(-0.1, 0.0, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
   Estrela(0.3, -0.3, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
   Estrela(-0.2, -0.5, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
   Estrela(-0.7, 0, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
   Estrela(0.1, 0.2, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)),
]

estrelas_originais = estrelas.copy()
dark_mode = False

# Fundo galáctico: criando várias estrelas aleatórias
NUM_ESTRELAS_FUNDO = 120
estrelas_fundo = [(random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)) for _ in range(NUM_ESTRELAS_FUNDO)]

def desenharFundoGalaxia():
    left, right, bottom, top = ortho_vals
    
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0.1, 0.0, 0.2)
    gl.glVertex2f(left, top)
    gl.glVertex2f(right, top)
    gl.glColor3f(0.0, 0.0, 0.0)
    gl.glVertex2f(right, bottom)
    gl.glVertex2f(left, bottom)
    gl.glEnd()

    gl.glPointSize(2)
    gl.glBegin(gl.GL_POINTS)
    gl.glColor3f(1.0, 1.0, 1.0)

    for (x, y) in estrelas_fundo:
        gl.glVertex2f(x * (right-left)/2, y * (top-bottom)/2)

    gl.glEnd()

def desenharEstrela(e):
    if dark_mode:
        gl.glColor3f(1.0, 1.0, 0.6)
    else:
        gl.glColor3f(*e.cor)
    gl.glBegin(gl.GL_POLYGON)
    for i in range(30):
        ang = 2 * math.pi * i / 30
        dx = math.cos(ang) * e.raio
        dy = math.sin(ang) * e.raio
        gl.glVertex2f(e.x + dx, e.y + dy)
    gl.glEnd()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glLoadIdentity()

    desenharFundoGalaxia()

    gl.glBegin(gl.GL_LINE_STRIP)
    for e in estrelas:
        gl.glVertex2f(e.x, e.y)
    gl.glEnd()

    for e in estrelas:
        desenharEstrela(e)

    gl.glColor3f(1, 1, 1)
    glut.glutSwapBuffers()

def interacoes(key, x, y):
    global estrelas, dark_mode
    if key == b'n':
        pos_x, pos_y = [random.uniform(-1, 1) for _ in range(2)]
        estrelas.append(Estrela(pos_x, pos_y, [random.uniform(0, 1) for _ in range(3)], random.uniform(0.01, 0.05)))
    elif key == b'x' and len(estrelas) > 0:
        index = random.randint(0, len(estrelas) - 1)
        estrelas.pop(index)
    elif key == b'r':
        global estrelas_originais
        estrelas = estrelas_originais.copy()
    elif key == b't':
        dark_mode = not dark_mode

    glut.glutPostRedisplay()

def reshape(width, height):
    global ortho_vals

    gl.glViewport(0, 0, width, height)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    aspect = width / height

    if aspect >= 1:
        left = -1.2 * aspect
        right = 1.2 * aspect
        bottom = -1.2
        top = 1.2
    else:
        left = -1.2
        right = 1.2
        bottom = -1.2 / aspect
        top = 1.2 / aspect

    ortho_vals = (left, right, bottom, top)

    gl.glOrtho(left, right, bottom, top, -1, 1)

    gl.glMatrixMode(gl.GL_MODELVIEW)

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)

glut.glutCreateWindow(b'Parte 6 - A Constelacao dos Guardioes')

glut.glutReshapeWindow(720, 720)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(interacoes)
glut.glutReshapeFunc(reshape)

glut.glutMainLoop()
