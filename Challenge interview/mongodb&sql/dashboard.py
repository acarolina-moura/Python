import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Comparação entre MongoDB e SQL Server"),
    
    html.Div([
        html.H2("MongoDB (Não Relacional)"),
        html.H3("Eventual Consistency"),
        html.P("Significa que a disponibilidade ocorre em detrimento da consistência."),
        
        html.H3("Propósito"),
        html.P("Em sistemas distribuídos, é possível que algumas partes estejam temporariamente indisponíveis ou atrasadas na atualização dos dados para manter a disponibilidade."),
        
        html.H3("Abordagem do MongoDB"),
        html.P("Significa que os dados são sempre disponibilizados em conjunto. Seu uso e estrutura éclear voltado para a aplicação, ele dita como a app vai funcionar."),
        html.P("Para isso, é preciso entender como funciona a app, o que os usuários mais vão consumir, o que o cliente precisa, para que assim o desenvolvedor estruture o modelo de dados e defina coleções."),
    ], style={'width': '45%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-right': '5%'}),
    
    html.Div([
        html.H2("SQL Relacional"),
        html.H3("Strong Consistency"),
        html.P("Consistência dos dados em função da disponibilidade dos dados."),
        
        html.H3("Propósito"),
        html.P("O SQL relacional é projetado para garantir integridade e consistência dos dados por meio de transações ACID (Atomicidade, Consistência, Isolamento e Durabilidade)."),
        
        html.H3("Abordagem do SQL"),
        html.P("Trabalha de forma reversa ao MongoDB. O modelo de dados é quem define como a aplicação funcionará. A estrutura das tabelas e as relações entre elas são fundamentais para o design da aplicação."),
        
        html.H2("SQL SERVER"),
        html.P("A maior diferença entre SQL Server é a possibiliadde de usar os dados tanto em um servidor local quanto em nuvem. E ele tem mais funcionalidades pensadas na segurança dos dados, como autenticação, autorização até criptografia de dados."),
    ], style={'width': '45%', 'display': 'inline-block', 'vertical-align': 'top'}),
    
    html.Div([
        html.Div([
            html.Img(src='../assets/mongodb.jpg', style={'width': '80%'}),
            html.P("Estrutura MongoDB", style={'text-align': 'center', 'margin-top': '5px'}),
        ], style={'text-align': 'center'}),
    ], style={'width': '45%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-right': '5%'}),
    
    html.Div([
        html.Div([
            html.Img(src='/assets/server.jpg', style={'width': '80%'}),
            html.P("Estrutura SQL Server", style={'text-align': 'center', 'margin-top': '5px'}),
        ], style={'text-align': 'center'}),
    ], style={'width': '45%', 'display': 'inline-block', 'vertical-align': 'top'}),
    
    html.Link(
        rel='stylesheet',
        href='/assets/styles.css'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
