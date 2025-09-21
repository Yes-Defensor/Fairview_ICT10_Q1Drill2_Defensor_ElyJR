from js import document

def generate_message():
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f"Student Profile\n" \
              f"👤 Name: {name}\n" \
              f"Age: {age}\n" \
              f"School: {school}\n\n" \
              f"📝 Notes:\n" \
              f"{name} is currently {age} years old and studies at {school}.\n" \
              f"\tThis information was gathered through input fields\n" \
              f"\tand displayed using a multiline string in Python via PyScript."

    # Append message without clearing previous content
    output = document.getElementById("output")
    output.innerText += message + "\n\n"
