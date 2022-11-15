from faker import Faker
from pages.models import Post

fake = Faker()
def gen_fake(num):
    title=fake.name()
    Post.objects.bulk_create(
        [Post(title=title, description=fake.text(), status="Publish", author_id=1, slug=str(title).replace(" ", "-")) for _ in range(num)]
    )
    print("success")
    return
        

