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
    return (
        "Guia de platina de KINGDOM HEARTS FINAL MIX (PS4) em PT-BR.\n\n"
        "A regra que organiza tudo: KH1 NÃO tem pós-jogo. Quando os créditos "
        "sobem, o save não volta para o mapa — então cada coletável precisa "
        "estar fechado antes de abrir a porta do Final Rest. Como um dos "
        "troféus pede menos de 15 horas de jogo, a platina custa duas zeradas:\n"
        "• Run 1, no Proud: corrida contra o relógio, sem Continue e sem trocar "
        "nenhum equipamento. No PS4 a dificuldade empilha, então essa zerada "
        "sozinha entrega Proud, Final Mix e Beginner.\n"
        "• Run 2, no Beginner: save novo, sem regra nenhuma, para os 99 "
        "dálmatas, as 46 trinities, o Diário do Jiminy inteiro, as quatro "
        "copas, os cinco chefes opcionais e o nível 100.\n\n"
        "O guia é uma lista de VISITAS: abra a que você vai jogar e o card "
        "mostra os passos daquela ida com foto, os troféus que saem ali e o "
        "aviso do que fecha depois. As abas seguintes trazem os 56 troféus, os "
        "coletáveis com foto e as builds de cada chefe opcional.\n\n"
        "O progresso é salvo em %APPDATA%/StreamerSidekick/platinas/"
        "kh1-final-mix/ e sobrevive a atualizações."
    )


def build_page(config=None):
    from .page import GuidePage

    return GuidePage()
