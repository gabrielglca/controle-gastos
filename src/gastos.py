import json
import os

ARQUIVO = "gastos.json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w") as f:
        json.dump(gastos, f, indent=2)


def adicionar_gasto(descricao, valor, categoria):
    if not descricao or not descricao.strip():
        raise ValueError("Descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero.")
    gastos = carregar_gastos()
    gasto = {"descricao": descricao, "valor": valor, "categoria": categoria}
    gastos.append(gasto)
    salvar_gastos(gastos)
    return gasto


def listar_gastos():
    return carregar_gastos()


def total_gastos():
    return sum(g["valor"] for g in carregar_gastos())


def remover_gasto(indice):
    gastos = carregar_gastos()
    if indice < 0 or indice >= len(gastos):
        raise IndexError("Índice inválido.")
    removido = gastos.pop(indice)
    salvar_gastos(gastos)
    return removido


def main():
    while True:
        print("\n===== Controle de Gastos =====")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Ver total")
        print("4. Remover gasto")
        print("5. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            desc = input("Descrição: ")
            try:
                valor = float(input("Valor (R$): "))
                cat = input("Categoria: ")
                g = adicionar_gasto(desc, valor, cat)
                print(f"✅ Gasto '{g['descricao']}' de R${g['valor']:.2f} adicionado!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif opcao == "2":
            gastos = listar_gastos()
            if not gastos:
                print("Nenhum gasto registrado.")
            for i, g in enumerate(gastos):
                print(f"{i}. [{g['categoria']}] {g['descricao']} — R${g['valor']:.2f}")

        elif opcao == "3":
            print(f"💰 Total de gastos: R${total_gastos():.2f}")

        elif opcao == "4":
            try:
                idx = int(input("Número do gasto para remover: "))
                g = remover_gasto(idx)
                print(f"🗑️ '{g['descricao']}' removido.")
            except (ValueError, IndexError) as e:
                print(f"❌ Erro: {e}")

        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()