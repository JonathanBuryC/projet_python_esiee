int** initMatrix(int N, int M){
    
    
     int** tab = (int**) malloc(sizeof(int*)*N + sizeof(int)*N*M);


     tab[0] = tab+N;

    for (int i = 0; i < N; i++) {

        tab[i] = tab[0]+ i*M;
    }
    for (int i = 0; i < N; i++) {
        tab[i][0]= i;
        for (int j = 1; j < M; j++) {
            tab[i][j]= tab[i][j-1]+1;
        }

    }
    return tab;
