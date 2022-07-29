from app.models.common import DateTimeModelMixin, IDModelMixin, PrimaryKeyModelMixin
from app.models.domain.answers import AnswerText, AnserImage, IsCorrectAnswer


class Answer(
    PrimaryKeyModelMixin,
    DateTimeModelMixin,
    IDModelMixin,
    AnswerText,
    AnserImage,
    IsCorrectAnswer,
):
    pass