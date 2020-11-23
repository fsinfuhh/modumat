from django.db import models


ANSWER_OPTIONS = (
    (-1, 'negative'),
    (0, 'neutral'),
    (1, 'positive'),
)


class Module(models.Model):
    shorthand = models.CharField(max_length=20)
    module_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.shorthand}: {self.module_name}"


class Question(models.Model):
    title = models.CharField(max_length=50)
    full_question = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def next_question(self):
        following_questions = Question.objects.filter(pk__gt=self.pk).order_by('pk')
        if len(following_questions) > 0:
            return following_questions[0]
        return None


class ModuleAnswer(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=ANSWER_OPTIONS)

    def __str__(self):
        return f"{self.question.title} - {self.module.shorthand}: {ANSWER_OPTIONS[self.answer+1][1]}"
