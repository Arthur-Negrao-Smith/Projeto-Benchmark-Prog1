#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//simplementação do Bubble Sort
//recebe: array, tamanho do array, ponteiros para contadores de comparações e trocas
void bubble_sort (int arr[], int n, int *comparisons, int *swaps){
    *comparisons = 0;
    *swaps = 0;
    //loop externo: passa por todos os elementos
    for (int i = 0; i<n-1; i++) {
        //loop interno: compara elementos adjacentes
        for (int j = 0; j<n-i-1; j++) {
            (*comparisons)++; //incrementa contador de comparações
            //se o elemento atual for maior que o próximo, troca eles
            if (arr[j]>arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                (*swaps)++; //incrementa contador de trocas
            }
        }
    }
}
//gera diferentes tipos de dados para teste
//recebe: array vazio, tamanho, e tipo de dados desejado
void generate_data(int arr[], int size, const char* data_type) {
     //array já ordenado (melhor caso para Bubble Sort)
    if (strcmp(data_type, "sorted") == 0) {
        for (int i = 0; i<size; i++) {
            arr[i] = i;  //preenche com valores de 0 a size-1
        }
    } //array em ordem reversa (pior caso para Bubble Sort)
    else if (strcmp(data_type, "reverse_sorted")==0){
        for (int i = 0; i<size; i++) {
            arr[i] = size - i; //preenche com valores de size a 1
        }
    }//array com valores aleatórios
    else if (strcmp(data_type, "ramdom") == 0) {
        for (int i = 0; i < size; i++) {
            arr[i] = rand() % size;//valores entre 0 e size-1
        }
    } //array com muitos valores repetidos
    else if (strcmp(data_type, "many_duplicates") == 0) {
        for(int i = 0; i<size; i++){
            //valores entre 0 e size/10 (garantindo repetições)
            arr[i] = rand() % (size/10);
        }
    }
}
//função que testa o Bubble Sort com diferentes configurações
void test_bubble_sort(){
    //tamanhos de arrays para teste
    int sizes[] = {1000, 10000, 100000};
    // Tipos de dados para teste
    const char* data_types[] = {"sorted", "reverse-_sorted", "random", "many_duplicates"};

    //calcula quantos tamanhos e tipos existem
    int num_sizes = sizeof(sizes)/sizeof(sizes[0]);
    int num_types = sizeof(data_types) / sizeof(data_types[0]);

    //cabeçalho dos resultados
    printf("Bubble Sort Performance Test\n");
    printf("Size\tData Type\t\tTime (s)\tComparisons\tSwap\n");
    printf("------------------------------------------------------------\n");

    //testa para cada combinação de tamanho e tipo de dados
    for (int i = 0; i<num_sizes; i++) {
        for (int j=0; j<num_types; j++){
            int size = sizes[i];
            //aloca memória para o array
            int* arr = (int*)malloc(size * sizeof(int));
            //gera dados conforme o tipo atual
            generate_data(arr, size, data_types[j]);

            int comparisions, swaps;//variáveis para métricas
            clock_t start = clock();//marca tempo inicial
            bubble_sort(arr, size, &comparisions, &swaps);//executa ordenação
            clock_t end = clock();//marca tempo final
            double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;//calcula tempo decorrido em segundos
            
            //imprime resultados formatados
            printf("%d\t%-16s\t%.6f\t%d\n",
            size, data_types[j], time_taken, comparisions, swaps);

            free(arr);//libera memória alocada
        }
    }
}

int main(){
    srand(time(0));
    test_bubble_sort();
    return 0;
}