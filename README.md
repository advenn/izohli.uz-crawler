[izohli.uz](https://izohli.uz) parser

parser and models work, saves to database.
to run it 
```shell
python manage.py shell
```

```python
from izohli_uz.parser.word_pages import parse_izohli_uz

parse_izohli_uz()
```
it 