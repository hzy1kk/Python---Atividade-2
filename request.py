import requests

nome = input("Digite o nome ou número do Pokémon: ").strip().lower()

if not nome:
    print("⚠️ Você não informou nenhum Pokémon.")
else:
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

    try:
        resposta = requests.get(url, timeout=10)

        if resposta.status_code == 404:
            print("❌ Pokémon não encontrado. Verifique o nome/número.")
        else:
            resposta.raise_for_status()  # trata outros erros HTTP (500, 403, etc.)

            try:
                dados = resposta.json()
            except ValueError:
                print("❌ Erro: a resposta da API não está em JSON válido.")
            else:
                try:
                    print("Nome:", dados["name"])
                except KeyError:
                    print("❌ Erro: campo 'name' não veio na resposta da API.")

    except requests.exceptions.Timeout:
        print("❌ A requisição demorou demais (timeout). Tente novamente.")
    except requests.exceptions.ConnectionError:
        print("❌ Sem conexão com a internet ou falha de rede.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição HTTP: {e}")