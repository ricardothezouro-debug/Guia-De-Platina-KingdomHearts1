"""Chaves de progresso do guia.

A espinha do guia é a VISITA: cada uma tem a própria caixa de "concluída" e as
caixas de cada passo dentro dela. Este módulo centraliza o formato das chaves
para que `module.py`, `page.py` e o importador/exportador falem a mesma língua.
"""
from __future__ import annotations

from . import guide_data


def visit_key(index: int) -> str:
    return f"visit_{index}"


def step_key(visit_index: int, step_index: int) -> str:
    return f"step_{visit_index}_{step_index}"


def steps_of(visit_index: int) -> list[dict]:
    return guide_data.VISITS[visit_index]["steps"]


def puppy_key(index: int) -> str:
    return f"puppy_{index}"


def trinity_key(index: int) -> str:
    return f"trinity_{index}"


def page_key(index: int) -> str:
    return f"page_{index}"


def postcard_key(index: int) -> str:
    return f"postcard_{index}"


def report_key(index: int) -> str:
    return f"report_{index}"


def material_key(index: int) -> str:
    return f"material_{index}"


def boss_key(index: int) -> str:
    return f"boss_{index}"


def prep_key(index: int) -> str:
    return f"prep_{index}"


def trophy_key(trophy_id: str) -> str:
    return f"trophy_{trophy_id}"


def trophy_keys() -> list[str]:
    return [trophy_key(t["id"]) for t in guide_data.TROPHIES]


def puppy_keys() -> list[str]:
    return [puppy_key(i) for i in range(len(guide_data.PUPPIES))]


def trinity_keys() -> list[str]:
    return [trinity_key(i) for i in range(len(guide_data.TRINITIES))]


def collectible_keys() -> list[str]:
    """Tudo que é coleção contável: dálmatas, trinities, páginas, postais,
    relatórios e os materiais raros da Ultima."""
    keys = puppy_keys() + trinity_keys()
    keys += [page_key(i) for i in range(len(guide_data.PAGES))]
    keys += [postcard_key(i) for i in range(len(guide_data.POSTCARDS))]
    keys += [report_key(i) for i in range(len(guide_data.REPORTS))]
    keys += [material_key(i) for i in range(len(guide_data.MATERIALS))]
    return keys


def all_keys() -> list[str]:
    """Todas as chaves marcáveis do guia, na ordem das abas."""
    keys: list[str] = []
    for i, visit in enumerate(guide_data.VISITS):
        keys.append(visit_key(i))
        keys += [step_key(i, j) for j in range(len(visit["steps"]))]
    keys += trophy_keys()
    keys += collectible_keys()
    keys += [boss_key(i) for i in range(len(guide_data.BOSSES))]
    keys += [prep_key(i) for i in range(len(guide_data.PREP))]
    return keys


def normalize_imported(raw) -> set[str]:
    """Aceita o formato deste plugin e um dicionário `{chave: bool}`."""
    if isinstance(raw, dict):
        raw = [key for key, value in raw.items() if value]
    return {str(key) for key in raw}
