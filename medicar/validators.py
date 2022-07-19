from datetime import datetime

def valida_dia(data_passada) -> bool:
    return data_passada >= datetime.date(datetime.now())
