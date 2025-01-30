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

# Exemplo de uso com input
numero_cartao = input("Digite o número do cartão de crédito: ")
bandeira = identificar_bandeira(numero_cartao)
print(f'A bandeira do cartão é: {bandeira}')
