# Projeto Final da Matéria de Programação de Computadores 1

O projeto consiste em comparar a performance das linguagens de programação C e Python em algoritmos de ordenação, dentre os algoritmos estão: Bubble sort, Merge sort, Quick sort. Utilizando de técnicas de benchmark, criaremos tabelas para demonstrar os resultados obtidos.

## Organização dos diretórios

Para manutenção da organização do projeto, foi decidido arbitrariamente a seguinte ávore de diretórios:

```
src/    # Localização dos códigos do projeto
├── C/          # Todo o projeto escrito em C
│   ├── bin/            # Todos os binários compilados de C
│   ├── include/        # Todos o arquivos de cabeçalho de C
│   ├── obj/            # Todos os arquivos objeto (.o) de C
│   └── src/            # Todo o código fonte em C
│
├── python/     # Todo o projeto escrito em Python
│   ├── libs/           # Todos os nossos módulos que serão importados para o Python
│   └── src/            # Todo o código fonte em Python
│
└── results/    # Local para armazenar todos os resultados obtidos nas simulações
    ├── data/           # Armazena todos os dados coletados durante as simulações
    └── pdf/            # Armazena todos os PDFs que foram gerados no projeto
```

## Dependências do Projeto

O projeto foi criado utilizando ferramentas de desenvolvimento específicas e escolhidas com o intuito de facilitar e aprimorar a construção geral dos testes. 

O projeto python foi inteiramente feito utilizando a versão `Python 3.12.9` com as bibliotecas: `pandas` e `numpy`. Enquanto o projeto em C foi utilizado o compilador gcc com a sua versão `gcc (Rev3, Built by MSYS2 project) 13.2.0`. Além disso, fez-se o uso da ferramenta auxiliadora de compilação `make` com a sua versão `GNU Make 4.4.1`. Para auxílio de manual do projeto, confira o arquivo [maunal de uso](MANUAL.md).

## Autores

- Arthur Negrão
- Francisco Braga