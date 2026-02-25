import sys

def ler_int_positivo(prompt: str) -> int:
    while True:
        try:
            texto = input(prompt).strip()

            if not texto:
                print("⚠️ Você precisa digitar um número inteiro.")
                continue

            qtd = int(texto)

            if qtd <= 0:
                print("⚠️ A quantidade de notas deve ser maior que zero.")
                continue

            return qtd

        except ValueError:
            print("⚠️ Entrada inválida. Digite um número inteiro (ex.: 3).")
        except EOFError:
            print("\n❌ Nenhuma entrada foi fornecida (EOF). Encerrando.")
            sys.exit(1)


def ler_float(prompt: str) -> float:
    while True:
        try:
            texto = input(prompt).strip()

            if not texto:
                print("⚠️ Você precisa digitar um número.")
                continue

            # Aceita tanto vírgula quanto ponto
            texto = texto.replace(",", ".")
            return float(texto)

        except ValueError:
            print("⚠️ Entrada inválida. Digite um número (ex.: 7.5 ou 7,5).")
        except EOFError:
            print("\n❌ Nenhuma entrada foi fornecida (EOF). Encerrando.")
            sys.exit(1)


def main():
    qtd = ler_int_positivo("Quantas notas? ")

    soma = 0.0
    for i in range(1, qtd + 1):
        nota = ler_float(f"Nota {i}: ")
        soma += nota

    # Aqui qtd é garantido > 0, então não há divisão por zero
    media = soma / qtd
    print("Média:", media)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⛔ Interrompido pelo usuário (Ctrl+C).")
        sys.exit(1)