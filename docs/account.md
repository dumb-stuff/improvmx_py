# Account
You already setup token. Do you?
<br>
If you aren't please go [back](./setup.md)
<br>
If you are let's go make some requests stuff!
<br>
So this we'll talk about how you can get account data from your token
<br>
If you already setup then you can do these instructions!
<br>
First You need to create instance of Account Because if you didn't you will get errors. Follow me through these steps!
```py
import improvmxpy
improvmxpy.SetUp("token")
account = improvmxpy.Account()
```
Now you can interact with Get Account Stuff Now!
```py
impromxpy.Account().GetAccountDetail()
```
This function don't need arguments
It will return your account data in form of JSON! 
<br>
Something like
```json
{
    "account": {
        "billing_email": null,
        "cancels_on": null,
        "card_brand": "Visa",
        "company_details": "1 Decentralized Street\n92024-2852 California",
        "company_name": "PiedPiper Inc.",
        "company_vat": null,
        "country": "US",
        "created": 1512139382000,
        "email": "richard.hendricks@gmail.com",
        "last4": "1234",
        "limits": {
            "aliases": 10000,
            "daily_quota": 100000,
            "domains": 10000,
            "ratelimit": 10,
            "redirections": 50,
            "subdomains": 2
        },
        "lock_reason": null,
        "locked": null,
        "password": true,
        "plan": {
            "aliases_limit": 10000,
            "daily_quota": 100000,
            "display": "Business - $249",
            "domains_limit": 10000,
            "kind": "enterprise",
            "name": "enterprise249",
            "price": 249,
            "yearly": false
        },
        "premium": true,
        "privacy_level": 1,
        "renew_date": 15881622590000
    },
    "success": true
}
```
*It's not mine tho it is example from their api* [API Documentation Reference](https://improvmx.com/api/#account-details)
<br>
Let's move on!
```py
impromxpy.Account().GetWhiteLabelDomain()
```
This function does not require arguments and this will return list of domain used whitelabel in form of JSON!
```json
{
    "whitelabels": [
        {
            "name": "piedpiper.com"
        }
    ],
    "success": true
}
```
[API Documentation Reference](https://improvmx.com/api/#account-whitelabels)
#### Oops You reached to the end!
