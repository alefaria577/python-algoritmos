"""Verificação de qualidade: todo exercício precisa ter cabeçalho e os próprios testes."""
import ast
from pathlib import Path

import pytest

PASTA_EXERCICIOS = Path(__file__).resolve().parent.parent / "exercicios"
CAMPOS_OBRIGATORIOS = ("Exercise:", "Topic:", "Level:", "Time:", "Space:")
ARQUIVOS = sorted(p for p in PASTA_EXERCICIOS.rglob("*.py") if p.name != "__init__.py")


def test_pasta_de_exercicios_existe():
    assert PASTA_EXERCICIOS.is_dir()


@pytest.mark.parametrize("caminho", ARQUIVOS, ids=lambda p: p.name)
def test_exercicio_tem_cabecalho_e_testes(caminho):
    arvore = ast.parse(caminho.read_text(encoding="utf-8"))
    docstring = ast.get_docstring(arvore) or ""
    faltando = [campo for campo in CAMPOS_OBRIGATORIOS if campo not in docstring]
    assert not faltando, f"{caminho.name}: falta {faltando} no cabeçalho"
    testes = [n for n in arvore.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
    assert testes, f"{caminho.name}: adicione pelo menos uma função test_"
