# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter, FuncFormatter

# Lendo URL do banco de dados
df = pd.read_excel('meusite/data/Indicadores_CCIH.xlsx')

# Criando dicionário dos indicadores
Indicadores = {'ID_01': ['Indicador_01', 'Taxa de infecção do sítio cirúrgico em cirurgias limpas', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_01.png'],
               'ID_02': ['Indicador_02', 'Taxa de infecção hospitalar', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_02.png'],
               'ID_03': ['Indicador_03', 'Taxa de infecção hospitalar por cirurgias eletivas', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_03.png'],
               'ID_04': ['Indicador_04', 'Taxa de infecção hospitalar por cesáreas', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_04.png'],
               'ID_05': ['Indicador_05', 'Taxa de infecção hospitalar por cirurgias pediátricas', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_05.png'],
               'ID_06': ['Indicador_06', 'Taxa de letalidade de paciente com infecção hospitalar', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_06.png'],
               'ID_07': ['Indicador_07', 'Percentual de pacientes que recebeu antibiótico-profilaxia no momento adequado', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_07.png'],
               'ID_08': ['Indicador_08', 'Percentual de pacientes com registro de antibiótico-profilaxia', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_08.png'],
               'ID_09': ['Indicador_09', 'Densidade de incidência de infecção primária de corrente sanguínea clínica sem confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (A- Menor que 750g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_09.png'],
               'ID_10': ['Indicador_10', 'Densidade de incidência de infecção primária de corrente sanguínea clínica sem confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (B- 750g a 999g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_10.png'],
               'ID_11': ['Indicador_11', 'Densidade de incidência de infecção primária de corrente sanguínea clínica sem confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (C- 1.000g a 1.499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_11.png'],
               'ID_12': ['Indicador_12', 'Densidade de incidência de infecção primária de corrente sanguínea clínica sem confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (D- 1.500g a 2.499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_12.png'],
               'ID_13': ['Indicador_13', 'Densidade de incidência de infecção primária de corrente sanguínea clínica sem confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (E- Maior ou igual a 2.500g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_13.png'],
               'ID_14': ['Indicador_14', 'Densidade de incidência de infecção primária de corrente sanguínea clínica sem confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (Em todos os pacientes)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_14.png'],
               'ID_15': ['Indicador_15', 'Densidade de incidência de infecção primária de corrente sanguínea clínica com confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (A- Menor que 750g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_15.png'],
               'ID_16': ['Indicador_16', 'Densidade de incidência de infecção primária de corrente sanguínea clínica com confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (B- 750g a 999g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_16.png'],
               'ID_17': ['Indicador_17', 'Densidade de incidência de infecção primária de corrente sanguínea clínica com confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (C- 1.000g a 1.499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_17.png'],
               'ID_18': ['Indicador_18', 'Densidade de incidência de infecção primária de corrente sanguínea clínica com confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (D- 1.500g a 2.499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_18.png'],
               'ID_19': ['Indicador_19', 'Densidade de incidência de infecção primária de corrente sanguínea clínica com confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (E- Maior ou igual a 2.500g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_19.png'],
               'ID_20': ['Indicador_20', 'Densidade de incidência de infecção primária de corrente sanguínea clínica com confirmação' + '\n laboratorial em pacientes em uso de cateter venoso central (Em todos os pacientes)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_20.png'],
               'ID_21': ['Indicador_21', 'Densidade de incidência de pneumonia associada à ventilação' + '\n mecânica (A- Menor que 750g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_21.png'],
               'ID_22': ['Indicador_22', 'Densidade de incidência de pneumonia associada à ventilação' + '\n mecânica (B- 750g a 999g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_22.png'],
               'ID_23': ['Indicador_23', 'Densidade de incidência de pneumonia associada à ventilação' + '\n mecânica (C- 1000g a 1499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_23.png'],
               'ID_24': ['Indicador_24', 'Densidade de incidência de pneumonia associada à ventilação' + '\n mecânica (D- 1.500g a 2.499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_24.png'],
               'ID_25': ['Indicador_25', 'Densidade de incidência de pneumonia associada à ventilação' + '\n mecânica (E- Maior ou igual a 2.500g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_25.png'],
               'ID_26': ['Indicador_26', 'Densidade de incidência de pneumonia associada à ventilação' + '\n mecânica (Em todos os pacientes)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_26.png'],
               'ID_27': ['Indicador_27', 'Densidade de incidência de infecção do trato urinário associada' + '\n à cateter vesical de demora (A- Menor que 750g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_27.png'],
               'ID_28': ['Indicador_28', 'Densidade de incidência de infecção do trato urinário associada' + '\n à cateter vesical de demora (B- 750g a 999g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_28.png'],
               'ID_29': ['Indicador_29', 'Densidade de incidência de infecção do trato urinário associada' + '\n à cateter vesical de demora (C- 1000g a 1499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_29.png'],
               'ID_30': ['Indicador_30', 'Densidade de incidência de infecção do trato urinário associada' + '\n à cateter vesical de demora (D- 1.500g a 2.499g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_30.png'],
               'ID_31': ['Indicador_31', 'Densidade de incidência de infecção do trato urinário associada' + '\n à cateter vesical de demora (E- Maior ou igual a 2.500g)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_31.png'],
               'ID_32': ['Indicador_32', 'Densidade de incidência de infecção do trato urinário associada' + '\n à cateter vesical de demora (Em todos os pacientes)', 'Por mil', 'meusite\static\Imagens\CCIH\grafico_32.png'],
               'ID_33': ['Indicador_33', 'Volume do uso de sabonete na UTI por pacientes dia', 'Litros', 'meusite\static\Imagens\CCIH\grafico_33.png'],
               'ID_34': ['Indicador_34', 'Volume do uso de álcool em gel na UTI por pacientes dia', 'Litros', 'meusite\static\Imagens\CCIH\grafico_34.png'],
               'ID_35': ['Indicador_35', 'Volume do uso de sabonete no HUAB por pacientes dia', 'Litros', 'meusite\static\Imagens\CCIH\grafico_35.png'],
               'ID_36': ['Indicador_36', 'Volume do uso de álcool em gel no HUAB por pacientes dia', 'Litros', 'meusite\static\Imagens\CCIH\grafico_36.png'],
               'ID_37': ['Indicador_37', 'Percentual de adesão de higiene das mãos realizada pelos profissionais de saúde', 'Percentual', 'meusite\static\Imagens\CCIH\grafico_37.png']}

# Função para rótulos de barras
def rotulos(barras):
    for i in barras:
        h = i.get_height()
        ax.annotate('{:.2f}'.format(h).replace('.', ','),
                    xy = (i.get_x() + i.get_width()/2, h),
                    xytext = (0, 3),
                    textcoords = 'offset points',
                    ha = 'center')

# Função para o tamanho do eixo y
def eixoy(barras):
    if max(barras) == 0:
        ax.set_ylim(0, 0.01)
    else:
        ax.set_ylim(0, max(barras)*1.2)

# Função para os valores do eixo y
def valores(x, pos):
    if pos is not None:
        return '{:.2f}'.format(x).replace('.', ',')
formatter = FuncFormatter(valores)


# Fazendo os gráficos
for i in Indicadores:
    fig, ax = plt.subplots(figsize = (10, 5))
    grafico = ax.bar(df['Mes'], df[Indicadores[i][0]], color = '#52ad1d')
    ax.set_title(Indicadores[i][1])
    ax.yaxis.set_major_formatter(formatter)
    ax.set_ylabel(Indicadores[i][2])
    eixoy(df[Indicadores[i][0]])
    rotulos(grafico)
    plt.savefig(Indicadores[i][3])