pessoa = {"nome": "João", "idade": 20}

try:
    chave = input("Qual campo quer ver? ").strip()

    if not chave:
        print("⚠️ Você não digitou nenhum campo.")
    else:
        try:
            print(pessoa[chave])
        except KeyError:
            print(f"⚠️ Campo '{chave}' não existe. Opções: {', '.join(pessoa.keys())}")

except EOFError:
    print("⚠️ Nenhuma entrada foi fornecida (EOF).")