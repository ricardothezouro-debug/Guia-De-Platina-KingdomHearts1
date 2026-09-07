# Kingdom Hearts Final Mix — Guia de Platina (PS4)

Plugin de **platina** para o [Streamer Sidekick](https://github.com/ricardothezouro-debug/streamer_sidekick).
Guia completo em PT-BR do KH1 Final Mix da coletânea *KINGDOM HEARTS HD 1.5+2.5
ReMIX*, montado para quem **nunca jogou** conseguir platinar com o mínimo de
zeradas possível.

## Por que duas zeradas (e não uma, nem três)

Kingdom Hearts 1 **não tem pós-jogo**: quando os créditos sobem, o save não
volta para o mapa. Então todo coletável precisa estar fechado antes de abrir a
porta do Final Rest. Como um dos troféus pede **menos de 15 horas de jogo**, é
impossível juntar o 100% com a corrida contra o relógio no mesmo save.

No PS4 os troféus de dificuldade **empilham** (no PS3 não), então:

| Run | Dificuldade | O que ela entrega |
| --- | --- | --- |
| **1** | Proud, ~12-15 h | Speedster, Undefeated, Unchanging Armor + Proud Player, Final Mix Master e Novice Player de uma vez |
| **2** | Beginner, ~40-60 h | Os outros 50 troféus: 99 dálmatas, 46 trinities, Diário do Jiminy 100%, as 4 copas, os 5 chefes opcionais, Ultima Weapon e nível 100 |

**Versão gamox** (na aba Builds & Chefes): inverta as duas — a cronometrada no
Beginner e o **100% inteiro no Proud**. Custa as mesmas duas zeradas, mas joga
Sephiroth, Kurt Zisa, o Unknown, o Ice Titan e a Hades Cup para o Proud, onde
eles são luta de verdade — e você chega neles com nível 80+, Ultima Weapon e
Ribbon. Para quem quer o desafio e não o relógio.

## O que tem dentro

- **Rota** — 23 visitas na ordem de jogo, 125 passos com **foto**, etiqueta de
  perdível/chefe/baú e o aviso do que fecha depois de cada avanço.
- **56 Troféus** — requisito e o caminho curto de cada um, com filtro por tier e
  "só pendentes".
- **Coletáveis** — os 33 baús dos 99 dálmatas, as 46 trinities (por cor), as 5
  Torn Pages, os 10 postais, os 13 Relatórios do Ansem e os materiais raros da
  Ultima Weapon — todos com local e foto.
- **Builds & Chefes** — a escolha do Despertar, os hábitos que decidem a run e
  build + estratégia dos cinco chefes opcionais (Ice Titan, Sephiroth, Kurt
  Zisa, Phantom e Unknown).
- **Fontes** — de onde veio cada dado.

Tudo com caixa de marcação, progresso salvo automaticamente, busca global e
exportar/importar progresso.

## Instalar

Pela aba **Platinas** do Streamer Sidekick — o guia aparece na lista e instala
em um clique.

## Rodar standalone (para testar)

```bash
pip install -r requirements.txt
```

Windows:

```bash
set PYTHONPATH=src && python -m platina_kh1
```

macOS / Linux:

```bash
PYTHONPATH=src python -m platina_kh1
```

## Onde fica o progresso

Na pasta de dados do Streamer Sidekick, `platinas/kh1-final-mix/` — que é
`%APPDATA%` no Windows, `~/Library/Application Support` no macOS e
`$XDG_CONFIG_HOME` (ou `~/.config`) no Linux. Fica fora da pasta do plugin, então
sobrevive a atualizações. O rodapé do guia mostra o caminho real do seu sistema.

---

Guia não oficial. Kingdom Hearts é marca da Square Enix e da Disney. As fotos
são carregadas dos sites citados na aba **Fontes**.
