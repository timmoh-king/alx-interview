## 0x00. Pascal's Triangle

Write a script that reads `stdin` line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
    - Total file size: `File size: <total size>`
    - where `<total size>` is the sum of all previous `<file size>` (see input format above)
    - Number of lines by status code:
        - possible status code: `200, 301, 400, 401, 403, 404, 405 and 500`
        - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
        - format: `<status code>: <number>`
        - status codes should be printed in ascending order

#### Warning:
In this sample, you will have random value - it’s normal to not have the same output as this one.

```
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
```