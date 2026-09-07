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
    "troféu de terminar em menos de 15 horas, é impossível juntar o 100% e a "
    "corrida contra o relógio no mesmo save. A boa notícia é que no PS4 os "
    "troféus de dificuldade empilham: uma zerada no Proud já entrega Beginner e "
    "Final Mix juntos. Este guia divide a platina nessas duas runs e depois te "
    "leva mundo por mundo, visita por visita, com foto de cada passo."
)

# Números de destaque exibidos no topo.
HERO_STATS = [
    {"value": "56", "label": "troféus"},
    {"value": "2", "label": "zeradas"},
    {"value": "23", "label": "visitas na ordem"},
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
        "title": "As visitas, na ordem",
        "lead": (
            "Abra a visita que você vai jogar: ela traz os passos daquela ida "
            "com foto, os troféus que saem ali e o aviso do que fecha depois. É "
            "a única aba que você precisa com o jogo aberto."
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
                    "Na Run 1 (a cronometrada) você só precisa selar os "
                    "keyholes de Cidade do Trânsito, País das Maravilhas, Selva "
                    "Profunda, Agrabah, Terra do Nunca e Hollow Bastion, mais "
                    "DOIS entre Monstro, Atlantica e Cidade do Halloween. O "
                    "terceiro fica para a Run 2."
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
                    "Deixe a maior parte disto para a Run 2, depois de ter High "
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
        "lead": "A escolha do Despertar, os hábitos que decidem a run, as builds por luta e os cinco chefes opcionais.",
        "notices": [],
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

# ── O plano das duas zeradas ───────────────────────────────────────────────
PLAN = [
    {
        "name": "Run 1 — Proud, cronometrada e sem trocar nada",
        "when": "~12 a 15 h",
        "why": (
            "É a run das três travas: menos de 15 horas de relógio, nenhum "
            "Continue e nenhum equipamento trocado do começo ao fim. Faça no "
            "PROUD: como a dificuldade empilha no PS4, esta única zerada já "
            "entrega Proud Player, Final Mix Master e Novice Player, e deixa a "
            "Run 2 livre para ser no Beginner — onde os superchefes viram outra "
            "conversa. Corra a história e ignore TUDO que for coleção."
        ),
        "gets": "Proud Player, Final Mix Master, Novice Player, Speedster, Undefeated, Unchanging Armor",
    },
    {
        "name": "Run 2 — Beginner, a run do 100%",
        "when": "~40 a 60 h",
        "why": (
            "Save novo no Beginner, sem pressa e sem regra nenhuma: troque "
            "equipamento à vontade, use Continue à vontade. É aqui que entram os "
            "99 dálmatas, as 46 trinities, o Diário do Jiminy inteiro, as quatro "
            "copas, os cinco chefes opcionais, a Ultima Weapon e o nível 100. Só "
            "encoste no chefe final quando o Diário estiver 100%."
        ),
        "gets": "Todos os outros 50 troféus",
    },
    {
        "name": "Se você prefere aprender antes de correr",
        "when": "alternativa",
        "why": (
            "Inverta: faça a Run 1 no Beginner (Speedster + Undefeated + "
            "Unchanging Armor + Novice Player + Final Mix Master) e a Run 2 no "
            "Proud, que aí carrega o Proud Player junto com o 100%. Custa a mesma "
            "quantidade de zeradas; o preço é enfrentar Sephiroth, Kurt Zisa e o "
            "Unknown no Proud."
        ),
        "gets": "Mesmos troféus, ordem trocada",
    },
]

# ── Hábitos e regras que decidem a run ─────────────────────────────────────
PREP = [
    {
        "name": "Não troque NENHUM equipamento na Run 1",
        "when": "Run 1, o tempo todo",
        "why": (
            "Unchanging Armor conta chaveiro (keychain), cajado, escudo e "
            "acessórios de QUALQUER personagem — Sora, Donald e Goofy. O que já "
            "vem equipado no começo pode ficar. Habilidades e itens de cura podem "
            "ser mexidos à vontade: só equipamento conta."
        ),
    },
    {
        "name": "Nunca aperte Continue — carregue o save",
        "when": "Run 1, o tempo todo",
        "why": (
            "Undefeated cai se você escolher Continue uma única vez. Morrer não é "
            "problema: no Game Over, saia e carregue o arquivo. Por isso, salve em "
            "TODO save point, principalmente antes de chefe."
        ),
    },
    {
        "name": "Na Run 1, sele só os keyholes obrigatórios",
        "when": "Run 1",
        "why": (
            "Cidade do Trânsito, País das Maravilhas, Selva Profunda, Agrabah, "
            "Terra do Nunca e Hollow Bastion são fixos; o Coliseu vem junto da "
            "história. Dos três restantes (Monstro, Atlantica, Cidade do "
            "Halloween) bastam DOIS. Atlantica é o mais lento — costuma ser o "
            "cortado."
        ),
    },
    {
        "name": "Equipe Lucky Strike em todo mundo na Run 2",
        "when": "Run 2",
        "why": (
            "Todos os materiais raros de síntese (Mystery Goo, Serenity Power, "
            "Stormy Stone, as gemas) são drop. Lucky Strike em Sora, Donald e "
            "Goofy é a diferença entre uma tarde e uma semana de farm para a "
            "Ultima Weapon."
        ),
    },
    {
        "name": "Não avance o Hollow Bastion antes de fechar o Coliseu",
        "when": "Run 2, Hollow Bastion Visita 1",
        "why": (
            "Vencer o Ansem-Riku (o chefe logo depois da Maleficent Dragão) muda "
            "os encontros e sobe os status dos inimigos em TODOS os mundos, "
            "permanentemente. Faça o farm e as copas que quiser antes de subir "
            "para o Grand Hall."
        ),
    },
    {
        "name": "Volte à Casa da Árvore e brigue com a Sabor de novo",
        "when": "Run 2, Selva Profunda",
        "why": (
            "Antes de avançar a história da Selva, encontre a Sabor mais uma vez "
            "na Casa da Árvore: ela abre um buraco no piso, e é esse buraco que "
            "torna o Pink Agaricus viável depois — o bicho que dropa o Serenity "
            "Power da Ultima Weapon."
        ),
    },
    {
        "name": "Confira o relógio da Terra do Nunca a cada hora",
        "when": "Run 2, depois da Terra do Nunca",
        "why": (
            "A torre do relógio dá 12 prêmios, um por hora do mostrador (que "
            "segue o seu tempo de jogo). Se perder uma hora, a chance só volta 11 "
            "horas depois. Tem Orichalcum, Mythril e Megalixir na lista."
        ),
    },
    {
        "name": "Só abra a porta do Final Rest com o Diário 100%",
        "when": "Run 2, Fim do Mundo",
        "why": (
            "É o ponto sem volta do jogo inteiro. Confirme no menu: Chronicles, "
            "Ansem's Report, Characters 1 e 2, Heartless, 101 Dálmatas, Trinity "
            "List e Mini Games, todos com o selo de completo."
        ),
    },
]

_AW = "https://www.khguides.com/kh/awakening/images/"
_DI = "https://www.khguides.com/kh/destiny-islands/images/"

# ── 01 — As visitas, na ordem de jogo ──────────────────────────────────────
# kind: "história" (obrigatória), "opcional" (só se você quiser), "limpeza"
# (fase de 100% da Run 2) e "final" (ponto sem volta).
VISITS = [
    {
        "world": "Despertar",
        "name": "Despertar — a escolha que define a run",
        "kind": "história",
        "level": "Battle LV 1",
        "run": "Run 1 e Run 2",
        "trophies": [],
        "note": (
            "A arma que você ESCOLHE e a que você ABRE MÃO decidem seus status "
            "iniciais e, principalmente, a ORDEM em que você aprende as "
            "habilidades até o nível 100. Para quem nunca jogou: escolha o "
            "ESCUDO e abra mão do CAJADO. O escudo entrega Guard cedo e Second "
            "Chance no nível 36 — é o que segura a run no Proud."
        ),
        "steps": [
            {
                "title": "Escolha o Escudo, abra mão do Cajado",
                "do": (
                    "Espada = força e combos cedo; Cajado = magia; Escudo = "
                    "defesa, Guard, Leaf Bracer e Second Chance cedo. Abrir mão "
                    "do cajado te dá 8 slots de item (o máximo) e mantém a força "
                    "decente. É a build mais perdoável para uma primeira run e a "
                    "melhor para a Run 1 cronometrada."
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
                    "noite (lento cedo, muito rápido depois do nível 60). Run 1: "
                    "escolha SEMPRE a primeira opção — você quer nível cedo e vai "
                    "parar por volta do 40. Run 2: escolha SEMPRE a última, "
                    "porque o nível 100 é troféu."
                ),
                "image": _AW + "t10.webp",
                "tag": "escolha",
            },
            {
                "title": "Aprenda a travar a mira e o Darkside",
                "do": (
                    "O jogo ensina lock-on aqui — use sempre. No fim da área vem "
                    "o Darkside: bata na mão quando ele socar o chão e suba pelo "
                    "braço para acertar a cabeça. Se você morrer aqui, o jogo "
                    "continua normalmente e isso NÃO quebra o Undefeated (não "
                    "existe tela de Continue nesta luta)."
                ),
                "image": _AW + "tb1.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Ilhas do Destino",
        "name": "Ilhas do Destino — o tutorial",
        "kind": "história",
        "level": "Battle LV 1",
        "run": "Run 1 e Run 2",
        "trophies": [],
        "note": (
            "É o único mundo do jogo ao qual você NUNCA volta. Mesmo assim não "
            "há nada perdível para a platina aqui: sem dálmatas, sem trinity, "
            "só um baú com o acessório Protect Chain."
        ),
        "steps": [
            {
                "title": "Junte os 4 primeiros itens da jangada",
                "do": (
                    "Dois Toras (um na beira da praia depois da ponte de madeira, "
                    "outro na ilhota do outro lado), uma Corda (canto da "
                    "plataforma alta de madeira, suba a escada) e um Pano (dentro "
                    "da casa da árvore). Se juntar tudo SEM pedir dica à Kairi, "
                    "ela te dá uma Hi-Potion."
                ),
                "image": _DI + "t1.webp",
                "tag": "coleta",
            },
            {
                "title": "Treine com Tidus, Selphie, Wakka e Riku",
                "do": (
                    "Na Run 2 vale muito: são os primeiros pontos de XP e o "
                    "melhor lugar do jogo para aprender a defletir (bata na bola "
                    "do Wakka no tempo certo). Na Run 1 cronometrada, pule — não "
                    "vale o relógio."
                ),
                "image": _DI + "t23.webp",
                "tag": "opcional",
            },
            {
                "title": "Corrida contra o Riku (nome da nave)",
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
                "title": "Baú do Protect Chain (o único da ilha)",
                "do": (
                    "Na Enseada (Cove), empurre o caixote de madeira que fica "
                    "perto da tirolesa até a parede de pedra, suba nele e alcance "
                    "a saliência acima; o baú dentro da gruta tem o Protect Chain. "
                    "Na Run 1 você pode até pegar, mas NÃO equipe — equipar quebra "
                    "o Unchanging Armor."
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
        "world": "Cidade do Trânsito",
        "name": "Cidade do Trânsito — Visita 1",
        "kind": "história",
        "level": "Battle LV 1",
        "run": "Run 1 e Run 2",
        "trophies": [],
        "note": (
            "É aqui que o Diário do Jiminy começa a contar. A partir de agora, "
            "todo Heartless novo que você derrota vira uma entrada — e o troféu "
            "Professor exige a lista inteira."
        ),
        "steps": [
            {
                "title": "Primeiro baú: Mythril Shard na Loja de Acessórios",
                "do": (
                    "Siga o Pluto, entre na loja pelo portão grande e fale com o "
                    "Cid. O baú fica em cima do armário verde, perto da porta."
                ),
                "image": _TT + "t4.webp",
                "tag": "baú",
            },
            {
                "title": "Segundo Distrito e a luta contra o Leon",
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
                "title": "O relógio secreto do quarto do Leon",
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
                "title": "Terceiro Distrito e o Guard Armor",
                "do": (
                    "Vá ao Terceiro Distrito passando por trás das lojas do "
                    "Segundo. Depois da emboscada vem o Guard Armor: mire nas MÃOS "
                    "primeiro (são as partes mais rápidas), depois pés, torso por "
                    "último. Se as peças subirem girando, pule para o lado."
                ),
                "image": _TT + "t19.webp",
                "tag": "chefe",
            },
            {
                "title": "Equipe Dodge Roll e destranque a porta do 3º Distrito",
                "do": (
                    "Donald ensina Fire e Goofy ensina Dodge Roll — equipe o Dodge "
                    "Roll imediatamente (habilidade não conta para o Unchanging "
                    "Armor). Antes de sair, examine o keyhole grande perto das "
                    "portas duplas do Terceiro Distrito: isso abre o atalho "
                    "1º↔3º Distrito para o resto do jogo."
                ),
                "image": _TT + "t25.webp",
                "tag": "atalho",
            },
            {
                "title": "Run 2: as primeiras Blue Trinities e os postais",
                "do": (
                    "Só as trinities AZUIS funcionam por enquanto. Faça a do 1º "
                    "Distrito (perto da saída), a do café (te leva à sacada com um "
                    "postal) e a do 3º Distrito atrás da fonte. Aproveite e pegue "
                    "os postais 1 a 4 — a lista completa está na aba Coletáveis."
                ),
                "image": _TN + "t2.webp",
                "tag": "Run 2",
            },
        ],
    },
    {
        "world": "País das Maravilhas",
        "name": "País das Maravilhas — Visita única",
        "kind": "história",
        "level": "Battle LV 3",
        "run": "Run 1 e Run 2",
        "trophies": ["The Rabbit Hole"],
        "note": (
            "Mundo obrigatório também na Run 1. As três caixas de dálmatas "
            "(13-15, 16-18, 19-21) e a quarta (58-60) precisam de Glide e da "
            "trinity Branca — ou seja, é volta na Run 2."
        ),
        "steps": [
            {
                "title": "Empurre a cama antes de encolher",
                "do": (
                    "No Quarto Bizarro, ANTES de beber da garrafa, empurre a cama "
                    "do canto: ela desliza e abre a passagem que você vai usar. Só "
                    "então beba e siga pelo corredor."
                ),
                "image": _WL + "t1.webp",
                "tag": "passo",
            },
            {
                "title": "Run 1: pegue só UMA prova e volte",
                "do": (
                    "O tribunal pede provas, mas basta UMA para prosseguir. Na "
                    "corrida, pegue a mais próxima (Pegadas, na alcova atrás da "
                    "flor vermelha grande) e volte. Você perde a Blizzard grátis, "
                    "mas ela cai do Trickmaster de qualquer jeito."
                ),
                "image": _WL + "t14.webp",
                "tag": "atalho",
            },
            {
                "title": "Run 2: as quatro provas na ordem certa",
                "do": (
                    "1) Dê uma Potion ao bulbo amarelo perto do lago para virar "
                    "gigante. 2) Como gigante, pule no toco de madeira do canto "
                    "oposto — isso levanta as vitórias-régias. 3) Examine a árvore "
                    "grande do centro e pegue a fruta para voltar ao tamanho "
                    "normal. 4) Pegadas na alcova atrás da flor vermelha; Antenas "
                    "em cima dos três cogumelos do fundo; Fedor pela passagem "
                    "escavada na árvore grande (leva ao fogão); Marcas de Garra "
                    "pela passagem do canto até a torneira — pule na prateleira. "
                    "As Marcas de Garra fazem o Cheshire te ensinar Blizzard."
                ),
                "image": _WL + "t15.webp",
                "tag": "coleta",
            },
            {
                "title": "Escolha a caixa e destrua a torre de manivelas",
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
                "title": "Acenda as duas lanternas do Quarto Bizarro",
                "do": (
                    "Volte à Floresta de Lótus, siga para o Jardim do Chá e entre "
                    "no chalé: o quarto está de cabeça para baixo. Suba nas duas "
                    "lanternas do centro e toque as duas. Depois abra a trava de "
                    "metal da parede do fundo."
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
                    "sem bastões acesos ele não tem ataque de fogo."
                ),
                "image": _WL + "t28.webp",
                "tag": "chefe",
            },
            {
                "title": "Run 2 depois: as flores e o Jardim do Chá",
                "do": (
                    "Volte com Glide e trinity Branca. As flores da Floresta de "
                    "Lótus trocam item por item (Ether → Camping Set, Hi-Potion → "
                    "Mega-Potion, Elixir → Mythril Shard). A flor ROSA da alcova "
                    "que se acessa pelo quadro do Quarto Bizarro dá os dálmatas "
                    "58-60 quando você lança Thunder nela. Sentar nas cadeiras do "
                    "Jardim do Chá também rende prêmios e fecha entradas do Diário."
                ),
                "image": _WL + "t36.webp",
                "tag": "Run 2",
            },
        ],
    },
    {
        "world": "Coliseu do Olimpo",
        "name": "Coliseu do Olimpo — Visita 1 (história)",
        "kind": "história",
        "level": "Battle LV 3",
        "run": "Run 1 e Run 2",
        "trophies": ["Junior Hero"],
        "note": (
            "O keyhole do Coliseu não é selado por você: ele sai da história "
            "(trinity Verde no Lobby). O troféu Junior Hero vem junto com o "
            "Cérbero."
        ),
        "steps": [
            {
                "title": "Treinamento do Phil (ganha Thunder)",
                "do": (
                    "Fale com o Phil, tente empurrar o pedestal e aceite o "
                    "treino: quebre todos os barris dentro do tempo usando "
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
                    "combo, ou Dodge Roll no golpe vertical e bate 2 vezes. "
                    "Perder para o Cloud NÃO dá Game Over."
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
                "title": "Fale com o Cloud na escadaria (Sonic Blade)",
                "do": (
                    "Depois da luta, saia do lobby e fale com o Cloud sentado na "
                    "escada em frente ao vestíbulo: ele ensina o Sonic Blade, uma "
                    "das melhores habilidades do jogo e útil até no Sephiroth."
                ),
                "image": _OC + "t1.webp",
                "tag": "habilidade",
            },
        ],
    },
    {
        "world": "Selva Profunda",
        "name": "Selva Profunda — Visita única",
        "kind": "história",
        "level": "Battle LV 5",
        "run": "Run 1 e Run 2",
        "trophies": ["Member of the Tribe"],
        "note": (
            "ATENÇÃO na Run 2: antes de avançar a história depois da cena da "
            "tenda, VOLTE à Casa da Árvore e lute com a Sabor de novo. Ela abre "
            "um buraco no chão que é o que torna o Pink Agaricus (material "
            "Serenity Power, da Ultima Weapon) viável mais tarde."
        ),
        "steps": [
            {
                "title": "Sobreviva à Sabor e desça para o acampamento",
                "do": (
                    "Role para os lados e bata combos de 3; Fire repetido também "
                    "resolve. Perder aqui não interrompe a história. Depois desça "
                    "pelo tronco oco e escorregue pelas árvores até o Camp."
                ),
                "image": _DJ + "t1.webp",
                "tag": "chefe",
            },
            {
                "title": "Os 6 slides do projetor",
                "do": (
                    "1) Em cima da tenda principal (suba pelas caixas perto do "
                    "globo). 2) Numa cômoda no canto, sob as lonas bege. 3) No "
                    "chão, ao lado do quadro-negro com o desenho do Tarzan. 4) Em "
                    "cima da pilha grande de caixas no centro. 5) Em cima da lona "
                    "junto à parede de bambu — suba na tenda e ande pelas lonas. "
                    "6) Em cima das caixas à direita da entrada da tenda. Depois, "
                    "examine o projetor."
                ),
                "image": _DJ + "t7.webp",
                "tag": "coleta",
            },
            {
                "title": "Cipós até as copas (ou o atalho dos hipopótamos)",
                "do": (
                    "Aperte o botão quando \"Jump Next\" acender. Se estiver "
                    "sofrendo, existe o caminho alternativo: pule nas costas dos "
                    "hipopótamos até a plataforma do fundo e suba pelo poste. No "
                    "último pulo, aperte ataque no ar para ganhar distância."
                ),
                "image": _DJ + "t16.webp",
                "tag": "passo",
            },
            {
                "title": "Limpe os Heartless das 5 áreas",
                "do": (
                    "Camp (Protect-G), Bambu (Fire-G), Penhasco (Aeroga-G), "
                    "Árvores de Escalada (Aeroga-G) e Casa da Árvore (Shell-G). "
                    "Cada área limpa dá um bloco gummi de um gorila. Jane, na "
                    "tenda, diz quais faltam."
                ),
                "image": _DJ + "t22.webp",
                "tag": "coleta",
            },
            {
                "title": "Sabor no bambuzal e o salvamento da Jane",
                "do": (
                    "A Sabor pula das árvores no bambuzal: encoste-a numa parede "
                    "e emende combos completos para mantê-la atordoada; Fire com "
                    "lock-on também funciona bem. Depois, nas Árvores de Escalada, "
                    "bata na fruta roxa grande para libertar a Jane — enquanto ela "
                    "estiver inteira, Powerwilds nascem infinitamente (ótimo XP na "
                    "Run 2; ignore na Run 1)."
                ),
                "image": _DJ + "t25.webp",
                "tag": "chefe",
            },
            {
                "title": "Clayton & Stealth Sneak",
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
                "title": "Sele o keyhole e ganhe a trinity Vermelha",
                "do": (
                    "Entre na caverna à esquerda da cachoeira e suba de saliência "
                    "em saliência. Depois de selar, o Tarzan te dá o chaveiro "
                    "Jungle King e a party passa a fazer trinities VERMELHAS — o "
                    "que destrava a Visita 2 da Cidade do Trânsito."
                ),
                "image": _DJ + "t31.webp",
                "tag": "troféu",
            },
            {
                "title": "Run 2: cozinha, Jungle Slider e cipós",
                "do": (
                    "Volte depois para as entradas de minijogo do Diário: Jungle "
                    "Slider (pegue as 10 frutas de cada percurso) e Vine Swing. Na "
                    "cozinha do acampamento, examine relógio e mastro (2 cartões "
                    "de receita) e roupa no varal, globo e vitrola (3 anotações) — "
                    "faça a experiência com só 2 anotações primeiro, depois pegue "
                    "a terceira e repita, para maximizar os Ethers."
                ),
                "image": _DJ + "t39.webp",
                "tag": "Run 2",
            },
        ],
    },
    {
        "world": "Cidade do Trânsito",
        "name": "Cidade do Trânsito — Visita 2 (o keyhole)",
        "kind": "história",
        "level": "Battle LV 5",
        "run": "Run 1 e Run 2",
        "trophies": ["Where the Bells Toll"],
        "note": "",
        "steps": [
            {
                "title": "Trinity Vermelha do Beco → Waterway",
                "do": (
                    "Vá ao Beco (canto sudoeste do 2º Distrito, perto da fonte) e "
                    "faça a trinity Vermelha no canal de água do fundo. Entre no "
                    "Waterway e fale com o Leon; fale com ele DE NOVO sobre o "
                    "bloco gummi da Selva para receber o Earthshine (que vira a "
                    "invocação do Simba)."
                ),
                "image": _TT + "t28.webp",
                "tag": "passo",
            },
            {
                "title": "O Livro Velho e o Merlin",
                "do": (
                    "Fale com o Cid na loja: ele pede que você entregue um Livro "
                    "Velho a um morador do 3º Distrito. Lá, use FIRE na porta de "
                    "madeira com o símbolo de chama, atravesse as pedras móveis e "
                    "entre na casa do lago para achar o Merlin."
                ),
                "image": _TT + "t34.webp",
                "tag": "passo",
            },
            {
                "title": "Simba e a Blue Trinity do estúdio",
                "do": (
                    "Entregue o livro. A Fada Madrinha transforma o Earthshine na "
                    "invocação SIMBA. Antes de sair, faça a Blue Trinity do quarto. "
                    "O Livro Velho abre o Bosque dos Cem Acres — opcional agora, "
                    "obrigatório na Run 2 (troféu Pooh's Friend)."
                ),
                "image": _TT + "t37.webp",
                "tag": "passo",
            },
            {
                "title": "Volte ao Cid e ganhe o Warp-G",
                "do": (
                    "Entre na casa vazia do 3º Distrito (subindo a escada perto da "
                    "passagem para o 2º) e fale com o Cid. Ele instala o gummi de "
                    "navegação e te dá o Warp-G: a partir daqui você viaja "
                    "instantaneamente para mundos já visitados. Isso sozinho salva "
                    "muito relógio na Run 1."
                ),
                "image": _TT + "t40.webp",
                "tag": "atalho",
            },
            {
                "title": "O sino do 2º Distrito e o Opposite Armor",
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
                "title": "Sele, pegue o Comet-G e conheça o Pinóquio",
                "do": (
                    "Selar dá o troféu Where the Bells Toll e a magia Aero. Fale "
                    "com o Cid atrás da loja (Comet-G grátis) e examine a pilha "
                    "colorida no chão da loja de acessórios para encontrar o "
                    "Pinóquio. A Phil Cup abre agora."
                ),
                "image": _TT + "t49.webp",
                "tag": "troféu",
            },
        ],
    },
    {
        "world": "Agrabah",
        "name": "Agrabah — Visita única",
        "kind": "história",
        "level": "Battle LV 8",
        "run": "Run 1 e Run 2",
        "trophies": ["Magic Lamp"],
        "note": (
            "37 baús: é o mundo com mais baú do jogo. Na Run 2 volte com High "
            "Jump e Glide — quatro caixas de dálmatas (37-39, 46-48, 49-51, "
            "52-54) e a Torn Page #1 estão aqui."
        ),
        "steps": [
            {
                "title": "Liberte o Tapete e ache a Jasmine",
                "do": (
                    "Suba o poste de madeira à direita para entrar na casa \"???\" "
                    "e EMPURRE a cômoda que prende o tapete mágico. Depois vá ao "
                    "Beco pela passagem em frente: cena com a Jasmine e o Jafar, e "
                    "uma leva de Heartless (Blizzard resolve bem em espaço "
                    "fechado)."
                ),
                "image": _AG + "t4.webp",
                "tag": "passo",
            },
            {
                "title": "Deserto: encontre o Aladdin",
                "do": (
                    "Volte ao ponto de chegada e passe pelo arco grande até a "
                    "muralha. Salve, deixe o tapete te levar ao deserto e limpe os "
                    "Heartless. Na volta, a Rua Principal está bloqueada: suba no "
                    "prédio e pule pelas lonas até o Beco."
                ),
                "image": _AG + "t10.webp",
                "tag": "passo",
            },
            {
                "title": "As 3 travas para chegar ao Jafar",
                "do": (
                    "1) Beco: numa saliência perto das lonas de madeira, em frente "
                    "à entrada da Praça. 2) Casa do Aladdin: empurre a cômoda da "
                    "parede do fundo. 3) Bazaar: numa saliência alta em frente à "
                    "entrada da Rua Principal — a passagem para o Bazaar fica numa "
                    "plataforma alta no canto da Rua Principal, alcançável pulando "
                    "das lonas ao lado da casa do Aladdin."
                ),
                "image": _AG + "t19.webp",
                "tag": "coleta",
            },
            {
                "title": "Pot Centipede",
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
                "title": "Guardião da Caverna das Maravilhas",
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
                "title": "Derrube a coluna da Sala Escondida",
                "do": (
                    "Entre na caverna e caia no buraco à direita (Relic Chamber). "
                    "Atravesse Dark Chamber e Silent Chamber até a Hidden Room, "
                    "saia da água, pule na coluna de pedra e bata nela. Para "
                    "acionar estátuas distantes, o ALADDIN precisa estar na party "
                    "(o Abu pula nelas)."
                ),
                "image": _AG + "t24.webp",
                "tag": "passo",
            },
            {
                "title": "Torn Page #1 (leve na Run 2)",
                "do": (
                    "Na Dark Chamber, a página fica numa plataforma no centro da "
                    "área — chega-se subindo a cachoeira a partir da Relic "
                    "Chamber. É a primeira das 5 páginas do Bosque dos Cem Acres."
                ),
                "image": _TR + "t103.webp",
                "tag": "coletável",
            },
            {
                "title": "Jafar e Jafar Gênio",
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
                    "pouco antes do impacto. Ao sair: chaveiro Three Wishes, "
                    "invocação do Gênio e a party ganha trinity VERDE — que abre a "
                    "Sala de Síntese na Cidade do Trânsito."
                ),
                "image": _AG + "t34.webp",
                "tag": "troféu",
            },
        ],
    },
]

VISITS += [
    {
        "world": "Cidade do Trânsito",
        "name": "Cidade do Trânsito — Visita 3 (síntese)",
        "kind": "opcional",
        "level": "—",
        "run": "Run 2",
        "trophies": [],
        "note": (
            "Parada opcional na história e PULÁVEL na Run 1. Na Run 2 é onde a "
            "síntese começa — e a síntese é 5 troféus."
        ),
        "steps": [
            {
                "title": "Abra a Sala de Síntese (trinity Verde)",
                "do": (
                    "Na loja de acessórios do 1º Distrito, ative a trinity VERDE "
                    "do chão e suba a escada. Fale com o Moogle da mesa (explicação) "
                    "e depois com o Moogle do forno para sintetizar. Saia pela "
                    "porta do fundo uma vez: isso destranca o acesso direto pelo "
                    "1º Distrito."
                ),
                "image": _TT + "t54.webp",
                "tag": "desbloqueio",
            },
            {
                "title": "Entregue a Torn Page #1 e ganhe o Bambi",
                "do": (
                    "Devolva a página do Agrabah ao Livro Velho no estúdio do "
                    "Merlin, jogue o episódio do Bosque e traga o Naturespark para "
                    "a Fada Madrinha: invocação BAMBI. O Bambi derruba orbes de MP "
                    "— ele é peça de build contra Kurt Zisa e no farm de cogumelos."
                ),
                "image": _TT + "t39.webp",
                "tag": "invocação",
            },
            {
                "title": "Postal #10 e armas novas para Donald e Goofy",
                "do": (
                    "O postal 10 está no panfleto da própria Sala de Síntese "
                    "(examine). A loja dos sobrinhos do Donald recebe armas novas a "
                    "cada visita — na Run 2 vale comprar sempre."
                ),
                "image": _TR + "t10.webp",
                "tag": "coletável",
            },
        ],
    },
    {
        "world": "Monstro",
        "name": "Monstro — Visita única",
        "kind": "história",
        "level": "Battle LV 12",
        "run": "Run 1 (opcional) e Run 2",
        "trophies": ["Honest Soul"],
        "note": (
            "Aqui você ganha o HIGH JUMP, que é a chave de meia dúzia de baús "
            "pelo jogo inteiro. Na Run 1 este é um dos três mundos \"escolha "
            "dois\" — e é o mais rápido dos três, então costuma entrar."
        ),
        "steps": [
            {
                "title": "A ordem das câmaras",
                "do": (
                    "Da Boca até a Câmara 4 o caminho não é linear. A ordem é: "
                    "Câmara 1 ► 2 ► 3 ► 2 ► 5 ► 6 ► 5 ► 4. As passagens certas "
                    "pulsam em verde. Search Ghosts flutuam alto: Fira e Blizzara "
                    "resolvem."
                ),
                "image": _MO + "t4.webp",
                "tag": "passo",
            },
            {
                "title": "Torn Page #2 e dálmatas 76-78 (Câmara 6)",
                "do": (
                    "Na Câmara 6, a página fica numa plataforma alta esverdeada em "
                    "frente à entrada da Câmara 5; a caixa de dálmatas 76-78 está "
                    "no nível do chão, também em frente à passagem da Câmara 5. Na "
                    "Câmara 5, os 79-81 ficam numa saliência alta sobre um barril."
                ),
                "image": _TR + "t129.webp",
                "tag": "coletável",
            },
            {
                "title": "Parasite Cage (1ª luta)",
                "do": (
                    "Só o rosto e a barriga levam dano. Bata combos aéreos BAIXOS "
                    "entre os golpes de braço; Guard deflete bem. Sem Guard, fique "
                    "na plataforma da entrada e bata do ar. O Riku ajuda e até cura "
                    "você. Prêmio: Goofy aprende Cheer."
                ),
                "image": _MO + "t11.webp",
                "tag": "chefe",
            },
            {
                "title": "Watergleam e o baú do High Jump",
                "do": (
                    "Depois da luta, desça pelo buraco: o nível da água na Boca "
                    "baixa. Na saliência mais alta da frente da Boca há um baú com "
                    "o WATERGLEAM (vira a invocação Dumbo). No navio do Geppetto, o "
                    "baú tem a habilidade compartilhada HIGH JUMP — equipe na hora."
                ),
                "image": _MO + "t12.webp",
                "tag": "habilidade",
            },
            {
                "title": "Parasite Cage II (Estômago)",
                "do": (
                    "Suba pela Garganta até o Estômago. Ele agora suga ácido e "
                    "cospe: fique na plataforma CENTRAL, dando a volta por trás "
                    "dele, e nunca pise no verde brilhante do chão. Se você bater "
                    "na cabeça algumas vezes ele abre a boca — trave na matéria "
                    "escura de dentro e bata sem parar. Prêmio: magia Stop."
                ),
                "image": _MO + "t18.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Cidade do Trânsito",
        "name": "Cidade do Trânsito — Visita 4 (Geppetto)",
        "kind": "opcional",
        "level": "—",
        "run": "Run 2",
        "trophies": [],
        "note": "Pulável na Run 1. Na Run 2 é a visita dos gummis e do Spellbinder.",
        "steps": [
            {
                "title": "Oficina do Geppetto e o Wishing Star",
                "do": (
                    "Prédio novo no canto nordeste do 1º Distrito. O Geppetto dá "
                    "plantas de gummi conforme o total de Heartless que você já "
                    "derrotou — volte sempre. O baú do canto tem o chaveiro "
                    "WISHING STAR (crítico em toda finalização de combo: é ele que "
                    "facilita matar o Black Fungus). Entre na casa 30 vezes e fale "
                    "com o Pinóquio para a planta Chocobo. Postal #9 está no potinho "
                    "da prateleira."
                ),
                "image": _TT + "t60.webp",
                "tag": "coletável",
            },
            {
                "title": "Spellbinder (7 magias) e o Dumbo",
                "do": (
                    "Com as SETE magias na mão, fale com o Merlin no estúdio: ele "
                    "dá o chaveiro SPELLBINDER, o melhor bastão de magia do jogo "
                    "até a Ultima — é ele que você usa contra Kurt Zisa e Phantom. "
                    "Entregue o Watergleam à Fada Madrinha para a invocação DUMBO."
                ),
                "image": _TT + "t63.webp",
                "tag": "build",
            },
            {
                "title": "Torn Page #2 devolvida",
                "do": (
                    "Devolva a página do Monstro ao Livro Velho e jogue o episódio "
                    "Block Tigger. A Pegasus Cup abre no Coliseu."
                ),
                "image": _TT + "t39.webp",
                "tag": "coletável",
            },
        ],
    },
    {
        "world": "Atlantica",
        "name": "Atlantica — Visita única",
        "kind": "história",
        "level": "Battle LV 15",
        "run": "Run 1 (opcional) e Run 2",
        "trophies": ["Master of the Seas"],
        "note": (
            "Mundo lento: nadar em 3D atrapalha o combate físico e o troféu não "
            "vale o relógio. Na Run 1, se for cortar um dos três \"escolha "
            "dois\", corte este. Sem nenhum dálmata aqui."
        ),
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
                "title": "Torn Page #3 na Gruta da Ariel",
                "do": (
                    "Siga os tridentes das paredes até o trono do Tritão (no "
                    "jato forte, cole na parede da direita). Na Gruta da Ariel, o "
                    "baú da página está numa prateleira na metade da altura, "
                    "junto de vasos e um porta-retrato."
                ),
                "image": _TR + "t146.webp",
                "tag": "coletável",
            },
            {
                "title": "O golfinho e o Tridente de Cristal",
                "do": (
                    "Limpe a Undersea Gorge, segure no golfinho por alguns "
                    "segundos e solte. Em Calm Depths, use FIRE no ouriço roxo da "
                    "parede para abrir o buraco. No Undersea Valley, segure no "
                    "golfinho de novo: ele te leva à caverna alta. Dentro do navio "
                    "afundado, o baú perto da janela tem o Tridente de Cristal — e "
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
                    "Firas. Só funciona depois que ela joga a primeira poção, e não "
                    "funciona enquanto um ataque dela está saindo do caldeirão. "
                    "Quando o caldeirão explodir em luz, ela fica tonta — é aí que "
                    "você bate de Keyblade. Vermelho = transborda (suba); azul = "
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
                    "trovão (Thundara Ring). Bata DUAS vezes na cara dela e mude de "
                    "posição — os raios teleguiados caem onde você está. STOP "
                    "funciona nela. Prêmio: Ansem's Report 3."
                ),
                "image": _AT + "t29.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Cidade do Halloween",
        "name": "Cidade do Halloween — Visita única",
        "kind": "história",
        "level": "Battle LV 17",
        "run": "Run 1 (opcional) e Run 2",
        "trophies": ["Pumpkin Prince"],
        "note": (
            "Quatro caixas de dálmatas (40-42, 64-66, 67-69, 70-72), a Torn Page "
            "#4 e a magia Gravira. Na Run 2 é visita obrigatória e longa."
        ),
        "steps": [
            {
                "title": "Torn Page #4 no laboratório",
                "do": (
                    "Assim que chegar ao Lab, examine a ESTANTE em frente ao "
                    "Doutor: é a quarta página do Bosque dos Cem Acres."
                ),
                "image": _TR + "t164.webp",
                "tag": "coletável",
            },
            {
                "title": "Sally e depois o Prefeito no cemitério",
                "do": (
                    "Vá ao Cemitério e limpe os Heartless para a Sally te dar o "
                    "Forget-Me-Not. Volte ao Lab, fale com o Doutor e retorne: "
                    "examine o caixão do fundo, fale com o Prefeito e examine as "
                    "lápides NA ORDEM em que os fantasmas aparecem. Acertando, a "
                    "abóbora grande explode e libera o baú do Jack-In-The-Box."
                ),
                "image": _HT + "t9.webp",
                "tag": "puzzle",
            },
            {
                "title": "Suba a Mansão do Oogie",
                "do": (
                    "Na área do Prefeito, examine o túmulo à direita da abóbora "
                    "explodida para ir a Moonlight Hill; examine a lápide torta na "
                    "base da colina para estendê-la. Na porta da mansão, use FIRE "
                    "na plataforma de metal do centro do chão para ativá-la e suba "
                    "até a Sala de Brinquedos no topo."
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
                "title": "ANTES do Oogie: a trinity Vermelha da mansão",
                "do": (
                    "Depois de puxar a alavanca da Sala de Brinquedos, faça a "
                    "trinity VERMELHA da entrada da mansão (no arco ao nível do "
                    "chão, perto do riacho que leva à Ponte) antes de descer para o "
                    "Oogie. Na versão PS2 americana ela sumia depois do chefe; no "
                    "Final Mix o relato é de que continua acessível, mas fazer "
                    "antes não custa nada e elimina o risco."
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
                "title": "Mansão do Oogie: as 7 bolhas escuras",
                "do": (
                    "Segunda fase: destrua as 7 manchas escuras espalhadas pelo "
                    "exterior da mansão (combos ou Fire repetido). Bater nelas "
                    "devolve MP, então não economize magia. Lance AERO e ignore os "
                    "Heartless comuns. Prêmio: Gravira; ao selar, o Jack te dá o "
                    "chaveiro Pumpkinhead."
                ),
                "image": _HT + "t23.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Terra do Nunca",
        "name": "Terra do Nunca — Visita única",
        "kind": "história",
        "level": "Battle LV 19",
        "run": "Run 1 e Run 2",
        "trophies": ["Pixie Dust"],
        "note": (
            "Mundo obrigatório. Você sai daqui com o GLIDE — a última ferramenta "
            "de movimento — e com o relógio de Londres, que dá 12 prêmios ao "
            "longo da Run 2."
        ),
        "steps": [
            {
                "title": "Farme itens no Anti-Sora dos corredores",
                "do": (
                    "Em cada área aparece um Sora-sombra que voa e chuta. Toda vez "
                    "que você zera o HP dele, ele derruba uma Mega-Potion e às "
                    "vezes um Elixir. Na Run 2 é o melhor estoque grátis do jogo "
                    "para as copas."
                ),
                "image": _NL + "t4.webp",
                "tag": "farm",
            },
            {
                "title": "Trinity Verde do Camarote (Donald e Goofy na party)",
                "do": (
                    "A trinity Verde do quarto derruba a escada. Trinity exige "
                    "Donald E Goofy — se o Peter Pan estiver na equipe, troque no "
                    "save point antes."
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
                "title": "Capitão Gancho",
                "do": (
                    "Lute NO CHÃO (esquiva e Guard funcionam melhor). Guard na "
                    "estocada e emende combo de chão. O Battleship que o ajuda "
                    "solta mísseis verdes que CURAM o Gancho: destrua os canhões "
                    "dos dois lados, mas não mate o navio — senão ele invoca "
                    "outro. Quando ele acena o gancho brilhando, não ataque: é "
                    "contra-ataque garantido. Prêmios: Ars Arcanum e Ansem's Report 9."
                ),
                "image": _NL + "t16.webp",
                "tag": "chefe",
            },
            {
                "title": "O relógio de Londres, o Glide e a Tinker Bell",
                "do": (
                    "Trave no ponteiro dos minutos que ainda não chegou ao XII e "
                    "bata até dar meia-noite. Selar dá Pixie Dust, o chaveiro "
                    "Fairyharp, a habilidade compartilhada GLIDE e a invocação "
                    "TINKER BELL (regen constante + um auto-life — ela é a peça "
                    "mais forte de build do jogo)."
                ),
                "image": _NL + "t17.webp",
                "tag": "troféu",
            },
            {
                "title": "Run 2: os 12 prêmios da torre",
                "do": (
                    "O mostrador marca o seu tempo de jogo (26:30 = 2:30). Examine "
                    "a porta com a luz acesa para receber o item daquela hora: "
                    "1h Orichalcum, 2h Power Up, 3h Mythril Shard, 4h Power Up, "
                    "5h AP Up, 6h Mythril, 7h AP Up, 8h Defense Up, 9h Orichalcum, "
                    "10h Defense Up, 11h Mythril Shard, 12h Megalixir. Perdeu uma? "
                    "Só volta 11 horas depois. Depois do Hollow Bastion Ep.1 você "
                    "precisa vencer o Phantom para reabrir a torre."
                ),
                "image": _NL + "t20.webp",
                "tag": "Run 2",
            },
        ],
    },
    {
        "world": "Cidade do Trânsito",
        "name": "Cidade do Trânsito — Visita 5 (Navi-G)",
        "kind": "opcional",
        "level": "—",
        "run": "Run 2",
        "trophies": [],
        "note": "Pulável na Run 1 (o Navi-G da história é instalado de qualquer forma quando você precisa).",
        "steps": [
            {
                "title": "Instale o Navi-G e ganhe o Transform-G",
                "do": (
                    "Fale com o Cid atrás da loja de acessórios. O Transform-G "
                    "permite trocar de nave em pleno voo — é exatamente o truque "
                    "recomendado para a Missão Gummi 3 de Hollow Bastion."
                ),
                "image": _TT + "t65.webp",
                "tag": "gummi",
            },
            {
                "title": "Devolva as Torn Pages #3 e #4",
                "do": (
                    "As páginas de Atlantica e da Cidade do Halloween vão para o "
                    "Livro Velho. Jogue Pooh's Swing e Tigger's Giant Pot: são duas "
                    "das cinco entradas de minijogo do Diário."
                ),
                "image": _TT + "t39.webp",
                "tag": "coletável",
            },
        ],
    },
]

VISITS += [
    {
        "world": "Hollow Bastion",
        "name": "Hollow Bastion — Visita 1",
        "kind": "história",
        "level": "Battle LV 28",
        "run": "Run 1 e Run 2",
        "trophies": [],
        "note": (
            "PONTO DE VIRADA DO JOGO. Vencer o Ansem-Riku (o chefe depois da "
            "Maleficent Dragão) sobe permanentemente o status dos inimigos em "
            "todos os mundos e muda os encontros. Na Run 2, faça ANTES tudo que "
            "você quiser farmar barato e as copas que der."
        ),
        "steps": [
            {
                "title": "Suba as Rising Falls e desça ao Waterway",
                "do": (
                    "Use High Jump e Glide nos blocos de gelo. Na metade, Donald e "
                    "Goofy saem e o FERA entra — sua espada de madeira quase não "
                    "machuca, mas sua MAGIA continua igual: use magia e deixe o "
                    "Fera bater. Examine o pedestal do topo, depois o nó da borda à "
                    "direita para descer e entre na bolha do canto."
                ),
                "image": _HB + "t1.webp",
                "tag": "passo",
            },
            {
                "title": "Abra o portão do castelo",
                "do": (
                    "Salve no Waterway. Use o comando Call nas paredes "
                    "quebráveis, suba de bolha em bolha ativando os interruptores "
                    "de cada área e, na última sala, examine o interruptor e o "
                    "mecanismo grande que abre a porta do castelo."
                ),
                "image": _HB + "t7.webp",
                "tag": "passo",
            },
            {
                "title": "Riku (Entrance Hall) — trinity Branca",
                "do": (
                    "Guard nos golpes rápidos e combo depois; AERO corta metade do "
                    "dano. Ele costuma abrir depois do golpe de cima e no fim do "
                    "pulo alto. Vencer libera as trinities BRANCAS — a última cor, "
                    "que abre 10 pontos espalhados pelo jogo."
                ),
                "image": _HB + "t14.webp",
                "tag": "chefe",
            },
            {
                "title": "A biblioteca: a ordem dos livros",
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
                "title": "As 4 peças do emblema",
                "do": (
                    "1) Quebre os potes ao lado da estátua perto das portas da "
                    "biblioteca — a peça cai na fonte abaixo. 2) Acenda as velas "
                    "das paredes com Fire: a chama central apaga e revela a peça. "
                    "3) Trinity VERMELHA na estátua da ponta sul — ela cai e "
                    "quebra. 4) Empurre a estátua da parede oposta à biblioteca: "
                    "aparece um baú numa plataforma abaixo. Falta MP? Bata nas "
                    "gárgulas entre as velas."
                ),
                "image": _HB + "t23.webp",
                "tag": "puzzle",
            },
            {
                "title": "Maleficent e Maleficent Dragão",
                "do": (
                    "Contra a Maleficent, GRAVITY derruba a plataforma flutuante "
                    "dela na hora — depois é combo livre. Contra o Dragão: invoque "
                    "a TINKER BELL logo no começo (regen + auto-life), lance AERO e "
                    "bata combos aéreos na cabeça. O giro de 360° se evita correndo "
                    "para a borda; do sopro de fogo, fuja de Glide. Prêmios: "
                    "Ansem's Report 5 e o Fireglow (invocação Mushu)."
                ),
                "image": _HB + "t41.webp",
                "tag": "chefe",
            },
            {
                "title": "PARE AQUI se ainda tem farm a fazer",
                "do": (
                    "O próximo chefe é o Ansem-Riku e é ele que endurece o jogo "
                    "inteiro para sempre. Na Run 2, este é o momento de: fechar "
                    "Phil, Pegasus e Hercules Cup, farmar materiais baratos e subir "
                    "nível. Depois dele, tudo custa mais caro."
                ),
                "image": _HB + "t42.webp",
                "tag": "missable",
            },
            {
                "title": "Ansem-Riku (solo) e a volta como Heartless",
                "do": (
                    "Luta SOLO: sem invocação. AERO, Guard no golpe de cima e "
                    "combo de chão; ele revida depois de 4 acertos. Quando sobrar "
                    "uma barra e ele subir brilhando, PULE e faça Glide em círculo "
                    "largo pela arena. Prêmio: Ragnarok. Depois você joga como "
                    "Heartless: desça o castelo (pode pular da lateral) até o "
                    "Entrance Hall e chegue na Kairi."
                ),
                "image": _HB + "t44.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Cidade do Trânsito",
        "name": "Cidade do Trânsito — Visita 6 (Oathkeeper)",
        "kind": "história",
        "level": "—",
        "run": "Run 1 e Run 2",
        "trophies": ["Oathkeeper"],
        "note": (
            "Obrigatória: é a visita que instala o gummi de navegação para "
            "voltar ao Hollow Bastion. O troféu Oathkeeper sai aqui."
        ),
        "steps": [
            {
                "title": "O gummi do Waterway e o chaveiro da Kairi",
                "do": (
                    "Fale com o Cid atrás da loja, vá ao Beco e entre no Waterway. "
                    "Caminhe até o MURAL da parede para receber o Gummi de "
                    "Navegação; depois volte até onde a Kairi está e fale com ela: "
                    "chaveiro OATHKEEPER (troféu). É um dos melhores chaveiros de "
                    "magia do jogo."
                ),
                "image": _TT + "t70.webp",
                "tag": "troféu",
            },
            {
                "title": "Mushu e o Lord Fortune",
                "do": (
                    "Suba a escada do Waterway até o estúdio e entregue o Fireglow "
                    "à Fada Madrinha: invocação MUSHU. Se você já tiver as SEIS "
                    "invocações, ela dá de bônus o Lord Fortune para o Donald."
                ),
                "image": _TT + "t73.webp",
                "tag": "invocação",
            },
            {
                "title": "Torn Page #5 (mais de 50 dálmatas)",
                "do": (
                    "Se você já devolveu mais de 50 filhotes ao Pongo e à Perdita, "
                    "eles entregam a QUINTA página — a que fecha a história do "
                    "Bosque dos Cem Acres. Devolva ao Livro Velho e jogue Pooh's "
                    "Muddy Path."
                ),
                "image": _TT + "t39.webp",
                "tag": "coletável",
            },
            {
                "title": "Instale o gummi com o Cid",
                "do": (
                    "Volte ao 1º Distrito e fale com o Cid para instalar. Um portal "
                    "novo aparece perto da Cidade do Trânsito: é o caminho de volta "
                    "para o Hollow Bastion."
                ),
                "image": _TT + "t68.webp",
                "tag": "passo",
            },
        ],
    },
    {
        "world": "Hollow Bastion",
        "name": "Hollow Bastion — Visita 2 (o keyhole final)",
        "kind": "história",
        "level": "Battle LV 33",
        "run": "Run 1 e Run 2",
        "trophies": ["End of the World"],
        "note": (
            "Depois de selar aqui, os Heartless somem do Hollow Bastion — é a "
            "melhor hora para caçar baús, dálmatas e trinities do mundo em paz."
        ),
        "steps": [
            {
                "title": "Belle e o chaveiro Divine Rose",
                "do": (
                    "Suba as Rising Falls, entre no Entrance Hall e vá à "
                    "biblioteca; suba a escada até a Belle. Depois do reencontro "
                    "dela com o Fera, fale com ela: chaveiro DIVINE ROSE."
                ),
                "image": _HB + "t53.webp",
                "tag": "coletável",
            },
            {
                "title": "Oblivion no Grand Hall (não perca)",
                "do": (
                    "Ao chegar ao portal em forma de coração, escale a borda da "
                    "área até a saliência alta: o baú tem o chaveiro OBLIVION. "
                    "Perto dali, na saliência à esquerda do portal, está a caixa "
                    "dos dálmatas 61-63."
                ),
                "image": _HB + "t55.webp",
                "tag": "baú",
            },
            {
                "title": "Behemoth",
                "do": (
                    "Corra para o lado assim que a luta começar. Só o CHIFRE leva "
                    "dano: GRAVITY tira um naco enorme do HP. Suba nas costas dele "
                    "usando as patas traseiras, trave no chifre e bata. Quando "
                    "formar a esfera laranja acima da cabeça, desça e fique embaixo "
                    "da barriga. Prêmios: Omega Arts e a magia Firaga."
                ),
                "image": _HB + "t56.webp",
                "tag": "chefe",
            },
            {
                "title": "Sele o keyhole e fale 3× com a Aerith",
                "do": (
                    "Selar dá o troféu End of the World e a magia Curaga vem da "
                    "Aerith. Volte à biblioteca e fale com ela TRÊS vezes: ela "
                    "entrega os Ansem's Reports 2, 4, 6 e 10 de uma vez. Quatro dos "
                    "treze relatórios estão aqui — dá para passar batido."
                ),
                "image": _HB + "t57.webp",
                "tag": "missable",
            },
            {
                "title": "Run 2: agora abrem os três superchefes",
                "do": (
                    "Com o Hollow Bastion Ep.1 concluído, ficam disponíveis Kurt "
                    "Zisa (Agrabah, falando com o Tapete na casa do Aladdin), "
                    "Phantom (Terra do Nunca, falando com a Tinker Bell na Cabine) "
                    "e Sephiroth (Coliseu, Platinum Match). O Unknown só aparece "
                    "depois que você entra no Fim do Mundo e vê a primeira cena."
                ),
                "image": _HB + "t60.webp",
                "tag": "Run 2",
            },
        ],
    },
    {
        "world": "Bosque dos Cem Acres",
        "name": "Bosque dos Cem Acres — os 5 episódios",
        "kind": "limpeza",
        "level": "—",
        "run": "Run 2",
        "trophies": ["Pooh's Friend", "Mini-Game Maniac"],
        "note": (
            "Cada episódio exige ter uma Torn Page no inventário. Os cinco "
            "minijogos daqui são as cinco entradas de Mini Games do Diário — "
            "sem eles não existe Record Keeper."
        ),
        "steps": [
            {
                "title": "Entrada: o baú do tronco e o Elixir do armário",
                "do": (
                    "Examine a pilha de gravetos e fale com o Pooh. No fim do "
                    "tronco oco há um baú com Mythril Shard. Suba no telhado da "
                    "casa do Pooh e bata na chaminé: cai um Mega-Ether lá dentro; o "
                    "armário do canto tem um Elixir."
                ),
                "image": _HA + "t17.webp",
                "tag": "baú",
            },
            {
                "title": "Pooh's Hunny Hunt (página 1)",
                "do": (
                    "Fique SEMPRE um galho abaixo do Pooh: dali você alcança as "
                    "abelhas dos dois lados. Depois de bater nas abelhas o Sora "
                    "volta sozinho ao galho mais próximo — não mexa no analógico. "
                    "Caiu? Use o comando Rush. Mais de 100 pontos conta para o Sora "
                    "aprender Cheer. Prêmio: Naturespark (invocação Bambi)."
                ),
                "image": _HA + "t17.webp",
                "tag": "minijogo",
            },
            {
                "title": "Block Tigger (página 2)",
                "do": (
                    "Use RUSH parado PERTO de uma cenoura ainda não pisada (não em "
                    "cima dela, senão o comando não aparece). Olhe a sombra do "
                    "Tigger e para onde ele está virado. Mais de 150 pontos conta "
                    "para o Cheer."
                ),
                "image": _HA + "t17.webp",
                "tag": "minijogo",
            },
            {
                "title": "Pooh's Swing (página 3)",
                "do": (
                    "Aperte quando a coruja abrir as asas ao MÁXIMO: manda o Pooh "
                    "uns 20 metros, o suficiente para cair na casa do Bisonho. Para "
                    "pontuação alta, aperte depois de a coruja fechar as asas e "
                    "antes de o Pooh chegar ao ponto mais baixo. Truque infalível: "
                    "deixe o Pooh comer o mel dos três potes antes — aí ele acerta "
                    "sempre. Mais de 40 metros conta para o Cheer. Prêmio: Stopra."
                ),
                "image": _HA + "t33.webp",
                "tag": "minijogo",
            },
            {
                "title": "Tigger's Giant Pot (página 4) e as nozes da coruja",
                "do": (
                    "Trave nas nozes e rebata; pular antes de bater aumenta a "
                    "pontuação, e acertar assim que a noz fica alcançável multiplica "
                    "mais. Menos de 30 segundos conta para o Cheer. Nesta página "
                    "estão também as 5 Nozes Raras da coruja: Power Up, Defense Up, "
                    "Mythril Shard, AP Up e ORICHALCUM — use os tocos e a gangorra "
                    "do Tigger e do Guru para alcançá-las."
                ),
                "image": _HA + "t33.webp",
                "tag": "minijogo",
            },
            {
                "title": "Pooh's Muddy Path (página 5) — fecha o troféu",
                "do": (
                    "É a página que só existe depois de 50 dálmatas devolvidos. "
                    "Encontre todos os amigos perdidos na trilha lamacenta; ao "
                    "terminar você sela o keyhole do Bosque (troféu Pooh's Friend). "
                    "Confira no Diário se a seção Mini Games está completa."
                ),
                "image": _HA + "t33.webp",
                "tag": "troféu",
            },
        ],
    },
    {
        "world": "Coliseu do Olimpo",
        "name": "Coliseu — as 4 copas + Gold e Platinum",
        "kind": "limpeza",
        "level": "—",
        "run": "Run 2",
        "trophies": [
            "Novice Hero",
            "Artisan Hero",
            "Hero of the Coliseum",
            "Coliseum Champion",
            "Supreme Soloist",
            "Time Attacker",
            "The Frost Giant",
            "One-Winged-Angel",
        ],
        "note": (
            "Cada copa tem TRÊS modos: normal (com a party), solo (só Sora) e "
            "contrarrelógio. Os modos solo e tempo só abrem depois de vencer a "
            "copa no normal — e é deles que saem o Supreme Soloist e o Time "
            "Attacker (basta UM de cada, em qualquer copa: faça na Phil Cup, que "
            "é a mais fácil)."
        ),
        "steps": [
            {
                "title": "Phil Cup (abre depois de selar a Cidade do Trânsito)",
                "do": (
                    "9 chaves. Prêmios: normal = magia Gravity; solo = Combo Plus; "
                    "contrarrelógio (3 min) = Tech Boost. Faça as três aqui e já "
                    "leve Supreme Soloist e Time Attacker."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Pegasus Cup (abre depois do Monstro)",
                "do": (
                    "Termina em Leon & Yuffie. Deflita as shurikens da Yuffie com "
                    "Guard e, com lock-on no Leon, mande uma shuriken nele para "
                    "atordoá-lo. Prêmios: Strike Raid, Orichalcum e Dark Matter."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Hercules Cup (abre com Halloween + Terra do Nunca selados)",
                "do": (
                    "Chave 5 é um Rare Truffle: um toque encerra a luta, mas você "
                    "pode ficar rebatendo para XP. Chave 4 é o Cloud e a final é o "
                    "Hércules — quando ele estiver com a aura dourada é invulnerável. "
                    "Prêmios: Herc's Shield, OLYMPIA e a trinity Push; solo = "
                    "Critical Plus; tempo = Gravity Break."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Hades Cup — 50 chaves e o Ansem's Report 8",
                "do": (
                    "A maratona do jogo: 50 chaves, com Hades na 10 e o Rock Titan "
                    "na final. É aqui que saem Firaga, Blizzaga e Thundaga — por "
                    "isso o guia recomenda fechá-la ANTES de encarar o Phantom. "
                    "Derrotar o Hades dá o Ansem's Report 8. Leve Elixires e "
                    "Megalixires (farmados no Anti-Sora da Terra do Nunca)."
                ),
                "image": _OC + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Gold Match — Ice Titan (nível 65+)",
                "do": (
                    "Abre depois de vencer as QUATRO copas. A luta inteira é "
                    "DEFLEXÃO: fique travado nele e use GUARD nos gelos que vêm — "
                    "eles voltam e machucam o Titã. NÃO lance Aerora/Aeroga: com o "
                    "buff ativo ele manda gelos que não dá para bloquear. Use Glide "
                    "quando ele der passos (o tremor não pega quem está no ar ou "
                    "nas escadas). Prêmio: chaveiro Diamond Dust."
                ),
                "image": _OC + "t1.webp",
                "tag": "chefe",
            },
            {
                "title": "Platinum Match — Sephiroth (nível 75+)",
                "do": (
                    "Abre depois de selar o keyhole do Hollow Bastion (não precisa "
                    "das copas, mas faça antes). NÃO se aproxime pelo chão: a "
                    "espada tem alcance absurdo. Use HIGH JUMP para passar por cima "
                    "do golpe horizontal e emende combo aéreo. Ele revida a cada 4 "
                    "acertos sem finalização. Strike Raid dá dano à distância E te "
                    "deixa invencível durante a animação. Build: Ultima ou Diamond "
                    "Dust, MP Rage no máximo, no máximo UM Combo Plus, acessórios "
                    "de defesa e resistência a trevas. Prêmios: chaveiro One Winged "
                    "Angel e Ansem's Report 12."
                ),
                "image": _OC + "t1.webp",
                "tag": "chefe",
            },
        ],
    },
]

VISITS += [
    {
        "world": "Superchefes",
        "name": "Os 3 chefes fora do Coliseu",
        "kind": "limpeza",
        "level": "nível 65 a 80",
        "run": "Run 2",
        "trophies": ["The Sandy Blade", "The Cloaked Shadow", "He Who Doesn't Exist"],
        "note": (
            "Cada um dá um Ansem's Report (11, 13) ou uma magia, e todos os três "
            "são troféu. A build completa de cada luta está na aba Builds & "
            "Chefes."
        ),
        "steps": [
            {
                "title": "Kurt Zisa — Agrabah (nível 75+)",
                "do": (
                    "Abre depois do Hollow Bastion Ep.1. Fale com o Tapete Mágico "
                    "na casa do Aladdin e escolha ir ao deserto. Leve o ALADDIN no "
                    "lugar do Donald. Prêmios: habilidade Zantetsuken e Ansem's "
                    "Report 11."
                ),
                "image": _AG + "t10.webp",
                "tag": "chefe",
            },
            {
                "title": "Phantom — Terra do Nunca (nível 65+)",
                "do": (
                    "Abre depois do Hollow Bastion Ep.1. Fale com a Tinker Bell na "
                    "Cabine do navio e escolha ir à torre do relógio. PETER PAN é "
                    "obrigatório na party. Faça a Hades Cup antes: você precisa de "
                    "Firaga, Blizzaga e Thundaga. Prêmio: Stopra/Stopga — e a torre "
                    "do relógio volta a funcionar."
                ),
                "image": _NL + "t20.webp",
                "tag": "chefe",
            },
            {
                "title": "Unknown — Hollow Bastion (nível 80+)",
                "do": (
                    "Só aparece depois de você ENTRAR no Fim do Mundo e ver a "
                    "primeira cena — então: entre lá, veja a cena, volte. O portal "
                    "roxo fica na Capela do Castelo. É a luta mais difícil do jogo. "
                    "Prêmios: acessório EXP Necklace e Ansem's Report 13."
                ),
                "image": _HB + "t60.webp",
                "tag": "chefe",
            },
        ],
    },
    {
        "world": "Limpeza final",
        "name": "Limpeza final — antes de abrir a porta",
        "kind": "limpeza",
        "level": "—",
        "run": "Run 2",
        "trophies": [
            "Record Keeper",
            "Top Dog",
            "Best Friend",
            "Professor",
            "Synthesis Master",
            "Blade Master",
            "Master Magician",
            "Master Defender",
            "Level Master",
            "Top Gun",
        ],
        "note": (
            "A lista do que precisa estar fechado. Se qualquer item aqui estiver "
            "aberto, NÃO abra a porta do Final Rest."
        ),
        "steps": [
            {
                "title": "99 dálmatas devolvidos ao Pongo e à Perdita",
                "do": (
                    "São 33 baús de 3 filhotes. A lista completa com foto está na "
                    "aba Coletáveis. Devolver os 99 dá o conjunto completo de "
                    "gummis e a magia Aeroga; aos 90 sai o RIBBON, o melhor "
                    "acessório do jogo."
                ),
                "image": _TR + "t26.webp",
                "tag": "troféu",
            },
            {
                "title": "46 trinities ativadas",
                "do": (
                    "17 Azuis, 6 Vermelhas, 9 Verdes, 4 Amarelas e 10 Brancas. "
                    "Todas na aba Coletáveis com foto. O Diário tem um contador por "
                    "cor — use-o para saber qual cor falta."
                ),
                "image": _TN + "t1.webp",
                "tag": "troféu",
            },
            {
                "title": "Todas as Keyblades, cajados e escudos",
                "do": (
                    "Blade Master, Master Magician e Master Defender. As armas de "
                    "Donald e Goofy vêm principalmente da loja dos sobrinhos (que "
                    "renova o estoque a cada visita), de baús do Fim do Mundo e da "
                    "síntese — por isso a loja precisa ser visitada em TODA volta "
                    "à Cidade do Trânsito."
                ),
                "image": _TT + "t58.webp",
                "tag": "troféu",
            },
            {
                "title": "Sintetizar TODOS os itens (inclui a Ultima Weapon)",
                "do": (
                    "As receitas do último grupo só aparecem depois de sintetizar "
                    "os 30 itens únicos dos grupos I a V. Materiais da Ultima: "
                    "Thunder Gem x5, Mystery Goo x5, Serenity Power x3, Stormy "
                    "Stone x3 e Dark Matter x3. Detalhe de cada um na aba "
                    "Coletáveis."
                ),
                "image": _TT + "t57.webp",
                "tag": "troféu",
            },
            {
                "title": "Diário do Jiminy: seção Heartless completa",
                "do": (
                    "O Professor é o troféu que mais pega gente de surpresa: exige "
                    "TODOS os Heartless, inclusive os raros de área — Sniperwild "
                    "(Cidade do Trânsito), Gigas Shadow (País das Maravilhas), "
                    "Black Ballade (Selva), Pot Scorpion (Agrabah), Grand Ghost "
                    "(Monstro), Chimera (Halloween), Jet Balloon (Terra do Nunca), "
                    "Stealth Soldier (Hollow Bastion), Neoshadow (Fim do Mundo) e "
                    "os quatro cogumelos (White Mushroom, Rare Truffle, Black "
                    "Fungus, Pink Agaricus)."
                ),
                "image": _TT + "t26.webp",
                "tag": "troféu",
            },
            {
                "title": "Sora no nível 100",
                "do": (
                    "Com a curva NOITE (as três últimas respostas no Despertar), o "
                    "trecho final voa. Melhores pontos: Hades Cup repetida, o Ice "
                    "Titan com todos os Tech Boost equipados, e as ondas de "
                    "Heartless do Fim do Mundo. Equipe o EXP Necklace (do Unknown) "
                    "e todos os Tech Boost."
                ),
                "image": _EW + "t14.webp",
                "tag": "troféu",
            },
            {
                "title": "Gummi: todas as rotas, as 3 missões e 30 plantas",
                "do": (
                    "Top Gun quer todas as rotas voadas ao menos uma vez (costuma "
                    "estourar ao ir de Hollow Bastion para o Fim do Mundo). Test/"
                    "Veteran/Ace Pilot querem UMA missão 1, UMA missão 2 e UMA "
                    "missão 3 — qualquer rota. Customizer é só editar e salvar uma "
                    "planta. Gummi Ship Collector quer 30 plantas (no PS4; no PS3 "
                    "são todas)."
                ),
                "image": _TT + "t76.webp",
                "tag": "troféu",
            },
            {
                "title": "Confirme o Diário 100% e SÓ ENTÃO vá ao Fim do Mundo",
                "do": (
                    "Menu → Journal. Chronicles, Ansem's Report, Characters 1, "
                    "Characters 2, The Heartless, 101 Dálmatas, Trinity List e Mini "
                    "Games precisam estar todos com o selo de completo. Aí sim: "
                    "Record Keeper."
                ),
                "image": _EW + "t17.webp",
                "tag": "missable",
            },
        ],
    },
    {
        "world": "Fim do Mundo",
        "name": "Fim do Mundo — o ponto sem volta",
        "kind": "final",
        "level": "Battle LV 40+",
        "run": "Run 1 e Run 2",
        "trophies": ["Speedster", "Undefeated", "Unchanging Armor", "Proud Player", "Final Mix Master", "Novice Player"],
        "note": (
            "Os Heartless daqui (Invisible, Angel Star, Arch Behemoth, Neoshadow) "
            "são os mais fortes do jogo. AERO o tempo todo e GRAVITY nos "
            "Invisibles."
        ),
        "steps": [
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
                    "voltam. O terminal verde grande é o do Bosque dos Cem Acres — "
                    "salve ali."
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
                "title": "A cratera e as ondas dos Mundos Ligados",
                "do": (
                    "Desça com Superglide passando por todos os portais brancos. "
                    "Nas ondas: AERO (Aerora chega a atordoar), invoque a Tinker "
                    "Bell, Gravity nos Invisibles e combos aéreos rápidos nos Angel "
                    "Stars — se um deles começar a brilhar azul, mate na hora ou "
                    "ele gera outro. É também o melhor lugar do jogo para farmar os "
                    "Neoshadows (Stormy Stone da Ultima)."
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
                    "limpa Shadows e bate no núcleo, fase 3 e 4 são as artilharias "
                    "e o rosto. Vencer aqui fecha a run."
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
        "where": "Coliseu do Olimpo",
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
        "where": "Coliseu do Olimpo",
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
        "where": "Terra do Nunca — fale com a Tinker Bell na Cabine",
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
    {"group": "1 · 2 · 3", "world": "Cidade do Trânsito", "area": "Casa Mística",
     "where": "Numa pedra junto à parede, atrás da casa do Merlin. Precisa de Glide.",
     "image": _TR + "t26.webp"},
    {"group": "4 · 5 · 6", "world": "Cidade do Trânsito", "area": "Beco",
     "where": "Atrás de uma parede de caixotes; ative a trinity Vermelha do 1º Distrito (na cerca de madeira do beco atrás da loja dos sobrinhos).",
     "image": _TR + "t23.webp"},
    {"group": "7 · 8 · 9", "world": "Cidade do Trânsito", "area": "Sala de Síntese",
     "where": "Numa mesa, perto de um dos Moogles.",
     "image": _TR + "t11.webp"},
    {"group": "10 · 11 · 12", "world": "Cidade do Trânsito", "area": "Waterway",
     "where": "Logo dentro da escadaria que leva ao Estúdio do Merlin.",
     "image": _TR + "t25.webp"},
    {"group": "13 · 14 · 15", "world": "País das Maravilhas", "area": "Castelo da Rainha",
     "where": "Numa saliência em frente ao save point; chega-se pela Floresta de Lótus.",
     "image": _TR + "t35.webp"},
    {"group": "16 · 17 · 18", "world": "País das Maravilhas", "area": "Floresta de Lótus",
     "where": "Numa vitória-régia perto do centro; pule nos cogumelos ao lado para alcançar.",
     "image": _TR + "t38.webp"},
    {"group": "19 · 20 · 21", "world": "País das Maravilhas", "area": "Jardim do Chá",
     "where": "Numa sebe junto à parede em frente ao chalé; passagem da Floresta de Lótus, precisa de Glide.",
     "image": _TR + "t46.webp"},
    {"group": "22 · 23 · 24", "world": "Coliseu do Olimpo", "area": "Portões",
     "where": "Trinity AZUL em frente à estátua de gladiador da DIREITA (de frente para as portas do vestíbulo).",
     "image": _TR + "t49.webp"},
    {"group": "25 · 26 · 27", "world": "Selva Profunda", "area": "Lagoa dos Hipopótamos",
     "where": "No lado oposto da lagoa; pule nas costas dos hipopótamos.",
     "image": _TR + "t65.webp"},
    {"group": "28 · 29 · 30", "world": "Selva Profunda", "area": "Cipós 2",
     "where": "Numa saliência no centro da área; use os cipós da direita ao entrar.",
     "image": _TR + "t66.webp"},
    {"group": "31 · 32 · 33", "world": "Selva Profunda", "area": "Caverna da Cachoeira",
     "where": "Numa saliência na metade da subida, logo abaixo de uma parede coberta de cipós.",
     "image": _TR + "t71.webp"},
    {"group": "34 · 35 · 36", "world": "Selva Profunda", "area": "Acampamento",
     "where": "Trinity AZUL perto da mesa de laboratório.",
     "image": _TR + "t60.webp"},
    {"group": "37 · 38 · 39", "world": "Agrabah", "area": "Caverna: Sala do Tesouro",
     "where": "Numa saliência perto da entrada do Bottomless Hall; pule de cima de uma pilha de tesouro.",
     "image": _TR + "t110.webp"},
    {"group": "40 · 41 · 42", "world": "Cidade do Halloween", "area": "Mansão do Oogie",
     "where": "Numa alcova na metade da subida da mansão; é preciso puxar antes a alavanca da Sala de Brinquedos.",
     "image": _TR + "t175.webp"},
    {"group": "43 · 44 · 45", "world": "Terra do Nunca", "area": "Convés do navio",
     "where": "Trinity BRANCA em frente ao timão.",
     "image": _TR + "t190.webp"},
    {"group": "46 · 47 · 48", "world": "Agrabah", "area": "Caverna: Sala Escondida",
     "where": "Ative a estátua para abrir a parede ao lado; precisa de trinity Amarela ou High Jump.",
     "image": _TR + "t106.webp"},
    {"group": "49 · 50 · 51", "world": "Agrabah", "area": "Caverna: Entrada",
     "where": "Em cima de um pilar perto da entrada do Hall; High Jump, Glide ou um pulo bem dado de cima de um barril.",
     "image": _TR + "t92.webp"},
    {"group": "52 · 53 · 54", "world": "Agrabah", "area": "Portões do Palácio",
     "where": "Na saliência mais alta do canto em frente aos portões; exige High Jump.",
     "image": _TR + "t89.webp"},
    {"group": "55 · 56 · 57", "world": "Monstro", "area": "Câmara 3",
     "where": "Numa plataforma esverdeada, logo acima da entrada da Câmara 2.",
     "image": _TR + "t123.webp"},
    {"group": "58 · 59 · 60", "world": "País das Maravilhas", "area": "Floresta de Lótus",
     "where": "Lance THUNDER nas flores rosas da alcova acessível pelo quadro do Quarto Bizarro de lado.",
     "image": _TR + "t42.webp"},
    {"group": "61 · 62 · 63", "world": "Hollow Bastion", "area": "Grand Hall",
     "where": "Na saliência à esquerda do portal que leva ao Dark Depths.",
     "image": _TR + "t228.webp"},
    {"group": "64 · 65 · 66", "world": "Cidade do Halloween", "area": "Cemitério",
     "where": "No canto do fundo, perto da lápide escrita \"RIP\".",
     "image": _TR + "t178.webp"},
    {"group": "67 · 68 · 69", "world": "Cidade do Halloween", "area": "Moonlight Hill",
     "where": "Trinity BRANCA em frente à colina, perto da plantação de abóboras.",
     "image": _TR + "t166.webp"},
    {"group": "70 · 71 · 72", "world": "Cidade do Halloween", "area": "Praça da Guilhotina",
     "where": "Dentro da boca de uma estrutura em forma de abóbora; chega-se com Glide.",
     "image": _TR + "t162.webp"},
    {"group": "73 · 74 · 75", "world": "Monstro", "area": "Boca",
     "where": "Numa plataforma alta junto à parede, em frente ao naufrágio; precisa de High Jump.",
     "image": _TR + "t117.webp"},
    {"group": "76 · 77 · 78", "world": "Monstro", "area": "Câmara 6",
     "where": "No nível do chão, em frente à passagem para a Câmara 5.",
     "image": _TR + "t128.webp"},
    {"group": "79 · 80 · 81", "world": "Monstro", "area": "Câmara 5",
     "where": "Numa saliência alta, em cima de um barril, em frente à passagem para a Câmara 4.",
     "image": _TR + "t127.webp"},
    {"group": "82 · 83 · 84", "world": "Terra do Nunca", "area": "Porão",
     "where": "Nas vigas superiores do lado de estibordo; precisa de Glide.",
     "image": _TR + "t181.webp"},
    {"group": "85 · 86 · 87", "world": "Terra do Nunca", "area": "Porão",
     "where": "Trinity AMARELA do porão; o baú verde fica sobre os rolos de lona.",
     "image": _TR + "t184.webp"},
    {"group": "88 · 89 · 90", "world": "Terra do Nunca", "area": "Camarote do Capitão",
     "where": "Ao lado da cama, perto da janela lateral.",
     "image": _TR + "t188.webp"},
    {"group": "91 · 92 · 93", "world": "Hollow Bastion", "area": "Rising Falls",
     "where": "Numa plataforma flutuante, mais ou menos a um quarto da subida.",
     "image": _TR + "t193.webp"},
    {"group": "94 · 95 · 96", "world": "Hollow Bastion", "area": "Portões do Castelo",
     "where": "Lance GRAVITY na pequena plataforma flutuante acima; o canto do fundo se alcança com Glide.",
     "image": _TR + "t219.webp"},
    {"group": "97 · 98 · 99", "world": "Hollow Bastion", "area": "Lift Stop",
     "where": "Lance GRAVITY na pequena plataforma flutuante acima; a área se acessa pela passagem da Biblioteca.",
     "image": _TR + "t213.webp"},
]

# ── 03 — As 46 trinities ──────────────────────────────────────────────────
TRINITIES = [
    {"color": "Azul", "num": 1, "world": "Cidade do Trânsito", "where": "1º Distrito — no chão perto da saída do mundo, em frente à loja de acessórios.", "reward": "120 munny", "image": _TN + "t1.webp"},
    {"color": "Azul", "num": 2, "world": "Cidade do Trânsito", "where": "1º Distrito — em frente ao café, perto da loja dos sobrinhos.", "reward": "Teleporta a party para a sacada do café, onde há um baú com um POSTAL.", "image": _TN + "t2.webp"},
    {"color": "Azul", "num": 3, "world": "Cidade do Trânsito", "where": "3º Distrito — atrás da fonte da Dama e o Vagabundo, no canto.", "reward": "60 munny, Camping Set", "image": _TN + "t3.webp"},
    {"color": "Azul", "num": 4, "world": "Cidade do Trânsito", "where": "Estúdio do Merlin — perto do save point.", "reward": "50 munny, Mega-Ether", "image": _TN + "t4.webp"},
    {"color": "Azul", "num": 5, "world": "País das Maravilhas", "where": "Floresta de Lótus — perto das flores amarelas, na alcova que se alcança pulando nas vitórias-régias.", "reward": "Orbes de MP, Camping Set", "image": _TN + "t5.webp"},
    {"color": "Azul", "num": 6, "world": "País das Maravilhas", "where": "Floresta de Lótus — perto dos cogumelos amarelos, na alcova em frente à passagem para o Castelo da Rainha.", "reward": "Orbes de MP, Ether, Potion, Tent", "image": _TN + "t6.webp"},
    {"color": "Azul", "num": 7, "world": "Coliseu do Olimpo", "where": "Portões — em frente à estátua de gladiador da ESQUERDA (de frente para o vestíbulo).", "reward": "Mythril Shard", "image": _TN + "t7.webp"},
    {"color": "Azul", "num": 8, "world": "Coliseu do Olimpo", "where": "Portões — em frente à estátua da DIREITA.", "reward": "Dálmatas 22-24", "image": _TN + "t8.webp"},
    {"color": "Azul", "num": 9, "world": "Selva Profunda", "where": "Acampamento — perto do equipamento de laboratório e da passagem para a Lagoa.", "reward": "Dálmatas 34-36", "image": _TN + "t9.webp"},
    {"color": "Azul", "num": 10, "world": "Selva Profunda", "where": "Árvores de Escalada — numa plataforma elevada, perto da passagem para a Casa da Árvore.", "reward": "Thundara-G", "image": _TN + "t10.webp"},
    {"color": "Azul", "num": 11, "world": "Agrabah", "where": "Bazaar — no nível do chão, no centro da área.", "reward": "200 munny, Mega-Ether", "image": _TN + "t11.webp"},
    {"color": "Azul", "num": 12, "world": "Agrabah", "where": "Caverna: Silent Chamber — na plataforma central, perto da passagem para o Hall.", "reward": "Thundara-G", "image": _TN + "t12.webp"},
    {"color": "Azul", "num": 13, "world": "Monstro", "where": "Boca — numa plataforma de madeira na frente da boca; só depois de derrotar o Parasite Cage.", "reward": "50 munny, Potion x2, Cottage", "image": _TN + "t13.webp"},
    {"color": "Azul", "num": 14, "world": "Monstro", "where": "Câmara 5 — no nível do chão, em frente à passagem para a Câmara 6.", "reward": "333 munny, Cottage", "image": _TN + "t14.webp"},
    {"color": "Azul", "num": 15, "world": "Monstro", "where": "Garganta — no nível mais baixo, no centro da área.", "reward": "100 munny, Mythril Shard", "image": _TN + "t15.webp"},
    {"color": "Azul", "num": 16, "world": "Hollow Bastion", "where": "Waterway: Masmorra — perto do centro, à esquerda da plataforma que leva ao Lift Stop.", "reward": "Cottage, Mega-Potion, Mega-Ether, orbes de HP", "image": _TN + "t16.webp"},
    {"color": "Azul", "num": 17, "world": "Hollow Bastion", "where": "Great Crest — no centro da área grande, depois de atravessar na plataforma flutuante.", "reward": "Megalixir, Cottage x2, orbes de MP", "image": _TN + "t17.webp"},

    {"color": "Vermelha", "num": 1, "world": "Cidade do Trânsito", "where": "1º Distrito — numa cerca de madeira no beco atrás da loja dos sobrinhos.", "reward": "Dálmatas 4-6", "image": _TN + "t18.webp"},
    {"color": "Vermelha", "num": 2, "world": "Cidade do Trânsito", "where": "Beco — na grade de metal que bloqueia o canal, no canto oposto à passagem para a Casa dos Dálmatas.", "reward": "Abre o Waterway (obrigatória na história)", "image": _TN + "t19.webp"},
    {"color": "Vermelha", "num": 3, "world": "Cidade do Trânsito", "where": "2º Distrito — nas tábuas de madeira em frente à torre do sino, acima da Gizmo Shop.", "reward": "Abre a torre do sino (obrigatória na história)", "image": _TN + "t20.webp"},
    {"color": "Vermelha", "num": 4, "world": "Agrabah", "where": "Sala do Tesouro — em frente a uma estátua de esfinge, do outro lado do save point.", "reward": "333 munny, Mythril Shard", "image": _TN + "t21.webp"},
    {"color": "Vermelha", "num": 5, "world": "Cidade do Halloween", "where": "Mansão do Oogie — no nível do chão, no arco perto do riacho que leva à Ponte.", "reward": "Mythril Shard", "image": _TN + "t22.webp"},
    {"color": "Vermelha", "num": 6, "world": "Hollow Bastion", "where": "Entrance Hall — na sacada do 2º andar, em frente a uma estátua de pedra com chifres, perto da borda interna.", "reward": "Peça do Emblema", "image": _TN + "t23.webp"},

    {"color": "Verde", "num": 1, "world": "Cidade do Trânsito", "where": "1º Distrito, loja de acessórios — em frente à mesa do centro.", "reward": "Abre a Sala de Síntese", "image": _TN + "t24.webp"},
    {"color": "Verde", "num": 2, "world": "País das Maravilhas", "where": "Quarto Bizarro — no nível do chão, dentro do forno.", "reward": "Mythril Shard", "image": _TN + "t25.webp"},
    {"color": "Verde", "num": 3, "world": "País das Maravilhas", "where": "Toca do Coelho — junto à parede, perto do save point.", "reward": "Elixir", "image": _TN + "t26.webp"},
    {"color": "Verde", "num": 4, "world": "Coliseu do Olimpo", "where": "Portões — junto à parede à direita da passagem para o mapa-múndi, entre dois braseiros.", "reward": "Mythril", "image": _TN + "t27.webp"},
    {"color": "Verde", "num": 5, "world": "Selva Profunda", "where": "Copas das Árvores — no centro da área (muito difícil de ver por causa da cor).", "reward": "Mythril Shard, orbes de HP", "image": _TN + "t28.webp"},
    {"color": "Verde", "num": 6, "world": "Agrabah", "where": "Depósito — perto das prateleiras, em frente ao save point.", "reward": "AP Up", "image": _TN + "t29.webp"},
    {"color": "Verde", "num": 7, "world": "Monstro", "where": "Boca — em cima do navio do Geppetto.", "reward": "Mythril Shard", "image": _TN + "t30.webp"},
    {"color": "Verde", "num": 8, "world": "Terra do Nunca", "where": "Cabine — no centro da sala.", "reward": "Abre o Camarote do Capitão (obrigatória na história)", "image": _TN + "t31.webp"},
    {"color": "Verde", "num": 9, "world": "Hollow Bastion", "where": "Biblioteca — 2º andar, em frente à estante perto da mesa e da sacada.", "reward": "Azal Vol. 3 (peça do puzzle dos livros)", "image": _TN + "t32.webp"},

    {"color": "Amarela", "num": 1, "world": "Cidade do Trânsito", "where": "Casa Mística — perto de uma pilha de caixotes grandes, atrás da casa do Merlin.", "reward": "AP Up", "image": _TN + "t33.webp"},
    {"color": "Amarela", "num": 2, "world": "Coliseu do Olimpo", "where": "Lobby — em frente ao pedestal grande.", "reward": "Sela o keyhole do Coliseu (obrigatória na história)", "image": _TN + "t34.webp"},
    {"color": "Amarela", "num": 3, "world": "Agrabah", "where": "Caverna: Hall — em frente a uma estátua de pedra perto do caminho da pedra rolante.", "reward": "Abre uma câmara com Thundara-G e Meteor-G", "image": _TN + "t35.webp"},
    {"color": "Amarela", "num": 4, "world": "Terra do Nunca", "where": "Porão — em frente à porta trancada, logo à esquerda depois de subir a escada.", "reward": "Orichalcum, Dark Matter, dálmatas 85-87 e a magia Aero", "image": _TN + "t36.webp"},

    {"color": "Branca", "num": 1, "world": "Cidade do Trânsito", "where": "Waterway — no piso de pedra, em frente ao mural.", "reward": "Orichalcum", "image": _TN + "t37.webp"},
    {"color": "Branca", "num": 2, "world": "País das Maravilhas", "where": "Floresta de Lótus — no centro da alcova acessível pelo quadro do Quarto Bizarro de lado.", "reward": "Chaveiro LADY LUCK", "image": _TN + "t38.webp"},
    {"color": "Branca", "num": 3, "world": "Coliseu do Olimpo", "where": "Portões — no centro da área.", "reward": "Cajado Violetta", "image": _TN + "t39.webp"},
    {"color": "Branca", "num": 4, "world": "Selva Profunda", "where": "Caverna dos Corações — no centro da área.", "reward": "Orichalcum", "image": _TN + "t40.webp"},
    {"color": "Branca", "num": 5, "world": "Agrabah", "where": "Caverna: Entrada — logo em frente à entrada, à sua esquerda (de frente para o Hall).", "reward": "Ifrit Belt", "image": _TN + "t41.webp"},
    {"color": "Branca", "num": 6, "world": "Monstro", "where": "Câmara 6 — no nível do chão, no centro da área.", "reward": "Dark Matter (material da Ultima)", "image": _TN + "t42.webp"},
    {"color": "Branca", "num": 7, "world": "Atlantica", "where": "Palácio do Tritão — dentro da grande concha roxa perto do centro.", "reward": "Orichalcum", "image": _TN + "t43.webp"},
    {"color": "Branca", "num": 8, "world": "Cidade do Halloween", "where": "Moonlight Hill — em frente à colina, perto da plantação de abóboras.", "reward": "Dálmatas 67-69", "image": _TN + "t44.webp"},
    {"color": "Branca", "num": 9, "world": "Terra do Nunca", "where": "Convés — em frente ao timão do navio.", "reward": "Dálmatas 43-45", "image": _TN + "t45.webp"},
    {"color": "Branca", "num": 10, "world": "Hollow Bastion", "where": "Rising Falls — na poça rasa mais ou menos na metade da subida.", "reward": "Thundaga-G", "image": _TN + "t46.webp"},
]

# ── 03 — As 5 Torn Pages do Bosque dos Cem Acres ──────────────────────────
PAGES = [
    {"num": "Página 1", "world": "Agrabah", "where": "Caverna: Dark Chamber — numa plataforma no centro da área; chega-se subindo a cachoeira a partir da Relic Chamber.", "image": _TR + "t103.webp"},
    {"num": "Página 2", "world": "Monstro", "where": "Câmara 6 — numa plataforma alta esverdeada, em frente à entrada da Câmara 5.", "image": _TR + "t129.webp"},
    {"num": "Página 3", "world": "Atlantica", "where": "Gruta da Ariel — num baú sobre uma prateleira, mais ou menos na metade da altura, junto de vasos e um porta-retrato.", "image": _TR + "t146.webp"},
    {"num": "Página 4", "world": "Cidade do Halloween", "where": "Laboratório — examine a estante em frente ao Doutor.", "image": _TR + "t164.webp"},
    {"num": "Página 5", "world": "Cidade do Trânsito", "where": "Casa dos Dálmatas — devolva mais de 50 filhotes ao Pongo e à Perdita.", "image": _TR + "t26.webp"},
]

# ── 03 — Os 10 postais (todos na Cidade do Trânsito) ──────────────────────
POSTCARDS = [
    {"num": "Postal 1", "where": "Trinity AZUL perto do café do 1º Distrito; abra o baú da sacada.", "prize": "Cottage", "image": _TR + "t2.webp"},
    {"num": "Postal 2", "where": "Bata no ventilador de teto da loja dos sobrinhos (1º Distrito).", "prize": "Mythril Shard", "image": _TR + "t8.webp"},
    {"num": "Postal 3", "where": "Baú no telhado da loja de acessórios (1º Distrito).", "prize": "Mega-Potion", "image": _TR + "t4.webp"},
    {"num": "Postal 4", "where": "Baú azul atrás da loja de acessórios (1º Distrito).", "prize": "Mega-Ether", "image": _TR + "t3.webp"},
    {"num": "Postal 5", "where": "Baú acima da lona da loja \"Boots & Shoes\" (2º Distrito).", "prize": "Mythril", "image": _TR + "t13.webp"},
    {"num": "Postal 6", "where": "Examine o canto da sacada do 3º Distrito; chega-se pelos telhados do lado leste do 2º Distrito.", "prize": "Elixir", "image": _TR + "t28.webp"},
    {"num": "Postais 7 e 8", "where": "Lance THUNDER no fio exposto do canto do 3º Distrito; depois, na Gizmo Shop, pule nos três botões em cima da máquina e examine o relógio central. Saem dois postais de uma vez.", "prize": "Megalixir e Orichalcum", "image": _TR + "t16.webp"},
    {"num": "Postal 9", "where": "Examine o potinho da prateleira na casa do Geppetto.", "prize": "AP Up", "image": _TR + "t7.webp"},
    {"num": "Postal 10", "where": "Examine o panfleto na Sala de Síntese (1º Distrito).", "prize": "Defense Up", "image": _TR + "t10.webp"},
]

# ── 03 — Os 13 Relatórios do Ansem ────────────────────────────────────────
REPORTS = [
    {"num": "Relatório 1", "how": "Derrote o Jafar Gênio, em Agrabah."},
    {"num": "Relatório 2", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 3", "how": "Derrote a Ursula Gigante, em Atlantica."},
    {"num": "Relatório 4", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 5", "how": "Derrote a Maleficent, no Hollow Bastion."},
    {"num": "Relatório 6", "how": "Fale com a Aerith na Biblioteca depois de selar o keyhole do Hollow Bastion."},
    {"num": "Relatório 7", "how": "Derrote o Oogie Boogie, na Cidade do Halloween."},
    {"num": "Relatório 8", "how": "Derrote o Hades, na Hades Cup do Coliseu."},
    {"num": "Relatório 9", "how": "Derrote o Capitão Gancho, na Terra do Nunca."},
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
            "confiável é o Rare Truffle no convés da Terra do Nunca: voando você "
            "consegue rebatê-lo no ar sem parar. 50 rebatidas = Elixir + 40% de "
            "Goo; 100 = Megalixir + Goo garantido."
        ),
    },
    {
        "name": "Serenity Power x3",
        "how": (
            "Só cai do PINK AGARICUS, na Casa da Árvore da Selva Profunda. Ele só "
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
            "Terra do Nunca. O contrarrelógio da Pegasus Cup também dá um."
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
     "shortcut": "Abre depois de selar a Cidade do Trânsito.", "image": ""},
    {"id": "t13", "name": "Artisan Hero", "tier": "bronze",
     "requirement": "Vença a Pegasus Cup.",
     "shortcut": "Abre depois do Monstro. Final: Leon & Yuffie.", "image": ""},
    {"id": "t14", "name": "Hero of the Coliseum", "tier": "bronze",
     "requirement": "Vença a Hercules Cup.",
     "shortcut": "Abre com Halloween e Terra do Nunca selados. Prêmio: Olympia.", "image": ""},
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
     "shortcut": "Sai sozinho na Run 2 — só Agrabah tem 37.", "image": ""},
    {"id": "t21", "name": "From Rags to Riches", "tier": "bronze",
     "requirement": "Acumule mais de 10.000 munny.",
     "shortcut": "É o total acumulado, não o que você tem na mão.", "image": ""},
    {"id": "t22", "name": "Heartless Hunter", "tier": "bronze",
     "requirement": "Derrote mais de 2.000 Heartless.",
     "shortcut": "A Hades Cup e o farm de materiais resolvem.", "image": ""},
    {"id": "t23", "name": "Where the Bells Toll", "tier": "bronze",
     "requirement": "Sele o keyhole da Cidade do Trânsito.",
     "shortcut": "Toque o sino 3× e vença o Opposite Armor.", "image": ""},
    {"id": "t24", "name": "The Rabbit Hole", "tier": "bronze",
     "requirement": "Sele o keyhole do País das Maravilhas.",
     "shortcut": "Vence o Trickmaster.", "image": ""},
    {"id": "t25", "name": "Junior Hero", "tier": "bronze",
     "requirement": "Sele o keyhole do Coliseu do Olimpo.",
     "shortcut": "Vem da história, junto com o Cérbero (trinity Amarela do Lobby).", "image": ""},
    {"id": "t26", "name": "Member of the Tribe", "tier": "bronze",
     "requirement": "Sele o keyhole da Selva Profunda.",
     "shortcut": "Caverna atrás da cachoeira, depois do Clayton.", "image": ""},
    {"id": "t27", "name": "Magic Lamp", "tier": "bronze",
     "requirement": "Sele o keyhole de Agrabah.",
     "shortcut": "Depois do Jafar Gênio e da fuga de tapete.", "image": ""},
    {"id": "t28", "name": "Honest Soul", "tier": "bronze",
     "requirement": "Escape do Monstro.",
     "shortcut": "Vença o Parasite Cage II no Estômago.", "image": ""},
    {"id": "t29", "name": "Master of the Seas", "tier": "bronze",
     "requirement": "Sele o keyhole de Atlantica.",
     "shortcut": "Depois da Ursula Gigante. É o mundo mais lento — pule na Run 1.", "image": ""},
    {"id": "t30", "name": "Pumpkin Prince", "tier": "bronze",
     "requirement": "Sele o keyhole da Cidade do Halloween.",
     "shortcut": "Depois das 7 bolhas escuras da mansão do Oogie.", "image": ""},
    {"id": "t31", "name": "Pixie Dust", "tier": "bronze",
     "requirement": "Sele o keyhole da Terra do Nunca.",
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
     "shortcut": "Qualquer rota. A de Wonderland ► Cidade do Trânsito é a mais simples.", "image": ""},
    {"id": "t51", "name": "Veteran Pilot", "tier": "bronze",
     "requirement": "Complete uma Missão Gummi 2.",
     "shortcut": "Coliseu ► Cidade do Trânsito: destrua os painéis roxos e pegue os 70 blocos de escudo.", "image": ""},
    {"id": "t52", "name": "Ace Pilot", "tier": "bronze",
     "requirement": "Complete uma Missão Gummi 3.",
     "shortcut": "Hollow Bastion ► Cidade do Trânsito, com o truque do Transform-G para atravessar as paredes de painéis.", "image": ""},
    {"id": "t53", "name": "Oathkeeper", "tier": "bronze",
     "requirement": "Obtenha o chaveiro Oathkeeper.",
     "shortcut": "Fale com a Kairi no Waterway, na 4ª ida à Cidade do Trânsito (depois do Hollow Bastion Ep.1).", "image": ""},
    {"id": "t54", "name": "Blade Master", "tier": "bronze",
     "requirement": "Obtenha todas as Keyblades.", "shortcut": "Chaveiros vêm de história, copas, trinities Brancas e síntese.", "image": ""},
    {"id": "t55", "name": "Master Magician", "tier": "bronze",
     "requirement": "Obtenha todos os cajados do Donald.",
     "shortcut": "Visite a loja dos sobrinhos em TODA volta à Cidade do Trânsito — o estoque renova.", "image": ""},
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
