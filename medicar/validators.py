from datetime import datetime


def valida_dia(data_passada, hora_passada: str) -> bool:
    data_texto: str = data_passada.strftime('%d/%m/%Y')
    data_formatada = '{} {}'.format(data_texto, hora_passada)
    data_objeto = datetime.strptime(data_formatada, '%d/%m/%Y %H:%M:%S')
    
    
    return data_objeto >= datetime.now()