import pandas as pd
import dash
from dash import dcc, html
from dash import dash_table
import plotly.express as px
from dash.dependencies import Input, Output

# Ajustar a configuração para mostrar todas as colunas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# Função para carregar os dados do arquivo CSV
def load_data(file_path):
    df = pd.read_csv(file_path)  # Carrega os dados
    if df.empty:  # Verifica se o DataFrame está vazio
        raise ValueError("O DataFrame está vazio. Por favor, verifique o arquivo CSV.")
    return df


# Carregar o arquivo CSV contendo os dados da população mundial
df = load_data('C:/Users/diogo/Downloads/WorldPopulation.csv')

# Calcular informações estatísticas sobre a população total
pop_max_total = df['Population'].max()  # População máxima
pop_min_total = df['Population'].min()  # População mínima
pop_mean_total = df['Population'].mean()  # Média da população

# Calcular estatísticas para a população urbana, se a coluna existir
urban_pop_max = urban_pop_min = urban_pop_mean = None
if 'Urban' in df.columns:
    urban_pop_max = df['Urban'].max()  # População urbana máxima
    urban_pop_min = df['Urban'].min()  # População urbana mínima
    urban_pop_mean = df['Urban'].mean()  # Média da população urbana

# Calcular estatísticas para a densidade populacional, se a coluna existir
density_max = density_min = density_mean = None
if 'Density' in df.columns:
    density_max = df['Density'].max()  # Densidade máxima
    density_min = df['Density'].min()  # Densidade mínima
    density_mean = df['Density'].mean()  # Média da densidade

# Configurações do Dash
app = dash.Dash(__name__)


# Função para criar gráfico de pizza
def create_pie_chart(data):
    pie_data = data.groupby('Year')['Population'].sum().reset_index()  # Agrupar dados por ano
    fig = px.pie(pie_data, values='Population', names='Year',
                 title='Distribuição da População Mundial por Ano')  # Criar gráfico de pizza
    return fig  # Retornar a figura


# Função para criar gráfico de barras
def create_bar_chart(data):
    fig = px.bar(data, x='Year', y='Population',
                 title='População Mundial ao Longo dos Últimos Anos',
                 labels={'Population': 'População', 'Year': 'Ano'})  # Criar gráfico de barras
    return fig  # Retornar a figura


# Função para criar gráfico de linhas
def create_line_chart(data):
    fig = px.line(data, x='Year', y='Population',
                  title='Tendência da População Mundial nos Últimos Anos',
                  markers=True)  # Criar gráfico de linhas
    return fig  # Retornar a figura


# Layout do Dash
app.layout = html.Div([
    html.H1("Análise da População Mundial"),  # Título do aplicativo

    # Instruções
    html.Div([
        html.P("Use os sliders abaixo para selecionar o intervalo de anos a serem exibidos nos gráficos.")
    ]),

    # Filtro de intervalo de anos para todos os gráficos
    dcc.RangeSlider(
        id='year-range-slider',  # ID do slider para todos os gráficos
        min=df['Year'].min(),  # Ano mínimo
        max=df['Year'].max(),  # Ano máximo
        value=[df['Year'].min(), df['Year'].max()],  # Valor padrão
        marks={str(year): str(year) for year in range(df['Year'].min(), df['Year'].max() + 1, 5)},
        # Marcas a cada 5 anos
        step=1  # Passo do slider
    ),

    # Seções para os gráficos
    html.Div([
        html.H2("Gráfico de Pizza"),
        dcc.Graph(id='pie-chart'),  # Gráfico de pizza
    ]),

    html.Div([
        html.H2("Gráfico de Barras"),
        dcc.Graph(id='bar-chart'),  # Gráfico de barras
    ]),

    html.Div([
        html.H2("Gráfico de Linhas"),
        dcc.Graph(id='line-chart'),  # Gráfico de linhas
    ]),

    # Seção para exibir estatísticas da população total
    html.Div([
        html.H2("Estatísticas da População Total"),
        html.P(f"População Máxima Total: {pop_max_total:,}"),  # Exibir população máxima
        html.P(f"População Mínima Total: {pop_min_total:,}"),  # Exibir população mínima
        html.P(f"Média da População Total: {pop_mean_total:,.2f}"),  # Exibir média da população
    ]),

    # Seção para exibir estatísticas urbanas, se disponível
    html.Div([
        html.H2("Estatísticas da População Urbana"),
        html.P(
            f"População Urbana Máxima: {urban_pop_max:,}" if urban_pop_max is not None else "Dados de população urbana não disponíveis."),
        html.P(
            f"População Urbana Mínima: {urban_pop_min:,}" if urban_pop_min is not None else "Dados de população urbana não disponíveis."),
        html.P(
            f"Média da População Urbana: {urban_pop_mean:,.2f}" if urban_pop_mean is not None else "Dados de população urbana não disponíveis."),
    ]),

    # Seção para exibir estatísticas da densidade populacional, se disponível
    html.Div([
        html.H2("Estatísticas da Densidade Populacional"),
        html.P(
            f"Densidade Máxima: {density_max:,.2f}" if density_max is not None else "Dados de densidade não disponíveis."),
        html.P(
            f"Densidade Mínima: {density_min:,.2f}" if density_min is not None else "Dados de densidade não disponíveis."),
        html.P(
            f"Média da Densidade: {density_mean:,.2f}" if density_mean is not None else "Dados de densidade não disponíveis."),
    ]),

    # Dropdown para selecionar o número de linhas a serem exibidas na tabela
    html.Div([
        html.H2("Selecionar Número de Linhas a Exibir:"),
        dcc.Dropdown(
            id='num-rows-dropdown',  # ID do dropdown
            options=[{'label': str(i), 'value': i} for i in [5, 10, 20, 50, 70, len(df)]],  # Opções de linhas
            value=10,  # Valor padrão
            clearable=False  # Não permitir limpeza do dropdown
        )
    ]),

    # Seção para exibir os dados em formato tabular
    html.Div([
        html.H2("Dados da População Mundial"),
        dash_table.DataTable(
            id='population-table',  # ID da tabela
            data=df.to_dict('records'),  # Converter DataFrame para dicionário
            columns=[{"name": i, "id": i} for i in df.columns],  # Definir colunas da tabela
            page_size=10,  # Número de linhas por página
            filter_action='native',  # Habilitar filtragem
            sort_action='native',  # Habilitar ordenação
            style_table={'overflowX': 'auto'},  # Permitir rolagem horizontal
        )
    ])
])


# Callbacks para atualizar os gráficos com base na seleção do slider de anos
@app.callback(
    Output('pie-chart', 'figure'),  # Atualizar o gráfico de pizza
    Output('bar-chart', 'figure'),  # Atualizar o gráfico de barras
    Output('line-chart', 'figure'),  # Atualizar o gráfico de linhas
    Input('year-range-slider', 'value')  # Obter valor do slider de anos
)
def update_charts(selected_years):
    # Filtrar dados com base no intervalo de anos selecionado
    filtered_data = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]

    # Retornar os gráficos atualizados
    return create_pie_chart(filtered_data), create_bar_chart(filtered_data), create_line_chart(filtered_data)


# Callback para atualizar a tabela com base na seleção do dropdown
@app.callback(
    Output('population-table', 'page_size'),  # Atualizar o tamanho da página da tabela
    Input('num-rows-dropdown', 'value')  # Obter valor do dropdown
)
def update_table_size(selected_size):
    return selected_size  # Retornar o tamanho selecionado


# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)  # Executar o aplicativo em modo de depuração