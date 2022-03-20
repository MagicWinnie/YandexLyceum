def creators(name, planets=8, alive=True):
    name_line = f"Система звезды {name}."
    planets_line = f"Количество планет: {planets}."
    alive_line = "Жизнь есть!" if alive else "Жизни нет."
    return "\n".join([name_line, planets_line, alive_line])
