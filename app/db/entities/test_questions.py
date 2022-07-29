from app.models.domain.questions import QuestionTitle, QuestionText, QuestionImage, Tips
from app.models.domain.tests import TestName
from app.models.domain.question_types import Type
from app.models.common import DateTimeModelMixin, PrimaryKeyModelMixin


class TestQuestion(
    PrimaryKeyModelMixin,
    DateTimeModelMixin,
    TestName,
    QuestionTitle,
    QuestionText,
    QuestionImage,
    Tips,
    Type,
):
    pass