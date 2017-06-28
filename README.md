# Projeto de Introdução a Multimídia

Em resumo, a proposta do projeto é estimar a quantidade de likes que, dada uma foto que será postada no Instagram, e o número de followers do usuário, o sistema preditar o número de likes que esta foto receberá. O algoritmo está fechado para um tipo de foto, mulheres fitness que postam fotos na academia.

# Tecnologias e linguagens

O projeto foi feito em Python, e utilizando as [APIs Google Cloud Vision](https://cloud.google.com/vision/) e [Imagga](https://imagga.com/), ambas tem a mesma funcionalidade, extração de algumas labels de uma imagem, do cenário e da pessoa, no caso da Google, e apenas da pessoa no caso da Imagga. Ainda estamos decidindo qual das duas utilizar, devido a diferença de labels extraidas de cada uma.

Junto ao código, estamos utilizando uma rede neural [MLP Regressor](http://scikit-learn.org/stable/modules/neural_networks_supervised.html#regression) (Multi-layer Perceptron) (MLP), e uma [Decision Tree Regression](http://scikit-learn.org/stable/modules/tree.html#regression) (DTR), para a parte de aprendizado de uma base de dados de fotos como já especificado. Ainda estamos decidindo qual das duas utilizar, devido alguns erros de precisão.

# Problemas

Um dos primeiros problemas enfrentados se encontra em quais labels utilizar na hora do treinamento dos dados e de teste, como dito anteriormente, as APIs não retornam as mesmas labels para diferente fotos, o que dificulta a padronização e o aprendizado da rede neural ou arvore de regressão. Até agora para contornar esse problema estamos analisando todas as labels retornadas, identificando a quantidade de vezes que aparecem em cada foto, e destacando aquelas que são mais frequentes. Após as mais frequentes serem armazenadas, formamos o primeiro input do algoritmo, e para as imagens que não tem uma das labels dentre as mais frequentes, zeramos seu valor. Assim a aparição de dados zerados nesse input pode ficar maior dependendo das fotos selecionadas para o aprendizado.

# Arquivos importantes:

- [data_input.csv](https://github.com/msb55/projeto-multimidia/blob/master/data_input.csv): resultado da API Imagga de acordo com os labels previamente definidos
- [data_input_google.csv](https://github.com/msb55/projeto-multimidia/blob/master/data_input_google.csv): resultado da API do Google
- [extracao-imagga.py](https://github.com/msb55/projeto-multimidia/blob/master/extracao-imagga.py): script em python para requisições a API Imagga, enviando as imagens e recebendo os dados gerados e armazenando os JSON no arquivo 'output-api-imagga.json'
- [followlikes.csv](https://github.com/msb55/projeto-multimidia/blob/master/followlikes.csv): para cada imagem, seguindo na ordem da numeração, uma linha corresponde aos numero de seguidores e quantidade de likes. Arquivo utilizado como input para a MLP e DTR
- [lercsv.py](https://github.com/msb55/projeto-multimidia/blob/master/lercsv.py): script em python para ler um arquivo csv com as tags identificadas, agrupar e contabilizar. e escrever no arquivo 'data_input.csv' as labels escolhidas dentre as mais frequentes
- [main.py](https://github.com/msb55/projeto-multimidia/blob/master/main.py): script em python para requisições a API do Google, enviando as imagens e recebendo os dados gerados e armazenando no arquivo 'output-api-imagga.json'
- [train.py](https://github.com/msb55/projeto-multimidia/blob/master/train.py): script em python que realiza o treinamento da MLP ou DTR de acordo com os dados de uma API e exibe os resultados
- [trainning.csv](https://github.com/msb55/projeto-multimidia/blob/master/trainning.csv): labels escolhidas dentre as mais frequentes

# Sub-diretórios

A pasta [images](https://github.com/msb55/projeto-multimidia/tree/master/images) encontra o data set atual de imagens que estão sendo utilizadas na extração de label, treinamento e testes

A pasta [backend](https://github.com/msb55/projeto-multimidia/tree/master/backend/network4like) encontra apenas uma base com o frontend da aplicação, uma interface de usuário para o upload da foto e exibição de resultados. O backend foi feito utilizando o framework Django, escrito tambem em Python
