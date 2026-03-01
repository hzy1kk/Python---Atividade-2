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
                print("⚠️ A quantidade deve ser maior que zero.")
                continue

            return qtd

        except ValueError:
            print("⚠️ Entrada inválida. Digite um número inteiro (ex.: 3).")
        except EOFError:
            print("\n❌ Nenhuma entrada foi fornecida (EOF). Encerrando.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n❌ Operação cancelada pelo usuário (Ctrl+C). Encerrando.")
            sys.exit(1)