def validar_cep(cep):
    if not cep:
        raise ValueError("CEP é obrigatório")

    if not cep.isdigit():
        raise ValueError("CEP deve conter apenas números")

    if len(cep) != 8:
        raise ValueError("CEP deve conter exatamente 8 dígitos")

    return cep
