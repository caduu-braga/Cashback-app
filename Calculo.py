
def calculadora_de_cashback(valor_inicial, desconto, vip):
    valor_final = valor_inicial * (1 - desconto / 100)

    valor_casback = valor_final * 0.05

    if vip == True:
        valor_casback += valor_casback * 0.10
    if valor_final > 500:
        valor_casback = valor_casback * 2

    return round(valor_casback, 2)

    