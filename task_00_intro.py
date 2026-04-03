import os

def generate_invitations(template, attendees):
    # Tip yoxlanışı
    if not isinstance(template, str):
        print("Error: template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: attendees is not a list of dictionaries.")
        return

    # Boş giriş yoxlanışı
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal
    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            val = attendee.get(key)
            if val is None:
                val = "N/A"
            content = content.replace(f"{{{key}}}", str(val))
        
        output_name = f"output_{i}.txt"
        with open(output_name, "w") as f:
            f.write(content)
