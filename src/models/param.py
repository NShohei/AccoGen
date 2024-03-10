import pydantic as pdtc


from models.enums import Locales


class LenghBasedGeneratorParam(pdtc.BaseModel):
    alphabet_max_length: int = pdtc.Field(ge=0, le=32)

    number_max_length: int = pdtc.Field(ge=0, le=32)

    symbol_max_length: int = pdtc.Field(ge=0, le=32)

    use_leet: bool = pdtc.Field()

    def __str__(self):
        return self.model_dump_json()

    @pdtc.model_validator(mode="after")
    def has_any_length_over_zero(self):
        if (
            self.alphabet_max_length == 0
            and self.number_max_length == 0
            and self.symbol_max_length == 0
        ):
            raise ValueError("Lengthがすべて0になっています。")


class FakerBasedGeneratorParam(pdtc.BaseModel):
    use_leet: bool = pdtc.Field()

    locale: Locales = pdtc.Field()

    def __str__(self):
        return self.model_dump_json()
