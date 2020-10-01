from uuid import uuid4
import neomodel as nm


class Post(nm.StructuredNode):
    uid = nm.StringProperty(unique_index=True, default=uuid4)
    create_datetime = nm.DateTimeProperty(default_now=True)
    content = nm.StringProperty(required=True)

    comments = nm.Relationship('Comment', 'COMMENTED')
    written_by = nm.Relationship('User', 'WRITTEN_BY')


class Like(nm.StructuredRel):
    create_datetime = nm.DateTimeProperty(default_now=True)


class Comment(nm.StructuredNode):
    create_datetime = nm.DateTimeProperty(default_now=True)
    content = nm.StringProperty(required=True)

    written_by = nm.Relationship('User', 'WRITTEN_BY')


class User(nm.StructuredNode):
    uid = nm.StringProperty(index=True, default=uuid4)
    create_datetime = nm.DateTimeProperty(default_now=True)
    email = nm.StringProperty(unique_index=True, required=True)
    password = nm.StringProperty(required=True)
    name = nm.StringProperty(required=True)

    liked_posts = nm.RelationshipTo('Post', 'LIKED', model=Like)
    followings = nm.RelationshipTo('User', 'FOLLOW')


"""
############ Followings & Followers
# user_aa = User(email="aa@gmail.com", password="something", name="aa").save()
# user_bb = User(email="bb@gmail.com", password="something", name="bb").save()
# user_cc = User(email="cc@gmail.com", password="something", name="cc").save()

user_aa.followings.connect(user_bb)
user_aa.followings.connect(user_cc)
user_bb.followings.connect(user_cc)

# Query followings of aa
for following in user_aa.followings.all():
    print(following)

# Query followers of user_cc
follower_definition = dict(
    node_class=User,
    direction=nm.match.INCOMING,
    relation_type='FOLLOW',
    model=None
)

relations_traversal = nm.Traversal(user_cc, 'User', follower_definition)
cc_followers = relations_traversal.all()

for follower in cc_folowers:
    print(follower)


############ Comments
# comment_1 = Comment(content="Comment 1.")
# comment_2 = Comment(content="Comment 2.")

comment_1.written_by.connect(user_aa)
comment_2.written_by.connect(user_aa)

# Query who wrote the comment_1
for user in comment1.written_by.all():
    print(user)

# Query comments written by user_aa
follower_definition = dict(
    node_class=User,
    direction=nm.match.INCOMING,
    relation_type='FOLLOW',
    model=None
)
"""
