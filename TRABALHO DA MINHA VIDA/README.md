# Sistema de Análise de Viagens Corporativas - Instituto Aquila

Sistema dinâmico baseado em JSON para análise de dados de viagens corporativas.

## Arquitetura do Projeto

```
projeto/
├── index.html              # Dashboard principal
├── pessoa.html             # Análise detalhada por pessoa
├── css/
│   └── style.css          # Estilos principais
├── js/
│   ├── app.js             # Lógica do dashboard
│   └── pessoa.js          # Lógica da análise por pessoa
├── data/
│   └── dados.json         # Dados dinâmicos em JSON
├── processador_csv_para_json.py  # Script Python para conversão CSV→JSON
└── README.md
```

## Funcionalidades

### Dashboard (index.html)
- Visualização geral das viagens
- Total de viagens e valor total
- Lista de todas as pessoas com dados de viagens
- Links para análise detalhada por pessoa

### Análise por Pessoa (pessoa.html)
- Detalhes das viagens de uma pessoa específica
- Ranking de passageiros por quantidade e valor
- Análise de rotas utilizadas
- Informações detalhadas por rota

## Pipeline de Dados

```
CSV → Python → JSON → Site HTML/JS
```

O script `processador_csv_para_json.py` converte arquivos CSV em um único arquivo JSON que alimenta o sistema.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript puro
- **Backend**: Python (pandas, json)
- **Dados**: JSON dinâmico

## Requisitos Técnicos

- Nenhum dado fixo em HTML
- Todos os dados vêm do JSON
- Sistema adapta-se automaticamente a mudanças no JSON
- Uso de fetch(), reduce(), filter(), map(), URLSearchParams
- Criação dinâmica de elementos DOM
- Agrupamento por pessoa e por rota

## Como Executar

1. Coloque seus arquivos CSV no diretório `csv_entrada/`
2. Execute o script Python: `python processador_csv_para_json.py`
3. Abra `index.html` em seu navegador

## Estrutura do JSON

O sistema espera um JSON com a seguinte estrutura:

```json
[
  {
    "empresa": "INSTITUTO AQUILA DE GESTAO LTDA",
    "passageiro": "PIRES JUNIOR/JOAO",
    "cidade_origem": "Belo Horizonte",
    "cidade_destino": "Recife",
    "data_partida": "20/10/2025",
    "cia_aerea": "AZUL LINHAS AEREAS BRASILEIRAS SA",
    "valor_total": 2751.98,
    "origem_destino": "CNF/REC",
    ...
  }
]
```

## Características do Sistema

- **Orientado a dados**: Toda a interface é gerada dinamicamente a partir do JSON
- **Escalável**: Novas pessoas, rotas ou viagens não exigem alterações de código
- **Autônomo**: O sistema se adapta automaticamente quando o JSON muda
- **Sem frameworks**: Apenas tecnologias web nativas
- **Preparado para crescimento**: Arquitetura modular e expansível