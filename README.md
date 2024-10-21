Dashboard de Análise da População Mundial
Visão Geral
Este dashboard oferece uma maneira interativa de analisar dados populacionais mundiais usando Dash e Plotly. Os usuários podem visualizar as tendências populacionais por meio de gráficos de pizza, barras e linhas, além de acessar estatísticas importantes sobre as populações total, urbana e densidade.

Recursos
Gráficos Interativos: Os usuários podem filtrar dados por ano usando um slider de intervalo, que atualiza as visualizações dinamicamente.
Estatísticas Populacionais: Exibe valores máximos, mínimos e médios da população, tanto para a população total quanto urbana, juntamente com estatísticas de densidade, se disponíveis.
Tabela de Dados: Os usuários podem selecionar quantas linhas de dados exibir em formato de tabela, que suporta ordenação e filtragem.
Requisitos
Para executar este aplicativo, você precisa das seguintes bibliotecas instaladas:

pandas
dash
plotly
Você pode instalá-las usando o pip:

bash
Copiar código
pip install pandas dash plotly
Fonte de Dados
Este aplicativo requer um arquivo CSV contendo dados da população mundial. O formato esperado do arquivo inclui as seguintes colunas:

Year: O ano da entrada de dados.
Population: A população total para aquele ano.
Urban: A população urbana (se disponível).
Density: A densidade populacional (se disponível).
Certifique-se de que o arquivo CSV esteja formatado corretamente e localizado no caminho especificado no código (por exemplo, C:/Users/diogo/Downloads/WorldPopulation.csv).

Executando o Aplicativo
Clone ou faça o download deste repositório.
Navegue até o diretório do projeto.
Execute o aplicativo:
bash
Copiar código
python app.py
Abra seu navegador e vá para http://127.0.0.1:8050 para visualizar o dashboard.
Uso
Use o slider de intervalo para selecionar os anos de interesse.
Veja os gráficos de pizza, barras e linhas atualizados refletindo o intervalo de dados selecionado.
Verifique a seção de estatísticas para obter insights populacionais chave.
Ajuste o dropdown para controlar o número de linhas exibidas na tabela de dados.
Contribuindo
Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request.

Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.

Se precisar de mais alguma coisa, é só avisar!
