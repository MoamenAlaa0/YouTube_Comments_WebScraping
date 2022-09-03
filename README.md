# :arrow_forward: YouTube Comments Web Scraping
Applying JavaScript command in the console to get the scroll Height.  
**JavaScript command:** `document.documentElement.scrollHeight`

Another way by using [requests_html](https://requests.readthedocs.io/projects/requests-html/en/latest/) library:
``` python
from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://www.youtube.com/watch?v=w8yWXqWQYmU')

script = '() => {return document.documentElement.scrollHeight}'
scroll_height = response.html.render(script=script, sleep=3, timeout=50000)
```
