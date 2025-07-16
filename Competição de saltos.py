# Lista para armazenar os dados dos atletas
atletas = []

# Coleta de dados de no máximo 5 atletas
for x in range(5):
    nome = input(f"Nome do atleta {x + 1} (ou 'fim' para encerrar): ").strip()
    if nome.lower() == 'fim':
        break  # Encerra a coleta se o usuário digitar 'fim'

    saltos = []  # Lista para armazenar os 5 saltos do atleta

    # Coleta dos 5 saltos
    for x in range(5):
        salto = float(input(f"Salto {x + 1}: "))
        saltos.append(salto)

    # Calcula a média dos saltos
    media = sum(saltos) / 5

    # Armazena os dados do atleta em um dicionário
    atleta = {'nome': nome, 'saltos': saltos, 'media': media}
    atletas.append(atleta)

# Verifica se há atletas cadastrados
if not atletas:
    print("Nenhum atleta cadastrado.")
else:
    # Encontra o melhor atleta comparando as médias manualmente
    melhor = atletas[0]
    for x in atletas:
        if x['media'] > melhor['media']:
            melhor = x

    # Exibe os dados de todos os atletas
    for x in atletas:
        print(f"\nAtleta: {x['nome']}")
        
        # Exibe os saltos separando por " - "
        # Exibe os saltos separando por " - "
print("Saltos:", end=" ")
for i in range(5):
    print(f"{round(x['saltos'][i], 2)}", end="")
    if i < 4:
        print(" - ", end="")
print()  # Quebra de linha após os saltos


        # Exibe a média dos saltos
print(f"Média dos saltos: {round(x['media'], 2)} metros")

    # Exibe o melhor atleta com sua média
print(f"\nMelhor atleta: {melhor['nome']} com média {round(melhor['media'], 2)} metros")
