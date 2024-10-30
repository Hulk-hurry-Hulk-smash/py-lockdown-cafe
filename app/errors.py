class VaccineError(Exception):
    """Base class for vaccine-related exceptions."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    def __init__(self, message: str = "Visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Exception raised when the visitor's vaccine has expired."""
    def __init__(self, message: str = "Vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    def __init__(
            self, message: str = "Visitor is not wearing a mask."
    ) -> None:
        super().__init__(message)
