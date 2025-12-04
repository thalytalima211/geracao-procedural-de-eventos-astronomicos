import random

# Probabilidades 
P_GIGANTE = 0.009       # Gigante Azul - 0,9%
P_SUPERMASSIVA = 0.005  # Estrela supermassiva - 0,5%
P_SUPERNOVA = 0.0003    # Supernova - 0,03%

def gerar_evento_raro():
    r = random.random()  # valor ∈ [0,1] para a geração procedural

    if r <= P_SUPERNOVA:
        return "SUPERNOVA"
    elif r <= P_SUPERMASSIVA:
        return "SUPERMASSIVA"
    elif r <= P_GIGANTE:
        return "GIGANTE"
    else:
        return "COMUM"
