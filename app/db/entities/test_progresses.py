from app.models.common import PrimaryKeyModelMixin
from app.models.domain.answers import AnserImage, AnswerText
from app.models.domain.questions import QuestionImage, QuestionText, QuestionTitle, Tips
from app.models.domain.tests import TestName
from app.models.domain.question_types import Type


class TestProgress(
    PrimaryKeyModelMixin,
    TestName,
    QuestionTitle,
    QuestionText,
    QuestionImage,
    Tips,
    Type,
    AnswerText,
    AnserImage,
):
    pass