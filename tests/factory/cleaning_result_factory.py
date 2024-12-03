from api.cleaning_result import CleaningResult


class CleaningResultFactory:
    def __init__(self):
        self._places_cleaned = 4

    def places_cleaned(self, places_cleaned: int):
        self._places_cleaned = places_cleaned
        return self

    def build(self) -> CleaningResult:
        return CleaningResult(places_cleaned=self._places_cleaned)
