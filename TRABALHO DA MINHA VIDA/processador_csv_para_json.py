#!/usr/bin/env python3
# Script para processar arquivos CSV e converter em um único arquivo JSON
# Este script faz parte do pipeline: CSV → Python → JSON → Site HTML/JS

import pandas as pd
import json
import os
import sys
from pathlib import Path


def br_to_float(value):
    """
    Converte valores monetários em formato brasileiro para float
    Ex: '1.234,56' -> 1234.56
    """
    if pd.isna(value) or value == '' or value is None:
        return 0.0
    
    # Converter para string e substituir vírgula por ponto
    str_value = str(value).replace('.', '').replace(',', '.')
    try:
        return float(str_value)
    except ValueError:
        return 0.0


def process_csv_to_json(csv_file_path, output_json_path):
    """
    Processa um arquivo CSV e converte para o formato JSON adequado
    """
    try:
        # Definir os nomes das colunas corretos
        headers = [
            "Empresa", "Mês/Ano", "Data Emissão ", "Dia Semana Em.", "Identificação", "OS", "Mercado",
            "Cia. Aerea", "Matricula", "Passageiro", "Top 10", "Centro Custo", "Data Partida",
            "Dia Semana Voo", "Tipo de Cabine", "Processos", "Origem/Destino", "Cidade Origem",
            "Cidade Destino", "Itinerário", "Tarifa Aplicada", "Taxas", "Fee", "Valor Total",
            "Tipo", "Faixa de Antecedência", "Antecedência de Compra", "Politica de Antecedência",
            "Política", "MédiaDentroPolitica", "MédiaForaPolítica", "PerdaForaPolítica", "Fatura"
        ]
        
        # Lê o arquivo CSV com separador ';' e sem cabeçalho
        df = pd.read_csv(csv_file_path, sep=';', header=None, names=headers)
        
        # Processa os dados
        processed_data = []
        for index, row in df.iterrows():
            record = {
                "empresa": row['Empresa'],
                "mes_ano": row['Mês/Ano'],
                "data_emissao": row['Data Emissão '],
                "dia_semana_em": row['Dia Semana Em.'],
                "identificacao": row['Identificação'],
                "os": row['OS'],
                "mercado": row['Mercado'],
                "cia_aerea": row['Cia. Aerea'],
                "matricula": row['Matricula'],
                "passageiro": row['Passageiro'],
                "top_10": row['Top 10'],
                "centro_custo": row['Centro Custo'],
                "data_partida": row['Data Partida'],
                "dia_semana_voo": row['Dia Semana Voo'],
                "tipo_cabine": row['Tipo de Cabine'],
                "processos": row['Processos'],
                "origem_destino": row['Origem/Destino'],
                "cidade_origem": row['Cidade Origem'],
                "cidade_destino": row['Cidade Destino'],
                "itinerario": row['Itinerário'],
                "tarifa_aplicada": br_to_float(row['Tarifa Aplicada']),
                "taxas": br_to_float(row['Taxas']),
                "fee": br_to_float(row['Fee']),
                "valor_total": br_to_float(row['Valor Total']),
                "tipo": row['Tipo'],
                "faixa_antecedencia": row['Faixa de Antecedência'],
                "antecedencia_compra": row['Antecedência de Compra'],
                "politica_antecedencia": row['Politica de Antecedência'],
                "politica": row['Política'],
                "media_dentro_politica": br_to_float(row['MédiaDentroPolitica']),
                "media_fora_politica": br_to_float(row['MédiaForaPolítica']),
                "perda_fora_politica": br_to_float(row['PerdaForaPolítica']),
                "fatura": row['Fatura']
            }
            processed_data.append(record)
        
        # Cria o diretório de saída se não existir
        output_dir = os.path.dirname(output_json_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Escreve o arquivo JSON
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        
        print(f'Sucesso: Arquivo JSON criado em {output_json_path}')
        print(f'Total de registros processados: {len(processed_data)}')
        
        return True
        
    except Exception as e:
        print(f'Erro ao processar o arquivo {csv_file_path}: {str(e)}')
        return False


def main():
    # Define os caminhos padrão
    input_dir = './csv_entrada'  # Diretório onde estão os arquivos CSV
    output_path = './data/dados.json'  # Caminho do arquivo JSON de saída
    
    # Se argumentos forem passados, usa-os
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    
    # Verifica se o diretório de entrada existe
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f'Diretório de entrada não encontrado: {input_dir}')
        print('Criando diretório de exemplo...')
        input_path.mkdir(parents=True, exist_ok=True)
        print(f'Diretório criado: {input_dir}')
        return
    
    # Procura por arquivos CSV no diretório
    csv_files = list(input_path.glob('*.csv'))
    
    if not csv_files:
        print(f'Nenhum arquivo CSV encontrado em: {input_dir}')
        return
    
    print(f'Encontrados {len(csv_files)} arquivos CSV para processar.')
    
    # Combina todos os dados dos CSVs em uma única lista
    all_data = []
    
    for csv_file in csv_files:
        print(f'Processando: {csv_file.name}')
        
        try:
            # Definir os nomes das colunas corretos
            headers = [
                "Empresa", "Mês/Ano", "Data Emissão ", "Dia Semana Em.", "Identificação", "OS", "Mercado",
                "Cia. Aerea", "Matricula", "Passageiro", "Top 10", "Centro Custo", "Data Partida",
                "Dia Semana Voo", "Tipo de Cabine", "Processos", "Origem/Destino", "Cidade Origem",
                "Cidade Destino", "Itinerário", "Tarifa Aplicada", "Taxas", "Fee", "Valor Total",
                "Tipo", "Faixa de Antecedência", "Antecedência de Compra", "Politica de Antecedência",
                "Política", "MédiaDentroPolitica", "MédiaForaPolítica", "PerdaForaPolítica", "Fatura"
            ]
            
            # Lê o arquivo CSV
            df = pd.read_csv(csv_file, sep=';', header=None, names=headers)
            
            # Processa os dados
            for index, row in df.iterrows():
                record = {
                    "empresa": row['Empresa'],
                    "mes_ano": row['Mês/Ano'],
                    "data_emissao": row['Data Emissão '],
                    "dia_semana_em": row['Dia Semana Em.'],
                    "identificacao": row['Identificação'],
                    "os": row['OS'],
                    "mercado": row['Mercado'],
                    "cia_aerea": row['Cia. Aerea'],
                    "matricula": row['Matricula'],
                    "passageiro": row['Passageiro'],
                    "top_10": row['Top 10'],
                    "centro_custo": row['Centro Custo'],
                    "data_partida": row['Data Partida'],
                    "dia_semana_voo": row['Dia Semana Voo'],
                    "tipo_cabine": row['Tipo de Cabine'],
                    "processos": row['Processos'],
                    "origem_destino": row['Origem/Destino'],
                    "cidade_origem": row['Cidade Origem'],
                    "cidade_destino": row['Cidade Destino'],
                    "itinerario": row['Itinerário'],
                    "tarifa_aplicada": br_to_float(row['Tarifa Aplicada']),
                    "taxas": br_to_float(row['Taxas']),
                    "fee": br_to_float(row['Fee']),
                    "valor_total": br_to_float(row['Valor Total']),
                    "tipo": row['Tipo'],
                    "faixa_antecedencia": row['Faixa de Antecedência'],
                    "antecedencia_compra": row['Antecedência de Compra'],
                    "politica_antecedencia": row['Politica de Antecedência'],
                    "politica": row['Política'],
                    "media_dentro_politica": br_to_float(row['MédiaDentroPolitica']),
                    "media_fora_politica": br_to_float(row['MédiaForaPolítica']),
                    "perda_fora_politica": br_to_float(row['PerdaForaPolítica']),
                    "fatura": row['Fatura']
                }
                all_data.append(record)
        
        except Exception as e:
            print(f'Erro ao processar {csv_file.name}: {str(e)}')
    
    # Cria o diretório de saída se não existir
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Escreve o arquivo JSON combinado
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f'\nSucesso: Arquivo JSON combinado criado em {output_path}')
    print(f'Total de registros combinados: {len(all_data)}')


if __name__ == '__main__':
    main()