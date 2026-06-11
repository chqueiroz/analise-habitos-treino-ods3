import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("graficos", exist_ok=True)
df = pd.read_csv("resultados_pesquisa.csv", encoding="utf-8-sig")


total_participantes = df.shape[0]
print(f"Total de participantes: {total_participantes}")


print("\n--- Idade ---")
media_idade = df["idade"].mean()
print(f"Média: {media_idade:.0f} anos")
mediana_idade = df["idade"].median()
print(f"Mediana: {mediana_idade:.0f} anos")
desv_pad_idade = df["idade"].std()
print(f"Desvio padrão: {desv_pad_idade:.1f} anos")
print(f"Faixa etária: mínima de {df['idade'].min()}, máxima de {df['idade'].max()}")
print(f"Com uma média de {media_idade:.0f} anos e desvio padrão de {desv_pad_idade:.1f} podemos ver que o público da pesquisa possui idades variadas.")


print("\n--- Gênero ---")
genero_df = (
    df["sexo"]
    .value_counts()
    .reset_index()
    .rename(columns={"sexo": "Gênero", "count": "Quantidade"})
)
total_genero = genero_df["Quantidade"].sum()
genero_df["(%)"] = (genero_df["Quantidade"] / total_genero * 100).round(1)
print(genero_df.to_string(index=False))
print("A distribuição por gênero permite observar a composição da amostra analisada.")


print("\n--- Frequência de treino por semana ---")
dias_treino_df = (
    df["dias_treino"]
    .value_counts()
    .reset_index()
    .rename(columns={'dias_treino': 'Dias de treino', 'count': 'Quantidade'})
)
print(dias_treino_df.to_string(index=False))
media_dias_treino = df["dias_treino"].mean()
print(f"Média: {media_dias_treino:.1f} dias por semana")
moda_dias_treino = df["dias_treino"].mode()[0]
print(f"Moda: {moda_dias_treino:.0f}")
print(f"Os participantes apresentaram distribuição entre 2 e 6 dias de treino semanais, com predominância de {moda_dias_treino} dias por semana.")


print("\n--- Consistência de treino(%) ---")
porcentagens = df["consistente"].value_counts(normalize=True) * 100
print(f"Sim: {porcentagens['Sim']:.1f}")
print(f"Não: {porcentagens['Não']:.1f}")
print("A maioria dos participantes considera sua rotina de treino consistente.")


print("\n--- Objetivo dos participantes ---")
objetivo_df = (
    df["objetivo"]
    .value_counts()
    .reset_index()
    .rename(columns={"objetivo": "Objetivo", "count": "Quantidade"})
)
total_obj = objetivo_df["Quantidade"].sum()
objetivo_df["(%)"] = (objetivo_df["Quantidade"] / total_obj * 100).round(1)
print(objetivo_df.to_string(index=False))
print("A hipertrofia foi o objetivo mais frequente entre os participantes, representando 33% da amostra.")


print("\n--- Experiência dos participantes ---")
experiencia_df = (
    df["experiencia"]
    .value_counts()
    .reset_index()
    .rename(columns={"experiencia": "Experiência", "count": "Quantidade"})
)
total_exp = experiencia_df["Quantidade"].sum()
experiencia_df["(%)"] = (experiencia_df["Quantidade"] / total_exp * 100).round(1)
print(experiencia_df.to_string(index=False))
print("A maior parte dos pesquisados são recentes na academia, o que pode sugerir uma tendência em suas respostas.")


print("\n--- Distribuição das Idades dos Participantes ---")
plt.figure(figsize=(10, 5))
plt.hist(
    df["idade"],
    bins=8,
    edgecolor="black")
plt.axvline(
    media_idade,
    color="red",
    linestyle="--",
    label=f"Média: {media_idade:.1f} anos")
plt.title("Distribuição das Idades dos Participantes")
plt.xlabel("Idade (anos)")
plt.ylabel("Quantidade de participantes")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig(
    "graficos/distribuicao_idades.png",
    dpi=300,
    bbox_inches="tight")
plt.show()


print("\n--- Gráfico: Frequência semanal de treinos ---")
dias_treino_grafico = (
    df["dias_treino"]
    .value_counts()
    .sort_index())
plt.figure(figsize=(10, 5))
barras = plt.bar(
    dias_treino_grafico.index,
    dias_treino_grafico.values,
    edgecolor="black")
plt.title("Distribuição da Frequência Semanal de Treinos")
plt.xlabel("Dias de treino por semana")
plt.ylabel("Quantidade de participantes")
plt.xticks([2, 3, 4, 5, 6])
plt.grid(axis="y", linestyle="--", alpha=0.5)
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.2,
        str(int(altura)),
        ha="center")
plt.tight_layout()
plt.savefig(
    "graficos/frequencia_semanal_treinos.png",
    dpi=300,
    bbox_inches="tight")
plt.show()


print("\n--- Gráfico: Objetivos dos participantes ---")
objetivos_grafico = (
    df["objetivo"]
    .value_counts()
    .sort_values())
plt.figure(figsize=(10, 5))
barras = plt.barh(
    objetivos_grafico.index,
    objetivos_grafico.values,
    edgecolor="black")
plt.title("Objetivos dos Participantes")
plt.xlabel("Quantidade de participantes")
plt.ylabel("Objetivo")
plt.grid(axis="x", linestyle="--", alpha=0.5)
for barra in barras:
    largura = barra.get_width()
    plt.text(
        largura + 0.2,
        barra.get_y() + barra.get_height()/2,
        str(int(largura)),
        va="center")
plt.tight_layout()
plt.savefig(
    "graficos/objetivos_participantes.png",
    dpi=300,
    bbox_inches="tight")
plt.show()


print("\n--- Gráfico: Consistência dos treinos ---")
consistencia_grafico = df["consistente"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    consistencia_grafico.values,
    labels=consistencia_grafico.index,
    autopct="%1.1f%%",
    startangle=90)
plt.title("Consistência dos Treinos")
plt.tight_layout()
plt.savefig(
    "graficos/consistencia_treinos.png",
    dpi=300,
    bbox_inches="tight")
plt.show()

print("\n--- ANÁLISE CONCLUÍDA ---")
print("Gráficos salvos na pasta 'graficos'.")
print("Resultados prontos para inclusão no relatório.")