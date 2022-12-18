import json

def load_candidates():
    with open("candidates.json", 'r', encoding="utf-8") as file:
        return json.load(file)


def get_all_candidates():
    "возвращает данные кандидатов"
    return load_candidates()


def get_candidate_by_pk(pk):
    """получает данные кандидата по pk"""
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate

    return

def get_candidate_by_name(candidate_name):
    """получает данные кандидата по имени"""
    candidates = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill):
    """перебирает и возвращает список кандидатов по навыку"""
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates