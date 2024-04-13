from django.db import models
import uuid


class Answer(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    value = models.CharField(max_length=255, null=False)
    questionnaire = models.CharField(max_length=255, null=True, blank=True)
    sub_questionnaire = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = (('key', 'user_id'),)
        db_table = 'answer_table'

    def to_answer_dict(self):
        # Converts the Answer instance into a dictionary representing the Answer object
        return {
            'questionKey': self.key,
            'value': self.value
        }

    def to_answer_with_questionnaire_dict(self):
        # Converts the Answer instance into a dictionary representing the AnswerWithQuestionnaire object
        return {
            'questionKey': self.key,
            'value': self.value,
            'questionnaire': self.questionnaire,
            'subQuestionnaireOf': self.sub_questionnaire
        }
