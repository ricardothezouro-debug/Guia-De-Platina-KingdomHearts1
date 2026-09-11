"""Dados do guia de platina de KINGDOM HEARTS FINAL MIX (PS4, PT-BR).

Estrutura centrada na VISITA: em KH1 quase tudo é decidido por "quando" você
entra em cada mundo — vários baús, trinities e dálmatas só existem depois de
ganhar High Jump, Glide, Gravity ou uma cor nova de trinity. Por isso a espinha
do guia é a lista de visitas na ordem de jogo, e cada visita carrega os passos
daquela ida, com foto, os troféus que saem ali e o aviso do que fecha depois.

Este é o ÚNICO arquivo específico do jogo — os demais módulos são genéricos.
"""

# Identificador único do guia (kebab-case): vira o id do plugin e o nome da
# pasta de progresso dentro da pasta de dados do Sidekick (ver paths.py).
GUIDE_ID = "kh1-final-mix"

GAME_NAME = "Kingdom Hearts Final Mix — Platina"
GAME_SUBTITLE = (
    "Guia PT-BR do PS4: as visitas de cada mundo na ordem, com foto, os 99 "
    "dálmatas, as 46 trinities e os 56 troféus."
)
ACCENT = "#3E6BE8"  # o azul do Kingdom Key

HERO_IMAGE = ""

# Fotos: todas as imagens vêm do KHGuides (khguides.com), citado nas Fontes.
_TT = "https://www.khguides.com/kh/traverse-town/images/"
_WL = "https://www.khguides.com/kh/wonderland/images/"
_OC = "https://www.khguides.com/kh/olympus-coliseum/images/"
_DJ = "https://www.khguides.com/kh/deep-jungle/images/"
_AG = "https://www.khguides.com/kh/agrabah/images/"
_MO = "https://www.khguides.com/kh/monstro/images/"
_AT = "https://www.khguides.com/kh/atlantica/images/"
_HT = "https://www.khguides.com/kh/halloween-town/images/"
_NL = "https://www.khguides.com/kh/neverland/images/"
_HB = "https://www.khguides.com/kh/hollow-bastion/images/"
_EW = "https://www.khguides.com/kh/end-of-the-world/images/"
_HA = "https://www.khguides.com/kh/hundred-acre-wood/images/"
_TR = "https://www.khguides.com/kh/collectibles/treasures/images/"
_TN = "https://www.khguides.com/kh/collectibles/trinities/images/"

# Parágrafo de abertura.
INTRO = (
    "São 56 troféus e, no PS4, DUAS zeradas — não uma, não três. O motivo é uma "
    "regra só deste jogo: Kingdom Hearts 1 não tem pós-jogo. Depois que os "
    "créditos sobem você não volta para mundo nenhum, então tudo que é coleção "
    "precisa estar fechado ANTES de abrir a porta do Final Rest. Como existe um "
    "troféu de terminar em menos de 15 horas, o 100% e a corrida contra o "
    "relógio não cabem no mesmo save.\n\n"
    "A PRIMEIRA run é a do 100% — é ela que você joga de verdade. A segunda é a "
    "cronometrada, e ela só é rápida porque a primeira já te ensinou o mapa "
    "inteiro. O guia chama as duas pelo nome, nunca por número, então nenhum "
    "passo muda de sentido no meio do caminho.\n\n"
    "A versão recomendada aqui é a gamox: o 100% inteiro no PROUD e a "
    "cronometrada no Beginner. Como a dificuldade empilha no PS4, terminar a "
    "primeira run no Proud já entrega Proud Player, Final Mix Master e Novice "
    "Player de uma vez — e joga os chefes opcionais para a run em que você tem "
    "nível, Ultima Weapon e invocação para encará-los."
)

# Números de destaque exibidos no topo.
HERO_STATS = [
    {"value": "56", "label": "troféus"},
    {"value": "2", "label": "zeradas"},
    {"value": "31", "label": "paradas na ordem"},
    {"value": "99", "label": "dálmatas com foto"},
    {"value": "46", "label": "trinities com foto"},
]

# As 5 abas do guia.
SECTIONS = [
    {
        "key": "route",
        "num": "01",
        "nav": "Rota",
        "eyebrow": "O guia",
        "title": "O walkthrough: 31 paradas na ordem de jogo",
        "lead": (
            "Uma lista só, na ordem em que você joga — Traverse Town aparece "
            "seis vezes porque você volta lá seis vezes. Cada parada traz os "
            "passos com foto, os troféus que saem ali e, no fim do card, os "
            "dálmatas, trinities, postais e páginas que dá para pegar NAQUELA "
            "ida, com foto e caixa de marcação. Os nomes de mundo e de área são "
            "os que aparecem na tela do jogo."
        ),
        "notices": [
            {
                "tone": "red",
                "text": (
                    "KH1 não tem pós-jogo: ao vencer o chefe final os créditos "
                    "sobem e o save não volta para o mapa. TUDO — dálmatas, "
                    "trinities, sínteses, copas, superchefes, nível 100 — "
                    "precisa estar fechado antes de abrir a porta do Final "
                    "Rest, no Fim do Mundo."
                ),
            },
            {
                "tone": "info",
                "text": (
                    "Na CRONOMETRADA você só precisa selar os "
                    "keyholes de Traverse Town, Wonderland, Selva "
                    "Profunda, Agrabah, Neverland e Hollow Bastion, mais "
                    "DOIS entre Monstro, Atlantica e Halloween Town. O "
                    "terceiro fica para a run do 100%."
                ),
            },
        ],
    },
    {
        "key": "trophies",
        "num": "02",
        "nav": "56 Troféus",
        "eyebrow": "Platina",
        "title": "Os 56 troféus do KH1 Final Mix",
        "lead": "1 platina, 2 ouro, 4 prata e 49 bronze. Nenhum é perdível — mas quase todos exigem a run certa.",
        "notices": [
            {
                "tone": "info",
                "text": (
                    "No PS4 a dificuldade empilha: zerar no Proud entrega Proud "
                    "Player, Final Mix Master e Novice Player de uma vez só. No "
                    "PS3 isso NÃO acontece (seriam três zeradas)."
                ),
            },
        ],
    },
    {
        "key": "collect",
        "num": "03",
        "nav": "Coletáveis",
        "eyebrow": "O 100% do Diário do Jiminy",
        "title": "Dálmatas, trinities, páginas, postais e relatórios",
        "lead": "As listas que fecham o Record Keeper, cada uma com o local e a foto do baú.",
        "notices": [
            {
                "tone": "info",
                "text": (
                    "Deixe quase tudo isto para a run do 100%, depois de ter High "
                    "Jump, Glide, Gravity e as trinities Amarela e Branca — boa "
                    "parte dos baús só existe com essas ferramentas na mão."
                ),
            },
        ],
    },
    {
        "key": "systems",
        "num": "04",
        "nav": "Builds & Chefes",
        "eyebrow": "Como sobreviver",
        "title": "O plano das duas runs, as builds e os superchefes",
        "lead": "Como as duas runs se dividem, o que o Proud cobra desde o começo, os hábitos que decidem cada run e os cinco chefes opcionais.",
        "notices": [
            {
                "tone": "info",
                "text": (
                    "O guia não numera as runs: chama cada uma pelo nome — a "
                    "\"run do 100%\" (a primeira, a longa) e a \"cronometrada\" "
                    "(a segunda, a das três travas). Assim nenhum passo muda de "
                    "sentido quando você troca de versão; o que muda entre a "
                    "Versão gamox e a tranquila é só a dificuldade de cada uma."
                ),
            },
        ],
    },
    {
        "key": "sources",
        "num": "05",
        "nav": "Fontes",
        "eyebrow": "Pesquisa cruzada",
        "title": "Fontes do guia",
        "lead": "A rota, os locais e as fotos vêm principalmente do KHGuides; a lista de troféus foi conferida em três lugares.",
        "notices": [],
    },
]

# ── Como a platina se divide ───────────────────────────────────────────────
# A primeira run é a do 100%. Parece contraintuitivo pôr a run longa na frente,
# mas é o que acontece de verdade: ninguém que nunca jogou KH1 faz (nem quer
# fazer) uma corrida de 15 h às cegas. Você joga o jogo, fecha o Diário, e só
# então a segunda run vira o que ela é de fato — uma revisita rápida de um mapa
# que você já sabe de cor.
PLAN = [
    {
        "name": "1ª run — a do 100%, a que você joga de verdade",
        "when": "~40 a 60 h",
        "why": (
            "É a run inteira: história, os 99 dálmatas, as 46 trinities, o Diário "
            "do Jiminy fechado, as quatro copas, os cinco chefes opcionais, a "
            "Ultima Weapon e o nível 100. Sem regra nenhuma — troque equipamento "
            "à vontade, use Continue à vontade.\n\n"
            "Ela vem primeiro por um motivo prático: KH1 não tem pós-jogo, então "
            "TUDO precisa estar fechado antes de você abrir a porta do Final Rest "
            "neste save. E porque a segunda run só é rápida depois que você "
            "aprendeu o mapa aqui."
        ),
        "gets": "50 dos 56 troféus — tudo menos os três de restrição e a dificuldade que sobrar",
    },
    {
        "name": "2ª run — a cronometrada, com o jogo já na cabeça",
        "when": "~12 a 15 h",
        "why": (
            "Save novo com três travas ao mesmo tempo: terminar em menos de 15 "
            "horas de relógio, nunca apertar Continue e nunca trocar um "
            "equipamento sequer. Parece muito; é a parte mais fácil da platina, "
            "porque você já sabe onde fica cada coisa.\n\n"
            "Corra a história e ignore toda coleção. Sele só os keyholes "
            "obrigatórios: Traverse Town, Wonderland, Selva "
            "Profunda, Agrabah, Neverland e Hollow Bastion, mais DOIS entre "
            "Monstro, Atlantica e Halloween Town."
        ),
        "gets": "Speedster, Undefeated, Unchanging Armor e a dificuldade que faltar",
    },
    {
        "name": "▶ Versão gamox — Proud desde o primeiro minuto",
        "when": "recomendada",
        "why": (
            "1ª run (100%) no PROUD · 2ª run (cronometrada) no BEGINNER.\n\n"
            "É a versão que este guia assume. Você começa no Proud e é nele que "
            "acontece tudo que vale a pena: Sephiroth, Kurt Zisa, o Unknown, o "
            "Ice Titan e as 50 chaves da Hades Cup viram luta de verdade — e você "
            "chega neles com nível 80+, Ultima Weapon, Ribbon e as seis "
            "invocações, que é exatamente o kit que a run do 100% constrói. No "
            "Beginner esses mesmos chefes entregam o ponto.\n\n"
            "E tem um ganho que não é óbvio: esta divisão também é a MENOS "
            "arriscada das duas. A run das três travas (sem Continue, sem trocar "
            "equipamento) cai no Beginner, que é onde um erro custa menos. Você "
            "escolhe a briga onde está forte e evita a briga onde estaria "
            "amarrado.\n\n"
            "O que o Proud cobra de você desde o primeiro mundo está no bloco "
            "\"Sobreviver no Proud\", logo abaixo."
        ),
        "gets": "Proud Player, Final Mix Master e Novice Player empilham no fim da 1ª run",
    },
    {
        "name": "Versão tranquila — Proud só no fim",
        "when": "alternativa",
        "why": (
            "1ª run (100%) no BEGINNER · 2ª run (cronometrada) no PROUD.\n\n"
            "Serve se a ideia é conhecer o jogo sem pressão e deixar a "
            "dificuldade para quando você já souber tudo. O preço é que a run das "
            "três travas passa a ser no Proud: menos de 15 horas, sem Continue e "
            "sem trocar equipamento, com os inimigos batendo forte. É a "
            "combinação mais perigosa da platina — um chefe mal jogado às 14 "
            "horas de relógio custa a run inteira."
        ),
        "gets": "Os mesmos 56 troféus; a dificuldade empilha no fim da 2ª run",
    },
]

# ── Sobreviver no Proud desde a primeira run (a Versão gamox) ──────────────
PROUD = [
    {
        "name": "Escudo — e sacrifique a ESPADA",
        "when": "Despertar",
        "why": (
            "Escudo escolhido + espada sacrificada dá STR 3 / DEF 4 / MP 2 / "
            "AP 3 e 8 slots de item. Sacrificando o cajado no lugar seria STR 4 / "
            "DEF 4 / MP 2 / AP 1. Você troca 1 de força por DOIS de AP — e AP no "
            "começo do Proud é o recurso mais escasso do jogo: é o que decide se "
            "você entra no Guard Armor com Dodge Roll equipado ou sem esquiva "
            "nenhuma."
        ),
    },
    {
        "name": "Aero antes de TODO chefe",
        "when": "a partir do Opposite Armor",
        "why": (
            "Aero corta o dano recebido pela metade. No Proud isso não é conforto, "
            "é a diferença entre morrer em três golpes e morrer em seis. Deixe "
            "Aero e Cure no menu de atalhos e recast a cada luta."
        ),
    },
    {
        "name": "Second Chance no nível 36 é o divisor de águas",
        "when": "nível 36",
        "why": (
            "Com a ordem do escudo você aprende Guard no 15, Lucky Strike no 24, "
            "Leaf Bracer no 27 e SECOND CHANCE no 36. Até o 36 o Proud é cruel; "
            "depois dele você sobrevive a quase tudo com 1 de HP e cura. Se uma "
            "luta parece impossível, quase sempre a resposta é subir até o 36 "
            "antes de insistir."
        ),
    },
    {
        "name": "O melhor XP do começo está na Deep Jungle",
        "when": "Deep Jungle",
        "why": (
            "Nas Árvores de Escalada, enquanto a fruta roxa grande estiver "
            "intacta, Powerwilds nascem sem parar. É o farm mais barato do início "
            "do jogo — e você já está lá pela história, para soltar a Jane."
        ),
    },
    {
        "name": "Cura infinita no Anti-Sora da Neverland",
        "when": "Neverland",
        "why": (
            "O Sora-sombra dos corredores do navio derruba uma Mega-Potion (e às "
            "vezes um Elixir) toda vez que você zera o HP dele, e ele reaparece. É "
            "daqui que sai o estoque para a Hades Cup e para os chefes opcionais "
            "no Proud."
        ),
    },
    {
        "name": "Tinker Bell é a melhor peça de build do jogo",
        "when": "depois da Neverland",
        "why": (
            "Regen constante na party e um auto-life de graça. Invoque no começo "
            "de toda luta difícil — Maleficent Dragão, Behemoth, Unknown. No Proud "
            "ela vale mais que qualquer acessório."
        ),
    },
    {
        "name": "Salve antes de tudo, mesmo com Continue liberado",
        "when": "sempre",
        "why": (
            "Na run do 100% o Continue é permitido (a trava do Undefeated é só na "
            "cronometrada), mas no Proud morrer custa caro em tempo. Salve em todo "
            "save point antes de chefe — o hábito ainda te treina para a segunda "
            "run, onde apertar Continue uma única vez derruba o troféu."
        ),
    },
]

# ── Hábitos e regras que decidem cada run ─────────────────────────────────
PREP = [
    {
        "name": "Não troque NENHUM equipamento",
        "when": "cronometrada, o tempo todo",
        "why": (
            "Unchanging Armor conta chaveiro (keychain), cajado, escudo e "
            "acessórios de QUALQUER personagem — Sora, Donald e Goofy. O que já "
            "vem equipado no começo pode ficar. Habilidades e itens de cura podem "
            "ser mexidos à vontade: só equipamento conta."
        ),
    },
    {
        "name": "Nunca aperte Continue — carregue o save",
        "when": "cronometrada, o tempo todo",
        "why": (
            "Undefeated cai se você escolher Continue uma única vez. Morrer não é "
            "problema: no Game Over, saia e carregue o arquivo. Por isso, salve em "
            "TODO save point, principalmente antes de chefe."
        ),
    },
    {
        "name": "Sele só os keyholes obrigatórios",
        "when": "cronometrada",
        "why": (
            "Traverse Town, Wonderland, Deep Jungle, Agrabah, "
            "Neverland e Hollow Bastion são fixos; o Coliseu vem junto da "
            "história. Dos três restantes (Monstro, Atlantica, Cidade do "
            "Halloween) bastam DOIS. Atlantica é o mais lento — costuma ser o "
            "cortado."
        ),
    },
    {
        "name": "Equipe Lucky Strike em todo mundo",
        "when": "run do 100%",
        "why": (
            "Todos os materiais raros de síntese (Mystery Goo, Serenity Power, "
            "Stormy Stone, as gemas) são drop. Lucky Strike em Sora, Donald e "
            "Goofy é a diferença entre uma tarde e uma semana de farm para a "
            "Ultima Weapon. Com a ordem do escudo ele chega cedo, no nível 24."
        ),
    },
    {
        "name": "Não avance o Hollow Bastion antes de fechar o Coliseu",
        "when": "run do 100%, Hollow Bastion Visita 1",
        "why": (
            "Vencer o Ansem-Riku (o chefe logo depois da Maleficent Dragão) muda "
            "os encontros e sobe os status dos inimigos em TODOS os mundos, "
            "permanentemente. Faça o farm e as copas que quiser antes de subir "
            "para o Grand Hall."
        ),
    },
    {
        "name": "Volte à Casa da Árvore e brigue com a Sabor de novo",
        "when": "run do 100%, Deep Jungle",
        "why": (
            "Antes de avançar a história da Selva, encontre a Sabor mais uma vez "
            "na Casa da Árvore: ela abre um buraco no piso, e é esse buraco que "
            "torna o Pink Agaricus viável depois — o bicho que dropa o Serenity "
            "Power da Ultima Weapon."
        ),
    },
    {
        "name": "Confira o relógio da Neverland a cada hora",
        "when": "run do 100%, depois da Neverland",
        "why": (
            "A torre do relógio dá 12 prêmios, um por hora do mostrador (que segue "
            "o seu tempo de jogo). Se perder uma hora, a chance só volta 11 horas "
            "depois. Tem Orichalcum, Mythril e Megalixir na lista."
        ),
    },
    {
        "name": "Só abra a porta do Final Rest com o Diário 100%",
        "when": "run do 100%, Fim do Mundo",
        "why": (
            "É o ponto sem volta do jogo inteiro. Confirme no menu: Chronicles, "
            "Ansem's Report, Characters 1 e 2, Heartless, 101 Dálmatas, Trinity "
            "List e Mini Games, todos com o selo de completo."
        ),
    },
]

_AW = "https://www.khguides.com/kh/awakening/images/"
_DI = "https://www.khguides.com/kh/destiny-islands/images/"

# ── 01 — O walkthrough: as visitas na ORDEM DE JOGO ────────────────────────
# Uma lista só, linear. Nada de agrupar por mundo: Traverse Town aparece seis
# vezes porque você volta lá seis vezes, e cada volta é uma parada diferente.
#
# Os nomes de mundo e de área são os que aparecem NA TELA (o jogo não tem
# português): "Wonderland", "Second District", "Lotus Forest". A explicação em
# português vem ao lado, no texto.
#
# kind: "história" (obrigatória), "opcional" (só no 100%), "varredura" (a volta
# ao mundo no fim, com Glide + trinity Branca) e "final" (ponto sem volta).
#
# Cada visita carrega os coletáveis que dá para pegar NAQUELA ida — a caixa de
# marcação é a mesma da aba Coletáveis, então marcar aqui marca lá:
#   puppies   → grupos de PUPPIES ("13 · 14 · 15")
#   trinities → cor + número de TRINITIES ("Azul 5")
#   postcards → POSTCARDS ("Postal 1")
#   pages     → PAGES ("Página 1")
VISITS = [
    {
        "world": "Dive to the Heart",
        "name": "Dive to the Heart — o Despertar, a escolha que define a run",
        "kind": "história",
        "level": "Battle LV 1",
        "run": "As duas runs",
        "trophies": [],
        "note": (
            "A arma que você ESCOLHE define a ordem em que aprende as "
            "habilidades até o nível 100; a que você ABRE MÃO define seus status "
            "iniciais e qual atributo cresce mais devagar. Escolha o ESCUDO e "
            "sacrifique a ESPADA — o porquê, com os números, está no passo 1."
        ),
        "steps": [
            {
                "title": "Escolha o ESCUDO (Dream Shield) e sacrifique a ESPADA (Dream Sword)",
                "do": (
                    "Escolher define as habilidades: o escudo entrega Guard no "
                    "nível 15, Lucky Strike no 24, Leaf Bracer no 27 e SECOND "
                    "CHANCE no 36 — é o kit que segura o Proud.\n\n"
                    "Sacrificar define os status. Comparando as duas opções de "
                    "escudo: sacrificando a ESPADA você começa com STR 3 / DEF 4 / "
                    "MP 2 / AP 3 e 8 slots de item; sacrificando o cajado seria "
                    "STR 4 / DEF 4 / MP 2 / AP 1. Você troca 1 ponto de força por "
                    "DOIS de AP.\n\n"
                    "É o melhor negócio do começo do jogo: AP é o que permite "
                    "equipar habilidade, e com 1 de AP você entra no Guard Armor "
                    "praticamente sem nada. Com 3, o Dodge Roll já está equipado. "
                    "A força crescer mais devagar combina com o resto do guia: as "
                    "builds de Kurt Zisa, Phantom, Sephiroth e Unknown são de "
                    "magia e esquiva, não de porrada."
                ),
                "image": _AW + "t1.webp",
                "tag": "build",
            },
            {
                "title": "Responda às três perguntas pensando no XP",
                "do": (
                    "As respostas dos três garotos definem sua curva de "
                    "experiência: primeira opção = amanhecer (sobe rápido cedo, "
                    "lento depois), do meio = meio-dia (equilibrado), última = "
                    "noite (lento cedo, muito rápido depois do nível 60).\n\n"
                    "Na run do 100%: escolha SEMPRE a última — o nível 100 é "
                    "troféu, e é no fim que a curva da noite dispara. Na "
                    "cronometrada: SEMPRE a primeira, porque você quer nível cedo "
                    "e vai parar por volta do 40."
                ),
                "image": _AW + "t10.webp",
                "tag": "escolha",
            },
            {
                "title": "Aprenda a travar a mira e derrote o Darkside",
                "do": (
                    "O jogo ensina o lock-on aqui — use sempre. No fim da área "
                    "vem o Darkside: bata na mão quando ele socar o chão e suba "
                    "pelo braço para acertar a cabeça. Morrer aqui não quebra "
                    "nada: o jogo continua e não existe tela de Continue nesta "
                    "luta."
                ),
                "image": _AW + "tb1.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Destiny Islands",
        "name": "Destiny Islands — a ilha do Sora, o tutorial",
        "kind": "história",
        "level": "Battle LV 1",
        "run": "As duas runs",
        "trophies": [],
        "note": (
            "É o único mundo do jogo ao qual você NUNCA volta. Mesmo assim não "
            "há nada da platina aqui: sem dálmata, sem trinity, só um baú com o "
            "acessório Protect Chain."
        ),
        "steps": [
            {
                "title": "Junte os 4 primeiros itens da jangada",
                "do": (
                    "Dois Logs (um na beira da praia depois da ponte de madeira, "
                    "outro na ilhota do outro lado), uma Rope (canto da plataforma "
                    "alta de madeira, suba a escada) e um Cloth (dentro da casa da "
                    "árvore). Se juntar tudo SEM pedir dica à Kairi, ela te dá "
                    "uma Hi-Potion."
                ),
                "image": _DI + "t1.webp",
                "tag": "coleta",
            },
            {
                "title": "Treine com Tidus, Selphie, Wakka e Riku",
                "do": (
                    "No 100% vale muito: são os primeiros pontos de XP e o melhor "
                    "lugar do jogo para aprender a defletir (bata na bola do "
                    "Wakka no tempo certo). Na cronometrada, pule — não vale o "
                    "relógio."
                ),
                "image": _DI + "t23.webp",
                "tag": "opcional",
            },
            {
                "title": "Corrida contra o Riku (dá nome à nave)",
                "do": (
                    "Vencer batiza sua Gummi Ship com o nome que você escolher; "
                    "perder batiza como \"Highwind\". Rota segura: desça na hora, "
                    "corra pela areia até a rampa do fundo, pule na árvore-estrela "
                    "até ela acender e volte pela praia."
                ),
                "image": _DI + "t25.webp",
                "tag": "minijogo",
            },
            {
                "title": "Baú do Protect Chain, na Cove",
                "do": (
                    "Na Cove (a enseada da jangada), empurre o caixote de madeira "
                    "que fica perto da tirolesa até a parede de pedra, suba nele e "
                    "alcance a saliência acima; o baú dentro da gruta tem o "
                    "Protect Chain. Na cronometrada você pode pegar, mas NÃO "
                    "equipe — equipar quebra o Unchanging Armor."
                ),
                "image": _DI + "t42.webp",
                "tag": "baú",
            },
            {
                "title": "Termine o dia e enfrente a tempestade",
                "do": (
                    "Junte os itens da segunda lista (2 cocos, 3 peixes, água e "
                    "cogumelo) e fale com a Kairi. À noite, sua espada de madeira "
                    "não machuca as sombras: corra para o galpão da cachoeira, "
                    "SALVE no save point, suba e atravesse a ponte para pegar a "
                    "Keyblade."
                ),
                "image": _DI + "t45.webp",
                "tag": "história",
            },
        ],
    },
    {
        "world": "Traverse Town",
        "name": "Traverse Town — 1ª visita: a cidade-refúgio, Leon e o Guard Armor",
        "kind": "história",
        "level": "Battle LV 1",
        "run": "As duas runs",
        "trophies": [],
        "note": (
            "É aqui que o Diário do Jiminy começa a contar. A partir de agora, "
            "todo Heartless novo que você derrota vira uma entrada — e o troféu "
            "Professor exige a lista inteira. No 100%, saia daqui com as três "
            "trinities Azuis feitas e os postais 1 a 6 no bolso: estão todos "
            "listados no fim deste card, com foto."
        ),
        "puppies": [],
        "trinities": ["Azul 1", "Azul 2", "Azul 3"],
        "postcards": ["Postal 1", "Postal 2", "Postal 3", "Postal 4", "Postal 5", "Postal 6"],
        "pages": [],
        "steps": [
            {
                "title": "Primeiro baú: Mythril Shard na Accessory Shop",
                "do": (
                    "Siga o Pluto, entre na loja pelo portão grande e fale com o "
                    "Cid. O baú fica em cima do armário verde, perto da porta."
                ),
                "image": _TT + "t4.webp",
                "tag": "baú",
            },
            {
                "title": "Second District e a luta contra o Leon",
                "do": (
                    "Saia da loja, suba a escada à esquerda e atravesse o portão "
                    "grande do canto direito. Depois da cena, derrote pelo menos "
                    "cinco Heartless e volte para falar com o Cid. Ao sair, você "
                    "encara o Leon: circule em volta dele e bata 1 ou 2 vezes "
                    "entre os golpes; a bola de fogo dele pode ser rebatida com o "
                    "ataque no tempo certo. Perder aqui NÃO dá Game Over — a "
                    "história segue."
                ),
                "image": _TT + "t7.webp",
                "tag": "chefe",
            },
            {
                "title": "O relógio secreto do quarto do hotel",
                "do": (
                    "Depois da cena, fale com a Yuffie, abra o baú da mesa "
                    "(Elixir) e bata DEZ vezes no canto do relógio grande acima do "
                    "Leon: aparece um baú na cômoda com um Mythril. Fácil de "
                    "esquecer e ninguém volta aqui por acaso."
                ),
                "image": _TT + "t10.webp",
                "tag": "baú",
            },
            {
                "title": "Third District e o Guard Armor",
                "do": (
                    "Vá ao Third District passando por trás das lojas do Second. "
                    "Depois da emboscada vem o Guard Armor: mire nas MÃOS primeiro "
                    "(são as partes mais rápidas), depois pés, torso por último. "
                    "Se as peças subirem girando, pule para o lado."
                ),
                "image": _TT + "t19.webp",
                "tag": "chefe",
            },
            {
                "title": "Equipe Dodge Roll e destranque a porta do Third District",
                "do": (
                    "Donald ensina Fire e Goofy ensina Dodge Roll — equipe o Dodge "
                    "Roll imediatamente (habilidade não conta para o Unchanging "
                    "Armor). Antes de sair, examine o keyhole grande perto das "
                    "portas duplas do Third District: isso abre o atalho "
                    "First↔Third District para o resto do jogo."
                ),
                "image": _TT + "t25.webp",
                "tag": "atalho",
            },
            {
                "title": "100%: as trinities Azuis e os postais desta visita",
                "do": (
                    "Só as trinities AZUIS funcionam por enquanto (Donald e Goofy "
                    "precisam estar na equipe). Faça as três listadas abaixo — a "
                    "do café te teleporta para a sacada com o Postal 1. Depois "
                    "recolha os postais 2 a 6 e jogue todos na caixa de correio do "
                    "First District: cada um vira um item."
                ),
                "image": _TN + "t2.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Wonderland",
        "name": "Wonderland — o mundo da Alice",
        "kind": "história",
        "level": "Battle LV 3",
        "run": "As duas runs",
        "trophies": ["The Rabbit Hole"],
        "note": (
            "Obrigatório nas duas runs. No 100%, duas caixas de dálmatas e duas "
            "trinities Azuis saem já nesta ida; as outras duas caixas (19-21 e "
            "58-60) e as trinities Verde e Branca ficam para a varredura, porque "
            "pedem Glide, Thunder e cores que você ainda não tem."
        ),
        "puppies": ["13 · 14 · 15", "16 · 17 · 18"],
        "trinities": ["Azul 5", "Azul 6"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Bizarre Room: empurre a cama antes de encolher",
                "do": (
                    "No Bizarre Room (o quarto da mesa com a garrafa), ANTES de "
                    "beber, empurre a cama do canto: ela desliza e abre a passagem "
                    "que você vai usar. Só então beba e siga pelo corredor até o "
                    "Queen's Castle, o tribunal."
                ),
                "image": _WL + "t1.webp",
                "tag": "passo",
            },
            {
                "title": "Cronometrada: pegue só UMA prova e volte",
                "do": (
                    "O tribunal pede provas, mas basta UMA para prosseguir. Na "
                    "corrida, pegue a mais próxima (Footprints, na alcova atrás da "
                    "flor vermelha grande da Lotus Forest) e volte. Você perde a "
                    "Blizzard grátis, mas ela cai do Trickmaster de qualquer jeito."
                ),
                "image": _WL + "t14.webp",
                "tag": "atalho",
            },
            {
                "title": "100%: as quatro provas da Lotus Forest, na ordem certa",
                "do": (
                    "1) Dê uma Potion ao bulbo amarelo perto do lago para virar "
                    "gigante. 2) Como gigante, pule no toco de madeira do canto "
                    "oposto — isso levanta as vitórias-régias. 3) Examine a árvore "
                    "grande do centro e pegue a fruta para voltar ao tamanho "
                    "normal. 4) Footprints na alcova atrás da flor vermelha; "
                    "Antennae em cima dos três cogumelos do fundo; Stench pela "
                    "passagem escavada na árvore grande (leva ao fogão do Bizarre "
                    "Room); Claw Marks pela passagem do canto até a torneira — "
                    "pule na prateleira. As Claw Marks fazem o Cheshire te "
                    "ensinar Blizzard. Aproveite que está na Lotus Forest: as "
                    "duas caixas de dálmatas e as duas trinities Azuis desta "
                    "visita estão aqui (fim do card)."
                ),
                "image": _WL + "t15.webp",
                "tag": "coleta",
            },
            {
                "title": "Escolha a caixa e destrua a Crank Tower",
                "do": (
                    "Fale com um soldado-carta e escolha uma caixa qualquer — pode "
                    "vir um Heartless, ou o Donald/Goofy presos em gaiola. Na "
                    "luta, o alvo é a TORRE do centro: circule, pule e bata. Bater "
                    "na Rainha congela alguns soldados por um tempo."
                ),
                "image": _WL + "t17.webp",
                "tag": "chefe",
            },
            {
                "title": "Tea Party Garden → Bizarre Room de cabeça para baixo",
                "do": (
                    "Volte à Lotus Forest, siga para o Tea Party Garden (o jardim "
                    "do chá) e entre no chalé: o Bizarre Room está de cabeça para "
                    "baixo. Suba nas duas lanternas do centro e toque as duas. "
                    "Depois abra a trava de metal da parede do fundo."
                ),
                "image": _WL + "t23.webp",
                "tag": "passo",
            },
            {
                "title": "Trickmaster — congele o fogão",
                "do": (
                    "Só o torso dele leva dano. Pule da mesa do centro para "
                    "encaixar combos aéreos inteiros. O truque que muda a luta: "
                    "trave a mira na BASE DO FOGÃO e lance Blizzard 1 a 3 vezes — "
                    "ele fica ~100 segundos sem conseguir acender os bastões, e "
                    "sem bastões acesos ele não tem ataque de fogo. Prêmio: "
                    "keyhole selado (troféu The Rabbit Hole) e o Navi-G Piece."
                ),
                "image": _WL + "t28.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Olympus Coliseum",
        "name": "Olympus Coliseum — 1ª visita: o coliseu do Hércules, Phil e o Cérbero",
        "kind": "história",
        "level": "Battle LV 3",
        "run": "As duas runs",
        "trophies": [],
        "note": (
            "O keyhole do Coliseu NÃO é selado nesta visita: ele exige a trinity "
            "AMARELA do Lobby, e a cor amarela só vem com a Hercules Cup, muito "
            "mais tarde. O troféu Junior Hero, portanto, fica para lá. Aqui você "
            "leva Thunder, o Sonic Blade e, no 100%, uma caixa de dálmatas."
        ),
        "puppies": ["22 · 23 · 24"],
        "trinities": ["Azul 7", "Azul 8"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Treinamento do Phil (ganha Thunder)",
                "do": (
                    "No Lobby, fale com o Phil, tente empurrar o pedestal e aceite "
                    "o treino: quebre todos os barris dentro do tempo usando "
                    "finalizações de combo e magia. No segundo percurso, quebre os "
                    "de baixo primeiro; use Fire (com lock-on) no barril da "
                    "plataforma flutuante. Prêmio: magia Thunder."
                ),
                "image": _OC + "t1.webp",
                "tag": "minijogo",
            },
            {
                "title": "Preliminares até o Cloud",
                "do": (
                    "São 7 chaves seguidas — jogue conservador, porque o HP não "
                    "recarrega entre elas. Contra o Cloud: ou você usa Guard para "
                    "quebrar a estocada dele (duas defesas seguidas) e emenda um "
                    "combo, ou Dodge Roll no golpe vertical e bate 2 vezes. Perder "
                    "para o Cloud NÃO dá Game Over."
                ),
                "image": _OC + "t1.webp",
                "tag": "chefe",
            },
            {
                "title": "Cérbero",
                "do": (
                    "Ele começa andando e cuspindo fogo teleguiado: role em "
                    "círculo fechado ao redor dele. Quando parar, ele morde com "
                    "uma cabeça de cada vez — depois de cada mordida, bata DUAS "
                    "vezes numa cabeça lateral e recue (não termine o combo). "
                    "Quando ele se erguer no ar, saia de baixo."
                ),
                "image": _OC + "t1.webp",
                "tag": "chefe",
            },
            {
                "title": "Fale com o Cloud na escadaria (Sonic Blade) e faça as trinities dos Gates",
                "do": (
                    "Depois da luta, saia do Lobby e fale com o Cloud sentado na "
                    "escada em frente ao vestíbulo: ele ensina o Sonic Blade, uma "
                    "das melhores habilidades do jogo. Nos Gates (a área de "
                    "entrada) há duas trinities Azuis, uma em frente a cada "
                    "estátua de gladiador — a da direita solta os dálmatas 22-24."
                ),
                "image": _TN + "t8.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Deep Jungle",
        "name": "Deep Jungle — a selva do Tarzan",
        "kind": "história",
        "level": "Battle LV 5",
        "run": "As duas runs",
        "trophies": ["Member of the Tribe"],
        "note": (
            "ATENÇÃO no 100%: antes de avançar a história depois da cena da "
            "tenda, VOLTE à Tree House e lute com a Sabor de novo. Ela abre um "
            "buraco no chão, e é esse buraco que torna o Pink Agaricus viável "
            "depois (material Serenity Power, da Ultima Weapon). Quatro caixas de "
            "dálmatas saem nesta ida."
        ),
        "puppies": ["25 · 26 · 27", "28 · 29 · 30", "31 · 32 · 33", "34 · 35 · 36"],
        "trinities": ["Azul 9", "Azul 10"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Sobreviva à Sabor e desça para o Camp",
                "do": (
                    "Role para os lados e bata combos de 3; Fire repetido também "
                    "resolve. Perder aqui não interrompe a história. Depois desça "
                    "pelo tronco oco e escorregue pelas árvores até o Camp, o "
                    "acampamento da Jane."
                ),
                "image": _DJ + "t1.webp",
                "tag": "chefe",
            },
            {
                "title": "Os 6 slides do projetor (no Camp)",
                "do": (
                    "1) Em cima da tenda principal (suba pelas caixas perto do "
                    "globo). 2) Numa cômoda no canto, sob as lonas bege. 3) No "
                    "chão, ao lado do quadro-negro com o desenho do Tarzan. 4) Em "
                    "cima da pilha grande de caixas no centro. 5) Em cima da lona "
                    "junto à parede de bambu — suba na tenda e ande pelas lonas. "
                    "6) Em cima das caixas à direita da entrada da tenda. Depois, "
                    "examine o projetor. A trinity Azul do Camp (dálmatas 34-36) "
                    "fica ao lado da mesa de laboratório."
                ),
                "image": _DJ + "t7.webp",
                "tag": "coleta",
            },
            {
                "title": "Hippos' Lagoon e os cipós até as copas",
                "do": (
                    "Nos cipós, aperte o botão quando \"Jump Next\" acender. Se "
                    "estiver sofrendo, há o caminho alternativo: pule nas costas "
                    "dos hipopótamos até a plataforma do fundo e suba pelo poste — "
                    "é do lado oposto da lagoa que está a caixa dos dálmatas "
                    "25-27. Na área Vines 2, use os cipós da direita para alcançar "
                    "a saliência central com os dálmatas 28-30. No último pulo, "
                    "aperte ataque no ar para ganhar distância."
                ),
                "image": _DJ + "t16.webp",
                "tag": "passo",
            },
            {
                "title": "Limpe os Heartless das 5 áreas",
                "do": (
                    "Camp (Protect-G), Bamboo Thicket (Fire-G), Cliff (Aeroga-G), "
                    "Climbing Trees (Aeroga-G) e Tree House (Shell-G). Cada área "
                    "limpa dá um bloco gummi de um gorila. Jane, na tenda, diz "
                    "quais faltam. Nas Climbing Trees, a trinity Azul fica numa "
                    "plataforma elevada perto da passagem para a Tree House."
                ),
                "image": _DJ + "t22.webp",
                "tag": "coleta",
            },
            {
                "title": "Sabor no Bamboo Thicket e o salvamento da Jane",
                "do": (
                    "A Sabor pula das árvores no bambuzal: encoste-a numa parede e "
                    "emende combos completos para mantê-la atordoada; Fire com "
                    "lock-on também funciona bem. Depois, nas Climbing Trees, bata "
                    "na fruta roxa grande para libertar a Jane — enquanto ela "
                    "estiver inteira, Powerwilds nascem infinitamente (o melhor XP "
                    "do começo do jogo; ignore na cronometrada)."
                ),
                "image": _DJ + "t25.webp",
                "tag": "chefe",
            },
            {
                "title": "Clayton & Stealth Sneak (no Cliff)",
                "do": (
                    "Role logo no início para desviar do primeiro tiro. Trave a "
                    "mira no bicho INVISÍVEL e bata combos aéreos até ele "
                    "aparecer. Quando o Clayton cair, trave nele e mande a party "
                    "atrás (dois toques no botão) enquanto você continua batendo "
                    "no Stealth Sneak. Você NÃO precisa matar o bicho: zerar o HP "
                    "do Clayton acaba a luta. Prêmio: magia Cure."
                ),
                "image": _DJ + "t30.webp",
                "tag": "chefe",
            },
            {
                "title": "Waterfall Cavern: sele o keyhole e ganhe a trinity Vermelha",
                "do": (
                    "Entre na caverna à esquerda da cachoeira e suba de saliência "
                    "em saliência — na metade da subida, logo abaixo de uma parede "
                    "de cipós, está a caixa dos dálmatas 31-33. Depois de selar "
                    "(troféu Member of the Tribe), o Tarzan te dá o chaveiro "
                    "Jungle King e a party passa a fazer trinities VERMELHAS — o "
                    "que destrava a próxima parada em Traverse Town."
                ),
                "image": _DJ + "t31.webp",
                "tag": "troféu",
            },
            {
                "title": "100%: cozinha, Jungle Slider e cipós",
                "do": (
                    "Entradas de minijogo do Diário: Jungle Slider (a partir do "
                    "Tunnel, pegue as 10 frutas de cada percurso) e Vine Swing. Na "
                    "cozinha do Camp, examine relógio e mastro (2 cartões de "
                    "receita) e roupa no varal, globo e vitrola (3 anotações) — "
                    "faça a experiência com só 2 anotações primeiro, depois pegue "
                    "a terceira e repita, para maximizar os Ethers."
                ),
                "image": _DJ + "t39.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Traverse Town",
        "name": "Traverse Town — 2ª visita: Merlin, o Livro Velho e o keyhole",
        "kind": "história",
        "level": "Battle LV 5",
        "run": "As duas runs",
        "trophies": ["Where the Bells Toll"],
        "note": (
            "Com a trinity Vermelha na mão, a cidade abre: o Waterway (com os "
            "dálmatas 10-12), o beco dos dálmatas 4-6 e a torre do sino. Com "
            "Thunder, saem também os postais 7 e 8. Tudo listado no fim do card."
        ),
        "puppies": ["4 · 5 · 6", "10 · 11 · 12"],
        "trinities": ["Vermelha 1", "Vermelha 2", "Vermelha 3", "Azul 4"],
        "postcards": ["Postais 7 e 8"],
        "pages": [],
        "steps": [
            {
                "title": "Trinity Vermelha do Alleyway → Waterway",
                "do": (
                    "Vá ao Alleyway (o beco no canto sudoeste do Second District, "
                    "perto da fonte) e faça a trinity Vermelha na grade do canal, "
                    "no fundo. Entre no Waterway e fale com o Leon; fale com ele "
                    "DE NOVO sobre o bloco gummi da selva para receber o "
                    "Earthshine (que vira a invocação do Simba). Logo dentro da "
                    "escadaria que sobe para o estúdio do Merlin está a caixa dos "
                    "dálmatas 10-12."
                ),
                "image": _TT + "t28.webp",
                "tag": "passo",
            },
            {
                "title": "O Livro Velho e a casa do Merlin",
                "do": (
                    "Fale com o Cid na Accessory Shop: ele pede que você entregue "
                    "um Old Book a um morador do Third District. Lá, use FIRE na "
                    "porta de madeira com o símbolo de chama, atravesse as pedras "
                    "móveis e entre na casa do lago (Mystical House) para achar o "
                    "Merlin."
                ),
                "image": _TT + "t34.webp",
                "tag": "passo",
            },
            {
                "title": "Simba, a trinity Azul do Magician's Study e o Bosque",
                "do": (
                    "Entregue o livro. A Fada Madrinha transforma o Earthshine na "
                    "invocação SIMBA. Antes de sair, faça a trinity Azul do "
                    "estúdio (perto do save point). O Livro Velho é a porta do 100 "
                    "Acre Wood, o mundo do Ursinho Pooh — opcional agora, "
                    "obrigatório no 100% (troféu Pooh's Friend); você vai entrar "
                    "nele com a primeira Torn Page, na 3ª visita."
                ),
                "image": _TT + "t37.webp",
                "tag": "passo",
            },
            {
                "title": "Volte ao Cid e ganhe o Warp-G",
                "do": (
                    "Entre na casa vazia do Third District (subindo a escada perto "
                    "da passagem para o Second) e fale com o Cid. Ele instala o "
                    "gummi de navegação e te dá o Warp-G: a partir daqui você "
                    "viaja instantaneamente para mundos já visitados. Isso sozinho "
                    "salva muito relógio na cronometrada."
                ),
                "image": _TT + "t40.webp",
                "tag": "atalho",
            },
            {
                "title": "O sino do Second District e o Opposite Armor",
                "do": (
                    "Entre na Gizmo Shop, saia pelo lado oposto, suba a escada da "
                    "esquerda e faça a trinity Vermelha na torre do sino. Toque o "
                    "sino TRÊS vezes: o keyhole aparece na fonte. Ao se aproximar, "
                    "o Guard Armor volta e vira Opposite Armor — mãos e pés "
                    "primeiro, torso por último; se o torso não perder HP, troque "
                    "o lock para a cabeça."
                ),
                "image": _TT + "t43.webp",
                "tag": "chefe",
            },
            {
                "title": "Sele, pegue o Comet-G, conheça o Pinóquio — e os postais 7 e 8",
                "do": (
                    "Selar dá o troféu Where the Bells Toll e a magia Aero. Fale "
                    "com o Cid atrás da loja (Comet-G grátis) e examine a pilha "
                    "colorida no chão da Accessory Shop para encontrar o Pinóquio. "
                    "No 100%: lance THUNDER no fio exposto do canto do Third "
                    "District, entre na Gizmo Shop, pule nos três botões em cima "
                    "da máquina e examine o relógio central — saem os postais 7 e "
                    "8 juntos. A trinity Vermelha da cerca atrás da Item Shop "
                    "libera os dálmatas 4-6. A Phil Cup abre agora."
                ),
                "image": _TT + "t49.webp",
                "tag": "troféu",
            },
        ],
    },
    {
        "world": "Olympus Coliseum",
        "name": "Olympus Coliseum — Phil Cup (e os dois troféus fáceis do coliseu)",
        "kind": "opcional",
        "level": "Battle LV 6+",
        "run": "Só na run do 100%",
        "trophies": ["Novice Hero", "Supreme Soloist", "Time Attacker"],
        "note": (
            "Abre depois de selar Traverse Town. Cada copa tem TRÊS modos: "
            "normal (com a party), solo (só o Sora) e contrarrelógio. Os dois "
            "últimos só aparecem depois de vencer o normal — e basta UM de cada, "
            "em qualquer copa, para Supreme Soloist e Time Attacker. Faça aqui, "
            "que é a copa mais fácil."
        ),
        "puppies": [],
        "trinities": [],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Phil Cup normal (troféu Novice Hero, ganha Gravity)",
                "do": (
                    "9 chaves. Blizzard resolve as chaves de Powerwild e Blue "
                    "Rhapsody agrupados; contra Large Body, derrote os Green "
                    "Requiem antes. Prêmio: a magia GRAVITY — que é a chave de "
                    "várias caixas de dálmatas do Hollow Bastion e de metade dos "
                    "chefes daqui para a frente."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Phil Cup solo (Supreme Soloist) e contrarrelógio (Time Attacker)",
                "do": (
                    "Solo dá Combo Plus; contrarrelógio de 3 minutos dá Tech "
                    "Boost. Os dois troféus caem aqui e você nunca mais precisa "
                    "repetir os modos extras em copa nenhuma."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
        ],
    },
]

VISITS += [
    {
        "world": "Agrabah",
        "name": "Agrabah — a cidade do Aladdin e a Cave of Wonders",
        "kind": "história",
        "level": "Battle LV 8",
        "run": "As duas runs",
        "trophies": ["Magic Lamp"],
        "note": (
            "37 baús: é o mundo com mais baú do jogo. Nesta ida saem uma caixa "
            "de dálmatas, três trinities e a Torn Page #1. As outras três "
            "caixas (46-48, 49-51, 52-54) pedem High Jump — ficam para a "
            "varredura."
        ),
        "puppies": ["37 · 38 · 39"],
        "trinities": ["Azul 11", "Azul 12", "Vermelha 4"],
        "postcards": [],
        "pages": ["Página 1"],
        "steps": [
            {
                "title": "Liberte o Tapete e ache a Jasmine",
                "do": (
                    "Suba o poste de madeira à direita para entrar na casa \"???\" "
                    "(Aladdin's House) e EMPURRE a cômoda que prende o tapete "
                    "mágico. Depois vá ao Alley pela passagem em frente: cena com "
                    "a Jasmine e o Jafar, e uma leva de Heartless (Blizzard "
                    "resolve bem em espaço fechado)."
                ),
                "image": _AG + "t4.webp",
                "tag": "passo",
            },
            {
                "title": "Desert: encontre o Aladdin",
                "do": (
                    "Volte ao ponto de chegada e passe pelo arco grande até a "
                    "muralha. Salve, deixe o tapete te levar ao deserto e limpe os "
                    "Heartless. Na volta, a Main Street está bloqueada: suba no "
                    "prédio e pule pelas lonas até o Alley."
                ),
                "image": _AG + "t10.webp",
                "tag": "passo",
            },
            {
                "title": "As 3 travas para chegar ao Jafar (e a trinity do Bazaar)",
                "do": (
                    "1) Alley: numa saliência perto das lonas de madeira, em "
                    "frente à entrada da Plaza. 2) Aladdin's House: empurre a "
                    "cômoda da parede do fundo. 3) Bazaar: numa saliência alta em "
                    "frente à entrada da Main Street — a passagem para o Bazaar "
                    "fica numa plataforma alta no canto da Main Street, "
                    "alcançável pulando das lonas ao lado da casa do Aladdin. No "
                    "centro do Bazaar, no chão, está a trinity Azul."
                ),
                "image": _AG + "t19.webp",
                "tag": "coleta",
            },
            {
                "title": "Pot Centipede (Palace Gates)",
                "do": (
                    "Leve o ALADDIN na party (ataque alto). Bata na CABEÇA — a "
                    "cauda tem dois balanços que machucam. Quando ele se quebrar "
                    "em Pot Spiders, um Blizzard bem posicionado limpa vários. "
                    "Quando as antenas brilharem azul, role para longe até "
                    "apagarem."
                ),
                "image": _AG + "t21.webp",
                "tag": "chefe",
            },
            {
                "title": "Cave of Wonders Guardian",
                "do": (
                    "Quando a caverna afundar o focinho na areia, suba nele e "
                    "fique. Só os OLHOS levam dano: trave num olho e bata combos "
                    "de chão; trocar o lock para o outro olho no meio do combo "
                    "ajuda a não cair. Lance AERO antes — corta metade do dano."
                ),
                "image": _AG + "t23.webp",
                "tag": "chefe",
            },
            {
                "title": "Relic → Dark → Silent Chamber → Hidden Room: derrube a coluna",
                "do": (
                    "Entre na caverna e caia no buraco à direita (Relic Chamber). "
                    "Atravesse Dark Chamber e Silent Chamber até a Hidden Room, "
                    "saia da água, pule na coluna de pedra e bata nela. Para "
                    "acionar estátuas distantes, o ALADDIN precisa estar na party "
                    "(o Abu pula nelas). A trinity Azul da Silent Chamber fica na "
                    "plataforma central, perto da passagem para o Hall."
                ),
                "image": _AG + "t24.webp",
                "tag": "passo",
            },
            {
                "title": "Torn Page #1 (Dark Chamber — só interessa no 100%)",
                "do": (
                    "Na Dark Chamber, a página fica numa plataforma no centro da "
                    "área — chega-se subindo a cachoeira a partir da Relic "
                    "Chamber. É a primeira das 5 páginas do 100 Acre Wood; você "
                    "vai devolvê-la ao Merlin na próxima parada em Traverse Town."
                ),
                "image": _TR + "t103.webp",
                "tag": "coletável",
            },
            {
                "title": "Treasure Room: dálmatas 37-39 e a trinity Vermelha",
                "do": (
                    "Na Treasure Room (a sala do save point antes da Lamp "
                    "Chamber), pule de cima de uma pilha de tesouro para a "
                    "saliência perto da entrada do Bottomless Hall — a caixa dos "
                    "dálmatas 37-39. A trinity Vermelha fica em frente à estátua "
                    "de esfinge, do outro lado do save point."
                ),
                "image": _TR + "t110.webp",
                "tag": "100%",
            },
            {
                "title": "Jafar e Jafar Gênio (Lamp Chamber)",
                "do": (
                    "Jafar flutua em círculo: pule das três plataformas de pedra e "
                    "bata combos aéreos; corra para os lados quando ele fizer o "
                    "encantamento que termina em chiado. Na segunda forma, o alvo "
                    "é a LÂMPADA nas mãos do Iago — trave nela, bata no ar e mande "
                    "a party junto; a lâmpada é imune a magia, mas o Jafar não. "
                    "Prêmio: Ansem's Report 1."
                ),
                "image": _AG + "t31.webp",
                "tag": "chefe",
            },
            {
                "title": "Fuga no tapete e a trinity Verde",
                "do": (
                    "Na fuga, segure para a ESQUERDA no primeiro trecho para "
                    "desviar de quase tudo; nos pilares de fogo, use a esquiva "
                    "pouco antes do impacto. Ao sair: troféu Magic Lamp, chaveiro "
                    "Three Wishes, invocação do Gênio e a party ganha trinity "
                    "VERDE — que abre a Sala de Síntese na próxima parada."
                ),
                "image": _AG + "t34.webp",
                "tag": "troféu",
            },
        ],
    },
    {
        "world": "Traverse Town",
        "name": "Traverse Town — 3ª visita: a Sala de Síntese e o 100 Acre Wood",
        "kind": "opcional",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": ["First Synthesis"],
        "note": (
            "Parada opcional na história e PULÁVEL na cronometrada. No 100% é "
            "onde a síntese começa (5 troféus) e onde você entra pela primeira "
            "vez no livro do Pooh."
        ),
        "puppies": ["7 · 8 · 9"],
        "trinities": ["Verde 1"],
        "postcards": ["Postal 10"],
        "pages": [],
        "steps": [
            {
                "title": "Abra o Item Workshop (trinity Verde da Accessory Shop)",
                "do": (
                    "Na Accessory Shop do First District, ative a trinity VERDE do "
                    "chão e suba a escada. Fale com o Moogle da mesa (explicação) e "
                    "depois com o Moogle do forno: a primeira síntese dá o troféu "
                    "First Synthesis. A caixa dos dálmatas 7-9 está numa mesa "
                    "perto de um dos Moogles e o Postal 10 é o panfleto da parede. "
                    "Saia pela porta do fundo uma vez: isso destranca o acesso "
                    "direto pelo First District."
                ),
                "image": _TT + "t54.webp",
                "tag": "desbloqueio",
            },
            {
                "title": "100 Acre Wood, episódio de entrada: o baú do tronco e o Elixir",
                "do": (
                    "Examine o Old Book no Magician's Study. Dentro, examine a "
                    "pilha de gravetos e fale com o Pooh. No fim do tronco oco há "
                    "um baú com Mythril Shard. Suba no telhado da casa do Pooh e "
                    "bata na chaminé: cai um Mega-Ether lá dentro; o armário do "
                    "canto tem um Elixir."
                ),
                "image": _HA + "t17.webp",
                "tag": "baú",
            },
            {
                "title": "Devolva a Torn Page #1 → Pooh's Hunny Hunt",
                "do": (
                    "Com a página de Agrabah no livro, examine a Hunny Tree no "
                    "canto superior esquerdo da página da direita e fale com o "
                    "Piglet. No minijogo, fique SEMPRE um galho abaixo do Pooh: "
                    "dali você alcança as abelhas dos dois lados. Depois de bater "
                    "nas abelhas o Sora volta sozinho ao galho — não mexa no "
                    "analógico. Caiu? Use Rush. Mais de 100 pontos conta para o "
                    "Cheer. Prêmio: Naturespark."
                ),
                "image": _HA + "t17.webp",
                "tag": "minijogo",
            },
            {
                "title": "Bambi",
                "do": (
                    "Traga o Naturespark para a Fada Madrinha no Magician's "
                    "Study: invocação BAMBI. O Bambi derruba orbes de MP — é peça "
                    "de build contra Kurt Zisa e no farm de cogumelos."
                ),
                "image": _TT + "t39.webp",
                "tag": "invocação",
            },
            {
                "title": "Compre as armas novas de Donald e Goofy",
                "do": (
                    "A Item Shop dos sobrinhos do Donald (Huey, Dewey e Louie) "
                    "recebe armas novas a cada visita. Blade Master, Master "
                    "Magician e Master Defender exigem TODAS — então compre "
                    "sempre que voltar aqui."
                ),
                "image": _TT + "t58.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Monstro",
        "name": "Monstro — a baleia; Pinóquio, Riku e o High Jump",
        "kind": "história",
        "level": "Battle LV 12",
        "run": "100% · opcional na cronometrada",
        "trophies": ["Honest Soul"],
        "note": (
            "Aqui você ganha o HIGH JUMP, a chave de meia dúzia de baús pelo "
            "jogo inteiro. Na cronometrada este é um dos três mundos \"escolha "
            "dois\" — e é o mais rápido dos três, então costuma entrar. No 100% "
            "saem quatro caixas de dálmatas, quatro trinities e a Torn Page #2."
        ),
        "puppies": ["55 · 56 · 57", "76 · 77 · 78", "79 · 80 · 81", "73 · 74 · 75"],
        "trinities": ["Azul 13", "Azul 14", "Azul 15", "Verde 7"],
        "postcards": [],
        "pages": ["Página 2"],
        "steps": [
            {
                "title": "A ordem das câmaras",
                "do": (
                    "Da Mouth (a boca) até a Chamber 4 o caminho não é linear: "
                    "Chamber 1 ► 2 ► 3 ► 2 ► 5 ► 6 ► 5 ► 4. As passagens certas "
                    "pulsam em verde. Search Ghosts flutuam alto: Fira e Blizzara "
                    "resolvem. No caminho: dálmatas 55-57 na Chamber 3 (plataforma "
                    "esverdeada sobre a entrada da 2), trinity Azul da Chamber 5 "
                    "(chão, em frente à passagem da 6) e dálmatas 79-81 na "
                    "Chamber 5 (saliência alta sobre um barril)."
                ),
                "image": _MO + "t4.webp",
                "tag": "passo",
            },
            {
                "title": "Chamber 6: Torn Page #2 e dálmatas 76-78",
                "do": (
                    "A página fica numa plataforma alta esverdeada em frente à "
                    "entrada da Chamber 5; a caixa de dálmatas 76-78 está no nível "
                    "do chão, também em frente à passagem da Chamber 5."
                ),
                "image": _TR + "t129.webp",
                "tag": "coletável",
            },
            {
                "title": "Parasite Cage (1ª luta, nas Bowels)",
                "do": (
                    "Só o rosto e a barriga levam dano. Bata combos aéreos BAIXOS "
                    "entre os golpes de braço; Guard deflete bem. Sem Guard, fique "
                    "na plataforma da entrada e bata do ar. O Riku ajuda e até "
                    "cura você. Prêmio: Goofy aprende Cheer."
                ),
                "image": _MO + "t11.webp",
                "tag": "chefe",
            },
            {
                "title": "Mouth: Watergleam, o baú do High Jump e três coletáveis",
                "do": (
                    "Depois da luta, desça pelo buraco: o nível da água na Mouth "
                    "baixa. Na saliência mais alta da frente há um baú com o "
                    "WATERGLEAM (vira a invocação Dumbo). No navio do Geppetto, o "
                    "baú tem a habilidade compartilhada HIGH JUMP — equipe na "
                    "hora. Com ela: dálmatas 73-75 na plataforma alta junto à "
                    "parede, em frente ao naufrágio. A trinity Azul fica na "
                    "plataforma de madeira da frente e a Verde em cima do navio."
                ),
                "image": _MO + "t12.webp",
                "tag": "habilidade",
            },
            {
                "title": "Throat: trinity Azul, depois Parasite Cage II (Stomach)",
                "do": (
                    "Suba pela Throat (a trinity Azul está no nível mais baixo, no "
                    "centro) até o Stomach. Ele agora suga ácido e cospe: fique na "
                    "plataforma CENTRAL, dando a volta por trás dele, e nunca pise "
                    "no verde brilhante do chão. Se bater na cabeça algumas vezes "
                    "ele abre a boca — trave na matéria escura de dentro e bata "
                    "sem parar. Prêmio: magia Stop e o troféu Honest Soul."
                ),
                "image": _MO + "t18.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Traverse Town",
        "name": "Traverse Town — 4ª visita: Geppetto, Spellbinder e o Dumbo",
        "kind": "opcional",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": "Pulável na cronometrada. No 100% é a visita dos gummis, do Spellbinder e do segundo episódio do Pooh.",
        "puppies": [],
        "trinities": [],
        "postcards": ["Postal 9"],
        "pages": [],
        "steps": [
            {
                "title": "Geppetto's House e o Wishing Star",
                "do": (
                    "Prédio novo no canto nordeste do First District. O Geppetto "
                    "dá plantas de gummi conforme o total de Heartless que você já "
                    "derrotou — volte sempre. O baú do canto tem o chaveiro "
                    "WISHING STAR (crítico em toda finalização de combo: é o que "
                    "facilita matar o Black Fungus). Entre na casa 30 vezes e fale "
                    "com o Pinóquio para a planta Chocobo. O Postal 9 está no "
                    "potinho da prateleira."
                ),
                "image": _TT + "t60.webp",
                "tag": "coletável",
            },
            {
                "title": "Spellbinder (7 magias) e o Dumbo",
                "do": (
                    "Com as SETE magias na mão (Fire, Blizzard, Thunder, Cure, "
                    "Gravity, Stop, Aero), fale com o Merlin: ele dá o chaveiro "
                    "SPELLBINDER, o melhor bastão de magia do jogo até a Ultima — "
                    "é ele que você usa contra Kurt Zisa e Phantom. Entregue o "
                    "Watergleam à Fada Madrinha para a invocação DUMBO."
                ),
                "image": _TT + "t63.webp",
                "tag": "build",
            },
            {
                "title": "Devolva a Torn Page #2 → Block Tigger",
                "do": (
                    "No livro, examine a casa com jardim na página da esquerda "
                    "(Rabbit's House). Arranque abóboras e repolhos do quintal "
                    "(chance de Potion e Elixir). Depois da cena, no minijogo use "
                    "RUSH parado PERTO de uma cenoura ainda não pisada (não em "
                    "cima dela, senão o comando não aparece). Olhe a sombra do "
                    "Tigger e para onde ele está virado. Mais de 150 pontos conta "
                    "para o Cheer."
                ),
                "image": _HA + "t17.webp",
                "tag": "minijogo",
            },
        ],
    },
    {
        "world": "Olympus Coliseum",
        "name": "Olympus Coliseum — Pegasus Cup",
        "kind": "opcional",
        "level": "Battle LV 12+",
        "run": "Só na run do 100%",
        "trophies": ["Artisan Hero"],
        "note": "Abre depois do Monstro. Termina em Leon & Yuffie.",
        "puppies": [],
        "trinities": ["Verde 4"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Pegasus Cup (troféu Artisan Hero)",
                "do": (
                    "Fire nos Barrel Spiders faz eles explodirem e levar os "
                    "vizinhos junto; Gravity nas chaves de Large Body e Toadstool. "
                    "Na final, deflita as shurikens da Yuffie com Guard e, com "
                    "lock-on no Leon, mande uma shuriken nele para atordoá-lo. "
                    "Prêmios: Strike Raid (normal), Orichalcum (solo) e Dark "
                    "Matter (contrarrelógio) — os dois últimos são materiais da "
                    "Ultima, então vale fazer os três modos."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Trinity Verde dos Gates",
                "do": (
                    "Já que está aqui: nos Gates, junto à parede à direita da "
                    "passagem para o mapa, entre dois braseiros. Dá um Mythril."
                ),
                "image": _TN + "t27.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Atlantica",
        "name": "Atlantica — o mundo da Pequena Sereia",
        "kind": "história",
        "level": "Battle LV 15",
        "run": "100% · opcional na cronometrada",
        "trophies": ["Master of the Seas"],
        "note": (
            "Mundo lento: nadar em 3D atrapalha o combate físico e o troféu não "
            "vale o relógio. Na cronometrada, se for cortar um dos três "
            "\"escolha dois\", corte este. Sem nenhum dálmata; a única trinity "
            "(Branca) fica para a varredura."
        ),
        "puppies": [],
        "trinities": [],
        "postcards": [],
        "pages": ["Página 3"],
        "steps": [
            {
                "title": "Magia, não Keyblade",
                "do": (
                    "Ataque físico embaixo d'água é sofrido; Fire, Blizzard e "
                    "Thunder resolvem tudo. Os Sea Neons soltam muitos orbes de "
                    "MP, então magia praticamente não acaba. Equipe Treasure "
                    "Magnet se já tiver."
                ),
                "image": _AT + "t1.webp",
                "tag": "build",
            },
            {
                "title": "Torn Page #3 na Ariel's Grotto",
                "do": (
                    "Siga os tridentes das paredes até o Triton's Throne (no jato "
                    "forte, cole na parede da direita). Na Ariel's Grotto (a "
                    "gruta), o baú da página está numa prateleira na metade da "
                    "altura, junto de vasos e um porta-retrato."
                ),
                "image": _TR + "t146.webp",
                "tag": "coletável",
            },
            {
                "title": "O golfinho e o Crystal Trident",
                "do": (
                    "Limpe a Undersea Gorge, segure no golfinho por alguns "
                    "segundos e solte. Em Calm Depths, use FIRE no ouriço roxo da "
                    "parede para abrir o buraco. No Undersea Valley, segure no "
                    "golfinho de novo: ele te leva à caverna alta. Dentro do "
                    "Sunken Ship, o baú perto da janela tem o Crystal Trident — e "
                    "o tubarão quebra o vidro."
                ),
                "image": _AT + "t15.webp",
                "tag": "passo",
            },
            {
                "title": "Ursula: magia no caldeirão",
                "do": (
                    "Leve ETHERS. A Ursula não pode ser atacada direto (ela "
                    "contra-ataca girando): trave no CALDEIRÃO e lance de 6 a 8 "
                    "Firas. Só funciona depois que ela joga a primeira poção, e "
                    "não funciona enquanto um ataque dela está saindo do "
                    "caldeirão. Quando o caldeirão explodir em luz, ela fica tonta "
                    "— aí é Keyblade. Vermelho = transborda (suba); azul = "
                    "redemoinhos (desça até o fundo). Prêmio: Mermaid Kick."
                ),
                "image": _AT + "t28.webp",
                "tag": "chefe",
            },
            {
                "title": "Ursula Gigante",
                "do": (
                    "Equipe Mermaid Kick e suba o jato de Calm Depths apertando o "
                    "botão sem parar até a caverna \"???\". Lance AERO (corta "
                    "metade do dano) e, se tiver, acessórios de resistência a "
                    "trovão (Thundara Ring). Bata DUAS vezes na cara dela e mude "
                    "de posição — os raios teleguiados caem onde você está. STOP "
                    "funciona nela. Prêmio: Ansem's Report 3 e o troféu Master of "
                    "the Seas."
                ),
                "image": _AT + "t29.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Halloween Town",
        "name": "Halloween Town — a cidade do Jack Skellington",
        "kind": "história",
        "level": "Battle LV 17",
        "run": "100% · opcional na cronometrada",
        "trophies": ["Pumpkin Prince"],
        "note": (
            "Nesta ida: duas caixas de dálmatas, a trinity Vermelha da mansão e "
            "a Torn Page #4. As caixas 67-69 (trinity Branca) e 70-72 (Glide) "
            "ficam para a varredura."
        ),
        "puppies": ["64 · 65 · 66", "40 · 41 · 42"],
        "trinities": ["Vermelha 5"],
        "postcards": [],
        "pages": ["Página 4"],
        "steps": [
            {
                "title": "Torn Page #4 no Lab",
                "do": (
                    "Assim que chegar ao Lab do Dr. Finkelstein, examine a "
                    "ESTANTE em frente ao Doutor: é a quarta página do 100 Acre "
                    "Wood."
                ),
                "image": _TR + "t164.webp",
                "tag": "coletável",
            },
            {
                "title": "Graveyard: Sally, depois o Prefeito — e os dálmatas 64-66",
                "do": (
                    "Vá ao Graveyard (cemitério) e limpe os Heartless para a Sally "
                    "te dar o Forget-Me-Not. A caixa dos dálmatas 64-66 está no "
                    "canto do fundo, perto da lápide escrita \"RIP\". Volte ao "
                    "Lab, fale com o Doutor e retorne: examine o caixão do fundo, "
                    "fale com o Prefeito e examine as lápides NA ORDEM em que os "
                    "fantasmas aparecem. Acertando, a abóbora grande explode e "
                    "libera o baú do Jack-In-The-Box."
                ),
                "image": _HT + "t9.webp",
                "tag": "puzzle",
            },
            {
                "title": "Moonlight Hill → Oogie's Manor",
                "do": (
                    "Na área do Prefeito, examine o túmulo à direita da abóbora "
                    "explodida para ir a Moonlight Hill; examine a lápide torta na "
                    "base da colina para estendê-la. Na porta da mansão, use FIRE "
                    "na plataforma de metal do centro do chão para ativá-la e suba "
                    "até o Evil Playroom, no topo."
                ),
                "image": _HT + "t16.webp",
                "tag": "passo",
            },
            {
                "title": "Lock, Shock e Barrel — na ordem",
                "do": (
                    "Derrote NESTA ordem para o XP máximo: Lock (vermelho, pula "
                    "alto — combos aéreos), Shock (chapéu de bruxa — Fire/Blizzard "
                    "ou combos completos) e Barrel (máscara branca — role para "
                    "fora do caminho e emende). Fora da ordem, cada um vale 10% "
                    "menos. Lance AERO antes."
                ),
                "image": _HT + "t19.webp",
                "tag": "chefe",
            },
            {
                "title": "Puxe a alavanca, pegue os dálmatas 40-42 e faça a trinity Vermelha ANTES do Oogie",
                "do": (
                    "Depois de puxar a alavanca do Evil Playroom, a alcova na "
                    "metade da subida da mansão libera a caixa dos dálmatas 40-42. "
                    "Depois faça a trinity VERMELHA da entrada da mansão (no arco "
                    "ao nível do chão, perto do riacho que leva à Bridge) antes de "
                    "descer para o Oogie. Na versão PS2 americana ela sumia depois "
                    "do chefe; no Final Mix o relato é de que continua acessível, "
                    "mas fazer antes elimina o risco."
                ),
                "image": _TN + "t22.webp",
                "tag": "missable",
            },
            {
                "title": "Oogie Boogie e a leitura dos dados",
                "do": (
                    "Pule no botão que estiver EM FRENTE ao Oogie para erguer a "
                    "plataforma e alcançá-lo. Os dados vermelhos definem o próximo "
                    "ataque: 1 serra circular, 2 Gargoyles, 3 Wight Knights, 4 "
                    "foices giratórias, 5 Search Ghosts, 6 ele se cura na máquina "
                    "(pule e mande Fire). Se você acertar/defletir cada dado antes "
                    "de parar, pula a rolagem inteira. Prêmios: Holy Circlet e "
                    "Ansem's Report 7."
                ),
                "image": _HT + "t20.webp",
                "tag": "chefe",
            },
            {
                "title": "Oogie's Manor: as 7 bolhas escuras",
                "do": (
                    "Segunda fase: destrua as 7 manchas escuras espalhadas pelo "
                    "exterior da mansão (combos ou Fire repetido). Bater nelas "
                    "devolve MP, então não economize magia. Lance AERO e ignore os "
                    "Heartless comuns. Prêmio: Gravira; ao selar (troféu Pumpkin "
                    "Prince), o Jack te dá o chaveiro Pumpkinhead."
                ),
                "image": _HT + "t23.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Neverland",
        "name": "Neverland — o navio do Capitão Gancho (a Neverland)",
        "kind": "história",
        "level": "Battle LV 19",
        "run": "As duas runs",
        "trophies": ["Pixie Dust"],
        "note": (
            "Mundo obrigatório. Você sai daqui com o GLIDE — a última ferramenta "
            "de movimento — e com o relógio de Londres, que dá 12 prêmios ao "
            "longo do 100%. Nesta ida só uma caixa de dálmatas; as outras três "
            "do navio pedem Glide, trinity Amarela e Branca — varredura."
        ),
        "puppies": ["88 · 89 · 90"],
        "trinities": ["Verde 8"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Farme itens no Anti-Sora dos corredores",
                "do": (
                    "Em cada área do porão aparece um Sora-sombra que voa e chuta. "
                    "Toda vez que você zera o HP dele, ele derruba uma Mega-Potion "
                    "e às vezes um Elixir. No 100% é o melhor estoque grátis do "
                    "jogo para as copas."
                ),
                "image": _NL + "t4.webp",
                "tag": "farm",
            },
            {
                "title": "Trinity Verde da Cabin (Donald e Goofy na party)",
                "do": (
                    "A trinity Verde do centro da Cabin derruba a escada. Trinity "
                    "exige Donald E Goofy — se o Peter Pan estiver na equipe, "
                    "troque no save point antes."
                ),
                "image": _TN + "t31.webp",
                "tag": "passo",
            },
            {
                "title": "Anti-Sora (chefe)",
                "do": (
                    "AERO obrigatório: ele bate muito. Os golpes dele são o combo "
                    "básico do Sora — Dodge Roll ou Guard resolvem. Quando ele "
                    "afundar no chão e criar cópias, use SCAN e troque o alvo até "
                    "achar o de HP alto; Thunder limpa as cópias. Prêmio: Raven's "
                    "Claw."
                ),
                "image": _NL + "t9.webp",
                "tag": "chefe",
            },
            {
                "title": "Captain's Cabin: dálmatas 88-90, depois o Capitão Gancho no Deck",
                "do": (
                    "No Captain's Cabin, a caixa dos dálmatas 88-90 fica ao lado "
                    "da cama, perto da janela lateral. No Deck, lute NO CHÃO "
                    "(esquiva e Guard funcionam melhor). Guard na estocada e "
                    "emende combo de chão. O Battleship que o ajuda solta mísseis "
                    "verdes que CURAM o Gancho: destrua os canhões dos dois lados, "
                    "mas não mate o navio — senão ele invoca outro. Quando ele "
                    "acena o gancho brilhando, não ataque: é contra-ataque "
                    "garantido. Prêmios: Ars Arcanum e Ansem's Report 9."
                ),
                "image": _NL + "t16.webp",
                "tag": "chefe",
            },
            {
                "title": "Clock Tower: o keyhole, o Glide e a Tinker Bell",
                "do": (
                    "Trave no ponteiro dos minutos que ainda não chegou ao XII e "
                    "bata até dar meia-noite. Selar dá Pixie Dust, o chaveiro "
                    "Fairyharp, a habilidade compartilhada GLIDE e a invocação "
                    "TINKER BELL (regen constante + um auto-life — a peça de build "
                    "mais forte do jogo)."
                ),
                "image": _NL + "t17.webp",
                "tag": "troféu",
            },
            {
                "title": "100%: os 12 prêmios da Clock Tower",
                "do": (
                    "O mostrador marca o seu tempo de jogo (26:30 = 2:30). Examine "
                    "a porta com a luz acesa para receber o item daquela hora: 1h "
                    "Orichalcum, 2h Power Up, 3h Mythril Shard, 4h Power Up, 5h AP "
                    "Up, 6h Mythril, 7h AP Up, 8h Defense Up, 9h Orichalcum, 10h "
                    "Defense Up, 11h Mythril Shard, 12h Megalixir. Perdeu uma? Só "
                    "volta 11 horas depois. Depois do Hollow Bastion, a torre só "
                    "reabre quando você vencer o Phantom."
                ),
                "image": _NL + "t20.webp",
                "tag": "100%",
            },
        ],
    },
]

VISITS += [
    {
        "world": "Olympus Coliseum",
        "name": "Olympus Coliseum — Hercules Cup e o keyhole (Junior Hero)",
        "kind": "opcional",
        "level": "Battle LV 20+",
        "run": "Só na run do 100%",
        "trophies": ["Hero of the Coliseum", "Junior Hero"],
        "note": (
            "Abre com Halloween Town e Neverland selados. É AQUI que o keyhole "
            "do Coliseu é selado: a Hercules Cup ensina o Trinity Push (a cor "
            "AMARELA), e a trinity Amarela do Lobby é o keyhole. Na "
            "cronometrada o Coliseu conta como selado pela história — não "
            "precisa vir."
        ),
        "puppies": [],
        "trinities": ["Amarela 2"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Hercules Cup (troféu Hero of the Coliseum)",
                "do": (
                    "Chave 5 é um Rare Truffle: um toque encerra a luta, mas você "
                    "pode ficar rebatendo para XP (e Mystery Goo). Chave 4 é o "
                    "Cloud e a final é o Hércules — quando ele estiver com a aura "
                    "dourada é invulnerável; pegue um barril e jogue nele. "
                    "Prêmios: Herc's Shield, OLYMPIA e a party aprende Trinity "
                    "Push; solo = Critical Plus; contrarrelógio = Gravity Break."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Trinity Amarela do Lobby = keyhole selado (troféu Junior Hero)",
                "do": (
                    "Volte ao Lobby e ative a trinity AMARELA em frente ao "
                    "pedestal grande: o pedestal sai do lugar, o keyhole aparece e "
                    "você sela. Sem isto, o Storyteller (Chronicles do Diário) não "
                    "fecha."
                ),
                "image": _TN + "t34.webp",
                "tag": "troféu",
            },
        ],
    },
    {
        "world": "Traverse Town",
        "name": "Traverse Town — 5ª visita: Navi-G, as páginas 3 e 4 e a volta com Glide",
        "kind": "opcional",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": (
            "Pulável na cronometrada (o Navi-G da história é instalado de "
            "qualquer forma quando você precisa). No 100%: com Glide e a cor "
            "Amarela, a Mystical House do Merlin entrega os dálmatas 1-3 e uma "
            "trinity."
        ),
        "puppies": ["1 · 2 · 3"],
        "trinities": ["Amarela 1"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Instale o Navi-G e ganhe o Transform-G",
                "do": (
                    "Fale com o Cid atrás da Accessory Shop. O Transform-G permite "
                    "trocar de nave em pleno voo — é exatamente o truque "
                    "recomendado para a Missão Gummi 3 de Hollow Bastion (troféu "
                    "Ace Pilot)."
                ),
                "image": _TT + "t65.webp",
                "tag": "gummi",
            },
            {
                "title": "Mystical House com Glide: dálmatas 1-3 e a trinity Amarela",
                "do": (
                    "Atrás da casa do Merlin (a Mystical House), plane até a "
                    "pedra junto à parede: caixa dos dálmatas 1-3. A trinity "
                    "Amarela fica perto da pilha de caixotes grandes, também atrás "
                    "da casa."
                ),
                "image": _TR + "t26.webp",
                "tag": "100%",
            },
            {
                "title": "Devolva a Torn Page #3 → Pooh's Swing",
                "do": (
                    "No livro, examine a árvore na colina perto do fundo da página "
                    "da direita. Resgate o Bisonho (Eeyore) no rio, trave no Pooh "
                    "e leve-o até o balanço. Aperte quando a coruja abrir as asas "
                    "ao MÁXIMO: manda o Pooh uns 20 metros. Truque infalível: "
                    "deixe o Pooh comer o mel dos três potes antes — aí ele acerta "
                    "sempre. Mais de 40 metros conta para o Cheer. Prêmio: Stopra. "
                    "Depois, lance Fire na fogueira em frente à casa do Pooh: "
                    "Mythril."
                ),
                "image": _HA + "t33.webp",
                "tag": "minijogo",
            },
            {
                "title": "Devolva a Torn Page #4 → Tigger's Giant Pot e as nozes da coruja",
                "do": (
                    "Examine a clareira lamacenta com tocos no meio da página da "
                    "direita. Siga os três padrões de pulo do Tigger sem cair, "
                    "depois fale com o Roo. Trave nas nozes e rebata; pular antes "
                    "de bater aumenta a pontuação. Menos de 30 segundos conta para "
                    "o Cheer. Nesta página estão as 5 Rare Nuts da coruja: Power "
                    "Up, Defense Up, Mythril Shard, AP Up e ORICHALCUM — use os "
                    "tocos e a gangorra do Tigger e do Roo para alcançá-las."
                ),
                "image": _HA + "t33.webp",
                "tag": "minijogo",
            },
            {
                "title": "Estoque e armas antes do Hollow Bastion",
                "do": (
                    "Compre as armas novas de Donald e Goofy na Item Shop e encha "
                    "os slots de item. O próximo mundo é o mais longo do jogo e "
                    "tem um ponto de não retorno no meio."
                ),
                "image": _TT + "t67.webp",
                "tag": "passo",
            },
        ],
    },
    {
        "world": "Hollow Bastion",
        "name": "Hollow Bastion — 1ª visita: o castelo da Maleficent",
        "kind": "história",
        "level": "Battle LV 28",
        "run": "As duas runs",
        "trophies": [],
        "note": (
            "PONTO DE VIRADA DO JOGO. Vencer o Ansem-Riku (o chefe depois da "
            "Maleficent Dragão) sobe permanentemente o status dos inimigos em "
            "todos os mundos e muda os encontros. No 100%, faça ANTES tudo que "
            "você quiser farmar barato. Nesta ida: duas caixas de dálmatas e "
            "quatro trinities."
        ),
        "puppies": ["91 · 92 · 93", "94 · 95 · 96"],
        "trinities": ["Azul 16", "Azul 17", "Vermelha 6", "Verde 9"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Rising Falls: os dálmatas 91-93 e a subida",
                "do": (
                    "Use High Jump e Glide nos blocos de gelo. A um quarto da "
                    "subida, numa plataforma flutuante, está a caixa dos dálmatas "
                    "91-93. Na metade, Donald e Goofy saem e o FERA entra — sua "
                    "espada de madeira quase não machuca, mas sua MAGIA continua "
                    "igual: use magia e deixe o Fera bater. Examine o pedestal do "
                    "topo."
                ),
                "image": _HB + "t1.webp",
                "tag": "passo",
            },
            {
                "title": "Castle Gates: dálmatas 94-96 com Gravity + Glide",
                "do": (
                    "Nos Castle Gates, plane até o canto do fundo e lance GRAVITY "
                    "na pequena plataforma flutuante acima: ela desce com a caixa "
                    "dos dálmatas 94-96. Depois examine o nó da borda à direita "
                    "para descer e entre na bolha do canto para o Waterway."
                ),
                "image": _TR + "t219.webp",
                "tag": "100%",
            },
            {
                "title": "Waterway e Dungeon: abra o portão (e a trinity Azul)",
                "do": (
                    "Salve no Waterway. Use o comando Call nas paredes "
                    "quebráveis, suba de bolha em bolha ativando os interruptores "
                    "de cada área e, na última sala, examine o interruptor e o "
                    "mecanismo grande que abre a porta do castelo. Na Dungeon "
                    "(masmorra), a trinity Azul fica perto do centro, à esquerda "
                    "da plataforma que leva ao Lift Stop."
                ),
                "image": _HB + "t7.webp",
                "tag": "passo",
            },
            {
                "title": "Riku (Entrance Hall) — libera a trinity Branca",
                "do": (
                    "Guard nos golpes rápidos e combo depois; AERO corta metade do "
                    "dano. Ele costuma abrir depois do golpe de cima e no fim do "
                    "pulo alto. Vencer libera as trinities BRANCAS — a última cor, "
                    "que abre 10 pontos espalhados pelo jogo (é o que justifica a "
                    "varredura de todos os mundos depois daqui)."
                ),
                "image": _HB + "t14.webp",
                "tag": "chefe",
            },
            {
                "title": "Library: a ordem dos livros (com a trinity Verde no meio)",
                "do": (
                    "Khama Vol.8 (chão do canto) → estante oposta. Mava Vol.6 "
                    "(última prateleira do 2º andar). Trinity VERDE do 2º andar → "
                    "Azal Vol.3. Theon Vol.6 (mesa do 2º andar). Azal Vol.3 → "
                    "estante do meio do 1º andar. Salegg Vol.6 (estante de volumes "
                    "verdes, 1º andar). Mava Vol.6 → espaço vazio à direita dessa "
                    "mesma estante. Salegg Vol.6 → estante diretamente oposta. "
                    "Nahara Vol.5 (estante do meio do 1º andar) → 3ª prateleira da "
                    "parede do 2º andar. Mava Vol.3 (prateleira que abriu) → "
                    "espaço vazio da estante do canto do 1º andar. Hafet Vol.4 "
                    "(escrivaninha) → prateleira recuada do 2º andar. Theon Vol.6 → "
                    "última prateleira da parede do 2º andar. Aperte o botão da "
                    "parede."
                ),
                "image": _HB + "t15.webp",
                "tag": "puzzle",
            },
            {
                "title": "Entrance Hall: as 4 peças do emblema (uma é a trinity Vermelha)",
                "do": (
                    "1) Quebre os potes ao lado da estátua perto das portas da "
                    "Library — a peça cai na fonte abaixo. 2) Acenda as velas das "
                    "paredes com Fire: a chama central apaga e revela a peça. 3) "
                    "Trinity VERMELHA na estátua com chifres da sacada do 2º andar "
                    "— ela cai e quebra. 4) Empurre a estátua da parede oposta à "
                    "Library: aparece um baú numa plataforma abaixo. Falta MP? "
                    "Bata nas gárgulas entre as velas."
                ),
                "image": _HB + "t23.webp",
                "tag": "puzzle",
            },
            {
                "title": "Great Crest: a trinity Azul do Megalixir",
                "do": (
                    "Na subida até a Castle Chapel você atravessa o Great Crest "
                    "numa plataforma flutuante. Do outro lado, no centro da área "
                    "grande, está a trinity Azul — Megalixir e dois Cottages."
                ),
                "image": _TN + "t17.webp",
                "tag": "100%",
            },
            {
                "title": "Maleficent e Maleficent Dragão (Castle Chapel)",
                "do": (
                    "Contra a Maleficent, GRAVITY derruba a plataforma flutuante "
                    "dela na hora — depois é combo livre. Contra o Dragão: invoque "
                    "a TINKER BELL logo no começo (regen + auto-life), lance AERO e "
                    "bata combos aéreos na cabeça. O giro de 360° se evita "
                    "correndo para a borda; do sopro de fogo, fuja de Glide. "
                    "Prêmios: Ansem's Report 5 e o Fireglow (invocação Mushu)."
                ),
                "image": _HB + "t41.webp",
                "tag": "chefe",
            },
            {
                "title": "PARE AQUI se ainda tem farm a fazer",
                "do": (
                    "O próximo chefe é o Ansem-Riku e é ele que endurece o jogo "
                    "inteiro para sempre. No 100%, este é o momento de farmar "
                    "materiais baratos e subir nível com calma. Depois dele, tudo "
                    "custa mais caro."
                ),
                "image": _HB + "t42.webp",
                "tag": "missable",
            },
            {
                "title": "Ansem-Riku (solo, Grand Hall) e a volta como Heartless",
                "do": (
                    "Luta SOLO: sem invocação. AERO, Guard no golpe de cima e "
                    "combo de chão; ele revida depois de 4 acertos. Quando sobrar "
                    "uma barra e ele subir brilhando, PULE e faça Glide em círculo "
                    "largo pela arena. Prêmio: Ragnarok. Depois você joga como "
                    "Heartless: desça o castelo (pode pular da lateral) até o "
                    "Entrance Hall e chegue na Kairi. Você é levado a Traverse "
                    "Town."
                ),
                "image": _HB + "t44.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Traverse Town",
        "name": "Traverse Town — 6ª visita: Kairi, o Oathkeeper e a última página",
        "kind": "história",
        "level": "—",
        "run": "As duas runs",
        "trophies": ["Oathkeeper", "Pooh's Friend", "Mini-Game Maniac"],
        "note": (
            "Obrigatória: é a visita que instala o gummi para voltar ao Hollow "
            "Bastion. O troféu Oathkeeper sai aqui. No 100%, se você seguiu o "
            "guia, já tem mais de 50 dálmatas — o Pongo entrega a 5ª página e "
            "você fecha o 100 Acre Wood."
        ),
        "puppies": [],
        "trinities": ["Branca 1"],
        "postcards": [],
        "pages": ["Página 5"],
        "steps": [
            {
                "title": "O gummi do Waterway e o chaveiro da Kairi (troféu Oathkeeper)",
                "do": (
                    "Fale com o Cid atrás da loja, vá ao Alleyway e entre no "
                    "Waterway. Caminhe até o MURAL da parede para receber o "
                    "Navigation Gummi; depois volte até onde a Kairi está e fale "
                    "com ela: chaveiro OATHKEEPER. É um dos melhores chaveiros de "
                    "magia do jogo. Já que está no Waterway: a trinity BRANCA fica "
                    "no piso de pedra em frente ao mural (Orichalcum)."
                ),
                "image": _TT + "t70.webp",
                "tag": "troféu",
            },
            {
                "title": "Mushu e o Lord Fortune",
                "do": (
                    "Suba a escada do Waterway até o Magician's Study e entregue o "
                    "Fireglow à Fada Madrinha: invocação MUSHU. Se você já tiver as "
                    "SEIS invocações, ela dá de bônus o Lord Fortune para o Donald."
                ),
                "image": _TT + "t73.webp",
                "tag": "invocação",
            },
            {
                "title": "Torn Page #5 (mais de 50 dálmatas) → Pooh's Muddy Path",
                "do": (
                    "Na Dalmatians' House (a casa do Pongo e da Perdita, no "
                    "Second District), com mais de 50 filhotes devolvidos, eles "
                    "entregam a QUINTA página. No livro, examine a trilha "
                    "lamacenta no canto inferior esquerdo da página da esquerda e "
                    "encontre todos os amigos perdidos. Ao terminar você sela o "
                    "keyhole do Bosque (troféu Pooh's Friend) e, com os cinco "
                    "minijogos feitos, fecha a seção Mini Games do Diário "
                    "(Mini-Game Maniac)."
                ),
                "image": _HA + "t33.webp",
                "tag": "troféu",
            },
            {
                "title": "Instale o gummi com o Cid",
                "do": (
                    "Volte ao First District e fale com o Cid para instalar. Um "
                    "portal novo aparece perto de Traverse Town: é o caminho de "
                    "volta para o Hollow Bastion. Armas novas na Item Shop."
                ),
                "image": _TT + "t68.webp",
                "tag": "passo",
            },
        ],
    },
    {
        "world": "Hollow Bastion",
        "name": "Hollow Bastion — 2ª visita: Belle, Behemoth e o keyhole final",
        "kind": "história",
        "level": "Battle LV 33",
        "run": "As duas runs",
        "trophies": ["End of the World"],
        "note": (
            "Depois de selar aqui, os Heartless somem do Hollow Bastion — é a "
            "melhor hora para as duas caixas de dálmatas e a trinity Branca das "
            "Rising Falls. E abrem os superchefes."
        ),
        "puppies": ["61 · 62 · 63", "97 · 98 · 99"],
        "trinities": ["Branca 10"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Belle e o chaveiro Divine Rose",
                "do": (
                    "Suba as Rising Falls (a trinity BRANCA fica na poça rasa da "
                    "metade da subida: Thundaga-G), entre no Entrance Hall e vá à "
                    "Library; suba a escada até a Belle. Depois do reencontro dela "
                    "com o Fera, fale com ela: chaveiro DIVINE ROSE."
                ),
                "image": _HB + "t53.webp",
                "tag": "coletável",
            },
            {
                "title": "Lift Stop: dálmatas 97-99 (Gravity)",
                "do": (
                    "Pela passagem da Library até o Lift Stop, lance GRAVITY na "
                    "pequena plataforma flutuante acima: caixa dos dálmatas 97-99."
                ),
                "image": _TR + "t213.webp",
                "tag": "100%",
            },
            {
                "title": "Grand Hall: Oblivion e os dálmatas 61-63",
                "do": (
                    "Ao chegar ao portal em forma de coração, escale a borda da "
                    "área até a saliência alta: o baú tem o chaveiro OBLIVION. Na "
                    "saliência à esquerda do portal está a caixa dos dálmatas "
                    "61-63."
                ),
                "image": _HB + "t55.webp",
                "tag": "baú",
            },
            {
                "title": "Behemoth (Dark Depths)",
                "do": (
                    "Corra para o lado assim que a luta começar. Só o CHIFRE leva "
                    "dano: GRAVITY tira um naco enorme do HP. Suba nas costas dele "
                    "usando as patas traseiras, trave no chifre e bata. Quando "
                    "formar a esfera laranja acima da cabeça, desça e fique "
                    "embaixo da barriga. Prêmios: Omega Arts e a magia Firaga."
                ),
                "image": _HB + "t56.webp",
                "tag": "chefe",
            },
            {
                "title": "Sele o keyhole e fale 3× com a Aerith",
                "do": (
                    "Selar dá o troféu End of the World e a magia Curaga vem da "
                    "Aerith. Volte à Library e fale com ela TRÊS vezes: ela "
                    "entrega os Ansem's Reports 2, 4, 6 e 10 de uma vez. Quatro dos "
                    "treze relatórios estão aqui — dá para passar batido."
                ),
                "image": _HB + "t57.webp",
                "tag": "missable",
            },
            {
                "title": "Cronometrada: daqui vá direto ao Fim do Mundo",
                "do": (
                    "Na cronometrada, acabou a coleta que não existe: siga para o "
                    "End of the World (o último card). No 100%, começa agora a "
                    "varredura dos mundos com Glide, Gravity e a trinity Branca — "
                    "os próximos cards, um por mundo."
                ),
                "image": _HB + "t60.webp",
                "tag": "atalho",
            },
        ],
    },
]

VISITS += [
    {
        "world": "Wonderland",
        "name": "Varredura — Wonderland: as caixas de Glide e Thunder e as trinities Verde e Branca",
        "kind": "varredura",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": "Volte com Glide, Thunder e a trinity Branca. Duas caixas de dálmatas, três trinities e o chaveiro Lady Luck.",
        "puppies": ["19 · 20 · 21", "58 · 59 · 60"],
        "trinities": ["Verde 2", "Verde 3", "Branca 2"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Rabbit Hole e Bizarre Room: as duas trinities Verdes",
                "do": (
                    "Na Rabbit Hole (a entrada), a trinity Verde fica junto à "
                    "parede, perto do save point (Elixir). No Bizarre Room, a "
                    "outra está no chão, DENTRO do forno (Mythril Shard)."
                ),
                "image": _TN + "t25.webp",
                "tag": "100%",
            },
            {
                "title": "Tea Party Garden com Glide: dálmatas 19-21",
                "do": (
                    "Pela passagem da Lotus Forest, plane até a sebe junto à "
                    "parede em frente ao chalé. Aproveite e sente nas cadeiras do "
                    "jardim: prêmios e entradas do Diário."
                ),
                "image": _TR + "t46.webp",
                "tag": "100%",
            },
            {
                "title": "A alcova do quadro: Thunder nas flores rosas (58-60) e a trinity Branca (Lady Luck)",
                "do": (
                    "Entre no Bizarre Room DE LADO (pela passagem da Lotus Forest "
                    "que te deixa na parede) e passe pelo QUADRO: é uma alcova "
                    "escondida da Lotus Forest. Lance THUNDER nas flores ROSAS "
                    "para soltar os dálmatas 58-60. No centro da alcova está a "
                    "trinity BRANCA — o chaveiro LADY LUCK, um dos melhores de "
                    "magia. As flores amarelas dali trocam Elixir por Mythril "
                    "Shard."
                ),
                "image": _TR + "t42.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Deep Jungle",
        "name": "Varredura — Deep Jungle: duas trinities e o Pink Agaricus",
        "kind": "varredura",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": "Duas trinities (Verde e Branca) e o farm do Serenity Power, material da Ultima.",
        "puppies": [],
        "trinities": ["Verde 5", "Branca 4"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Treetops (Verde) e Cavern of Hearts (Branca)",
                "do": (
                    "Nas Treetops (as copas), a trinity Verde fica no centro da "
                    "área e é MUITO difícil de ver pela cor — ande pelo meio até o "
                    "comando aparecer. Na Cavern of Hearts (a caverna do keyhole), "
                    "a Branca está no centro: Orichalcum."
                ),
                "image": _TN + "t28.webp",
                "tag": "100%",
            },
            {
                "title": "Pink Agaricus na Tree House (Serenity Power x3)",
                "do": (
                    "Entre na Tree House até chegar uma vez em que NENHUM "
                    "Heartless nasce: é o sinal. Invoque o Bambi (MP) e lance STOP "
                    "em três White Mushrooms escondidos pela área (rede sob a "
                    "casa, varanda de trás, barco suspenso, telhado — use as "
                    "escadas e o Glide). Aí o Pink Agaricus aparece: bata o máximo "
                    "de golpes possível enquanto ele está parado. Lucky Strike em "
                    "todo mundo. Precisa de 3 Serenity Power para a Ultima; com "
                    "sorte cai também o Prime Cap."
                ),
                "image": _DJ + "t19.webp",
                "tag": "farm",
            },
        ],
    },
    {
        "world": "Agrabah",
        "name": "Varredura — Agrabah: as três caixas de High Jump, três trinities e o Kurt Zisa",
        "kind": "varredura",
        "level": "nível 75+ para o Kurt Zisa",
        "run": "Só na run do 100%",
        "trophies": ["The Sandy Blade"],
        "note": "O mundo que mais rende na varredura: 9 dálmatas, três trinities e um troféu de superchefe.",
        "puppies": ["52 · 53 · 54", "49 · 50 · 51", "46 · 47 · 48"],
        "trinities": ["Verde 6", "Amarela 3", "Branca 5"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Storage e Palace Gates: trinity Verde e dálmatas 52-54",
                "do": (
                    "No Storage (a salinha do save point ao lado de onde você "
                    "chega), a trinity Verde fica perto das prateleiras (AP Up). "
                    "Nos Palace Gates, use High Jump para a saliência mais alta do "
                    "canto em frente aos portões: dálmatas 52-54."
                ),
                "image": _TR + "t89.webp",
                "tag": "100%",
            },
            {
                "title": "Cave of Wonders, Entrance: dálmatas 49-51 e a trinity Branca",
                "do": (
                    "Logo na entrada da caverna, à esquerda (de frente para o "
                    "Hall), está a trinity BRANCA — Ifrit Belt. Em cima de um "
                    "pilar perto da entrada do Hall, a caixa dos dálmatas 49-51: "
                    "High Jump ou Glide resolvem."
                ),
                "image": _TR + "t92.webp",
                "tag": "100%",
            },
            {
                "title": "Hall (trinity Amarela) e Hidden Room (dálmatas 46-48)",
                "do": (
                    "No Hall, em frente à estátua perto do caminho da pedra "
                    "rolante, a trinity AMARELA abre uma câmara com Thundara-G e "
                    "Meteor-G. Na Hidden Room, ative a estátua para abrir a parede "
                    "ao lado (High Jump): caixa dos dálmatas 46-48."
                ),
                "image": _TR + "t106.webp",
                "tag": "100%",
            },
            {
                "title": "Kurt Zisa (troféu The Sandy Blade)",
                "do": (
                    "Fale com o Tapete Mágico na Aladdin's House e escolha ir ao "
                    "deserto. ALADDIN no lugar do Donald, chaveiro de magia "
                    "(Spellbinder/Oathkeeper/Lady Luck), MP Rage e MP Haste em "
                    "todo mundo, Thundaga e Aerora nos atalhos. Fase 1 ele "
                    "silencia a party: role e bata nos ORBES das mãos. Orbes "
                    "quebrados, ele cai: combo aéreo na cabeça de cobra, cure e "
                    "Aero AGORA. Barreira: Thundaga, com o Bambi repondo MP. "
                    "Build completa na aba Builds & Chefes. Prêmios: Zantetsuken e "
                    "Ansem's Report 11."
                ),
                "image": _AG + "t10.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Monstro",
        "name": "Varredura — Monstro: a trinity Branca do Dark Matter",
        "kind": "varredura",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": "Uma parada rápida: a trinity Branca da Chamber 6 dá um Dark Matter, material da Ultima.",
        "puppies": [],
        "trinities": ["Branca 6"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Chamber 6, centro do chão",
                "do": (
                    "Mouth ► Chamber 1 ► 2 ► 3 ► 2 ► 5 ► 6. A trinity BRANCA está no "
                    "nível do chão, bem no centro da câmara. Um dos 3 Dark Matters "
                    "da Ultima Weapon."
                ),
                "image": _TN + "t42.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Atlantica",
        "name": "Varredura — Atlantica: a trinity Branca e as Thunder Gems",
        "kind": "varredura",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": "A trinity Branca do palácio e o melhor farm de Thunder Gem do jogo (5 para a Ultima).",
        "puppies": [],
        "trinities": ["Branca 7"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Triton's Palace: a concha roxa",
                "do": (
                    "Dentro da grande concha roxa perto do centro do Triton's "
                    "Palace está a trinity BRANCA — Orichalcum."
                ),
                "image": _TN + "t43.webp",
                "tag": "100%",
            },
            {
                "title": "Thunder Gem x5: o loop do Triton's Throne",
                "do": (
                    "Entre pelo Triton's Throne, nade até o Triton's Palace e "
                    "mate todos os Screwdivers e Aquatanks com Firaga; volte ao "
                    "Throne, saia do mundo e entre de novo — repita. Lucky Strike "
                    "em todo mundo. Alternativa: três Thunders no mesmo White "
                    "Mushroom."
                ),
                "image": _AT + "t21.webp",
                "tag": "farm",
            },
        ],
    },
    {
        "world": "Halloween Town",
        "name": "Varredura — Halloween Town: as duas últimas caixas e a trinity Branca",
        "kind": "varredura",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [],
        "note": "Seis dálmatas (uma caixa por Glide, outra pela trinity Branca).",
        "puppies": ["70 · 71 · 72", "67 · 68 · 69"],
        "trinities": ["Branca 8"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Guillotine Square com Glide: dálmatas 70-72",
                "do": (
                    "Na Guillotine Square (a praça da guilhotina), plane até a "
                    "boca da estrutura em forma de abóbora: a caixa dos dálmatas "
                    "70-72 fica lá dentro."
                ),
                "image": _TR + "t162.webp",
                "tag": "100%",
            },
            {
                "title": "Moonlight Hill: a trinity Branca solta os dálmatas 67-69",
                "do": (
                    "Em frente à colina, perto da plantação de abóboras, a trinity "
                    "BRANCA libera a caixa dos dálmatas 67-69. Se quiser Mystery "
                    "Goo: o Black Fungus aparece aqui — jogue abóboras nele para o "
                    "golpe final (conta como crítico)."
                ),
                "image": _TR + "t166.webp",
                "tag": "100%",
            },
        ],
    },
    {
        "world": "Neverland",
        "name": "Varredura — Neverland: o navio inteiro e o Phantom",
        "kind": "varredura",
        "level": "nível 65+ para o Phantom",
        "run": "Só na run do 100%",
        "trophies": ["The Cloaked Shadow"],
        "note": "Nove dálmatas no navio, duas trinities e o Phantom — faça a Hades Cup ANTES dele (você precisa das magias -aga).",
        "puppies": ["82 · 83 · 84", "85 · 86 · 87", "43 · 44 · 45"],
        "trinities": ["Amarela 4", "Branca 9"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Hold: dálmatas 82-84 (Glide) e a trinity Amarela (85-87)",
                "do": (
                    "No Hold (o porão), plane até as vigas superiores do lado de "
                    "estibordo: dálmatas 82-84. Logo à esquerda depois de subir a "
                    "escada, em frente à porta trancada, a trinity AMARELA abre "
                    "uma sala com Orichalcum, Dark Matter, a magia Aero e o baú "
                    "verde sobre os rolos de lona com os dálmatas 85-87."
                ),
                "image": _TR + "t184.webp",
                "tag": "100%",
            },
            {
                "title": "Deck: a trinity Branca em frente ao timão (43-45)",
                "do": (
                    "No convés, em frente ao timão, a trinity BRANCA libera a "
                    "caixa dos dálmatas 43-45. Aproveite o convés para rebater "
                    "Rare Truffles voando: 100 rebatidas = Megalixir + Mystery "
                    "Goo garantido."
                ),
                "image": _TR + "t190.webp",
                "tag": "100%",
            },
            {
                "title": "Phantom (troféu The Cloaked Shadow)",
                "do": (
                    "Fale com a Tinker Bell na Cabin e escolha ir à Clock Tower. "
                    "PETER PAN obrigatório; Goofy com MP Gift e sem habilidades de "
                    "ataque. Ele lança Doom no relógio: trave nos PONTEIROS e "
                    "lance STOP a cada 30-45 s, senão um personagem sai da luta "
                    "para sempre. O dano só entra no coração sob o manto, com a "
                    "magia da cor dele. Guarde sempre 2 de MP para o relógio. "
                    "Build completa na aba Builds & Chefes. Prêmio: Stopra/Stopga "
                    "— e a Clock Tower volta a dar os prêmios por hora."
                ),
                "image": _NL + "t20.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Olympus Coliseum",
        "name": "Olympus Coliseum — Hades Cup, Gold Match e Platinum Match",
        "kind": "varredura",
        "level": "nível 65+ (Ice Titan) · 75+ (Sephiroth)",
        "run": "Só na run do 100%",
        "trophies": ["Coliseum Champion", "The Frost Giant", "One-Winged-Angel"],
        "note": "A Hades Cup abre depois do Hollow Bastion. Traga Elixires e Megalixires (Anti-Sora da Neverland).",
        "puppies": [],
        "trinities": ["Branca 3"],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Trinity Branca dos Gates (Violetta)",
                "do": "No centro dos Gates. Dá o cajado Violetta — conta para o Master Magician.",
                "image": _TN + "t39.webp",
                "tag": "100%",
            },
            {
                "title": "Hades Cup — 50 chaves (troféu Coliseum Champion)",
                "do": (
                    "A maratona do jogo: Hades na chave 10 (Ansem's Report 8), "
                    "Cloud & Leon na 20, Cérbero na 30, Behemoth na 40 e o Rock "
                    "Titan na final. É aqui que saem Firaga, Blizzaga e Thundaga. "
                    "Gravity nos grupos de Defender e Large Body; Thunder nas "
                    "levas de Darkball assim que elas se materializam."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Gold Match — Ice Titan (troféu The Frost Giant)",
                "do": (
                    "Abre depois de vencer as QUATRO copas. A luta inteira é "
                    "DEFLEXÃO: fique travado nele e use GUARD nos gelos — eles "
                    "voltam e machucam o Titã. NÃO lance Aerora/Aeroga: com o buff "
                    "ativo ele manda gelos que não dá para bloquear. Glide quando "
                    "ele der passos. Prêmio: chaveiro Diamond Dust."
                ),
                "image": _OC + "t1.webp",
                "tag": "chefe",
            },
            {
                "title": "Platinum Match — Sephiroth (troféu One-Winged-Angel)",
                "do": (
                    "Abre ao selar o Hollow Bastion. NÃO se aproxime pelo chão: a "
                    "espada tem alcance absurdo. HIGH JUMP por cima do golpe "
                    "horizontal e combo aéreo. Ele revida a cada 4 acertos sem "
                    "finalização. Strike Raid dá dano à distância E te deixa "
                    "invencível durante a animação. Build completa na aba Builds & "
                    "Chefes. Prêmios: One Winged Angel e Ansem's Report 12."
                ),
                "image": _OC + "t1.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Limpeza final",
        "name": "Limpeza final — o que precisa estar fechado antes da porta",
        "kind": "varredura",
        "level": "—",
        "run": "Só na run do 100%",
        "trophies": [
            "Record Keeper", "Top Dog", "Best Friend", "Professor", "Storyteller",
            "Searcher", "Synthesis Master", "Blade Master", "Master Magician",
            "Master Defender", "Level Master", "Top Gun",
        ],
        "note": (
            "A lista do que precisa estar fechado. Se qualquer item aqui estiver "
            "aberto, NÃO abra a porta do Final Rest."
        ),
        "puppies": [],
        "trinities": [],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "99 dálmatas devolvidos (Top Dog) e 46 trinities (Best Friend)",
                "do": (
                    "Se você marcou as caixas ao longo da rota, os contadores do "
                    "topo do guia dizem quanto falta. O Diário do Jiminy mostra "
                    "por mundo quais filhotes faltam e quantas trinities de cada "
                    "cor você ativou. Devolver os 99 dá Aeroga; aos 90 sai o "
                    "RIBBON, o melhor acessório do jogo."
                ),
                "image": _TR + "t26.webp",
                "tag": "troféu",
            },
            {
                "title": "Diário: Heartless raros (Professor)",
                "do": (
                    "O troféu que mais pega gente de surpresa: exige TODOS os "
                    "Heartless, inclusive os raros de área — Sniperwild (Traverse "
                    "Town), Gigas Shadow (Wonderland), Black Ballade (Deep "
                    "Jungle), Pot Scorpion (Agrabah), Grand Ghost (Monstro), "
                    "Chimera (Halloween Town), Jet Balloon (Neverland), Stealth "
                    "Soldier (Hollow Bastion), Neoshadow (End of the World) e os "
                    "quatro cogumelos (White Mushroom, Rare Truffle, Black Fungus, "
                    "Pink Agaricus)."
                ),
                "image": _TT + "t26.webp",
                "tag": "troféu",
            },
            {
                "title": "Sintetizar TODOS os itens (Synthesis Master)",
                "do": (
                    "As receitas do último grupo só aparecem depois de sintetizar "
                    "os 30 itens únicos dos grupos I a V. Materiais da Ultima: "
                    "Thunder Gem x5 (Atlantica), Mystery Goo x5 (Rare Truffle no "
                    "Deck da Neverland), Serenity Power x3 (Pink Agaricus), Stormy "
                    "Stone x3 (Neoshadow, End of the World) e Dark Matter x3 "
                    "(trinities Branca do Monstro e Amarela da Neverland + "
                    "contrarrelógio da Pegasus Cup)."
                ),
                "image": _TT + "t57.webp",
                "tag": "troféu",
            },
            {
                "title": "Todas as Keyblades, cajados e escudos",
                "do": (
                    "Blade Master, Master Magician e Master Defender. As armas de "
                    "Donald e Goofy vêm da Item Shop (que renova a cada visita), "
                    "de trinities Brancas, de baús do End of the World e da "
                    "síntese."
                ),
                "image": _TT + "t58.webp",
                "tag": "troféu",
            },
            {
                "title": "Sora no nível 100 (Level Master)",
                "do": (
                    "Com a curva NOITE, o trecho final voa. Melhores pontos: Hades "
                    "Cup repetida, o Ice Titan com todos os Tech Boost equipados, "
                    "e as ondas de Heartless do End of the World. Equipe o EXP "
                    "Necklace (do Unknown) e todos os Tech Boost."
                ),
                "image": _EW + "t14.webp",
                "tag": "troféu",
            },
            {
                "title": "Gummi: todas as rotas, as 3 missões e 30 plantas",
                "do": (
                    "Top Gun quer todas as rotas voadas ao menos uma vez (costuma "
                    "estourar ao ir de Hollow Bastion para o End of the World). "
                    "Test/Veteran/Ace Pilot querem UMA missão 1, UMA missão 2 e UMA "
                    "missão 3 — qualquer rota. Customizer é só editar e salvar uma "
                    "planta. Gummi Ship Collector quer 30 plantas."
                ),
                "image": _TT + "t76.webp",
                "tag": "troféu",
            },
            {
                "title": "Confirme o Diário 100% (Record Keeper)",
                "do": (
                    "Menu → Journal. Chronicles, Ansem's Report, Characters 1, "
                    "Characters 2, The Heartless, 101 Dalmatians, Trinity List e "
                    "Mini Games precisam estar todos com o selo de completo. O "
                    "Ansem's Report 13 (Unknown) você pega no próximo card, "
                    "antes de fechar."
                ),
                "image": _EW + "t17.webp",
                "tag": "missable",
            },
        ],
    },
    {
        "world": "End of the World",
        "name": "End of the World — o Unknown, o ponto sem volta e o fim",
        "kind": "final",
        "level": "Battle LV 40+",
        "run": "As duas runs",
        "trophies": [
            "He Who Doesn't Exist", "Speedster", "Undefeated", "Unchanging Armor",
            "Proud Player", "Final Mix Master", "Novice Player",
        ],
        "note": (
            "Os Heartless daqui (Invisible, Angel Star, Arch Behemoth, Neoshadow) "
            "são os mais fortes do jogo. AERO o tempo todo e GRAVITY nos "
            "Invisibles. No 100%, entrar aqui é o que libera o Unknown — e "
            "depois você VOLTA ao Hollow Bastion para ele antes de seguir."
        ),
        "puppies": [],
        "trinities": [],
        "postcards": [],
        "pages": [],
        "steps": [
            {
                "title": "Entre, veja a primeira cena — e (100%) volte para o Unknown",
                "do": (
                    "A primeira cena do End of the World é o gatilho do Unknown. "
                    "No 100%: saia pelo save point, volte ao Hollow Bastion e entre "
                    "no portal roxo da Castle Chapel. Nível 80+, Ultima ou Diamond "
                    "Dust, SEM Combo Plus, Gravity/Aero/Cure nos atalhos, Tinker "
                    "Bell no início. A janela é quando ele lança dois orbes e "
                    "começa a teleportar: Gravity travado nele. Na maldição, "
                    "selecione RELEASE (nunca Shock). Build completa na aba Builds "
                    "& Chefes. Prêmios: EXP Necklace, Ansem's Report 13 e o troféu "
                    "He Who Doesn't Exist. Só então retorne aqui."
                ),
                "image": _HB + "t60.webp",
                "tag": "chefe",
            },
            {
                "title": "O caminho invisível e o World Terminus",
                "do": (
                    "Ande pelo caminho invisível: cada plataforma pequena aponta "
                    "para a próxima. No fim, um Arch Behemoth — Gravity derruba o "
                    "HP dele rápido. Depois você cai no World Terminus: desça até a "
                    "plataforma mais baixa, SALVE e entre no círculo de luz."
                ),
                "image": _EW + "t1.webp",
                "tag": "passo",
            },
            {
                "title": "Os terminais dos mundos",
                "do": (
                    "Cada feixe de luz é um mundo, com um baú dentro. Terminal AZUL "
                    "= você não selou o keyhole daquele mundo e é OBRIGADO a limpar "
                    "os Heartless de dentro; ROSA = pode passar direto. Os portais "
                    "azuis brilhantes da borda levam ao próximo terminal, os verdes "
                    "voltam. O terminal verde grande é o do 100 Acre Wood — salve "
                    "ali."
                ),
                "image": _EW + "t7.webp",
                "tag": "passo",
            },
            {
                "title": "A sala secreta e o Chernabog",
                "do": (
                    "O último feixe vermelho/laranja leva a uma sala do Hollow "
                    "Bastion: derrote os Invisibles, examine o console, derrote "
                    "outra leva e pegue o Megalixir do baú do canto. Saia pelo "
                    "portal laranja e pule no buraco. Chernabog é luta voando: "
                    "trave na cabeça, AERO sempre, e quando ele abaixar a cabeça, "
                    "afaste-se do pilar de fogo. Prêmio: SUPERGLIDE — equipe."
                ),
                "image": _EW + "t13.webp",
                "tag": "chefe",
            },
            {
                "title": "A cratera e as ondas dos Linked Worlds (farm de Neoshadow)",
                "do": (
                    "Desça com Superglide passando por todos os portais brancos. "
                    "Nas ondas: AERO (Aerora chega a atordoar), invoque a Tinker "
                    "Bell, Gravity nos Invisibles e combos aéreos rápidos nos Angel "
                    "Stars — se um deles começar a brilhar azul, mate na hora ou "
                    "ele gera outro. É também o lugar dos Neoshadows (Stormy Stone "
                    "da Ultima e entrada do Diário)."
                ),
                "image": _EW + "t16.webp",
                "tag": "farm",
            },
            {
                "title": "Final Rest — a última chance",
                "do": (
                    "Salve. Equipe os melhores itens de cura em Sora, Donald e "
                    "Goofy e use um Cottage. Depois de abrir a porta NÃO existe "
                    "mais menu de mundo, e depois dos créditos não existe mais save "
                    "para continuar. Confira o Diário mais uma vez."
                ),
                "image": _EW + "t17.webp",
                "tag": "missable",
            },
            {
                "title": "Ansem, Ansem solo e World of Chaos",
                "do": (
                    "Ansem 1: role para fugir do Guardião; quando ele gritar "
                    "\"submit!\", role imediatamente — se pegar, use Strike Raid. "
                    "Entre as fases há uma última janela de menu: reequipe e use um "
                    "Cottage. Ansem solo: sem invocação; role dos rasgos escuros e "
                    "use Guard na investida. World of Chaos: fase 1 voando (fique "
                    "junto à ombreira do Guardião para esperar os ataques), fase 2 "
                    "limpa Shadows e bate no núcleo, depois as artilharias e o "
                    "rosto. Vencer aqui fecha a run — e, na cronometrada, o "
                    "relógio precisa marcar menos de 15:00 neste momento."
                ),
                "image": _EW + "t21.webp",
                "tag": "chefe",
            },
        ],
    },
]

# ── 04 — Os cinco chefes opcionais, com build ─────────────────────────────
BOSSES = [
    {
        "name": "Ice Titan (Gold Match)",
        "where": "Olympus Coliseum",
        "unlock": "Vença as quatro copas (Phil, Pegasus, Hercules e Hades).",
        "level": "Nível 65+",
        "build": (
            "GUARD equipado (é a luta inteira), Glide ou Superglide, Leaf Bracer, "
            "todos os Tech Boost (esta luta dá muito XP), acessórios de "
            "resistência a gelo: Shiva Belt e Blizzara Ring."
        ),
        "how": (
            "Fique travado nele o tempo todo. Deflita os gelos com Guard — eles "
            "voltam e machucam o Titã; pule ou role nos que não dá para bloquear. "
            "NUNCA lance Aerora/Aeroga: com o buff ativo ele passa a mandar gelos "
            "indefensáveis. Quando ele der passos, use Glide ou fique nas escadas "
            "da arena para o tremor não pegar. Quando ele cair, 3 ou 4 combos "
            "aéreos. Para curar, PULE antes de lançar Cure."
        ),
        "reward": "Chaveiro Diamond Dust · troféu The Frost Giant",
    },
    {
        "name": "Sephiroth (Platinum Match)",
        "where": "Olympus Coliseum",
        "unlock": "Sele o keyhole do Hollow Bastion (as copas não são obrigatórias, mas ajudam).",
        "level": "Nível 75+",
        "build": (
            "Ultima Weapon ou Diamond Dust (alcance + MP), Dodge Roll, Glide, "
            "Leaf Bracer, Strike Raid, o máximo de MP Rage, NO MÁXIMO um Combo "
            "Plus. Acessórios de defesa e resistência a trevas: Heartguard e "
            "Raven's Claw. Aero e Cure nos atalhos. Muitos Elixires."
        ),
        "how": (
            "Nunca se aproxime pelo chão — a espada alcança de longe. Use HIGH "
            "JUMP para passar por cima do golpe horizontal e emende um combo "
            "aéreo completo. Ele revida depois de 4 acertos sem finalização (ou 4 "
            "acertos extras se o terceiro foi finalização). Depois de uma "
            "finalização ele sempre usa um corte seguido dos pilares de fogo — se "
            "você for pego, bata nele para atordoar ou cure no fim da animação. "
            "Strike Raid dá dano à distância e te deixa invencível durante a "
            "animação: é a saída para as fases em que ele não abre."
        ),
        "reward": "Chaveiro One Winged Angel · Ansem's Report 12 · troféu One-Winged-Angel",
    },
    {
        "name": "Kurt Zisa",
        "where": "Agrabah — fale com o Tapete Mágico na casa do Aladdin",
        "unlock": "Conclua o primeiro episódio do Hollow Bastion.",
        "level": "Nível 75+",
        "build": (
            "ALADDIN no lugar do Donald. Chaveiro de magia (Spellbinder ou "
            "Oathkeeper), todos os MP Rage e MP Haste em todo mundo, acessórios de "
            "defesa (Heartguard, Gaia Bangle). Thundaga e Aerora/ga nos atalhos. "
            "Alguns Elixires e Ethers."
        ),
        "how": (
            "Ele começa SILENCIANDO a party: sem magia e sem invocação. Nessa "
            "fase, role dos cortes e bata combos aéreos nos dois ORBES das mãos "
            "dele. Com os orbes destruídos, ele cai — aí é combo aéreo livre na "
            "cabeça de cobra e a magia volta (cure e lance Aero AGORA). Depois ele "
            "levanta uma barreira e flutua pela borda: Thundaga é o que mais "
            "machuca a barreira, e o Bambi invocado repõe seu MP. Barreira "
            "quebrada, ele cai de novo. Depois das duas primeiras barras ele "
            "ganha o giro aéreo: o horizontal se evita com High Jump + Glide, o "
            "vertical exige rolar na diagonal no último instante."
        ),
        "reward": "Habilidade Zantetsuken · Ansem's Report 11 · troféu The Sandy Blade",
    },
    {
        "name": "Phantom",
        "where": "Neverland — fale com a Tinker Bell na Cabin",
        "unlock": "Conclua o primeiro episódio do Hollow Bastion.",
        "level": "Nível 65+",
        "build": (
            "PETER PAN é obrigatório. Goofy com MP Gift equipado e TODAS as "
            "habilidades de ataque dele desequipadas. Chaveiro de magia "
            "(Spellbinder/Oathkeeper), acessórios de magia (Atlas Armlet, Crystal "
            "Crown, Ray of Light), todos os MP Rage e MP Haste. Stopra e "
            "Aerora/ga nos atalhos. Feche a HADES CUP antes: você precisa de "
            "Firaga, Blizzaga e Thundaga."
        ),
        "how": (
            "Ele lança Doom no relógio: se o relógio bater meia-noite, o "
            "personagem marcado sai da luta de vez. Para segurar, trave nos "
            "PONTEIROS e lance STOP a cada 30-45 segundos (ou a cada ~5 ataques "
            "dele). O dano só entra no CORAÇÃO sob o manto, e só com a magia da "
            "cor certa do coração no momento. Guarde sempre 2 de MP para o "
            "relógio. Quando ele for para a frente da torre e começar a formar "
            "algo na boca, voe para o lado da torre."
        ),
        "reward": "Magia Stopra/Stopga · a torre do relógio reabre · troféu The Cloaked Shadow",
    },
    {
        "name": "Unknown (o Homem Misterioso)",
        "where": "Hollow Bastion — portal roxo na Capela do Castelo",
        "unlock": "Entre no Fim do Mundo e veja a primeira cena; depois volte.",
        "level": "Nível 80+",
        "build": (
            "A luta mais dura do jogo. Ultima Weapon ou Diamond Dust, Dodge Roll, "
            "Glide, Leaf Bracer, Strike Raid, o máximo de MP Rage e MP Haste, "
            "Crystal Crown e Gaia Bangle. NÃO equipe Combo Plus nem Air Combo Plus "
            "— combos longos te deixam preso. Gravity, Aero e Cure nos atalhos. "
            "Elixires e Megalixires."
        ),
        "how": (
            "Invoque a Tinker Bell no começo (regen + auto-life) e lance Aero. A "
            "melhor janela: quando ele lança dois orbes grandes e começa a "
            "teleportar, lance GRAVITY travado nele — se o feitiço terminar no "
            "instante em que ele vira vapor, ele trava e você encaixa vários "
            "golpes. Gravity Break como finalizador faz o mesmo por acaso. Quando "
            "ele erguer a barreira, role ATRAVÉS dela e dê 2-3 golpes (bater na "
            "barreira faz ele atravessar e cortar duas vezes). Na segunda fase "
            "vem a maldição: seu menu embaralha e o HP drena — selecione RELEASE "
            "o mais rápido possível (SHOCK machuca ainda mais); dá para "
            "pausar-buffar para achar o comando. Strike Raid dá dano seguro de "
            "longe."
        ),
        "reward": "Acessório EXP Necklace · Ansem's Report 13 · troféu He Who Doesn't Exist",
    },
]

# ── 03 — Os 99 dálmatas: 33 baús de 3 filhotes ────────────────────────────
PUPPY_REWARDS = [
    {"count": "12", "prize": "Curaga-G"},
    {"count": "21", "prize": "Firaga-G"},
    {"count": "30", "prize": "Thundara-G"},
    {"count": "42", "prize": "Mythril Shard"},
    {"count": "51", "prize": "Torn Page (a 5ª!) e Mythril"},
    {"count": "60", "prize": "Megalixir"},
    {"count": "72", "prize": "Orichalcum"},
    {"count": "81", "prize": "Ultima-G"},
    {"count": "90", "prize": "RIBBON e Sora aprende Tech Boost"},
    {"count": "99", "prize": "Conjunto completo de gummis e a magia Aeroga"},
]

PUPPIES = [
    {"group": "1 · 2 · 3", "world": "Traverse Town", "area": "Mystical House",
     "where": "Numa pedra junto à parede, atrás da casa do Merlin. Precisa de Glide.",
     "image": _TR + "t26.webp"},
    {"group": "4 · 5 · 6", "world": "Traverse Town", "area": "Alleyway",
     "where": "Atrás de uma parede de caixotes; ative a trinity Vermelha do First District (na cerca de madeira do beco atrás da loja dos sobrinhos).",
     "image": _TR + "t23.webp"},
    {"group": "7 · 8 · 9", "world": "Traverse Town", "area": "Item Workshop",
     "where": "Numa mesa, perto de um dos Moogles.",
     "image": _TR + "t11.webp"},
    {"group": "10 · 11 · 12", "world": "Traverse Town", "area": "Waterway",
     "where": "Logo dentro da escadaria que leva ao Estúdio do Merlin.",
     "image": _TR + "t25.webp"},
    {"group": "13 · 14 · 15", "world": "Wonderland", "area": "Queen's Castle",
     "where": "Numa saliência em frente ao save point; chega-se pela Lotus Forest.",
     "image": _TR + "t35.webp"},
    {"group": "16 · 17 · 18", "world": "Wonderland", "area": "Lotus Forest",
     "where": "Numa vitória-régia perto do centro; pule nos cogumelos ao lado para alcançar.",
     "image": _TR + "t38.webp"},
    {"group": "19 · 20 · 21", "world": "Wonderland", "area": "Tea Party Garden",
     "where": "Numa sebe junto à parede em frente ao chalé; passagem da Lotus Forest, precisa de Glide.",
     "image": _TR + "t46.webp"},
    {"group": "22 · 23 · 24", "world": "Olympus Coliseum", "area": "Gates",
     "where": "Trinity AZUL em frente à estátua de gladiador da DIREITA (de frente para as portas do vestíbulo).",
     "image": _TR + "t49.webp"},
    {"group": "25 · 26 · 27", "world": "Deep Jungle", "area": "Hippos' Lagoon",
     "where": "No lado oposto da lagoa; pule nas costas dos hipopótamos.",
     "image": _TR + "t65.webp"},
    {"group": "28 · 29 · 30", "world": "Deep Jungle", "area": "Vines 2",
     "where": "Numa saliência no centro da área; use os cipós da direita ao entrar.",
     "image": _TR + "t66.webp"},
    {"group": "31 · 32 · 33", "world": "Deep Jungle", "area": "Waterfall Cavern",
     "where": "Numa saliência na metade da subida, logo abaixo de uma parede coberta de cipós.",
     "image": _TR + "t71.webp"},
    {"group": "34 · 35 · 36", "world": "Deep Jungle", "area": "Camp",
     "where": "Trinity AZUL perto da mesa de laboratório.",
     "image": _TR + "t60.webp"},
    {"group": "37 · 38 · 39", "world": "Agrabah", "area": "Cave of Wonders: Treasure Room",
     "where": "Numa saliência perto da entrada do Bottomless Hall; pule de cima de uma pilha de tesouro.",
     "image": _TR + "t110.webp"},
    {"group": "40 · 41 · 42", "world": "Halloween Town", "area": "Oogie's Manor",
     "where": "Numa alcova na metade da subida da mansão; é preciso puxar antes a alavanca da Sala de Brinquedos.",
     "image": _TR + "t175.webp"},
    {"group": "43 · 44 · 45", "world": "Neverland", "area": "Ship (Deck)",
     "where": "Trinity BRANCA em frente ao timão.",
     "image": _TR + "t190.webp"},
    {"group": "46 · 47 · 48", "world": "Agrabah", "area": "Cave of Wonders: Hidden Room",
     "where": "Ative a estátua para abrir a parede ao lado; precisa de trinity Amarela ou High Jump.",
     "image": _TR + "t106.webp"},
    {"group": "49 · 50 · 51", "world": "Agrabah", "area": "Cave of Wonders: Entrance",
     "where": "Em cima de um pilar perto da entrada do Hall; High Jump, Glide ou um pulo bem dado de cima de um barril.",
     "image": _TR + "t92.webp"},
    {"group": "52 · 53 · 54", "world": "Agrabah", "area": "Palace Gates",
     "where": "Na saliência mais alta do canto em frente aos portões; exige High Jump.",
     "image": _TR + "t89.webp"},
    {"group": "55 · 56 · 57", "world": "Monstro", "area": "Chamber 3",
     "where": "Numa plataforma esverdeada, logo acima da entrada da Câmara 2.",
     "image": _TR + "t123.webp"},
    {"group": "58 · 59 · 60", "world": "Wonderland", "area": "Lotus Forest",
     "where": "Lance THUNDER nas flores rosas da alcova acessível pelo quadro do Bizarre Room de lado.",
     "image": _TR + "t42.webp"},
    {"group": "61 · 62 · 63", "world": "Hollow Bastion", "area": "Grand Hall",
     "where": "Na saliência à esquerda do portal que leva ao Dark Depths.",
     "image": _TR + "t228.webp"},
    {"group": "64 · 65 · 66", "world": "Halloween Town", "area": "Graveyard",
     "where": "No canto do fundo, perto da lápide escrita \"RIP\".",
     "image": _TR + "t178.webp"},
    {"group": "67 · 68 · 69", "world": "Halloween Town", "area": "Moonlight Hill",
     "where": "Trinity BRANCA em frente à colina, perto da plantação de abóboras.",
     "image": _TR + "t166.webp"},
    {"group": "70 · 71 · 72", "world": "Halloween Town", "area": "Guillotine Square",
     "where": "Dentro da boca de uma estrutura em forma de abóbora; chega-se com Glide.",
     "image": _TR + "t162.webp"},
    {"group": "73 · 74 · 75", "world": "Monstro", "area": "Mouth",
     "where": "Numa plataforma alta junto à parede, em frente ao naufrágio; precisa de High Jump.",
     "image": _TR + "t117.webp"},
    {"group": "76 · 77 · 78", "world": "Monstro", "area": "Chamber 6",
     "where": "No nível do chão, em frente à passagem para a Câmara 5.",
     "image": _TR + "t128.webp"},
    {"group": "79 · 80 · 81", "world": "Monstro", "area": "Chamber 5",
     "where": "Numa saliência alta, em cima de um barril, em frente à passagem para a Câmara 4.",
     "image": _TR + "t127.webp"},
    {"group": "82 · 83 · 84", "world": "Neverland", "area": "Hold",
     "where": "Nas vigas superiores do lado de estibordo; precisa de Glide.",
     "image": _TR + "t181.webp"},
    {"group": "85 · 86 · 87", "world": "Neverland", "area": "Hold",
     "where": "Trinity AMARELA do porão; o baú verde fica sobre os rolos de lona.",
     "image": _TR + "t184.webp"},
    {"group": "88 · 89 · 90", "world": "Neverland", "area": "Captain's Cabin",
     "where": "Ao lado da cama, perto da janela lateral.",
     "image": _TR + "t188.webp"},
    {"group": "91 · 92 · 93", "world": "Hollow Bastion", "area": "Rising Falls",
     "where": "Numa plataforma flutuante, mais ou menos a um quarto da subida.",
     "image": _TR + "t193.webp"},
    {"group": "94 · 95 · 96", "world": "Hollow Bastion", "area": "Castle Gates",
     "where": "Lance GRAVITY na pequena plataforma flutuante acima; o canto do fundo se alcança com Glide.",
     "image": _TR + "t219.webp"},
    {"group": "97 · 98 · 99", "world": "Hollow Bastion", "area": "Lift Stop",
     "where": "Lance GRAVITY na pequena plataforma flutuante acima; a área se acessa pela passagem da Biblioteca.",
     "image": _TR + "t213.webp"},
]

# ── 03 — As 46 trinities ──────────────────────────────────────────────────
TRINITIES = [
    {"color": "Azul", "num": 1, "world": "Traverse Town", "where": "First District — no chão perto da saída do mundo, em frente à loja de acessórios.", "reward": "120 munny", "image": _TN + "t1.webp"},
    {"color": "Azul", "num": 2, "world": "Traverse Town", "where": "First District — em frente ao café, perto da loja dos sobrinhos.", "reward": "Teleporta a party para a sacada do café, onde há um baú com um POSTAL.", "image": _TN + "t2.webp"},
    {"color": "Azul", "num": 3, "world": "Traverse Town", "where": "Third District — atrás da fonte da Dama e o Vagabundo, no canto.", "reward": "60 munny, Camping Set", "image": _TN + "t3.webp"},
    {"color": "Azul", "num": 4, "world": "Traverse Town", "where": "Magician's Study — perto do save point.", "reward": "50 munny, Mega-Ether", "image": _TN + "t4.webp"},
    {"color": "Azul", "num": 5, "world": "Wonderland", "where": "Lotus Forest — perto das flores amarelas, na alcova que se alcança pulando nas vitórias-régias.", "reward": "Orbes de MP, Camping Set", "image": _TN + "t5.webp"},
    {"color": "Azul", "num": 6, "world": "Wonderland", "where": "Lotus Forest — perto dos cogumelos amarelos, na alcova em frente à passagem para o Castelo da Rainha.", "reward": "Orbes de MP, Ether, Potion, Tent", "image": _TN + "t6.webp"},
    {"color": "Azul", "num": 7, "world": "Olympus Coliseum", "where": "Gates — em frente à estátua de gladiador da ESQUERDA (de frente para o vestíbulo).", "reward": "Mythril Shard", "image": _TN + "t7.webp"},
    {"color": "Azul", "num": 8, "world": "Olympus Coliseum", "where": "Gates — em frente à estátua da DIREITA.", "reward": "Dálmatas 22-24", "image": _TN + "t8.webp"},
    {"color": "Azul", "num": 9, "world": "Deep Jungle", "where": "Camp — perto do equipamento de laboratório e da passagem para a Lagoa.", "reward": "Dálmatas 34-36", "image": _TN + "t9.webp"},
    {"color": "Azul", "num": 10, "world": "Deep Jungle", "where": "Climbing Trees — numa plataforma elevada, perto da passagem para a Casa da Árvore.", "reward": "Thundara-G", "image": _TN + "t10.webp"},
    {"color": "Azul", "num": 11, "world": "Agrabah", "where": "Bazaar — no nível do chão, no centro da área.", "reward": "200 munny, Mega-Ether", "image": _TN + "t11.webp"},
    {"color": "Azul", "num": 12, "world": "Agrabah", "where": "Cave of Wonders: Silent Chamber — na plataforma central, perto da passagem para o Hall.", "reward": "Thundara-G", "image": _TN + "t12.webp"},
    {"color": "Azul", "num": 13, "world": "Monstro", "where": "Mouth — numa plataforma de madeira na frente da boca; só depois de derrotar o Parasite Cage.", "reward": "50 munny, Potion x2, Cottage", "image": _TN + "t13.webp"},
    {"color": "Azul", "num": 14, "world": "Monstro", "where": "Chamber 5 — no nível do chão, em frente à passagem para a Câmara 6.", "reward": "333 munny, Cottage", "image": _TN + "t14.webp"},
    {"color": "Azul", "num": 15, "world": "Monstro", "where": "Throat — no nível mais baixo, no centro da área.", "reward": "100 munny, Mythril Shard", "image": _TN + "t15.webp"},
    {"color": "Azul", "num": 16, "world": "Hollow Bastion", "where": "Waterway: Dungeon — perto do centro, à esquerda da plataforma que leva ao Lift Stop.", "reward": "Cottage, Mega-Potion, Mega-Ether, orbes de HP", "image": _TN + "t16.webp"},
    {"color": "Azul", "num": 17, "world": "Hollow Bastion", "where": "Great Crest — no centro da área grande, depois de atravessar na plataforma flutuante.", "reward": "Megalixir, Cottage x2, orbes de MP", "image": _TN + "t17.webp"},

    {"color": "Vermelha", "num": 1, "world": "Traverse Town", "where": "First District — numa cerca de madeira no beco atrás da loja dos sobrinhos.", "reward": "Dálmatas 4-6", "image": _TN + "t18.webp"},
    {"color": "Vermelha", "num": 2, "world": "Traverse Town", "where": "Alleyway — na grade de metal que bloqueia o canal, no canto oposto à passagem para a Casa dos Dálmatas.", "reward": "Abre o Waterway (obrigatória na história)", "image": _TN + "t19.webp"},
    {"color": "Vermelha", "num": 3, "world": "Traverse Town", "where": "Second District — nas tábuas de madeira em frente à torre do sino, acima da Gizmo Shop.", "reward": "Abre a torre do sino (obrigatória na história)", "image": _TN + "t20.webp"},
    {"color": "Vermelha", "num": 4, "world": "Agrabah", "where": "Cave of Wonders: Treasure Room — em frente a uma estátua de esfinge, do outro lado do save point.", "reward": "333 munny, Mythril Shard", "image": _TN + "t21.webp"},
    {"color": "Vermelha", "num": 5, "world": "Halloween Town", "where": "Oogie's Manor — no nível do chão, no arco perto do riacho que leva à Ponte.", "reward": "Mythril Shard", "image": _TN + "t22.webp"},
    {"color": "Vermelha", "num": 6, "world": "Hollow Bastion", "where": "Entrance Hall — na sacada do 2º andar, em frente a uma estátua de pedra com chifres, perto da borda interna.", "reward": "Peça do Emblema", "image": _TN + "t23.webp"},

    {"color": "Verde", "num": 1, "world": "Traverse Town", "where": "First District, loja de acessórios — em frente à mesa do centro.", "reward": "Abre a Sala de Síntese", "image": _TN + "t24.webp"},
    {"color": "Verde", "num": 2, "world": "Wonderland", "where": "Bizarre Room — no nível do chão, dentro do forno.", "reward": "Mythril Shard", "image": _TN + "t25.webp"},
    {"color": "Verde", "num": 3, "world": "Wonderland", "where": "Rabbit Hole — junto à parede, perto do save point.", "reward": "Elixir", "image": _TN + "t26.webp"},
    {"color": "Verde", "num": 4, "world": "Olympus Coliseum", "where": "Gates — junto à parede à direita da passagem para o mapa-múndi, entre dois braseiros.", "reward": "Mythril", "image": _TN + "t27.webp"},
    {"color": "Verde", "num": 5, "world": "Deep Jungle", "where": "Treetops — no centro da área (muito difícil de ver por causa da cor).", "reward": "Mythril Shard, orbes de HP", "image": _TN + "t28.webp"},
    {"color": "Verde", "num": 6, "world": "Agrabah", "where": "Storage — perto das prateleiras, em frente ao save point.", "reward": "AP Up", "image": _TN + "t29.webp"},
    {"color": "Verde", "num": 7, "world": "Monstro", "where": "Mouth — em cima do navio do Geppetto.", "reward": "Mythril Shard", "image": _TN + "t30.webp"},
    {"color": "Verde", "num": 8, "world": "Neverland", "where": "Cabin — no centro da sala.", "reward": "Abre o Camarote do Capitão (obrigatória na história)", "image": _TN + "t31.webp"},
    {"color": "Verde", "num": 9, "world": "Hollow Bastion", "where": "Library — 2º andar, em frente à estante perto da mesa e da sacada.", "reward": "Azal Vol. 3 (peça do puzzle dos livros)", "image": _TN + "t32.webp"},

    {"color": "Amarela", "num": 1, "world": "Traverse Town", "where": "Mystical House — perto de uma pilha de caixotes grandes, atrás da casa do Merlin.", "reward": "AP Up", "image": _TN + "t33.webp"},
    {"color": "Amarela", "num": 2, "world": "Olympus Coliseum", "where": "Lobby — em frente ao pedestal grande.", "reward": "Sela o keyhole do Coliseu (obrigatória na história)", "image": _TN + "t34.webp"},
    {"color": "Amarela", "num": 3, "world": "Agrabah", "where": "Cave of Wonders: Hall — em frente a uma estátua de pedra perto do caminho da pedra rolante.", "reward": "Abre uma câmara com Thundara-G e Meteor-G", "image": _TN + "t35.webp"},
    {"color": "Amarela", "num": 4, "world": "Neverland", "where": "Hold — em frente à porta trancada, logo à esquerda depois de subir a escada.", "reward": "Orichalcum, Dark Matter, dálmatas 85-87 e a magia Aero", "image": _TN + "t36.webp"},

    {"color": "Branca", "num": 1, "world": "Traverse Town", "where": "Waterway — no piso de pedra, em frente ao mural.", "reward": "Orichalcum", "image": _TN + "t37.webp"},
    {"color": "Branca", "num": 2, "world": "Wonderland", "where": "Lotus Forest — no centro da alcova acessível pelo quadro do Bizarre Room de lado.", "reward": "Chaveiro LADY LUCK", "image": _TN + "t38.webp"},
    {"color": "Branca", "num": 3, "world": "Olympus Coliseum", "where": "Gates — no centro da área.", "reward": "Cajado Violetta", "image": _TN + "t39.webp"},
    {"color": "Branca", "num": 4, "world": "Deep Jungle", "where": "Cavern of Hearts — no centro da área.", "reward": "Orichalcum", "image": _TN + "t40.webp"},
    {"color": "Branca", "num": 5, "world": "Agrabah", "where": "Cave of Wonders: Entrance — logo em frente à entrada, à sua esquerda (de frente para o Hall).", "reward": "Ifrit Belt", "image": _TN + "t41.webp"},
    {"color": "Branca", "num": 6, "world": "Monstro", "where": "Chamber 6 — no nível do chão, no centro da área.", "reward": "Dark Matter (material da Ultima)", "image": _TN + "t42.webp"},
    {"color": "Branca", "num": 7, "world": "Atlantica", "where": "Triton's Palace — dentro da grande concha roxa perto do centro.", "reward": "Orichalcum", "image": _TN + "t43.webp"},
    {"color": "Branca", "num": 8, "world": "Halloween Town", "where": "Moonlight Hill — em frente à colina, perto da plantação de abóboras.", "reward": "Dálmatas 67-69", "image": _TN + "t44.webp"},
    {"color": "Branca", "num": 9, "world": "Neverland", "where": "Ship (Deck) — em frente ao timão do navio.", "reward": "Dálmatas 43-45", "image": _TN + "t45.webp"},
    {"color": "Branca", "num": 10, "world": "Hollow Bastion", "where": "Rising Falls — na poça rasa mais ou menos na metade da subida.", "reward": "Thundaga-G", "image": _TN + "t46.webp"},
]

# ── 03 — As 5 Torn Pages do Bosque dos Cem Acres ──────────────────────────
PAGES = [
    {"num": "Página 1", "world": "Agrabah", "where": "Cave of Wonders: Dark Chamber — numa plataforma no centro da área; chega-se subindo a cachoeira a partir da Relic Chamber.", "image": _TR + "t103.webp"},
    {"num": "Página 2", "world": "Monstro", "where": "Chamber 6 — numa plataforma alta esverdeada, em frente à entrada da Câmara 5.", "image": _TR + "t129.webp"},
    {"num": "Página 3", "world": "Atlantica", "where": "Ariel's Grotto — num baú sobre uma prateleira, mais ou menos na metade da altura, junto de vasos e um porta-retrato.", "image": _TR + "t146.webp"},
    {"num": "Página 4", "world": "Halloween Town", "where": "Laboratório — examine a estante em frente ao Doutor.", "image": _TR + "t164.webp"},
    {"num": "Página 5", "world": "Traverse Town", "where": "Casa dos Dálmatas — devolva mais de 50 filhotes ao Pongo e à Perdita.", "image": _TR + "t26.webp"},
]

# ── 03 — Os 10 postais (todos na Traverse Town) ──────────────────────
POSTCARDS = [
    {"num": "Postal 1", "where": "Trinity AZUL perto do café do First District; abra o baú da sacada.", "prize": "Cottage", "image": _TR + "t2.webp"},
    {"num": "Postal 2", "where": "Bata no ventilador de teto da loja dos sobrinhos (First District).", "prize": "Mythril Shard", "image": _TR + "t8.webp"},
    {"num": "Postal 3", "where": "Baú no telhado da loja de acessórios (First District).", "prize": "Mega-Potion", "image": _TR + "t4.webp"},
    {"num": "Postal 4", "where": "Baú azul atrás da loja de acessórios (First District).", "prize": "Mega-Ether", "image": _TR + "t3.webp"},
    {"num": "Postal 5", "where": "Baú acima da lona da loja \"Boots & Shoes\" (Second District).", "prize": "Mythril", "image": _TR + "t13.webp"},
    {"num": "Postal 6", "where": "Examine o canto da sacada do Third District; chega-se pelos telhados do lado leste do Second District.", "prize": "Elixir", "image": _TR + "t28.webp"},
    {"num": "Postais 7 e 8", "where": "Lance THUNDER no fio exposto do canto do Third District; depois, na Gizmo Shop, pule nos três botões em cima da máquina e examine o relógio central. Saem dois postais de uma vez.", "prize": "Megalixir e Orichalcum", "image": _TR + "t16.webp"},
    {"num": "Postal 9", "where": "Examine o potinho da prateleira na casa do Geppetto.", "prize": "AP Up", "image": _TR + "t7.webp"},
    {"num": "Postal 10", "where": "Examine o panfleto na Item Workshop (First District).", "prize": "Defense Up", "image": _TR + "t10.webp"},
]

# ── 03 — Os 13 Relatórios do Ansem ────────────────────────────────────────
REPORTS = [
    {"num": "Relatório 1", "how": "Derrote o Jafar Gênio, em Agrabah."},
    {"num": "Relatório 2", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 3", "how": "Derrote a Ursula Gigante, em Atlantica."},
    {"num": "Relatório 4", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 5", "how": "Derrote a Maleficent, no Hollow Bastion."},
    {"num": "Relatório 6", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 7", "how": "Derrote o Oogie Boogie, na Halloween Town."},
    {"num": "Relatório 8", "how": "Derrote o Hades, na Hades Cup do Coliseu."},
    {"num": "Relatório 9", "how": "Derrote o Capitão Gancho, na Neverland."},
    {"num": "Relatório 10", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 11", "how": "Derrote o Kurt Zisa, em Agrabah."},
    {"num": "Relatório 12", "how": "Derrote o Sephiroth, no Coliseu (Platinum Match)."},
    {"num": "Relatório 13", "how": "Derrote o Unknown, no Hollow Bastion."},
]

# ── 03 — Os materiais raros da Ultima Weapon ──────────────────────────────
MATERIALS = [
    {
        "name": "Thunder Gem x5",
        "how": (
            "Drop de Screwdiver e Aquatank em Atlantica. Entre pelo Trono do "
            "Tritão, nade até o Palácio, mate tudo com Firaga, volte ao Trono, "
            "saia do mundo e entre de novo — repita. Também sai lançando três "
            "Thunders num White Mushroom."
        ),
    },
    {
        "name": "Mystery Goo x5",
        "how": (
            "Só cai de White Mushroom, Rare Truffle e Black Fungus. O jeito mais "
            "confiável é o Rare Truffle no Deck da Neverland: voando você "
            "consegue rebatê-lo no ar sem parar. 50 rebatidas = Elixir + 40% de "
            "Goo; 100 = Megalixir + Goo garantido."
        ),
    },
    {
        "name": "Serenity Power x3",
        "how": (
            "Só cai do PINK AGARICUS, na Tree House da Deep Jungle. Ele só "
            "aparece quando você entra na área e NENHUM Heartless nasce. Primeiro "
            "lance STOP em três White Mushrooms escondidos pela área (invoque o "
            "Bambi para repor MP), e só então ele surge. É por isso que o guia "
            "manda encontrar a Sabor de novo na Casa da Árvore antes de avançar a "
            "história: o buraco que ela abre no piso é o que torna isso viável."
        ),
    },
    {
        "name": "Stormy Stone x3",
        "how": "Só cai do NEOSHADOW, no Fim do Mundo (área Linked Worlds — as ondas de Heartless).",
    },
    {
        "name": "Dark Matter x3",
        "how": (
            "Pode ser sintetizado e também está em 9 baús pelo jogo — entre eles a "
            "trinity Branca da Câmara 6 do Monstro e a trinity Amarela do porão da "
            "Neverland. O contrarrelógio da Pegasus Cup também dá um."
        ),
    },
]

# ── 02 — Os 56 troféus ────────────────────────────────────────────────────
TROPHIES = [
    {"id": "plat", "name": "KINGDOM HEARTS Master", "tier": "platina",
     "requirement": "Conquiste todos os outros 55 troféus.",
     "shortcut": "Duas zeradas: a cronometrada e a do 100%.", "image": ""},

    {"id": "t02", "name": "Proud Player", "tier": "ouro",
     "requirement": "Zere o jogo no Proud.",
     "shortcut": "No PS4 empilha: esta zerada entrega também Final Mix Master e Novice Player.", "image": ""},
    {"id": "t03", "name": "Speedster", "tier": "ouro",
     "requirement": "Derrote o World of Chaos com menos de 15 horas de jogo.",
     "shortcut": "É o troféu que obriga a segunda run. Sele só os keyholes obrigatórios, ignore coletáveis e use o Warp-G assim que o Cid entregar.", "image": ""},

    {"id": "t04", "name": "Final Mix Master", "tier": "prata",
     "requirement": "Zere o Final Mix.",
     "shortcut": "Sai junto com qualquer zerada.", "image": ""},
    {"id": "t05", "name": "Unchanging Armor", "tier": "prata",
     "requirement": "Zere sem trocar nenhum equipamento.",
     "shortcut": "Chaveiro, cajado, escudo e acessórios de Sora, Donald e Goofy. O que já vem equipado pode ficar; habilidades e itens podem ser mexidos.", "image": ""},
    {"id": "t06", "name": "Undefeated", "tier": "prata",
     "requirement": "Zere sem usar Continue nenhuma vez.",
     "shortcut": "Morreu? Saia e carregue o save. Salve em todo save point.", "image": ""},
    {"id": "t07", "name": "Level Master", "tier": "prata",
     "requirement": "Leve o Sora ao nível 100.",
     "shortcut": "Curva NOITE no Despertar, EXP Necklace do Unknown, Hades Cup repetida e as ondas do Fim do Mundo.", "image": ""},

    {"id": "t08", "name": "Novice Player", "tier": "bronze",
     "requirement": "Zere o Final Mix no Beginner.",
     "shortcut": "Empilha com o Proud no PS4.", "image": ""},
    {"id": "t09", "name": "He Who Doesn't Exist", "tier": "bronze",
     "requirement": "Derrote o Homem Misterioso no Hollow Bastion.",
     "shortcut": "Portal roxo na Capela; só aparece depois de você entrar no Fim do Mundo e ver a primeira cena. Nível 80+.", "image": ""},
    {"id": "t10", "name": "The Cloaked Shadow", "tier": "bronze",
     "requirement": "Derrote o Phantom na torre do relógio.",
     "shortcut": "Fale com a Tinker Bell na Cabine. Peter Pan obrigatório e Stop no relógio a cada 30-45 s.", "image": ""},
    {"id": "t11", "name": "The Sandy Blade", "tier": "bronze",
     "requirement": "Derrote o Kurt Zisa em Agrabah.",
     "shortcut": "Fale com o Tapete na casa do Aladdin. Leve o Aladdin e um chaveiro de magia.", "image": ""},
    {"id": "t12", "name": "Novice Hero", "tier": "bronze",
     "requirement": "Vença a Phil Cup.",
     "shortcut": "Abre depois de selar a Traverse Town.", "image": ""},
    {"id": "t13", "name": "Artisan Hero", "tier": "bronze",
     "requirement": "Vença a Pegasus Cup.",
     "shortcut": "Abre depois do Monstro. Final: Leon & Yuffie.", "image": ""},
    {"id": "t14", "name": "Hero of the Coliseum", "tier": "bronze",
     "requirement": "Vença a Hercules Cup.",
     "shortcut": "Abre com Halloween e Neverland selados. Prêmio: Olympia.", "image": ""},
    {"id": "t15", "name": "Coliseum Champion", "tier": "bronze",
     "requirement": "Vença a Hades Cup.",
     "shortcut": "50 chaves. Dá as magias -aga e o Ansem's Report 8 (no Hades, chave 10).", "image": ""},
    {"id": "t16", "name": "The Frost Giant", "tier": "bronze",
     "requirement": "Derrote o Ice Titan no Gold Match.",
     "shortcut": "Abre com as quatro copas vencidas. Guard nos gelos e NUNCA Aerora/Aeroga.", "image": ""},
    {"id": "t17", "name": "One-Winged-Angel", "tier": "bronze",
     "requirement": "Derrote o Sephiroth no Platinum Match.",
     "shortcut": "Abre ao selar o Hollow Bastion. Nível 75+, High Jump e Strike Raid.", "image": ""},
    {"id": "t18", "name": "Supreme Soloist", "tier": "bronze",
     "requirement": "Complete um torneio do Coliseu só com o Sora.",
     "shortcut": "Basta UM: faça o solo da Phil Cup.", "image": ""},
    {"id": "t19", "name": "Time Attacker", "tier": "bronze",
     "requirement": "Complete um contrarrelógio do Coliseu.",
     "shortcut": "Basta UM: o da Phil Cup, 3 minutos.", "image": ""},
    {"id": "t20", "name": "Treasure Hunter", "tier": "bronze",
     "requirement": "Abra 100 baús.",
     "shortcut": "Sai sozinho na run do 100% — só Agrabah tem 37.", "image": ""},
    {"id": "t21", "name": "From Rags to Riches", "tier": "bronze",
     "requirement": "Acumule mais de 10.000 munny.",
     "shortcut": "É o total acumulado, não o que você tem na mão.", "image": ""},
    {"id": "t22", "name": "Heartless Hunter", "tier": "bronze",
     "requirement": "Derrote mais de 2.000 Heartless.",
     "shortcut": "A Hades Cup e o farm de materiais resolvem.", "image": ""},
    {"id": "t23", "name": "Where the Bells Toll", "tier": "bronze",
     "requirement": "Sele o keyhole da Traverse Town.",
     "shortcut": "Toque o sino 3× e vença o Opposite Armor.", "image": ""},
    {"id": "t24", "name": "The Rabbit Hole", "tier": "bronze",
     "requirement": "Sele o keyhole do Wonderland.",
     "shortcut": "Vence o Trickmaster.", "image": ""},
    {"id": "t25", "name": "Junior Hero", "tier": "bronze",
     "requirement": "Sele o keyhole do Olympus Coliseum.",
     "shortcut": "Vem da história, junto com o Cérbero (trinity Amarela do Lobby).", "image": ""},
    {"id": "t26", "name": "Member of the Tribe", "tier": "bronze",
     "requirement": "Sele o keyhole da Deep Jungle.",
     "shortcut": "Caverna atrás da cachoeira, depois do Clayton.", "image": ""},
    {"id": "t27", "name": "Magic Lamp", "tier": "bronze",
     "requirement": "Sele o keyhole de Agrabah.",
     "shortcut": "Depois do Jafar Gênio e da fuga de tapete.", "image": ""},
    {"id": "t28", "name": "Honest Soul", "tier": "bronze",
     "requirement": "Escape do Monstro.",
     "shortcut": "Vença o Parasite Cage II no Estômago.", "image": ""},
    {"id": "t29", "name": "Master of the Seas", "tier": "bronze",
     "requirement": "Sele o keyhole de Atlantica.",
     "shortcut": "Depois da Ursula Gigante. É o mundo mais lento — pule na cronometrada.", "image": ""},
    {"id": "t30", "name": "Pumpkin Prince", "tier": "bronze",
     "requirement": "Sele o keyhole da Halloween Town.",
     "shortcut": "Depois das 7 bolhas escuras da mansão do Oogie.", "image": ""},
    {"id": "t31", "name": "Pixie Dust", "tier": "bronze",
     "requirement": "Sele o keyhole da Neverland.",
     "shortcut": "Acerte o ponteiro do relógio de Londres até meia-noite.", "image": ""},
    {"id": "t32", "name": "End of the World", "tier": "bronze",
     "requirement": "Sele o keyhole do Hollow Bastion.",
     "shortcut": "Depois do Behemoth, na Visita 2.", "image": ""},
    {"id": "t33", "name": "Pooh's Friend", "tier": "bronze",
     "requirement": "Sele o keyhole do Bosque dos Cem Acres.",
     "shortcut": "Precisa das 5 Torn Pages — e a 5ª só vem com mais de 50 dálmatas devolvidos.", "image": ""},
    {"id": "t34", "name": "Record Keeper", "tier": "bronze",
     "requirement": "Complete todas as entradas do Diário do Jiminy.",
     "shortcut": "Sai automaticamente quando Storyteller, Searcher, Professor, Top Dog, Best Friend e Mini-Game Maniac estiverem todos conquistados.", "image": ""},
    {"id": "t35", "name": "Storyteller", "tier": "bronze",
     "requirement": "Complete a seção Chronicles do Diário.",
     "shortcut": "Exige TODOS os keyholes selados, inclusive Atlantica e o Bosque dos Cem Acres.", "image": ""},
    {"id": "t36", "name": "Searcher", "tier": "bronze",
     "requirement": "Reúna os 13 Relatórios do Ansem.",
     "shortcut": "Quatro deles vêm de falar 3× com a Aerith; três vêm dos chefes opcionais.", "image": ""},
    {"id": "t37", "name": "Professor", "tier": "bronze",
     "requirement": "Complete as seções de personagens e Heartless do Diário.",
     "shortcut": "O mais traiçoeiro: exige derrotar cada Heartless raro de área e os quatro cogumelos. Lista na aba Rota, em Limpeza final.", "image": ""},
    {"id": "t38", "name": "Top Dog", "tier": "bronze",
     "requirement": "Devolva os 99 dálmatas.",
     "shortcut": "33 baús de 3. Lista completa com foto na aba Coletáveis.", "image": ""},
    {"id": "t39", "name": "Best Friend", "tier": "bronze",
     "requirement": "Complete a Trinity List do Diário.",
     "shortcut": "46 trinities: 17 Azuis, 6 Vermelhas, 9 Verdes, 4 Amarelas e 10 Brancas.", "image": ""},
    {"id": "t40", "name": "Mini-Game Maniac", "tier": "bronze",
     "requirement": "Complete as entradas de minijogo do Diário.",
     "shortcut": "Os cinco episódios do Bosque dos Cem Acres.", "image": ""},
    {"id": "t41", "name": "Synthesis Master", "tier": "bronze",
     "requirement": "Sintetize todos os itens.",
     "shortcut": "Inclui a Ultima Weapon, que só aparece depois dos 30 itens dos grupos I-V.", "image": ""},
    {"id": "t42", "name": "First Synthesis", "tier": "bronze",
     "requirement": "Sintetize um item pela primeira vez.",
     "shortcut": "Trinity Verde na loja de acessórios abre a Sala de Síntese.", "image": ""},
    {"id": "t43", "name": "Synthesis Novice", "tier": "bronze",
     "requirement": "Sintetize 3 tipos de item.", "shortcut": "", "image": ""},
    {"id": "t44", "name": "Synthesis Amateur", "tier": "bronze",
     "requirement": "Sintetize 15 tipos de item.", "shortcut": "", "image": ""},
    {"id": "t45", "name": "Synthesis Vet", "tier": "bronze",
     "requirement": "Sintetize 30 tipos de item.", "shortcut": "É o gate que libera as receitas finais.", "image": ""},
    {"id": "t46", "name": "Gummi Ship Collector", "tier": "bronze",
     "requirement": "Obtenha 30 ou mais plantas de nave gummi (no PS4).",
     "shortcut": "Caem de naves inimigas e o Geppetto entrega conforme seu total de Heartless derrotados.", "image": ""},
    {"id": "t47", "name": "Flying Ace", "tier": "bronze",
     "requirement": "Destrua mais de 2.500 naves inimigas.",
     "shortcut": "Sai sozinho ao viajar; se faltar, refaça uma rota curta.", "image": ""},
    {"id": "t48", "name": "Customizer", "tier": "bronze",
     "requirement": "Modifique uma nave gummi e salve os dados.",
     "shortcut": "Entre no menu da nave, edite qualquer coisa e salve.", "image": ""},
    {"id": "t49", "name": "Top Gun", "tier": "bronze",
     "requirement": "Complete todas as rotas de nave gummi.",
     "shortcut": "Costuma estourar ao voar de Hollow Bastion para o Fim do Mundo.", "image": ""},
    {"id": "t50", "name": "Test Pilot", "tier": "bronze",
     "requirement": "Complete uma Missão Gummi 1.",
     "shortcut": "Qualquer rota. A de Wonderland ► Traverse Town é a mais simples.", "image": ""},
    {"id": "t51", "name": "Veteran Pilot", "tier": "bronze",
     "requirement": "Complete uma Missão Gummi 2.",
     "shortcut": "Coliseu ► Traverse Town: destrua os painéis roxos e pegue os 70 blocos de escudo.", "image": ""},
    {"id": "t52", "name": "Ace Pilot", "tier": "bronze",
     "requirement": "Complete uma Missão Gummi 3.",
     "shortcut": "Hollow Bastion ► Traverse Town, com o truque do Transform-G para atravessar as paredes de painéis.", "image": ""},
    {"id": "t53", "name": "Oathkeeper", "tier": "bronze",
     "requirement": "Obtenha o chaveiro Oathkeeper.",
     "shortcut": "Fale com a Kairi no Waterway, na 6ª ida a Traverse Town (depois do Hollow Bastion Ep.1).", "image": ""},
    {"id": "t54", "name": "Blade Master", "tier": "bronze",
     "requirement": "Obtenha todas as Keyblades.", "shortcut": "Chaveiros vêm de história, copas, trinities Brancas e síntese.", "image": ""},
    {"id": "t55", "name": "Master Magician", "tier": "bronze",
     "requirement": "Obtenha todos os cajados do Donald.",
     "shortcut": "Visite a loja dos sobrinhos em TODA volta à Traverse Town — o estoque renova.", "image": ""},
    {"id": "t56", "name": "Master Defender", "tier": "bronze",
     "requirement": "Obtenha todos os escudos do Goofy.",
     "shortcut": "Mesma regra dos cajados, mais os baús do Fim do Mundo.", "image": ""},
]

# ── 05 — Fontes consultadas ───────────────────────────────────────────────
SOURCES = [
    {
        "title": "KHGuides — Kingdom Hearts Final Mix",
        "url": "https://www.khguides.com/kh/",
        "note": "Origem da rota por visita, dos locais de dálmatas, trinities, postais, páginas e materiais — e de todas as fotos deste guia.",
    },
    {
        "title": "KHGuides — Trophy Guide (KH1FM)",
        "url": "https://www.khguides.com/kh/collectibles/trophies/",
        "note": "Lista dos 56 troféus, a nota de que a dificuldade empilha no PS4 e os keyholes mínimos do Speedster.",
    },
    {
        "title": "KHGuides — 99 Puppies e Trinities",
        "url": "https://www.khguides.com/kh/collectibles/puppies/",
        "note": "Os 33 baús de filhotes com foto e a tabela de recompensas do Pongo e da Perdita.",
    },
    {
        "title": "KHGuides — Mushroom Heartless e Ultima Weapon",
        "url": "https://www.khguides.com/kh/side-quests/ultima-weapon/",
        "note": "Os cinco materiais raros, o método do Rare Truffle e o pré-requisito do Pink Agaricus.",
    },
    {
        "title": "PlayStationTrophies — Kingdom Hearts Final Mix (PS4)",
        "url": "https://www.playstationtrophies.org/game/kingdom-hearts-final-mix-ps4/guide/",
        "note": "Conferência do empilhamento de dificuldade e da regra do Unchanging Armor com o equipamento inicial.",
    },
    {
        "title": "PlayStationTrophies — lista completa dos troféus",
        "url": "https://www.playstationtrophies.org/game/kingdom-hearts-final-mix-ps4/trophies/",
        "note": "Conferência dos 56 troféus e da divisão 1 platina / 2 ouro / 4 prata / 49 bronze.",
    },
]

# Rodapé do guia. O caminho real do progresso é acrescentado pela página,
# porque ele muda de sistema para sistema (ver paths.guide_dir_label).
FOOTER = "Kingdom Hearts Final Mix (PS4) — Platina PT-BR • guia não oficial"
