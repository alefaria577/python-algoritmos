# Python 🐍

![tests](https://github.com/alefaria577/exercicios-python-e-algoritmos/actions/workflows/testes.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)

## Descrição do Projeto 📝

Repositório com os exercícios que resolvi em Python na minha preparação para entrevistas técnicas de Software Development Engineer. São **mais de 90 exercícios**, do básico da linguagem até estruturas de dados, algoritmos, orientação a objetos e SQL, organizados por módulo.

Cada exercício é um arquivo independente (`exercicios/modulo-XX-tema/ex_X_Y_Z_titulo.py`) com:
- **Cabeçalho** com o tópico, o nível (Easy ou Medium) e a complexidade de tempo e de espaço (Big O);
- **A solução**;
- **Testes automatizados** com casos normais e casos de borda (lista vazia, valores repetidos, números negativos…).

A cada `git push`, o GitHub Actions roda todos os testes e uma verificação de qualidade que garante que nenhum exercício está sem documentação ou sem testes.

| Módulo | Pasta | Tópicos |
|---|---|---|
| 0 | `modulo-00-primeiros-passos` | primeiro exercício para treinar o ciclo criar → testar → enviar |
| 1 | `modulo-01-fundamentos-python` | tipos, operadores, condições, laços, funções e exceções |
| 2 | `modulo-02-estruturas-nativas` | listas e fatias, strings, dicionários, sets, `collections` e `heapq` |
| 3 | `modulo-03-resolver-problemas` | Big O e o método de resolução em 6 passos |
| 4 | `modulo-04-padroes-arrays-strings` | hashing, dois ponteiros, janela deslizante, ordenação, guloso e somas de prefixo |
| 5 | `modulo-05-pilhas-filas-listas-busca` | pilha, fila, pilha monotônica, lista ligada e busca binária |
| 6 | `modulo-06-arvores-grafos-heaps` | árvores binárias, BST, BFS, DFS, grafos em grade e heaps |
| 7 | `modulo-07-recursao-programacao-dinamica` | recursão, memoization, tabulação, programação dinâmica e backtracking |
| 8 | `modulo-08-orientacao-objetos-codigo-limpo` | classes, herança, polimorfismo, `dataclass` e refatoração |
| 10 | `modulo-10-sql-e-fundamentos` | SQL (`WHERE`, `ORDER BY`, `JOIN`, `GROUP BY`, `HAVING`) com SQLite |
| 11 | `modulo-11-simulados` | simulados de entrevista cronometrados |

## Componentes Utilizados 🛠️

- **Python 3.12** para as soluções
- **pytest** para os testes automatizados
- **SQLite** (`sqlite3`, já incluído no Python) para os exercícios de SQL
- **GitHub Actions** para rodar os testes a cada push (integração contínua)

## Como acessar

1. Instale o **Python 3.12+** (python.org, marcando *Add Python to PATH*) e o **Git** (git-scm.com).
2. Baixe o projeto e entre na pasta:

```bash
git clone https://github.com/alefaria577/exercicios-python-e-algoritmos.git
cd exercicios-python-e-algoritmos
```

3. Crie o ambiente virtual e instale as dependências:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

4. Rode todos os testes, ou só os de um exercício:

```bash
python -m pytest
python -m pytest exercicios/modulo-04-padroes-arrays-strings
```

Para ler uma solução, abra qualquer arquivo dentro de `exercicios/` no VS Code ou direto no GitHub.

---

**Autor:** Alexandre Silva de Faria — Engenharia de Software, FIAP · [LinkedIn](https://linkedin.com/in/alexandrefariadev)
