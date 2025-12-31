import requests

def consultar_cep(cep: str) -> dict:
    """
    Recebe um CEP (string com 8 dígitos) e retorna um dicionário
    com os dados do endereço ou uma mensagem de erro.
    """

    # Validação básica
    if not cep or not cep.isdigit() or len(cep) != 8:
        return {"erro": "CEP inválido. Deve conter 8 dígitos numéricos."}

    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return {"erro": "Erro ao acessar a API do ViaCEP."}

    dados = resposta.json()

    if "erro" in dados:
        return {"erro": "CEP não encontrado."}

    return dados
