from app.models.domain.questions import QuestionTitle, QuestionText, QuestionImage, Tips
from app.models.domain.question_types import Type
from app.models.common import DateTimeModelMixin, IDModelMixin, PrimaryKeyModelMixin


class Question(
    PrimaryKeyModelMixin,
    DateTimeModelMixin,
    IDModelMixin,
    QuestionTitle,
    QuestionText,
    QuestionImage,
    Tips,
    Type,
):
    pass