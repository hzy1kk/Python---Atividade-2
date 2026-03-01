try:
    texto = input("Preço do produto: ").strip().replace(",", ".")
    preco = float(texto)

    if preco < 0:
        raise ValueError("Preço negativo não permitido.")

    imposto = 1.1
    print("Preço com imposto:", preco * imposto)

except ValueError as e:
    # pega tanto erro de conversão quanto o nosso erro de negativo
    print(f"Preço inválido: {e}. Digite um valor numérico maior ou igual a zero.")

except EOFError:
    print("Nenhuma entrada foi fornecida.")