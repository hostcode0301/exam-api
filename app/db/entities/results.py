from app.models.common import DateTimeModelMixin, PrimaryKeyModelMixin
from app.models.domain.results import Result, PublishDate

class Result(
    PrimaryKeyModelMixin,
    DateTimeModelMixin,
    Result,
    PublishDate,
):
    pass