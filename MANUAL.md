# Manual de uso do projeto

O trabalho foi realizado utilizando ferramentas comuns de python e c, entretanto, o mesmo possui suas características especiais que podem diferir a forma de usar. Para evitar confusões, esse mini guia tenta auxiliar todos os testes e formas de usar o projeto.

## Diretório principal

Sempre mantenha o seu diretório que irá rodar os códigos como o diretório mais acima do projeto, no caso o "Projeto-BenchMark_Prog1", isso evitará possíveis erros de _PATH_ e irá permitir que todos os módulos do projeto sejam acessados sem erros.

## Compilação do projeto

Como o projeto é em parte feito na linguagem compilada C, optou-se pela utilização da ferramenta Make para diminuir o tempo de desenvolvimento gasto com a repetição de comandos de compilação.

Para utilizar a compilação do projeto com esse ferramenta varia com o seu sistema operacional. Os códigos foram feitos para funcionar em ambos os sistemas operacionais: Windows e sistemas baseados no kernel Linux. Desse modo, para conseguir compilar com o Makefile, utiliza-se, mas não se limita, os seguintes códigos:

```
Comandos:
    
    make            # Mostra toda a documentação do Makefile e compila o projeto para Linux

    make linux      # Compila o projeto para sistemas Linux

    make windows    # Compila o projeto para sistemas Windows

    make run        # Roda os algoritmos caso já tenham sido compilados

    make clean      # Limpa todos os arquivos objetos e binários do projeto

    make help       # Mostra todos os comandos do arquivo Makefile
```

Com esses comandos, é perfeitamente possível utilizar o código em C com uma dificuldade extremamente reduzida.

## Python e suas dependências

O projeto em Python fez uso do python `3.12.9`, entretanto, foi utilizado em conjunto bibliotecas para o manuseio de dados. Dentre elas, está a bibliotecas: `pandas` e `numpy`, além do ambiente `jupyter`, para baixa-las deve seguir os passos que serão descritos.

### Configuração do ambiente virtual

Utilizar um ambiente virtual python da sua preferência é essencial para o isolamento dos pacotes python do sistema e do projeto. No nosso caso, utilizamos o `conda`, porém, o ambiente `venv` do próprio python já serve muito bem a esse propósito. Para mais detalhes sobre o ambiente conda, olhe a [documentação](https://docs.conda.io).

Ativar o ambiente em questão é algo necessário para a continuidade do projeto. Caso opte por usar o ambiente conda use os comandos:

```
conda create --name nome_do_ambiente python=3.12.9 # Irá criar o ambiente. Troque o nome_do_ambiente para um nome da sua preferência

conda activate nome_do_ambiente # Irá ativar o ambiente. Troque o nome_do_ambiente para o nome do ambiente criado
```

Entretanto, caos opte por utilizar o ambiente `venv` é necessário seguir os seguintes comandos:

```
python3 -m venv .venv # Utilize apenas python ao invés de python3 caso esteja em um abiente windows
```

E ative a venv. Caso seja um sistema Linux:

```
source .venv/bin/activate
```

Caso seja um sistema Windows:

```
.\.venv\Scripts\activate.bat
```

Ao fim do seu ambiente virtual, utilize o comando Linux `which python` para saber se o python está dentro do ambiente virtual, no caso do cmd Windows, utilize o comando `where python`.

### Instalando as dependências

para instalar as dependências pelo próprio gerenciador de pacotes do python, utilize o `pip`:

```
pip install pandas=2.2.3 ipykernel
```

Após essa linha de código, já poderá usar o projeto como ele foi planejado.

## Localizaçao dos notebooks python

O projeto python é gerido por notebooks jupyter com a finalidade puramente didática e de manipulação dos dados. Para acessar os notebooks basta seguir o caminho `src/python/src/` dentro deste diretórios está o benchmark_simulations.ipynb e data_manipulation.ipynb, ambos notebooks jupyter.

## Inserção de dados já calculados

Caso já tenha algum dado calculado, é possível aplicar os arquivos CSVs dentro do diretório `src/results/data/`. Os arquivos inseridos devem seguir a seguinte estrutura:

```
nome_do_algorithmo-linguagem.csv
↑                   ↑
↑                   linguagens aceitas: python ou c
↑
Nomes possíveis são: bubble, merge ou quick
```

## Utilização dos notebooks

Caso queira rodar alguma simulação do notebook, basta rodar todas as células em ordem sequencial do arquivo benchmark_simulations.ipynb, isso irá rodar todos os testes dos algoritmos python.

Caso queira ver os dados coletados, basta rodar todas as células sequenciais do arquivo data_manipulation.ipynb, lá é possível selecionar a linguagem, algoritmo, tamanho do array/lista e a ordenação dos dados da lista. Todos os outputs estarão sendo mostrados na última célula. Para mudar os dados que gostaria de ver, é necessário mudar o valor das seguintes variáveis:

```
size: int = FIRST_SIZE             # <-- Seleciona o tamanho do array/lista: FIRST_SIZE, SECOND_SIZE, THIRD_SIZE, FOURTH_SIZE
order: str = FIRST_ORDER           # <-- Seleciona a ordem do array/lista: FIRST_ORDER, SECOND_ORDER, THIRD_ORDER, FOURTH_ORDER
algorithm_name: str = MERGE_NAME   # <-- Seleciona o algoritimo: BUBBLE_NAME, MERGE_NAME ou QUICK_NAME
language: str = PYTHON_LANG        # <-- Seleceiona a linguagem: PYTHON_LANG ou C_LANG
```

Caso não tenha nenhum arquivo CSV, o código apresentará erro.