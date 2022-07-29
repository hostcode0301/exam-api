from app.models.common import PrimaryKeyModelMixin
from app.models.domain.answers import AnswerText, AnserImage, IsCorrectAnswer
from app.models.domain.result_answers import IsUserChoice


class ResultAnswer(
    PrimaryKeyModelMixin,
    AnswerText,
    AnserImage,
    IsCorrectAnswer,
    IsUserChoice,
):
    pass