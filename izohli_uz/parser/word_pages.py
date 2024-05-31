import requests

from izohli_uz.models import Word, Description, Letter

base_url = "https://api.izohla.uz"
letter_page = "/words?character={letter}&per_page=100&page={page_num}"


def get_letter_page(letter, page_num=1):
    url = base_url + letter_page.format(letter=letter, page_num=page_num)
    response = requests.get(url)
    json_res = response.json()
    result = json_res["results"]
    for word in result:
        print(f"word: {word['label']}")
        word_model, created = Word.objects.get_or_create(
            label=word["label"],
            id=word['id'],
            defaults={
                'label': word['label'],
                "id": word['id'],
                "transcription": word['transcription']
            })
        descriptions = word["descriptions"]
        for description in descriptions:
            description = Description.objects.get_or_create(
                id=description["id"],
                content=description["content"],
                source=description['source'],
                word_id=word_model.id,
                defaults={
                    "id": description["id"],
                    "word_id": word_model.id,
                    "content": description["content"],
                    "source": description["source"]
                }
            )


def extract_page_nums(letter):
    url = base_url + letter_page.format(letter=letter, page_num=1)
    response = requests.get(url)
    json_res = response.json()
    pages = json_res["pages"]
    return pages


def fetch_words(letter):
    pages = extract_page_nums(letter)
    for page in range(1, pages + 1):
        print("Fetching page {page} of letter {letter}".format(page=page, letter=letter))
        get_letter_page(letter, page)


def parse_izohli_uz():
    letters = Letter.objects.all()
    for letter in letters:
        fetch_words(letter.letter)
