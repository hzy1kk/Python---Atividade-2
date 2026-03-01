nomes = ["Arthur", "Gabriel", "Enzo", "Julia"]

try:
    texto = input(f"Indique um número de 0 a {len(nomes)-1} para sortear uma pessoa: ").strip()
    i = int(texto)

    print("Nome:", nomes[i])

except ValueError:
    print("⚠️ Entrada inválida. Digite um número inteiro (ex.: 0, 1, 2, 3).")
except IndexError:
    print(f"⚠️ Índice fora do intervalo. Use um número entre 0 e {len(nomes)-1}.")
except EOFError:
    print("⚠️ Nenhuma entrada foi fornecida (EOF).")