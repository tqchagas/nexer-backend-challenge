# nexer-backend-challenge
## Requerimentos
* Django
* Django rest framework
* Requests
```
pip install -r requirements.txt
```

## Testes
```
./manage.py test api
```

## Aplicação
```
./manage.py runserver
```

## Endpoints
```
curl -XGET 'http://127.0.0.1:8000/api/reservas/?data=2017-05-03'
curl -XDELETE 'http://127.0.0.1:8000/api/reservas/?data=2017-05-03'

```
