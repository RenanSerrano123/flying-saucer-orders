def obter_planeta(codigo):
    planetas = {80: "Marte",81: "Saturno",90: "Netuno",91: "HD21749b"}
    return planetas.get(codigo, "Desconhecido")
def obter_modelo(codigo):
    modelos = {60: "A6000",61: "B7500",62: "C9000"}
    return modelos.get(codigo, "Desconhecido")
def main():
        numero = input()
        if len(numero) == 6 and numero.isdigit():
            origem_codigo = int(numero[:2])
            destino_codigo = int(numero[2:4])
            modelo_codigo = int(numero[4:])
            origem = obter_planeta(origem_codigo)
            destino = obter_planeta(destino_codigo)
            modelo = obter_modelo(modelo_codigo)
            print(f"{origem}")
            print(f"{destino}")
            print(f"{modelo}")
        else:
            print("Número inválido. Digite um número de 6 dígitos.")
main()