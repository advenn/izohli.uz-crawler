[izohli.uz](https://izohli.uz) parser

parser and models work, saves to database.
run app:

* fill .env vars based on .env.dist
* Initialize project and migrate

```shell
pip install -r requirements.txt
python manage.py migrate
```

to parse data

```shell
python manage.py shell
```

```python
from izohli_uz.parser.word_pages import parse_izohli_uz

parse_izohli_uz()
```

i wanted to write api using drf, but it seemed the site itself written using drf, and i gave up

i don't have any relation with izohli.uz and i hope i haven't broken any rule by parsing and sharing this code

Please use this feature responsibly and ensure your actions comply with their terms and conditions, as misuse may violate
their community guidelines.

