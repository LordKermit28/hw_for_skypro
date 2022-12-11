import json


def load_candidates():
    with open("data.json", 'r', encoding="utf-8") as file:
        return json.load(file)


def get_all():
    "возвращает данные кандидатов"
    return load_candidates()


def get_candidate_by_pk(pk):
    """получает данные кандидата по pk"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate

    return


def get_candidates_by_skill(skill):
    """перебирает и возвращает список кандидатов по навыку"""
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidate