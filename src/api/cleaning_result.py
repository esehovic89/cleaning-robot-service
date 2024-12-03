from pydantic import BaseModel


class CleaningResult(BaseModel):
    places_cleaned: int
