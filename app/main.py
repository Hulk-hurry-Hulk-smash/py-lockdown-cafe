from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError, NotVaccinatedError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1
        except VaccineError:
            return "All friends should be vaccinated"

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
