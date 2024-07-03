# Análise de Dados de Saúde com Python

Este projeto demonstra como realizar análise de dados de saúde utilizando Python, pandas e scikit-learn. O objetivo é calcular o tempo de espera e a nota de atendimento com base nos registros de consultas médicas, ordená-los pelo tempo de espera decrescente e salvar os resultados em um arquivo CSV.

## Requisitos

Para executar este projeto, é necessário ter o Python instalado juntamente com as seguintes bibliotecas Python:

- pandas
- scikit-learn

Você pode instalar as dependências usando pip:

```bash
pip install pandas scikit-learn
```
```arvore
analisePacientes/
│
├── dados.csv       # Arquivo CSV com os dados das consultas médicas
├── processing.py      # Script Python para análise dos dados de saúde
└── README.md             # Este arquivo, documentando o projeto
```

## Funcionalidades

1. **Carregamento dos Dados**: Os dados são carregados a partir de um arquivo CSV que contém informações sobre consultas médicas.
   
2. **Preprocessamento dos Dados**: As colunas de data e hora são convertidas para tipos datetime completo para facilitar a manipulação. Calcula-se o tempo de espera entre a hora de entrada e a alta do paciente.

3. **Cálculo da Nota de Atendimento**: A nota de atendimento é calculada com base no tempo de espera. Quanto menor o tempo de espera, melhor é a nota.

4. **Ordenação dos Dados**: Os dados são ordenados pelo tempo de espera decrescente para identificar os casos com maiores tempos de espera.

5. **Exportação dos Resultados**: Os dados processados e ordenados são salvos em um arquivo CSV na raiz da pasta.

## Execução

Para executar o código:

1. Certifique-se de ter o Python e as bibliotecas necessárias instaladas.
2. Baixe o arquivo `dados.csv` e coloque-o na mesma pasta do script Python.
3. Execute o script `processing.py`.
4. Será gerado um csv na raiz do projeto `returnDate.csv`.

Certifique-se de ajustar o nome do arquivo CSV e o nome do script Python conforme necessário para corresponder aos seus arquivos específicos. Esta configuração pressupõe que você está trabalhando em um ambiente onde Python está instalado e configurado corretamente.
