# Aliases
Again Initialize class
```py
aliases = improvmxpy.Aliases()
```
```py
improvmxpy.Aliases().AliasDomainList()
```
List aliases for a given domain need 4 argument
- domain = Required The domain want to list aliases
- q = Search the domains starting by this value.
- is_active = Accept bool return 1 for active else return 0.
- page = Current page to load. 1-based (The first, default page is at page = 1).
Result pretty much like this
```json
{
    "aliases": [
        {
            "forward": "richard.hendricks@gmail.com", 
            "alias": "richard", 
            "id": 4
        },
        {
            "forward": "jared.dunn@gmail.com", 
            "alias": "jared", 
            "id": 5
        },
        {
            "forward": "monica.hall@gmail.com", 
            "alias": "monica", 
            "id": 6
        },
        {
            "forward": "dinesh.chugtai@gmail.com", 
            "alias": "dinesh", 
            "id": 7
        },
        {
            "forward": "bertram.gilfoyle@gmail.com", 
            "alias": "bertram", 
            "id": 8
        }
    ],
    "limit": 5,
    "page": 1,
    "total": 6,
    "success": true
}
```
```py
improvmxpy.Aliases().AddNewAlias()
```
This will add new alias need 2 argument
- domain = Required the domain
- alias = required The name infront of your domain
- forward = required The email wanted to forward