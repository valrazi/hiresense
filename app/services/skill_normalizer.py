def normalize_skill(skill: str):

    skill = skill.lower().strip()

    replacements = {
        "vue.js": "vue",
        "vue 3": "vue",
        "nodejs": "node",
        "node.js": "node",
        "postgresql": "postgres",
        "postgres": "postgres",
        "mongodb": "mongodb",
        "restful": "rest api",
        "rest": "rest api",
        "graphql api": "graphql",
        "tailwind css": "tailwind",
        "scalable api": "api"
    }

    for key, value in replacements.items():
        skill = skill.replace(key, value)

    return skill