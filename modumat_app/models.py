from django.db import models


ANSWER_OPTIONS = (
    (-1, 'negative'),
    (0, 'neutral'),
    (1, 'positive'),
)


class Module(models.Model):
    """University course
    """
    shorthand = models.CharField(max_length=20)
    module_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.shorthand}: {self.module_name}"

    def calculateAgreementPoints(self, session):
        """Returns an integer representing the degree of agreement between user and module
        """
        agreement_points = 0
        all_module_answers = ModuleAnswer.objects.filter(module=self.pk)
        for module_answer in all_module_answers:
            if str(module_answer.question.pk) in session:
                agreement_points += 2 - abs(module_answer.answer - int(session[str(module_answer.question.pk)]))

        return agreement_points


class Question(models.Model):
    """Question or statement that is answered by the user or a Module
    """
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
    """Answer for a given Question by one Module
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=ANSWER_OPTIONS)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['module', 'question'], name='unique_module_answer')
        ]

    def __str__(self):
        return f"{self.question.title} - {self.module.shorthand}: {ANSWER_OPTIONS[self.answer+1][1]}"
