Projeto computaçao na cloud
Microservico de review de pedidos


# Gerar API keys
1. Activar ambiente virtual
2. Executar shell python django
python manage.py shell
3. Gerar uma nova API key:
>>> from rest_framework_api_key.models import APIKey
>>> api_key, generated_key = APIKey.objects.create_key(name="Backend API")
>>> print(generated_key)
4. No postman, entrar em headers e adicionar "x-api-key"
5. Colar a api key no campo