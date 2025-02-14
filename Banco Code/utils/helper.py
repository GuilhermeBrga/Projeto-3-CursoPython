from datetime import date
from datetime import datetime

def data_str(data: date) -> str:
    return data.strftime("%d/%m/%Y")

def str_data(data: str) -> date:
    return datetime.strptime(data, "%d/%m/%Y")

def formata_float_str_moeda(valor: float) -> str:

    return f"R$ {valor:.2f}"

