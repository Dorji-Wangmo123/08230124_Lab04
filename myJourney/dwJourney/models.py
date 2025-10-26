from django.db import models

# ===========================
# Models for index.html
# ===========================

class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Short description about the topic")
    order = models.PositiveIntegerField(default=0, help_text="Order in which the topic appears")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Challenge(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='challenges')
    description = models.TextField()
    difficulty_level = models.CharField(
        max_length=50,
        choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')],
        default='Medium'
    )

    def __str__(self):
        return f"{self.topic.title} Challenge"

# ===========================
# Models for aboutMe.html
# ===========================

class AboutMe(models.Model):
    name = models.CharField(max_length=100, default="Dorji Wangmo")
    intro = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True, help_text="Short bio or tagline")

    def __str__(self):
        return self.name

class Hobby(models.Model):
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='hobbies')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(
        max_length=50,
        choices=[('Beginner','Beginner'), ('Intermediate','Intermediate'), ('Advanced','Advanced')],
        default='Intermediate'
    )

    def __str__(self):
        return self.name
