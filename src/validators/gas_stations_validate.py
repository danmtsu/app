def validate_gas_station(data):
    errors = []
    
    # Verifica se os campos obrigatórios estão presentes e são strings
    mandatory_fields = ['name', 'address', 'city', 'state']
    for field in mandatory_fields:
        if field not in data or not data[field]:
            errors.append(f"O campo '{field}' é obrigatório.")
        elif not isinstance(data[field], str):
            errors.append(f"O campo '{field}' deve ser preenchido com uma string.")

    # Verifica se os campos de preço são floats positivos (se estiverem presentes)
    optional_float_fields = ['preco_etanol', 'preco_gasolina', 'preco_diesel']
    for field in optional_float_fields:
        if field in data:
            if not isinstance(data[field], float) or data[field] <= 0:
                errors.append(f"O campo '{field}' deve ser um número float positivo.")

    return errors
