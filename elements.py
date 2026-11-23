
# pyright: reportMissingImports=false
from pyscript import document


# Dictionary containing non-metal elements
non_metals = {
    "H": {"name": "Hydrogen", "number": 1, "mass": 1.008},
    "He": {"name": "Helium", "number": 2, "mass": 4.003},
    "C": {"name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"name": "Oxygen", "number": 8, "mass": 15.999},
    "F": {"name": "Fluorine", "number": 9, "mass": 18.998},
    "Ne": {"name": "Neon", "number": 10, "mass": 20.180},
    "P": {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S": {"name": "Sulfur", "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine", "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon", "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium", "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine", "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton", "number": 36, "mass": 83.798},
    "I": {"name": "Iodine", "number": 53, "mass": 126.904},
    "Xe": {"name": "Xenon", "number": 54, "mass": 131.293},
    "Rn": {"name": "Radon", "number": 86, "mass": 222}
}


# Function to search for an element
def candidate_checker(event):

    element = document.getElementById("element").value.strip().title()

    result = document.getElementById("result")

    # Check for empty input
    if not element:
        result.innerText = "Please enter a chemical symbol."
        return

    # Retrieve element information
    element_info = non_metals.get(element)

    # Check whether the element exists
    if element_info is None:
        result.innerText = "Element not found. Please try another symbol."
        return

    # Display element information
    result.innerHTML = f"""
        <b>Symbol:</b> {element}<br>
        <b>Element:</b> {element_info["name"]}<br>
        <b>Atomic Number:</b> {element_info["number"]}<br>
        <b>Atomic Mass:</b> {element_info["mass"]}
    """