from django.shortcuts import render
from django.http import Http404

"""Contains posts.
organised as dictionary
key is id
inside it listed:
id (the same as key)
location (str format)
date (str format)
category (str format, english language)
text (str format)"""
posts = [
    {
        "id": 0,
        "location": "Остров отчаянья",
        "date": "30 сентября 1659 года",
        "category": "travel",
        "text": """Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.""",
    },
    {
        "id": 1,
        "location": "Остров отчаянья",
        "date": "1 октября 1659 года",
        "category": "not-my-day",
        "text": """Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.""",
    },
    {
        "id": 2,
        "location": "Остров отчаянья",
        "date": "25 октября 1659 года",
        "category": "not-my-day",
        "text": """Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.""",
    },
]


class PostStorage:
    def __init__(self, posts_val=None, default=False):
        if default:
            posts_val = posts
        self.posts = dict()
        if posts_val:
            for post in posts_val:
                self.posts[post["id"]] = post


post_storage = PostStorage(default=True)


def index(request):
    return render(request, "blog/index.html",
                  {"posts": reversed(post_storage.posts.items())})


def post_detail(request, post_id: int):
    if post_id not in post_storage.posts:
        raise Http404(f"post with id {id} does not exist")
    return render(request, "blog/detail.html",
                  {"post": post_storage.posts[post_id], "post_id": post_id})


def category_posts(request, category):
    filtred = []
    for id, post in post_storage.posts.items():
        if post["category"] == category:
            filtred.append((id, post))
    return render(
        request, "blog/category.html",
        {"posts": reversed(filtred), "category": category}
    )
