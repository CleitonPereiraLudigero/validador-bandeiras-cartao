# Validador de Bandeiras de Cartão de Crédito em Python

Este é um projeto simples em Python para identificar a bandeira de um cartão de crédito com base no número do cartão. O código verifica os prefixos dos números dos cartões e retorna a bandeira associada, como Visa, MasterCard, American Express, Discover, entre outras.

## Funcionalidades

- Identifica a bandeira do cartão com base nos primeiros dígitos do número do cartão.
- Suporta bandeiras como Visa, MasterCard, American Express, Discover, JCB, Diners Club, Hipercard e outras.
- O código permite que o usuário insira o número do cartão de crédito para validação interativamente.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada.
- Nenhuma dependência externa (somente bibliotecas padrão do Python).

## Como Usar

1. Clone este repositório:
   ```bash
   https://github.com/CleitonPereiraLudigero/validador-bandeiras-cartao.git
   
2. Navegue até o diretório do projeto:
   ```bash
   cd validador-bandeiras-cartao

3. Execute o script Python:
   ```bash
   python validador.py

4. O script pedirá para você digitar o número do cartão de crédito e, em seguida, identificará a bandeira.

## Código Fonte
O código está no arquivo validador.py Aqui está uma visão geral do código:

```bash
def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito com base nos primeiros dígitos do número do cartão.
    
    Args:
    numero_cartao (str): Número do cartão de crédito.
    
    Returns:
    str: Bandeira do cartão de crédito.
    """
    if numero_cartao.startswith(('34', '37')):
        return 'American Express'
    elif numero_cartao.startswith('4'):
        return 'Visa'
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return 'MasterCard'
    elif numero_cartao.startswith('6011') or numero_cartao.startswith(('622126', '622925')) or numero_cartao.startswith(('644', '645', '646', '647', '648', '649')) or numero_cartao.startswith('65'):
        return 'Discover'
    elif numero_cartao.startswith('35'):
        return 'JCB'
    elif numero_cartao.startswith('36') or numero_cartao.startswith('38'):
        return 'Diners Club'
    elif numero_cartao.startswith('60'):
        return 'Hipercard'
    else:
        return 'Bandeira desconhecida'


numero_cartao = input("Digite o número do cartão de crédito: ")
bandeira = identificar_bandeira(numero_cartao)
print(f'A bandeira do cartão é: {bandeira}')
```

## Como o código funciona:
1. A função identificar_bandeira(numero_cartao) recebe o número do cartão como argumento.
2. Ela verifica os primeiros dígitos do número para identificar a bandeira.
3. Retorna a bandeira correspondente (ou "Bandeira desconhecida" se não for encontrada).
4. O usuário insere o número do cartão, e o código imprime a bandeira identificada.

## Autor
Feito por Cleiton Pereira Ludigero - c.ludigero@gmail.com



