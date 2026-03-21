import polars as pl

# Login using e.g. `huggingface-cli login` to access this dataset
df = pl.read_ndjson('hf://datasets/proj-persona/PersonaHub/math.jsonl')


print(df)