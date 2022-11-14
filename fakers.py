from faker import Faker
from pages.models import Post

fake = Faker()
def gen_fake(num):
    Post.objects.bulk_create(
        [Post(title=fake.name(), description=fake.text(), status="Publish", author_id=1, slug=str(fake.name()).replace(" ", "-")) for _ in range(num)]
    )
    print("success")
    return
        

