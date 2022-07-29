from app.models.common import PrimaryKeyModelMixin
from app.models.domain.questions import QuestionTitle, QuestionText, QuestionImage, Tips, Type
from app.models.domain.result_questions import Mark, IsCorrect


class ResultQuestion(
    PrimaryKeyModelMixin,
    QuestionTitle,
    QuestionText,
    QuestionImage,
    Tips,
    Type,
    Mark,
    IsCorrect,
):
    pass