import matplotlib.pyplot as plt
import seaborn as sns



def plot_model_metrics(data):
    fig, axs = plt.subplots(2, 2, figsize=(8, 8), sharex=True)

    comparar_metricas = [
        "time_seconds",
        "test_r2",
        "test_neg_mean_absolute_error",
        "test_neg_root_mean_squared_error",
    ]
    
    nomes_metricas = [
        "Tempo (s)",
        "R2",
        "MAE",
        "RMSE"
    ]




    for ax, metrica, nome in zip(axs.flatten(), comparar_metricas, nomes_metricas):
        sns.boxplot(
            x="model",
            y=metrica,
            data=data,
            ax=ax,
            showmeans=True
        )
        ax.set_title(nome)
        ax.set_ylabel(nome)
        ax.tick_params(axis="x", rotation=90)
    
    plt.tight_layout()
    plt.show()
