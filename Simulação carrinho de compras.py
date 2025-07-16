catalogo = {
    "001": {"nome": "Arroz 1kg", "preco": 5.50},
    "002": {"nome": "Feijão 1kg", "preco": 8.00},
    "003": {"nome": "Leite Litro", "preco": 4.25},
    "004": {"nome": "Pão de Forma", "preco": 6.75}
}
total_compra = 0.0
carrinho = []
print (catalogo)
while True:
    produto = input('Digite o código do seu produto (ou "fim" para encerrar): ').strip().lower()
    if produto == 'fim':
        break
    if produto not in catalogo:
        print('Produto não esta no catalogo')
    else:
        print('Produto adicionado ao carrinho', catalogo[produto]['nome'])
        carrinho.append(catalogo[produto])
print('--- CUPOM FISCAL ---')

for produto in carrinho:
    total_compra += produto['preco']
    print(f"{produto['nome']} - R$ {produto['preco']:.2f}")
print(f"Total: R$ {total_compra:.2f}")
print(total_compra)
