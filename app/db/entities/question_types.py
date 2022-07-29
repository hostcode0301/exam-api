from app.models.common import IDModelMixin, PrimaryKeyModelMixin
from app.models.domain.question_types import Type


class QuestionType(
    PrimaryKeyModelMixin,
    IDModelMixin,
    Type,
):
    pass