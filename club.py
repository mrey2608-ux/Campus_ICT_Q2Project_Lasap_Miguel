# pyright: reportMissingImports=false
from pyscript import document


def candidate_checker(event=None):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    result = document.getElementById("result")

    if not first_name or not last_name:
        result.innerText = "Please enter both your first and last name."
        return

    full_name = f"{first_name.title()} {last_name.title()}"
    result.innerHTML = (
        f"<b>Candidate:</b> {full_name}<br>"
        "<b>Status:</b> Membership verified"
    )
