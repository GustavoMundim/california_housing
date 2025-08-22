from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "data"


DADOS_ORIGINAIS = PASTA_DADOS / "external/housing.csv.zip"
DADOS_TRATADOS = PASTA_DADOS / "processed/housing_data_fix.parquet"


MODELO_FINAL = PASTA_PROJETO / "model/ridge_polyfeat_target_quantile.joblib"
