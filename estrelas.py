import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math
import random

class Estrela():
    def __init__(self, x, y, cor, raio):
        self.x = x
        self.y = y
        self.cor = cor
        self.raio = raio

        # parâmetros que alteram a intensidade do brilho
        self.phase = random.uniform(0, 1000)
        self.speed = random.uniform(0.3, 1.3)
        self.intensidade = random.uniform(0.85, 1.0)
        self.brilho = 1.0

def atualizar_brilho(estrelas):
    tempo = glut.glutGet(glut.GLUT_ELAPSED_TIME) / 1000.0

    for e in estrelas:
        if not hasattr(e, "brilho"):
            e.brilho = 1.0

        pulsar = 0.20 * math.sin(tempo * (3.0 + e.raio * 40))
        e.brilho = max(0.3, 1.0 + pulsar)

def desenharEstrela(e):
    r, g, b = e.cor
    brilho = getattr(e, "brilho", 1.0)

    # ESTRELA COMUM
    if e.raio <= 0.002:
        gl.glBegin(gl.GL_POLYGON)
        gl.glColor4f(r * brilho, g * brilho, b * brilho, brilho)
        for i in range(30):
            ang = 2 * math.pi * i / 30
            gl.glVertex2f(e.x + math.cos(ang) * e.raio,
                          e.y + math.sin(ang) * e.raio)
        gl.glEnd()
        return

    # GIGANTE AZUL
    if 0.02 <= e.raio <= 0.036:
        steps = 50
        # camada externa branca
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 1.0 * brilho, 1.0 * brilho, 0.12 * brilho)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(1.0 * brilho, 1.0 * brilho, 1.0 * brilho, 0.0)
        for i in range(steps+1):
            ang = 2*math.pi * i/steps
            gl.glVertex2f(e.x + math.cos(ang)*(e.raio*3.2),
                          e.y + math.sin(ang)*(e.raio*3.2))
        gl.glEnd()

        # camada média azulada
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(0.6 * brilho, 0.75 * brilho, 1.0 * brilho, 0.30 * brilho)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(0.6 * brilho, 0.75 * brilho, 1.0 * brilho, 0.0)
        for i in range(steps+1):
            ang = 2*math.pi * i/steps
            gl.glVertex2f(e.x + math.cos(ang)*(e.raio*2.1),
                          e.y + math.sin(ang)*(e.raio*2.1))
        gl.glEnd()

        # núcleo azul
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(0.25 * brilho, 0.45 * brilho, 1.0 * brilho, 0.95)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(0.25 * brilho, 0.45 * brilho, 1.0 * brilho, 0.0)
        for i in range(steps+1):
            ang = 2*math.pi * i/steps
            gl.glVertex2f(e.x + math.cos(ang)*(e.raio),
                          e.y + math.sin(ang)*(e.raio))
        gl.glEnd()

        # centro branco
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 1.0 * brilho, 1.0 * brilho, 1.0 * brilho)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(1.0 * brilho, 1.0 * brilho, 1.0 * brilho, 0.0)
        for i in range(20):
            ang = 2 * math.pi * i / 20
            gl.glVertex2f(e.x + math.cos(ang)*(e.raio*0.45),
                          e.y + math.sin(ang)*(e.raio*0.45))
        gl.glEnd()
        return

    # SUPERMASSIVA
    if 0.040 <= e.raio <= 0.055:
        steps = 70
        tempo = glut.glutGet(glut.GLUT_ELAPSED_TIME) / 500.0
        pulsar = 1.0 + 0.06 * math.sin(tempo * 1.7)

        # camada externa
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 0.75 * brilho, 0.35 * brilho, 0.10 * brilho)
        gl.glVertex2f(e.x, e.y)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            raioExt = e.raio * (3.2 * pulsar)
            gl.glColor4f(1.0, 0.75, 0.35, 0.0)
            gl.glVertex2f(e.x + math.cos(ang) * raioExt,
                          e.y + math.sin(ang) * raioExt)
        gl.glEnd()

        # camada média
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 0.65 * brilho, 0.20 * brilho, 0.35 * brilho)
        gl.glVertex2f(e.x, e.y)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            raioMedio = e.raio * (2.3 + 0.12 * math.sin(tempo * 2.3 + i))
            gl.glColor4f(1.0, 0.65, 0.20, 0.0)
            gl.glVertex2f(e.x + math.cos(ang) * raioMedio,
                          e.y + math.sin(ang) * raioMedio)
        gl.glEnd()
        
        # camada interna
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 0.50 * brilho, 0.10 * brilho, 0.75 * brilho)
        gl.glVertex2f(e.x, e.y)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            raioQ = e.raio * 1.4
            gl.glColor4f(1.0, 0.50, 0.10, 0.0)
            gl.glVertex2f(e.x + math.cos(ang) * raioQ,
                          e.y + math.sin(ang) * raioQ)
        gl.glEnd()

        # núcleo
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 1.0 * brilho, 1.0 * brilho, 0.9 * brilho)
        gl.glVertex2f(e.x, e.y)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            raioCore = e.raio * 0.55
            gl.glColor4f(1.0, 1.0, 1.0, 0.0)
            gl.glVertex2f(e.x + math.cos(ang) * raioCore,
                          e.y + math.sin(ang) * raioCore)
        gl.glEnd()
        gl.glColor4f(1,1,1,1)
        return

    # SUPERNOVA
    if 0.060 <= e.raio <= 0.080:
        if not hasattr(e, "boomTime"):
            e.boomTime = glut.glutGet(glut.GLUT_ELAPSED_TIME)

        tempo = (glut.glutGet(glut.GLUT_ELAPSED_TIME) - e.boomTime) / 350.0
        steps = 70

        # desaparece depois de 4.0s
        if tempo > 4.0:
            e.raio = 0
            return

        explosao = 1.0 + tempo * 0.55
        fade = max(0.10, 1.0 - tempo * 0.45)

        # anel externo
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 0.7 * brilho, 0.3 * brilho, 0.18 * fade)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(1.0, 0.5, 0.2, 0.0)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            radius = e.raio * explosao * (4.0 + 0.2 * math.sin(i + tempo * 5))
            gl.glVertex2f(e.x + math.cos(ang) * radius,
                          e.y + math.sin(ang) * radius)
        gl.glEnd()

        # gases ionizados
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0 * brilho, 0.4 * brilho, 0.15 * brilho, 0.30 * fade)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(1.0, 0.2, 0.05, 0.0)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            radius = e.raio * explosao * (2.4 + 0.25 * math.sin(i * 1.5 + tempo * 4))
            gl.glVertex2f(e.x + math.cos(ang) * radius,
                          e.y + math.sin(ang) * radius)
        gl.glEnd()

        # turbulência
        gl.glBegin(gl.GL_POINTS)
        for i in range(30):
            ang = (i * 12.17 + tempo * 5)
            radius = e.raio * explosao * (1.6 + math.sin(i * 7 + tempo * 10)*0.4)
            brilho_var = max(0, fade * (0.7 + math.sin(i + tempo) * 0.3))
            gl.glColor4f(1.0, 0.8, 0.4, brilho_var)
            gl.glVertex2f(e.x + math.cos(ang) * radius,
                          e.y + math.sin(ang) * radius)
        gl.glEnd()

        # núcleo final
        core_size = e.raio * max(0.3, 1.0 - tempo * 0.4)
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor4f(1.0, 1.0, 1.0, 0.9 * fade)
        gl.glVertex2f(e.x, e.y)
        gl.glColor4f(1.0, 1.0, 1.0, 0.0)
        for i in range(steps+1):
            ang = 2 * math.pi * i / steps
            gl.glVertex2f(e.x + math.cos(ang) * core_size,
                          e.y + math.sin(ang) * core_size)
        gl.glEnd()
        return
