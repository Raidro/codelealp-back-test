# Backend teste for codeleap

## Repositorio feito para a vaga de backedn da codeleap - usando Python, Django e DRF(Django Rest Framework)
 
### Server data structure

### **Please note: due to how Django works, a finishing slash “/” is required. Failure to include so could cause CORS related issues.**

The base backend url is: `https://dev.codeleap.co.uk/careers/`

The item data structure is as follows:

```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
``` 


To create a post, send a POST http request with the data structure below. Remember we don’t have an ID yet:

POST to `https://dev.codeleap.co.uk/careers/`

The item data structure is as follows:

```json
{
    "username": "string",
    "title": "string",
    "content": "string"
}
```

To get the list of posts, hit the server with the following GET request. This is an example of what will return from the server:

GET to `https://dev.codeleap.co.uk/careers/`

The item data structure is as follows:

```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
```

To update an item, hit the server with the PATCH request below. Note that we must send the ID in the URL this time too. You cannot change the “id”, “username” or “created_datetime” properties.

PATCH to `https://dev.codeleap.co.uk/careers/{OBJECT_ID}/`

The item data structure is as follows:

```json
{
    "title": "string",
    "content": "string"
}
```


Last but not least, to delete an item simply hit the server with a DELETE request with the ID in the url. Please note nothing will return from the server.

DELETE to `https://dev.codeleap.co.uk/careers/{OBJECT_ID}/`

The item data structure is as follows:

```json
{}
```
