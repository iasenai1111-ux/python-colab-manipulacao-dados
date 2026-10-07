# Laboratório prático: Google Colab e manipulação de dados com Python

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/iasenai1111-ux/python-colab-manipulacao-dados/blob/main/Aula_Pratica_Colab_Dados_Aluno.ipynb)

Primeira prática da trilha de Python: você recebe as planilhas de três dias de um posto de combustível e precisa juntar tudo em uma base única, resumir os dados e entregar um arquivo consolidado.

| | |
|---|---|
| **Nível** | Iniciante (não precisa ter programado antes) |
| **Ambiente** | Google Colab, direto no navegador |
| **Tempo estimado** | 2h30 a 3h |
| **Entrega** | Notebook executado + `dias_consolidados.csv` + registro técnico |

## O que você vai aprender

- Enviar arquivos para uma sessão do Google Colab
- Ler planilhas Excel com `pandas`
- Consolidar tabelas com `pd.concat()`
- Validar linhas, colunas e índice de um DataFrame
- Gerar estatísticas descritivas e interpretar quartis
- Filtrar com valores fixos e com variáveis
- Ler a mesma tabela em Excel, CSV e TXT, com separadores diferentes
- Limpar uma planilha com colunas e linhas que não são dados
- Exportar o resultado para CSV

## Como começar

1. Baixe o [`dados.zip`](dados.zip) e extraia os sete arquivos no seu computador.
2. Clique no botão **Abrir no Colab** no topo desta página.
3. No Colab, use **Arquivo → Salvar uma cópia no Drive** para ter a sua versão.
4. Siga as etapas na ordem, completando só as lacunas marcadas com `TODO`.

Se preferir ler no papel, o mesmo roteiro está em [`material/Material_Aluno_Colab_Dados.docx`](material/Material_Aluno_Colab_Dados.docx), com espaço para respostas.

## Arquivos da prática

| Arquivo | Uso |
|---|---|
| `dia01.xlsx`, `dia02.xlsx`, `dia03.xlsx` | Projeto principal: litros vendidos por hora em três dias |
| `diaxx_gerador_aleatorio.xlsx` | Desafio de limpeza: colunas extras e uma linha de total |
| `mussum.xlsx`, `mussum.csv`, `mussum2.txt` | A mesma tabela em três formatos |

Todos ficam na pasta [`dados/`](dados). São dados fictícios, gerados pelo script [`scripts/gerar_dados.py`](scripts/gerar_dados.py).

## Roteiro

| Etapa | O que você faz | Tempo |
|---|---|---|
| 1 | Enviar os arquivos para o Colab | 10 min |
| 2 | Importar o `pandas` | 5 min |
| 3 | Ler as três planilhas diárias | 15 min |
| 4 | Conferir linhas e colunas | 15 min |
| 5 | Consolidar com `pd.concat()` | 20 min |
| 6 | Validar a tabela consolidada | 10 min |
| 7 | Estatísticas com `describe()` | 15 min |
| 8 | Guardar os quartis em variáveis | 10 min |
| 9 | Aplicar filtros com `query()` | 20 min |
| 10 | Criar a coluna `TOTAL_COMBUSTIVEL` | 10 min |
| 11 | Encontrar o maior movimento | 10 min |
| 12 | Ler Excel, CSV e TXT | 20 min |
| 13 | Desafio de limpeza | 20 min |
| 14 e 15 | Exportar e baixar o CSV | 10 min |
| Final | Registro técnico individual | 20 min |

## Como saber se está no caminho certo

- Depois da etapa 4, as três planilhas têm o mesmo número de linhas e as mesmas cinco colunas.
- Antes de executar a etapa 5, faça a conta: quantas linhas a tabela consolidada deve ter?
- Depois da etapa 6, o índice começa em 0 e segue sem reiniciar a cada arquivo.
- Depois da etapa 10, aparece uma coluna nova no final da tabela.
- Depois da etapa 13, a planilha limpa tem o mesmo formato das planilhas diárias.

## Problemas comuns

| Mensagem | Causa provável |
|---|---|
| `FileNotFoundError` | O arquivo não foi enviado, a sessão do Colab reiniciou ou o nome está digitado diferente |
| `NameError: name 'pd' is not defined` | A célula que importa o `pandas` não foi executada |
| Tabela com uma coluna só ao ler CSV ou TXT | Faltou informar o separador certo em `sep` |
| `UndefinedVariableError` no `query()` | Variável do Python usada dentro do filtro sem o `@` na frente |

O Colab apaga os arquivos enviados quando a sessão termina. Se você fechar e voltar depois, envie de novo ou use a célula alternativa do notebook, que busca os arquivos direto deste repositório.

## Para o seu portfólio

Depois de concluir, transforme a prática em um projeto seu:

1. Responda uma pergunta nova com os mesmos dados, por exemplo: em que hora do dia o posto mais vende? Qual combustível varia mais?
2. Faça um gráfico com o resultado.
3. Publique o notebook no seu GitHub, com um README seguindo o [modelo de projeto](https://github.com/iasenai1111-ux/modelo-portfolio).
