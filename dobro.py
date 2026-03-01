def dobro(x):
    return float(x) * 2

while True:
    valor = input("Digite um número: ").strip()
    if valor == "":
        print("Você não digitou nada. Tente de novo.")
        continue

    try:
        print(dobro(valor))
        break
    except ValueError:
        print("Entrada inválida: digite um número (ex.: 10, 3.5).")