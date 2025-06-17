# Sistema Simplificado de Lógica de Predicados em Python

Este repositório contém um código Python que implementa um sistema básico de lógica de predicados, permitindo a definição de fatos e regras, e a realização de consultas para inferir novos conhecimentos. É uma demonstração didática de como uma pequena base de conhecimento com capacidade de raciocínio lógico pode ser construída.

## Estrutura do Projeto

O projeto consiste em um único arquivo Python:

-   `calculo_predicados.py`: Contém as classes e a lógica para o sistema de lógica de predicados.

## Como Rodar o Código

Para executar o código e ver a demonstração das consultas, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.x instalado em sua máquina.

2.  **Navegue até o Diretório:** Abra seu terminal ou prompt de comando e navegue até o diretório onde você salvou o arquivo `calculo_predicados.py`.

    ```bash
    cd /caminho/para/o/seu/diretorio
    ```

3.  **Execute o Script:** Utilize o comando `python` (ou `python3` ou `python3.11`, dependendo da sua configuração) seguido do nome do arquivo:

    ```bash
    python3.11 calculo_predicados.py
    ```

    ou

    ```bash
    python3 calculo_predicados.py
    ```

    A saída das consultas será exibida diretamente no terminal.

## Classes Principais

O código é estruturado em torno das seguintes classes:

-   `Predicado`: Define um predicado com seu nome e aridade (número de argumentos).
-   `Fato`: Representa uma afirmação concreta, combinando um predicado com argumentos específicos.
-   `Variavel`: Representa uma variável simbólica usada em regras, permitindo generalizações.
-   `Regra`: Define uma regra lógica com uma cabeça (consequência) e um corpo (condições).
-   `BaseDeConhecimento` (e `BaseDeConhecimentoMelhorada`): Gerencia a coleção de fatos e regras e fornece um mecanismo de consulta, incluindo uma simulação de unificação para regras com variáveis.




## Exemplo de Uso e Retorno Esperado

O arquivo `calculo_predicados.py` inclui um exemplo de uso prático que demonstra a criação de uma base de conhecimento, a adição de fatos e regras, e a realização de consultas. Este exemplo ilustra como o sistema infere novos conhecimentos a partir das informações fornecidas.

### Cenário do Exemplo:

O exemplo define os predicados `homem` e `mortal`, ambos com aridade 1. Em seguida, fatos como `homem(socrates)`, `homem(platao)` e `mortal(joao)` são adicionados à base de conhecimento. A regra principal é "Para todo X, se X é homem, então X é mortal", representada simbolicamente como `mortal(X) :- homem(X)`.

### Consultas Realizadas e Seus Resultados:

O script executa uma série de consultas e imprime seus resultados. Abaixo, detalhamos cada consulta e o porquê de seu retorno:

-   **`Consulta: mortal(socrates)`**
    -   **Processo:** Não é um fato direto. A regra `mortal(X) :- homem(X)` é aplicada. `X` é unificado com `socrates`. A condição `homem(socrates)` é verificada na base de fatos e é encontrada como verdadeira. Assim, `mortal(socrates)` é inferido.
    -   **Retorno Esperado:** `True`

-   **`Consulta: mortal(platao)`**
    -   **Processo:** Similar à consulta anterior. `mortal(platao)` não é um fato direto. A regra é aplicada, `X` é unificado com `platao`. A condição `homem(platao)` é verificada e encontrada como verdadeira. `mortal(platao)` é inferido.
    -   **Retorno Esperado:** `True`

-   **`Consulta: mortal(joao)`**
    -   **Processo:** Este é um fato direto, presente na base de conhecimento desde o início.
    -   **Retorno Esperado:** `True`

-   **`Consulta: mortal(maria)`**
    -   **Processo:** `mortal(maria)` não é um fato direto. A regra `mortal(X) :- homem(X)` é aplicada, `X` é unificado com `maria`. A condição `homem(maria)` **não** é encontrada na base de fatos. Portanto, `mortal(maria)` não pode ser inferido.
    -   **Retorno Esperado:** `False`

-   **`Consulta: homem(socrates)`**
    -   **Processo:** Este é um fato direto, presente na base de conhecimento.
    -   **Retorno Esperado:** `True`

-   **`Consulta: homem(zeus)`**
    -   **Processo:** `homem(zeus)` não é um fato direto e não há regras que possam inferir essa informação a partir de outros fatos neste sistema simplificado.
    -   **Retorno Esperado:** `False`

### Saída Completa da Execução:

Ao rodar o script `calculo_predicados.py`, você verá a seguinte saída no seu terminal:

```
--- Consultas ---
Consulta: mortal(socrates) -> True
Consulta: mortal(platao) -> True
Consulta: mortal(joao) -> True
Consulta: mortal(maria) -> False
Consulta: homem(socrates) -> True
Consulta: homem(zeus) -> False
```

Esta saída demonstra a capacidade do sistema de inferir novos conhecimentos (como a mortalidade de Sócrates e Platão) a partir de fatos básicos e regras lógicas, além de verificar fatos diretamente conhecidos e identificar consultas que não podem ser provadas com o conhecimento disponível.


