preco = float(input("Preço do produto: "))
imposto = 1.1
print("Preço com imposto:", preco * imposto)

try:
    texto = input("Preço do produto: ").strip().replace(",", ".")
    preco = float(texto)

    if preco < 0:
        raise ValueError("Preço negativo não permitido.")

    imposto = 1.1
    print("Preço com imposto:", preco * imposto)
except ValueError:
    print("Preço inválido. Digite um valor numérico maior ou igual a zero.")
except EOFError:
    print("Nenhuma entrada foi fornecida.")