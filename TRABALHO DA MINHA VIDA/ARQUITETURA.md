# Arquitetura do Sistema de Análise de Viagens

## Visão Geral

Este é um sistema de análise de dados de viagens corporativas baseado em uma arquitetura orientada a dados (JSON-driven), projetado para transformar dados estáticos em um sistema dinâmico completamente controlado por dados externos.

## Componentes do Sistema

### 1. Pipeline de Dados

**CSV → Python → JSON → Site HTML/JS**

- **Entrada**: Arquivos CSV com dados de viagens
- **Processamento**: Script Python (`processador_csv_para_json.py`) converte CSV em JSON
- **Armazenamento**: Arquivo `/data/dados.json` com todos os dados estruturados
- **Visualização**: Interfaces HTML dinâmicas que consomem o JSON

### 2. Frontend

#### Dashboard (index.html)
- Mostra estatísticas gerais de todas as viagens
- Lista todas as pessoas com links para análise detalhada
- Calcula dinamicamente totais sem dados fixos

#### Análise por Pessoa (pessoa.html)
- Análise detalhada para uma pessoa específica
- Ranking de passageiros por quantidade e valor
- Análise de rotas utilizadas
- Detalhes de cada viagem

### 3. Backend (Python)

Script `processador_csv_para_json.py`:
- Lê múltiplos arquivos CSV
- Converte valores monetários do formato brasileiro
- Combina todos os dados em um único JSON
- Gera estrutura compatível com o frontend

## Arquitetura de Dados

### Estrutura do JSON

O sistema trabalha com um array de objetos, onde cada objeto representa uma viagem com os seguintes campos:

```json
{
  "empresa": "string",
  "passageiro": "string",
  "cidade_origem": "string",
  "cidade_destino": "string",
  "data_partida": "string",
  "cia_aerea": "string",
  "valor_total": "number",
  "origem_destino": "string",
  "tipo": "string",
  ...
}
```

### Agrupamentos Dinâmicos

O sistema implementa agrupamentos dinâmicos:
- Por pessoa (para análise individual)
- Por rota (para análise de rotas)
- Por companhia aérea
- Por período

## Princípios Arquiteturais

### 1. Zero Dados Fixos
- Nenhum valor hard-coded em HTML ou JS
- Toda informação vem do JSON
- Interface se adapta automaticamente a mudanças de dados

### 2. Escalabilidade
- Suporte a novas pessoas sem alteração de código
- Suporte a novas rotas sem alteração de código
- Sistema se expande automaticamente com crescimento do JSON

### 3. Manutenibilidade
- Código JavaScript bem comentado
- Separação clara de responsabilidades
- Estrutura modular e reutilizável

### 4. Desempenho
- Uso eficiente de métodos como `reduce()`, `filter()`, `map()`
- Carregamento único do JSON
- Renderização otimizada de elementos DOM

## Segurança e Confiabilidade

- Tratamento adequado de erros
- Conversão segura de valores monetários
- Validação de dados de entrada
- Recuperação de falhas na leitura de dados

## Extensibilidade

O sistema foi projetado para fácil expansão:
- Adição de novas visualizações
- Integração com APIs externas
- Exportação de relatórios
- Filtros avançados

## Tecnologias

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Backend**: Python com Pandas
- **Formato de Dados**: JSON
- **Sem frameworks**: Apenas tecnologias nativas

## Benefícios do Sistema

1. **Automação**: Atualização automática com novos dados
2. **Visibilidade**: Insights claros sobre despesas de viagem
3. **Controle**: Gestão centralizada de todas as informações
4. **Adaptabilidade**: Sistema se ajusta a diferentes formatos de dados
5. **Eficiência**: Análise rápida e precisa dos dados de viagem

Esta arquitetura permite que o Instituto Aquila tenha um sistema de análise de viagens corporativas robusto, escalável e totalmente orientado a dados.