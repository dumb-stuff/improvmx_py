# Domain
You just come through from account section! Let's move on! Again Initialize class
```py
domain = impromxpy.Domain()
```

```py
impromxpy.Domain().ListDomain()
```
This function need 4 arguments
- query = This will find domain with this argument
- is_active = This will find argument that was active or not (Accept only "true" or "false" in string)
- limit = This will limit query search default is 50 
- page = This will scroll through pages default value is 1
Return JSON something like this
```json
{
    "domains": [
        {
            "active": true, 
            "domain": "google.com",
            "display": "google.com",
            "dkim_selector": "dkimprovmx",
            "notification_email": null,
            "whitelabel": null,
            "added": 1559639697000,
            "aliases": [
                {
                    "forward": "sergey@gmail.com", 
                    "alias": "sergey", 
                    "id": 1
                },
                {
                    "forward": "larry@gmail.com", 
                    "alias": "larry", 
                    "id": 2
                }
            ]
        }, 
        {
            "active": true, 
            "domain": "facebook.com",
            "display": "facebook.com",
            "dkim_selector": "dkimprovmx",
            "notification_email": null,
            "whitelabel": null,
            "added": 1559639727000,
            "aliases": [
                {
                    "forward": "mark@facebook-mail.com", 
                    "alias": "*", 
                    "id": 3
                }
            ]
        }, 
        {
            "active": false, 
            "domain": "piedpiper.com",
            "display": "piedpiper.com",
            "dkim_selector": "dkimprovmx",
            "notification_email": null,
            "whitelabel": null,
            "added": 1559639733000,
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
                },
                {
                    "forward": "nelson.bighetti@gmail.com", 
                    "alias": "nelson", 
                    "id": 9
                }
            ]
        }
    ], 
    "total": 3,
    "limit": 50,
    "page": 1,
    "success": true
}
```
[API Dcoumentation Reference](https://improvmx.com/api/#domains-list)
```py
improvmxpy.Domain().AddDomain()
```
This function have 3 arguments
- domain = Required A domain that wanted to add
- notify_email = Choose email that want to send notification
- whitelabel = Parent’s domain that will be displayed for the DNS settings.
Return JSON something like this
```json
{
    "domain": {
        "active": false, 
        "domain": "newdomain.com",
        "display": "newdomain.com",
        "dkim_selector": "dkimprovmx",
        "notification_email": null,
        "whitelabel": null,
        "added": 1559652806000,
        "aliases": [
            {
                "forward": "contact@your-company.tld", 
                "alias": "*", 
                "id": 12
            }
        ]
    }, 
    "success": true
}
```
[API Documentation Reference](https://improvmx.com/api/#domains-add)
```py
improvmxpy.Domain().DomainDetail()
```
This function will get Domain Detial that was in argument Return in json
```json
{
    "domain": {
        "active": false, 
        "domain": "piedpiper.com", 
        "added": 1559639733000, 
        "display": "piedpiper.com",
        "dkim_selector": "dkimprovmx",
        "notification_email": null,
        "whitelabel": null,
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
            },
            {
                "forward": "nelson.bighetti@gmail.com", 
                "alias": "nelson", 
                "id": 9
            }
        ]
    },
    "success": true
}
```
[API Documentation Reference](https://improvmx.com/api/#domain-details)
```py
improvmxpy.Domain().EditDomain()
```
This function allow you to edit domain it need 3 argument
- domain = Required The domain you want to edit
- notify_email = Email where the notifications related to this domain will be sent.
- whitelabel = The parent’s domain owner.
It will return JSON
```json
{
    "domain": {
        "active": false, 
        "domain": "piedpiper.com", 
        "added": 1559639733000, 
        "display": "piedpiper.com",
        "dkim_selector": "dkimprovmx",
        "notification_email": null,
        "whitelabel": "hooli.com",
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
            },
            {
                "forward": "nelson.bighetti@gmail.com", 
                "alias": "nelson", 
                "id": 9
            }
        ]
    },
    "success": true
}
```
[API Documentation Reference](https://improvmx.com/api/#domain-update)
```py
improvmxpy.Domain().DeleteDomain()
```
This function will delete your domain that specified in argument
```
```
It will return true if it is successfully else return false
```
```
[API Documentation Reference](https://improvmx.com/api/#domain-delete)
```py
improvmxpy.Domain().CheckMXDomain()
```
This function will check your dns 