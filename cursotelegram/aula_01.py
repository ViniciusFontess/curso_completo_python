for i in range(5): #i começa em 0 automaticamente
    print(i)

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for i in range(len(produtos)):
    print('{} unidades produzidas de {}'.format(producao[i], produtos[i]))

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
texto = 'lira@gmail.com'

for item in produtos:
    print(item)

for produto in produtos:
    print('O produto é {}' .format(produto))

for ch in texto:
    print(ch)    