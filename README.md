# Projeto Final da Matéria de Programação de Computadores 1

O projeto consiste em comparar a performance das linguagens de programação C e Python em algoritmos de ordenação, dentre os algoritmos estão: Bubble sort, Merge sort, Quick sort. Utilizando de técnicas de benchmark, criaremos gráficos para demonstrar os resultados obtidos.

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

## Autores

- Arthur Negrão
- Francisco Braga