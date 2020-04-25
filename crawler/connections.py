"""
    Connections Class for APIClients
"""


class IBGEConnection:
    URL_STATES = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/"
    URL_CITIES = (
        "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios/"
    )

    _connection_error_messages = {
        "connection_error": "Não foi possível estabeler uma conexão com o sistema do IBGE"
    }
