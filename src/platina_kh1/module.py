"""Adaptador de plugin do Streamer Sidekick (categoria: platina)."""
from dataclasses import dataclass

from . import guide_data

MODULE_ID = guide_data.GUIDE_ID


@dataclass(frozen=True)
class ModuleInfo:
    module_id: str
    title: str
    subtitle: str
    status: str
    accent: str


def module_info():
    from .progress import trophy_keys
    from .storage import load_progress

    done_keys = load_progress()
    trophies = trophy_keys()
    done = sum(1 for key in trophies if key in done_keys)
    data = dict(
        module_id=guide_data.GUIDE_ID,
        title=guide_data.GAME_NAME,
        subtitle=guide_data.GAME_SUBTITLE,
        status=f"{done}/{len(trophies)} troféus",
        accent=guide_data.ACCENT,
    )
    try:
        from streamer_sidekick.core.modules import ModuleInfo as SidekickModuleInfo

        return SidekickModuleInfo(**data)
    except Exception:
        return ModuleInfo(**data)


def help_text() -> str:
    from .paths import guide_dir_label

    return (
        "Guia de platina de KINGDOM HEARTS FINAL MIX (PS4) em PT-BR.\n\n"
        "A regra que organiza tudo: KH1 NÃO tem pós-jogo. Quando os créditos "
        "sobem, o save não volta para o mapa — então cada coletável precisa "
        "estar fechado antes de abrir a porta do Final Rest. Como um dos "
        "troféus pede menos de 15 horas de jogo, a platina custa duas zeradas, "
        "nesta ordem:\n"
        "• 1ª — a run do 100%: história, 99 dálmatas, 46 trinities, Diário do "
        "Jiminy inteiro, as quatro copas, os cinco chefes opcionais, Ultima "
        "Weapon e nível 100. É a que você joga de verdade.\n"
        "• 2ª — a cronometrada: save novo, menos de 15 h, sem Continue e sem "
        "trocar equipamento. Só é rápida porque a primeira já te ensinou o mapa.\n\n"
        "Versão gamox (a recomendada aqui): o 100% inteiro no PROUD e a "
        "cronometrada no Beginner. A dificuldade empilha no PS4, então terminar "
        "a primeira run no Proud entrega Proud, Final Mix e Beginner de uma vez "
        "— e joga os chefes opcionais para a run em que você tem nível e "
        "equipamento para encará-los. A aba Builds & Chefes traz o bloco "
        "\"Sobreviver no Proud\" para quem começa direto nele.\n\n"
        "O guia é uma lista de VISITAS: abra a que você vai jogar e o card "
        "mostra os passos daquela ida com foto, os troféus que saem ali e o "
        "aviso do que fecha depois. As abas seguintes trazem os 56 troféus, os "
        "coletáveis com foto e as builds de cada chefe opcional.\n\n"
        f"O progresso é salvo em {guide_dir_label()} — fora da pasta do "
        "plugin, então sobrevive a atualizações."
    )


def build_page(config=None):
    from .page import GuidePage

    return GuidePage()
