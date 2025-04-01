#include <stdio.h>   //para funções de entrada/saída (printf, etc.)
#include <stdlib.h>  //para alocação de memória (malloc, free) e números aleatórios (rand)
#include <time.h>    //para medir tempo de execução (clock()) e gerar sementes aleatórias (time)
#include <string.h>  //para comparar strings (strcmp)


int partition(int arr[], int low, int high, int *comparisons, int *swaps);
void quick_sort_helper(int arr[], int low, int high, int *comparisons, int *swaps);
void quick_sort(int arr[], int n, int *comparisons, int *swaps);
void generate_data(int arr[], int size, const char* data_type);
void test_quick_sort();


int main() {
    srand(time(0));//inicializa a semente para números aleatórios
    test_quick_sort();//executa os testes
    return 0;//retorna 0 indicando sucesso
}



/* Função de partição para o Quick Sort (esquema de Lomuto*/
int partition(int arr[], int low, int high, int *comparisons, int *swaps) {
    int pivot = arr[high];//seleciona o último elemento como pivô
    int i = (low - 1);//indice do menor elemento

    for (int j = low; j <= high - 1; j++) {
        (*comparisons)++;  //incrementa a cada comparação
        //se elemento atual é menor que o pivô
        if (arr[j] < pivot) {
            i++;//incrementa o índice do menor elemento
            //troca arr[i] e arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            (*swaps)++;//conta cada troca
        }
    }
    //coloca o pivô na posição correta
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    (*swaps)++;//conta a troca do pivô
    return (i + 1);//retorna a posição do pivô
}

/*Função recursiva auxiliar do Quick Sort*/
void quick_sort_helper(int arr[], int low, int high, int *comparisons, int *swaps) {
    if (low < high) {
        //obtém o índice do pivô após a partição
        int pi = partition(arr, low, high, comparisons, swaps);
        
        //ordena recursivamente os elementos antes e depois do pivô
        quick_sort_helper(arr, low, pi - 1, comparisons, swaps);
        quick_sort_helper(arr, pi + 1, high, comparisons, swaps);
    }
}

/* Função principal do Quick Sort*/
void quick_sort(int arr[], int n, int *comparisons, int *swaps) {
    *comparisons = 0;//inicializa contador de comparações
    *swaps = 0;//inicializa contador de trocas
    quick_sort_helper(arr, 0, n - 1, comparisons, swaps);  // Chama a função auxiliar
}

/* Gera diferentes tipos de dados para teste*/
void generate_data(int arr[], int size, const char* data_type) {
    if (strcmp(data_type, "sorted") == 0) {
        //array já ordenado (melhor caso para Quick Sort com pivô inteligente)
        for (int i = 0; i < size; i++) {
            arr[i] = i;
        }
    } else if (strcmp(data_type, "reverse_sorted") == 0) {
        //array em ordem decrescente (pior caso para Quick Sort com pivô fixo)
        for (int i = 0; i < size; i++) {
            arr[i] = size - i;
        }
    } else if (strcmp(data_type, "random") == 0) {
        //array com valores aleatórios (caso médio)
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % size;//gera números entre 0 e size-1
        }
    } else if (strcmp(data_type, "many_duplicates") == 0) {
        //array com muitos valores repetidos
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % (size / 10);//gera números entre 0 e size/10
        }
    }
}

/* Função que testa o Quick Sort com diferentes configurações */
void test_quick_sort() {
    //tamanhos de arrays para teste
    int sizes[] = {1000, 10000, 100000, 1000000};
    // Tipos de dados para teste
    const char* data_types[] = {"sorted", "reverse_sorted", "random", "many_duplicates"};
    
    //calcula quantos tamanhos e tipos de dados existem
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types)/sizeof(data_types[0]);

    //cabeçalho dos resultados
    printf("Teste de Performance do Quick Sort\n");
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

            int comparisons, swaps;//variáveis para armazenar as métricas
            clock_t start = clock(); //marca o tempo inicial
            quick_sort(arr, size, &comparisons, &swaps); // Executa a ordenação
            clock_t end = clock();//marca o tempo final
            
            //calcula o tempo decorrido em segundos
            double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

            //imprime os resultados formatados
            printf("%d\t%-16s\t%.6f\t%d\t\t%d\n", 
                   size, data_types[j], time_taken, comparisons, swaps);

            free(arr);//libera a memória alocada para o array
        }
    }
}
