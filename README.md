# Resolução de modelos de classificação multilabels

Nesse projeto utilizei as bibliotecas e ferramentas mais populares para resolução de um problema de identificação de tags em discursões do StackOverFlow. Através de técnicas de NLP, os dados textuais foram transformados e realizada a aplicação dos algoritmos de classificação de múltiplas labels.

# Resultados

Utilizando como base apenas o algortimos de Regressão logística, foi empregado estratégias de classificação de múltiplas labels. A estratégia OneVsRest conquistou uma acuária **exata** de 41.68% e um Hamming loss de ~18%. A estratégia de classificação em cadeia da biblioteca Scikit-MultiLearn atingiu uma previsão exata 49.82% e um Hamming Loss de 21.10%.

# Conclusão

A escolha do melhor modelo depende diretamente do proposito do uso. A acurácia exata pode ser ou não a métrica definitiva de desempenho. Devemos avaliar se é tolerável que as labels apresentem classificações individuais erradas ou se somente classificações exatas são válidas para determinação da escolha do melhor modelo. É importante resaltar também que o presente projeto não teve o objetivo de desenvolver o melhor modelo para uso, tendo como único propósito a exploração de técnicas e ferramentas para classificação de múltiplas labels. Caso houvesse a supracitada necessidade, o projeto necessitaria de uma maior quantidade de dados relacionados ao objetivo visado, além de técnicas de validação mais robustas como o método de validação cruzada e ainda a utilização de técnicas de otimização do modelo por meio de algoritmos como GridSearch ou ainda o algoritmo de RandomSearch, para circustâncias onde existe uma carência de poder computacional.