# gerar_visualizacoes.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# --- Configurações dos Gráficos ---
sns.set_theme(style="whitegrid", palette="viridis")
PASTA_GRAFICOS = "graficos"
PASTA_RESULTADOS = "resultados"
os.makedirs(PASTA_GRAFICOS, exist_ok=True)

# --- Funções de Plotagem ---

def plotar_tempo_construcao(df):
    df_melted = df.melt(id_vars='idioma', value_vars=['build_hash_time', 'build_avl_time'],
                        var_name='Estrutura', value_name='Tempo (s)')
    df_melted['Estrutura'] = df_melted['Estrutura'].map({'build_hash_time': 'Tabela Hash', 'build_avl_time': 'Árvore AVL'})

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='idioma', y='Tempo (s)', hue='Estrutura', data=df_melted)
    ax.set_title('Tempo de Construção por Idioma', fontsize=16, pad=20)
    ax.set_xlabel('Idioma', fontsize=12)
    ax.set_ylabel('Tempo (segundos)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "tempo_construcao.png"))
    print(f"Gráfico 'tempo_construcao.png' salvo.")
    plt.close()

def plotar_tempo_busca(df):
    df_melted = df.melt(id_vars='idioma', value_vars=['search_hash_time', 'search_avl_time'],
                        var_name='Estrutura', value_name='Tempo (s)')
    df_melted['Estrutura'] = df_melted['Estrutura'].map({'search_hash_time': 'Tabela Hash', 'search_avl_time': 'Árvore AVL'})
    
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='idioma', y='Tempo (s)', hue='Estrutura', data=df_melted)
    ax.set_title('Tempo de Busca (10.000 operações)', fontsize=16, pad=20)
    ax.set_xlabel('Idioma', fontsize=12)
    ax.set_ylabel('Tempo (segundos)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "tempo_busca.png"))
    print(f"Gráfico 'tempo_busca.png' salvo.")
    plt.close()

# ATUALIZAÇÃO: Esta função agora gera dois gráficos
def plotar_sugestao_individual(df):
    df_melted = df.melt(id_vars='idioma', value_vars=['suggest_1x_hash_time', 'suggest_1x_avl_time'],
                        var_name='Estrutura', value_name='Tempo (s)')
    df_melted['Estrutura'] = df_melted['Estrutura'].map({'suggest_1x_hash_time': 'Tabela Hash', 'suggest_1x_avl_time': 'Árvore AVL'})

    # Gráfico 1: Escala Linear
    plt.figure(figsize=(10, 6))
    ax_linear = sns.barplot(x='idioma', y='Tempo (s)', hue='Estrutura', data=df_melted)
    ax_linear.set_title('Tempo para 1 Sugestão Individual (Escala Linear)', fontsize=16, pad=20)
    ax_linear.set_xlabel('Idioma', fontsize=12)
    ax_linear.set_ylabel('Tempo (segundos)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "tempo_sugestao_1x_linear.png"))
    print(f"Gráfico 'tempo_sugestao_1x_linear.png' salvo.")
    plt.close()

    # Gráfico 2: Escala Logarítmica
    plt.figure(figsize=(10, 6))
    ax_log = sns.barplot(x='idioma', y='Tempo (s)', hue='Estrutura', data=df_melted)
    ax_log.set_title('Tempo para 1 Sugestão Individual (Escala Logarítmica)', fontsize=16, pad=20)
    ax_log.set_xlabel('Idioma', fontsize=12)
    ax_log.set_ylabel('Tempo (segundos)', fontsize=12)
    ax_log.set_yscale('log')
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "tempo_sugestao_1x_log.png"))
    print(f"Gráfico 'tempo_sugestao_1x_log.png' salvo.")
    plt.close()
    
def plotar_sugestao_escala(df):
    df_melted = df.melt(id_vars='idioma', value_vars=['suggest_10x_hash_time', 'suggest_1000x_avl_time'],
                        var_name='Estrutura', value_name='Tempo (s)')
    df_melted['Estrutura'] = df_melted['Estrutura'].map({'suggest_10x_hash_time': 'Tabela Hash (10x)', 'suggest_1000x_avl_time': 'Árvore AVL (1000x)'})

    # Gráfico 1: Escala Linear
    plt.figure(figsize=(10, 6))
    ax_linear = sns.barplot(x='idioma', y='Tempo (s)', hue='Estrutura', data=df_melted)
    ax_linear.set_title('Tempo de Sugestão em Larga Escala (Escala Linear)', fontsize=16, pad=20)
    ax_linear.set_xlabel('Idioma', fontsize=12)
    ax_linear.set_ylabel('Tempo (segundos)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "tempo_sugestao_escala_linear.png"))
    print(f"Gráfico 'tempo_sugestao_escala_linear.png' salvo.")
    plt.close()

    # Gráfico 2: Escala Logarítmica
    plt.figure(figsize=(10, 6))
    ax_log = sns.barplot(x='idioma', y='Tempo (s)', hue='Estrutura', data=df_melted)
    ax_log.set_title('Tempo de Sugestão em Larga Escala (Escala Logarítmica)', fontsize=16, pad=20)
    ax_log.set_xlabel('Idioma', fontsize=12)
    ax_log.set_ylabel('Tempo (segundos)', fontsize=12)
    ax_log.set_yscale('log')
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "tempo_sugestao_escala_log.png"))
    print(f"Gráfico 'tempo_sugestao_escala_log.png' salvo.")
    plt.close()

def plotar_consumo_memoria(df):
    df_melted = df.melt(id_vars='idioma', value_vars=['mem_hash_mb', 'mem_avl_mb'],
                        var_name='Estrutura', value_name='Memória (MB)')
    df_melted['Estrutura'] = df_melted['Estrutura'].map({'mem_hash_mb': 'Tabela Hash', 'mem_avl_mb': 'Árvore AVL'})

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='idioma', y='Memória (MB)', hue='Estrutura', data=df_melted)
    ax.set_title('Pico de Consumo de Memória na Construção', fontsize=16, pad=20)
    ax.set_xlabel('Idioma', fontsize=12)
    ax.set_ylabel('Memória (MB)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(PASTA_GRAFICOS, "consumo_memoria.png"))
    print(f"Gráfico 'consumo_memoria.png' salvo.")
    plt.close()


# --- Script Principal (sem alterações) ---
if __name__ == "__main__":
    ARQUIVO_TEMPO = os.path.join(PASTA_RESULTADOS, "resultados_tempo.json")
    ARQUIVO_MEMORIA = os.path.join(PASTA_RESULTADOS, "resultados_memoria.json")

    if not os.path.exists(ARQUIVO_TEMPO) or not os.path.exists(ARQUIVO_MEMORIA):
        print("Erro: Arquivos de resultado não encontrados.")
        print(f"Por favor, execute 'experimento_tempo.py' e 'experimento_memoria.py' primeiro.")
    else:
        with open(ARQUIVO_TEMPO, 'r') as f:
            dados_tempo = json.load(f)
        with open(ARQUIVO_MEMORIA, 'r') as f:
            dados_memoria = json.load(f)

        df_tempo = pd.DataFrame(dados_tempo)
        df_memoria = pd.DataFrame(dados_memoria)
        df_completo = pd.merge(df_tempo, df_memoria, on=['idioma', 'num_palavras'])

        print("Gerando gráficos a partir dos resultados salvos...")
        
        plotar_tempo_construcao(df_completo)
        plotar_tempo_busca(df_completo)
        plotar_sugestao_individual(df_completo) # Agora gera 2 gráficos
        plotar_sugestao_escala(df_completo)
        plotar_consumo_memoria(df_completo)
        
        print("\nProcesso concluído. Gráficos salvos na pasta 'graficos'.")
        
        print("\n--- Tabela Final em formato Markdown ---")
        df_tabela = df_completo.rename(columns={
            'build_hash_time': 'Build Hash (s)', 'build_avl_time': 'Build AVL (s)',
            'mem_hash_mb': 'Mem Hash (MB)', 'mem_avl_mb': 'Mem AVL (MB)',
            'search_hash_time': 'Search Hash (s)', 'search_avl_time': 'Search AVL (s)',
            'suggest_1x_hash_time': 'Suggest Hash (1x)', 'suggest_1x_avl_time': 'Suggest AVL (1x)',
            'suggest_10x_hash_time': 'Suggest Hash (10x)', 'suggest_1000x_avl_time': 'Suggest AVL (1000x)'
        })
        colunas_tabela = [
            'idioma', 'num_palavras', 'Build Hash (s)', 'Build AVL (s)', 
            'Mem Hash (MB)', 'Mem AVL (MB)', 'Search Hash (s)', 'Search AVL (s)',
            'Suggest Hash (1x)', 'Suggest AVL (1x)', 'Suggest Hash (10x)', 'Suggest AVL (1000x)'
        ]
        
        print(df_tabela[colunas_tabela].to_markdown(index=False, floatfmt=".6f"))