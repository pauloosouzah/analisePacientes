import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar os dados
df = pd.read_csv('dados.csv', sep=';')

# Converter as colunas de data e hora para tipos datetime completo
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['horaEntrada'] = pd.to_datetime(df['horaEntrada'], format='%H:%M:%S').dt.time
df['horaAlta'] = pd.to_datetime(df['horaAlta'], format='%H:%M:%S').dt.time

# Ordenar os dados por idPaciente e data
df.sort_values(by=['idPaciente', 'data'], inplace=True)

# Calcular o número de retornos por idPaciente
df['retornos'] = df.groupby('idPaciente').cumcount() + 1  # Começando de 1 ao invés de 0

# Converter horaEntrada e horaAlta para datetime completo (incluindo data)
df['horaEntrada'] = pd.to_datetime(df['data'].astype(str) + ' ' + df['horaEntrada'].astype(str))
df['horaAlta'] = pd.to_datetime(df['data'].astype(str) + ' ' + df['horaAlta'].astype(str))

# Calcular o tempo de espera entre horaEntrada e horaAlta em minutos
df['tempo_espera_minutos'] = (df['horaAlta'] - df['horaEntrada']).dt.total_seconds() / 60

# Corrigir tempo de espera negativo (caso paciente chegue em um dia e saia no outro)
df['tempo_espera_minutos'] = df['tempo_espera_minutos'].abs()

# Converter tempo de espera para formato H:m:s
df['tempo_espera'] = pd.to_datetime(df['tempo_espera_minutos'], unit='m').dt.strftime('%H:%M:%S')

# Normalizar o tempo de espera para atribuir uma nota
scaler = StandardScaler()
df['nota_atendimento'] = scaler.fit_transform(df[['tempo_espera_minutos']].values)

# Ajustar a escala da nota para um intervalo de 1 a 5 e arredondar
df['nota_atendimento'] = 5 - (df['nota_atendimento'] - df['nota_atendimento'].min()) / (df['nota_atendimento'].max() - df['nota_atendimento'].min()) * 4
df['nota_atendimento'] = df['nota_atendimento'].round()

# Ordenar por tempo de espera
df.sort_values(by='tempo_espera_minutos', ascending=False, inplace=True)

# Salvar os dados ordenados em CSV
df.to_csv('returnDate.csv', sep=';', encoding='utf-8')