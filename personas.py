def get_persona(intensity, sleep, emotion, social):

    if intensity > 70 and sleep < 50:
        return {
            "name": "🔥 The Midnight Strategist",
            "animal": "🦉 Shadow Owl",
            "description": "You thrive in quiet intensity. Night energy fuels your focus, but balance may be slipping."
        }

    if emotion > 60 and social < 50:
        return {
            "name": "🌙 The Escapist Dreamer",
            "animal": "🦊 Silver Fox",
            "description": "You seek emotional refuge in digital realms. Clever, reflective, but easily detached."
        }

    if intensity > 70 and emotion > 50:
        return {
            "name": "⚡ The Dopamine Chaser",
            "animal": "🐯 Neon Tiger",
            "description": "You chase stimulation and adrenaline. Powerful drive, but risk of burnout."
        }

    if intensity < 50 and social > 60:
        return {
            "name": "🎯 The Balanced Explorer",
            "animal": "🦅 Golden Eagle",
            "description": "Disciplined and strategic. You balance worlds with precision."
        }

    return {
        "name": "🧩 The Solo Architect",
        "animal": "🐺 Lone Wolf",
        "description": "Independent and analytical. You prefer depth over noise."
    }



# def get_persona(intensity, sleep, emotion, social):
    
#     if intensity > 70 and sleep < 50:
#         return "🔥 The Midnight Strategist"
    
#     if emotion > 60 and social < 50:
#         return "🌙 The Escapist Dreamer"
    
#     if intensity > 70 and emotion > 50:
#         return "⚡ The Dopamine Chaser"
    
#     if intensity < 50 and social > 60:
#         return "🎯 The Balanced Explorer"
    
#     return "🧩 The Solo Architect"
