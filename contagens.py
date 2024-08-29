import time

def contagem_regressiva():
    try:
        temporizador = int(input("Digite o tempo da regressão:"))

        while temporizador > 0:

            minutos,segundos = divmod(temporizador, 60)
            formato = f"{minutos:02d}:{segundos:02d}"
            print(formato, end="\r")
            time.sleep(1)
            temporizador -= 1
        print(" Feliz Natal!!")    
    except ValueError:
        print("Número inválido")        
contagem_regressiva()