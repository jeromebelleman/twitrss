Sample `~/.twitrss/twitrss.yaml` file:

```
url: "http://example.com/rss"

auth:
    consumer-key: "foo"
    consumer-secret: "bar"
    access-token: "baz"
    access-token-secret: "boo"

run:
    dryrun: true
    debug: true
    notrack: false

    sleep: 3600 # In seconds, don't loop if unset
    daemon: false

tweet:
    limit: 140
    url: "http://example.com"
    title: true
    specials:
        "January": "Jan"
        "February": "Feb"
        "March": "Mar"
        "April": "Apr"
        "May": "May"
        "June": "Jun"
        "July": "Jul"
        "August": "Aug"
        "September": "Sep"
        "October": "Oct"
        "November": "Nov"
        "December": "Dec"

        "Monday": "Mon"
        "Tuesday": "Tue"
        "Wednesday": "Wed"
        "Thursday": "Thu"
        "Friday": "Fri"
        "Saturday": "Sat"
        "Sunday": "Sun"
```
