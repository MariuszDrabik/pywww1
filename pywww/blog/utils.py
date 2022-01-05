from random import randint
from faker import Faker
from .models import Post


def create_posts(n=10):
    anty_unicode = {
        'ą': 'a',
        'ł': 'l',
        'ę': 'e',
        'ę': 'e',
        'ó': 'o',
        'ż': 'z',
        'ź': 'z',
        'ć': 'c',
        'ń': 'n',
        'ś': 's',
    }
    for _ in range(0, n):
        fake = Faker('pl_PL')
        title = fake.text(randint(25, 30)).replace(".", "")
        slug = "-".join(title.split()).lower().translate(str.maketrans(anty_unicode))
        content = fake.text(randint(450, 890))
        print(title)
        print(slug)
        print(content)
        post = Post.objects.create(
            title=title,
            slug=slug,
            content=content,
            published=True,
        )
        print(post)
        post.save()


# create_posts()
