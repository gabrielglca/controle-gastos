import pytest
from src.gastos import adicionar_gasto, listar_gastos, total_gastos, remover_gasto
import os

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