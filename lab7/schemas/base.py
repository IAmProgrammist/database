from typing import Annotated, Union

from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator

RuNumberType = Annotated[
    Union[str, PhoneNumber],
    PhoneNumberValidator(supported_regions=['RU'], number_format="E164", default_region='RU')
]


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
