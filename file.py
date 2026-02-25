nome_arquivo = input("Arquivo: ").strip()

if not nome_arquivo:
    print("Você não informou nenhum arquivo.")
else:
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            print(f.read())

    except FileNotFoundError:
        print("Erro: arquivo não encontrado. Verifique o nome/caminho.")
    except IsADirectoryError:
        print("Erro: o caminho informado é um diretório, não um arquivo.")
    except PermissionError:
        print("Erro: sem permissão para ler esse arquivo.")
    except UnicodeDecodeError:
        print("Erro: não foi possível ler o arquivo como UTF-8 (encoding diferente).")
    except OSError as e:
        print(f"Erro do sistema ao abrir/ler o arquivo: {e}")