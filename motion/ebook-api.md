# Fake e-book data

## URL for Author page

https://api.ebooks.com/authors/b8a99e2

## Fake Response

```json
{
    "uri": "/authors/b8a99e2",
    "author_id": "b8a99e2",
    "name": "Joanne Lipman",
    "books": [
        {
            "title": "That's What She Said: What Men Need to Know (and Women Need to Tell Them) About Working Together",
            "uri": "/books/B0716GZT1P",
            "alternate_url": "https://www.amazon.com/gp/product/B0716GZT1P/"
        }
    ]
}
```

## Python loading json

```python
>>> import json
>>> author = json.loads(json_response)
>>> author['name']
'Joanne Lipman'
>>> author['books'][0]['title']
"That's What She Said: What Men Need to Know (and Women Need to Tell Them) About Working Together"
```
