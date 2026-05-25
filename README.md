# Estrutura de Dados — Pilha Dinâmica (LIFO)

Este repositório apresenta a implementação manual de uma **Pilha (Last In, First Out)** em Python, sem utilização de bibliotecas externas. O arquivo principal já possui uma suíte de testes integrada, validando tanto operações comuns quanto situações de erro previstas durante o uso da estrutura.

---

# Como Executar

## Pré-requisitos

Certifique-se de possuir o Python 3.x instalado em sua máquina.  
Para verificar, execute no terminal:

```bash
python --version
```

## Executando o Programa

Acesse a pasta do projeto e rode:

```bash
python pilha_dinamica.py
```

Ao executar, o programa exibirá quatro blocos de teste numerados, demonstrando o funcionamento correto da pilha em diferentes cenários.

---

# Estrutura da Classe `PilhaDinamica`

| Método | Descrição |
|---|---|
| `__init__(capacidade)` | Inicializa a pilha. `capacidade=None` define pilha sem limite. |
| `empilhar(elemento)` | Adiciona um elemento ao topo da pilha. |
| `desempilhar()` | Remove e retorna o elemento do topo (ordem LIFO). |
| `topo()` | Consulta o elemento do topo sem removê-lo. |
| `esta_vazia()` | Retorna `True` caso a pilha esteja vazia. |
| `esta_cheia()` | Retorna `True` quando a capacidade máxima for atingida. |
| `quantidade()` | Retorna o total atual de elementos armazenados. |
| `limpar()` | Remove todos os elementos da pilha. |

---

# Cenários de Teste

O bloco `if __name__ == "__main__"` contempla os seguintes casos:

## Teste 1 — Empilhamento e remoção

Inserção de elementos, consulta do topo e remoção seguindo a lógica LIFO.

## Teste 2 — Limpeza completa da pilha

Utilização do método `limpar()` para remover todos os elementos de uma única vez.

## Teste 3 — Operações em pilha vazia

Tentativa de executar `desempilhar()` e `topo()` em uma pilha sem elementos → captura de `IndexError`.

## Teste 4 — Limite de capacidade

Tentativa de inserir novos elementos em uma pilha já cheia → captura de `OverflowError`.

---

# Tratamento de Erros

| Situação | Exceção Lançada |
|---|---|
| Remover ou consultar elemento de pilha vazia | `IndexError` |
| Inserir elemento em pilha com capacidade máxima | `OverflowError` |

---

# Princípio de Funcionamento

A pilha segue o conceito **LIFO (Last In, First Out)**, onde o último elemento inserido será sempre o primeiro a ser removido. Esse comportamento é amplamente utilizado em sistemas de desfazer/refazer ações, controle de chamadas de funções, gerenciamento de memória e navegação entre páginas.