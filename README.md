# 💰 Controle de Gastos Pessoais

![CI](https://github.com/gabrielglca/controle-gastos/actions/workflows/ci.yml/badge.svg)

## 📋 Descrição do Problema

Muitas pessoas têm dificuldade em acompanhar seus gastos do dia a dia, o que leva a decisões financeiras ruins, dívidas e falta de controle do orçamento pessoal. Esse problema afeta especialmente jovens e pessoas de baixa renda que não têm acesso a ferramentas financeiras complexas.

## 💡 Proposta da Solução

Uma aplicação simples via linha de comando (CLI) que permite registrar, listar, calcular e remover gastos pessoais de forma rápida e sem complicação, ajudando o usuário a ter consciência de para onde vai o seu dinheiro.

## 👥 Público-Alvo

Qualquer pessoa que queira organizar seus gastos pessoais de forma simples, sem precisar de aplicativos complexos ou internet.

## ✅ Funcionalidades

- Adicionar gasto com descrição, valor e categoria
- Listar todos os gastos registrados
- Ver o total gasto
- Remover um gasto pelo número
- Armazenamento automático em arquivo JSON

## 🛠️ Tecnologias Utilizadas

- Python 3.8+
- pytest (testes automatizados)
- ruff (análise estática de código)
- GitHub Actions (integração contínua)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/gabrielglca/controle-gastos.git
cd controle-gastos
```

2. Instale as dependências:
```bash
pip install pytest ruff
```

## ▶️ Como Executar

```bash
python -m src.gastos
```

## 🧪 Como Rodar os Testes

```bash
pytest tests/
```

## 🔍 Como Rodar o Lint

```bash
ruff check src/ tests/
```

## 📦 Versão Atual

1.0.0

## 👤 Autor

Gabriel Lucas Carvalho de Andrade  
Disciplina: Bootcamp2  
Repositório: https://github.com/gabrielglca/controle-gastos