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
day = [0.529, 0.808, 0.922, 0]
night = [0.05, 0.05, 0.2, 0]
background_color = day

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
    gl.glClearColor(*background_color)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_LINE_STRIP)
    for e in estrelas:
        gl.glVertex2f(e.x, e.y)
    gl.glEnd()
    for e in estrelas:
        desenharEstrela(e)
    gl.glColor3f(1, 1, 1)
    glut.glutSwapBuffers()

def interacoes(key, x, y):
    global estrelas
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
        global dark_mode, background_color
        dark_mode = not dark_mode
        if dark_mode:
            background_color = night
        else:
            background_color = day
    glut.glutPostRedisplay()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutCreateWindow(b'Parte 6 - A Constelacao dos Guardioes')
glut.glutReshapeWindow(720, 720)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(interacoes)
glut.glutMainLoop()
