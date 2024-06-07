def procurar_carro(nome_carro, lista_de_carros):
    for carro in lista_de_carros:
        if carro.lower() == nome_carro.lower():
            return "Carro encontrado!"
    return "Carro não encontrado!"

def avaliacao_carro(preco_carro):
    if preco_carro < 10000:
        return "Mal estado"
    elif preco_carro < 30000:
        return "Conservado"
    elif preco_carro < 60000:
        return "Seminovo"
    else:
        return "Novo"

def main():
    lista_de_carros = ["Gol", "Palio", "Corolla", "Civic", "HB20", "Fiesta", "Uno", "Celta", "Onix", "Fox",
                       "Tucson", "Sandero", "Siena", "Prisma", "Kicks", "HR-V", "Renegade", "Compass", "Creta", "Fusion"]

    while True:
        nome_carro = input("Digite o nome do carro que deseja comprar (ou digite 'fim' para encerrar): ")
        if nome_carro.lower() == "fim":
            break
        
        preco_carro = float(input("Digite o preço que está disposto a pagar pelo carro: "))
        
        print(f"O usuário gostaria de saber se o carro {nome_carro} está disponível e gostaria de pagar {preco_carro} reais nesse carro.")
        
        resultado_procura = procurar_carro(nome_carro, lista_de_carros)
        print(resultado_procura)
        
        resultado_avaliacao = avaliacao_carro(preco_carro)
        print(resultado_avaliacao)
        
        if resultado_procura == "Carro encontrado!":
            qualidade_carro = avaliacao_carro(preco_carro)
            print(f"O usuário gostaria de um carro {nome_carro} na qualidade de {qualidade_carro}. O valor do {nome_carro} é o mesmo recebido na entrada. Já o valor da {qualidade_carro} é recebido através da avaliação do preço.")
        
        continuar = input("Deseja continuar? (sim/não): ")
        if continuar.lower() != "sim":
            break

if __name__ == "__main__":
    main()
