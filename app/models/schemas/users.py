from app.models.domain import (
    users as _user_domains,
    rwmodel as _rwmodel,
)

class UserInCreate(
    _rwmodel.RWModel,
    _user_domains.Fullname,
    _user_domains.Address,
    _user_domains.DateOfBirth,
):
    pass

class UserEntity(
    UserInCreate,
    _user_domains.Id,
):
    pass

class UserInResponse(UserEntity):
    pass

class UserInUpdate(
    _rwmodel.RWModel,
    _user_domains.OptionalFullname,
    _user_domains.OptionalAddress,
    _user_domains.OptionalDateOfBirth,
):
    pass
