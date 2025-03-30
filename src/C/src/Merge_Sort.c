#include <stdio.h>   // Para funções de entrada/saída (printf, etc.)
#include <stdlib.h>  // Para alocação de memória (malloc, free) e rand()
#include <time.h>    // Para medir tempo de execução (clock()) e gerar números aleatórios (time())
#include <string.h>  // Para comparar strings (strcmp())

void merge(int arr[], int l, int m, int r, int *comparisons, int *swaps);
void merge_sort_helper(int arr[], int l, int r, int *comparisons, int *swaps);
void merge_sort(int arr[], int n, int *comparisons, int *swaps);
void generate_data(int arr[], int size, const char* data_type);
void test_merge_sort();



int main() {
    srand(time(0));//inicializa a semente para números aleatórios
    test_merge_sort();//executa os testes
    return 0;//retorna 0 indicando sucesso
}




/*função que combina dois subarrays ordenados em um único array ordenado
   parâmetros:
   -arr[]: Array principal que será ordenado
   -l: Índice inicial do subarray esquerdo
   -m: Índice do meio (fim do subarray esquerdo)
   -r: Índice final do subarray direito
   -comparisons: Ponteiro para contador de comparações
   -swaps: ponteiro para contador de trocas*/
void merge(int arr[], int l, int m, int r, int *comparisons, int *swaps) {
    int i, j, k;
    int n1 = m - l + 1;  //tamanho do subarray esquerdo
    int n2 = r - m;//tamanho do subarray direito

    //arrays temporários para armazenar as metades
    int L[n1], R[n2];

    //copia os dados para os arrays temporários
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];  //correção: alterado de arr[1+i] para arr[l+i]
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Combina os arrays temporários de volta no array principal
    i = 0;  //indice inicial do subarray esquerdo
    j = 0;  //indice inicial do subarray direito
    k = l;  //indice inicial do array combinado
    
    while (i < n1 && j < n2) {
        (*comparisons)++;  //incrementa o contador de comparações
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
            (*swaps)++;//incrementa o contador de trocas
        }
        k++;
    }

    //copia os elementos restantes do subarray esquerdo, se houver
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    //copia os elementos restantes do subarray direito, se houver
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/*função auxiliar recursiva que implementa o Merge Sort
   parâmetros:
   -arr[]: Array a ser ordenado
   -l: Índice inicial
   -r: Índice final
   -comparisons: Ponteiro para contador de comparações
   -swaps: Ponteiro para contador de trocas*/
void merge_sort_helper(int arr[], int l, int r, int *comparisons, int *swaps) {
    if (l < r) {
        //encontra o ponto médio para dividir o array
        int m = l + (r - l) / 2;
        
        //ordena primeira e segunda metades
        merge_sort_helper(arr, l, m, comparisons, swaps);
        merge_sort_helper(arr, m + 1, r, comparisons, swaps);
        
        //combina as metades ordenadas
        merge(arr, l, m, r, comparisons, swaps);
    }
}

/*função principal do Merge Sort que inicia o processo de ordenação
   parametros:
   -arr[]: Array a ser ordenado
   -n: Tamanho do array
   -comparisons: Ponteiro para contador de comparações
   -swaps: Ponteiro para contador de trocas*/
void merge_sort(int arr[], int n, int *comparisons, int *swaps) {
    *comparisons = 0;  //inicializa contador de comparações
    *swaps = 0;//inicializa contador de trocas
    merge_sort_helper(arr, 0, n - 1, comparisons, swaps);  //chama a função auxiliar
}

/*gera diferentes tipos de dados para teste
   Parâmetros:
   -arr[]: Array a ser preenchido
   -size: Tamanho do array
   -data_type: Tipo de dados a ser gerado*/
void generate_data(int arr[], int size, const char* data_type) {
    if (strcmp(data_type, "sorted") == 0) {
        //array já ordenado
        for (int i = 0; i < size; i++) {
            arr[i] = i;
        }
    } else if (strcmp(data_type, "reverse_sorted") == 0) {
        //array em ordem decrescente (pior caso para alguns algoritmos)
        for (int i = 0; i < size; i++) {
            arr[i] = size - i; //correção: alterado de size-1 para size-i
        }
    } else if (strcmp(data_type, "random") == 0) {
        //array com valores aleatórios
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % size;  //gera números entre 0 e size-1
        }
    } else if (strcmp(data_type, "many_duplicates") == 0) {
        //array com muitos valores repetidos
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % (size / 10);//gera números entre 0 e size/10
        }
    }
}

/*função que testa o Merge Sort com diferentes configurações*/
void test_merge_sort() {
    //tamanhos de arrays para teste
    int sizes[] = {1000, 10000, 100000, 1000000};
    //tipos de dados para teste
    const char* data_types[] = {"sorted", "reverse_sorted", "random", "many_duplicates"};
    
    //calcula quantos tamanhos e tipos de dados existem
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types)/sizeof(data_types[0]);

    //cabeçalho dos resultados
    printf("Teste de Performance do Merge Sort\n");
    printf("Tamanho\tTipo de Dados\t\tTempo (s)\tComparações\tTrocas\n");
    printf("------------------------------------------------------------\n");

    //testa para cada combinação de tamanho e tipo de dados
    for (int i = 0; i < num_sizes; i++) {
        for (int j = 0; j < num_types; j++) {
            int size = sizes[i];
            //aloca memória para o array
            int* arr = (int*)malloc(size * sizeof(int));
            
            //gera dados conforme o tipo atual
            generate_data(arr, size, data_types[j]);

            int comparisons, swaps;// Variáveis para armazenar as métricas
            clock_t start = clock();//marca o tempo inicial
            merge_sort(arr, size, &comparisons, &swaps);//executa a ordenação
            clock_t end = clock();   //marca o tempo final
            
            //calcula o tempo decorrido em segundos
            double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

            //imprime os resultados formatados
            printf("%d\t%-16s\t%.6f\t%d\t\t%d\n", 
                   size, data_types[j], time_taken, comparisons, swaps);

            free(arr);//libera a memória alocada para o array
        }
    }
}
