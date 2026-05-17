from unittest.mock import patch
import pytest
import os
from src.gastos import adicionar_gasto, listar_gastos, total_gastos, remover_gasto
from src.services import buscar_cotacao

# Limpa o arquivo antes de cada teste
@pytest.fixture(autouse=True)
def limpar():
    if os.path.exists("gastos.json"):
        os.remove("gastos.json")
    yield
    if os.path.exists("gastos.json"):
        os.remove("gastos.json")


def test_adicionar_gasto_valido():
    g = adicionar_gasto("Almoço", 25.50, "Alimentação")
    assert g["descricao"] == "Almoço"
    assert g["valor"] == 25.50


def test_valor_negativo_invalido():
    with pytest.raises(ValueError):
        adicionar_gasto("Teste", -10, "Outros")


def test_descricao_vazia_invalida():
    with pytest.raises(ValueError):
        adicionar_gasto("", 10, "Outros")


def test_total_gastos():
    adicionar_gasto("A", 10, "X")
    adicionar_gasto("B", 20, "Y")
    assert total_gastos() == 30


def test_remover_gasto():
    adicionar_gasto("Uber", 15, "Transporte")
    remover_gasto(0)
    assert listar_gastos() == []


def test_remover_indice_invalido():
    with pytest.raises(IndexError):
        remover_gasto(99)


def test_buscar_cotacao_sucesso():
    mock_data = {
        "USDBRL": {"bid": "5.05"},
        "EURBRL": {"bid": "5.90"}
    }
    with patch("src.services.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_data
        resultado = buscar_cotacao()
        assert resultado["dolar"] == 5.05
        assert resultado["euro"] == 5.90


def test_buscar_cotacao_erro():
    with patch("src.services.requests.get") as mock_get:
        mock_get.side_effect = Exception("Erro de conexão")
        resultado = buscar_cotacao()
        assert resultado["dolar"] is None
        assert resultado["euro"] is None