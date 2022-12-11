import json




def load_candidates():
    with open("data.json", 'r', encoding="utf-8") as file:
        return json.load(file)


def get_all():
    "возвращает данные кандидатов"
    return load_candidates()


def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate

    return


def get_candidates_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidate