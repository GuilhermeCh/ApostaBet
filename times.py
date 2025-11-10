import random

# --- Escolha dos times de forma aleátória ---
def escolhe_time():
    times = ["São Paulo", "Palmeiras", "Santos", "Bragantino","Corinthians", "Flamengo", "Vasco", "Fluminense", "Botafogo", "Gremio", "Internacional","Bahia", "Fortaleza", "Cruzeiro", "Atlético Mineiro"]
    
    time_escolhido1 = random.randint(0, 14)
    time_escolhido2 = random.randint(0, 14)
    
    while time_escolhido1 == time_escolhido2:
        time_escolhido2 = random.randint(0, len(times) - 1)
    
    return times[time_escolhido1], times[time_escolhido2]

# --- Escolha dos resultados de forma aleátória ---
def define_resultado():
    resultado_time1 = random.randint(0, 5)
    resultado_time2 = random.randint(0, 5)

    return resultado_time1, resultado_time2