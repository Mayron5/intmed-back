# Desafio IntMed - Backend

### Pre-requisitos

- Primeiro crie um ambiente virtual e ative ele:
```console
python3 -m venv ./venv
venv\Scripts\activate -> comando para windows
```
- Após isso, instale as dependências do projeto com o comando:

```console
pip install -r requirements.txt
```

---
### Rodando a aplicacao

- Para iniciar a aplicacao, insira o seguinte comando:

```console
python manage.py runserver
```

Com a aplicacao iniciada, acesse a pagina:

<a href='http://127.0.0.1:8000/admin'>Pagina de administracao da aplicacao</a>

Nela o administrador podera popular dados, exclui-los e edita-los.

---

As rotas podem ser visualizadas em setup/urls.py
Elas foram criadas de acordo com a necessidade dos dados no frontend.

