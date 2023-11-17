from django.db import models
from apps.user.models import User

def forumImageTo(instance,filename):
    return f"forum/{instance.forum.id}/{filename}"

def commentImageTo(instance,filename):
    if instance.response_of:
        return f"comments/responses/{instance.response_of}/{filename}"
    return f"comments/{instance.forum.id}/{filename}"


class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
 
    def update_likes_dislikes_count(self):
        self.likes = LikesDislikeForum.objects.filter(forum=self, like=True).count()
        self.dislikes = LikesDislikeForum.objects.filter(forum=self, dislike=True).count()
        # self.save()

    def save(self, *args, **kwargs):
        self.update_likes_dislikes_count()
        super().save(*args, **kwargs)

class Gallery(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    principal = models.BooleanField(default=False)
    image = models.ImageField(upload_to=forumImageTo)

class LikesDislikeForum(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.forum.update_likes_dislikes_count()

class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    image = models.ImageField(upload_to=commentImageTo,blank=True,null=True)
    response_of = models.ForeignKey('self',related_name="responses_comment",on_delete=models.CASCADE,blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def update_likes_dislikes_count(self):
        self.likes = LikesDislikeForumComment.objects.filter(comment=self, like=True).count()
        self.dislikes = LikesDislikeForumComment.objects.filter(comment=self, dislike=True).count()
        # self.save()

    def save(self, *args, **kwargs):
        self.update_likes_dislikes_count()
        super().save(*args, **kwargs)

class LikesDislikeForumComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.comment.update_likes_dislikes_count()
