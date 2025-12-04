import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random

from geracao_eventos import gerar_evento_raro
from estrelas import Estrela, desenharEstrela, atualizar_brilho

estrelas = []

num_eventos = {
    "COMUM": 0,
    "GIGANTE": 0,
    "SUPERMASSIVA": 0,
    "SUPERNOVA": 0
}

# Fundo galáctico: criando várias estrelas aleatórias
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

    gl.glEnd()

# Desenhando o quadradinho com o contador
def desenharContador():
    
    tamanho = 0.15
    padding = 0.02

    left, right, bottom, top = ortho_vals

    x0 = left + padding
    y0 = bottom + padding
    x1 = x0 + tamanho
    y1 = y0 + tamanho

    gl.glBegin(gl.GL_QUADS)
    gl.glColor4f(0.0, 0.0, 0.0, 0.5)
    gl.glVertex2f(x0, y0)
    gl.glVertex2f(x1, y0)
    gl.glVertex2f(x1, y1)
    gl.glVertex2f(x0, y1)
    gl.glEnd()

    gl.glColor3f(1.0, 1.0, 1.0)
    gl.glRasterPos2f(x0 + 0.02, y0 + 0.05)

    texto = f"COMUM: {num_eventos['COMUM']}\nGIGANTE: {num_eventos['GIGANTE']}\nSUPERMASSIVA: {num_eventos['SUPERMASSIVA']}\nSUPERNOVA: {num_eventos['SUPERNOVA']}"

    linhas = texto.split("\n")
    for i, linha in enumerate(linhas):
        gl.glRasterPos2f(x0 + 0.02, y0 + 0.05 + i*0.03)
        for c in linha:
            glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_12, ord(c))

# Fazendo o display de tudo na tela
def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glLoadIdentity()

    desenharFundoGalaxia()

    for e in estrelas:
        desenharEstrela(e)

    desenharContador()

    gl.glColor3f(1, 1, 1)
    glut.glutSwapBuffers()


def interacoes(key, x, y):
    global estrelas

    # Tecla N para criar estrela
    if key == b'n':
        evento = gerar_evento_raro()
        num_eventos[evento] += 1

        if evento == "COMUM":
            cor = [1.0, 1.0, 0.9]
            raio = random.uniform(0.0007, 0.002)

        elif evento == "GIGANTE":
            cor = [0.75, 0.85, 1.0]
            raio = random.uniform(0.02, 0.035)

        elif evento == "SUPERMASSIVA":
            cor = [1.0, 0.4, 0.1]
            raio = random.uniform(0.040, 0.055)

        elif evento == "SUPERNOVA":
            cor = [1.0, 1.0, 0.2]
            raio = random.uniform(0.060, 0.080)

        left, right, bottom, top = ortho_vals
        pos_x = random.uniform(left, right)
        pos_y = random.uniform(bottom, top)

        nova = Estrela(pos_x, pos_y, cor, raio)
        estrelas.append(nova)

        glut.glutPostRedisplay()

    # Tecla ESC para sair do programa
    elif key  == b'\x1b':
        glut.glutLeaveMainLoop()

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

glut.glutCreateWindow(b'Geracao procedural de eventos astronomicos')

glut.glutFullScreen()

gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
glut.glutIdleFunc(lambda: (atualizar_brilho(estrelas), glut.glutPostRedisplay()))
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(interacoes)
glut.glutReshapeFunc(reshape)

glut.glutMainLoop()
