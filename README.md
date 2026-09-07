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

A **primeira** run é a do 100% — é ela que você joga de verdade. A segunda é a
cronometrada, e ela só é rápida porque a primeira já te ensinou o mapa inteiro.
O guia chama as duas pelo nome, nunca por número.

| Ordem | O que é | O que entrega |
| --- | --- | --- |
| **1ª** | A run do 100%, ~40-60 h, sem regra nenhuma | 50 dos 56 troféus: 99 dálmatas, 46 trinities, Diário do Jiminy 100%, as 4 copas, os 5 chefes opcionais, Ultima Weapon e nível 100 |
| **2ª** | A cronometrada, ~12-15 h: menos de 15 h, sem Continue, sem trocar equipamento | Speedster, Undefeated, Unchanging Armor |

### Versão gamox (a recomendada)

**1ª run no PROUD · 2ª no Beginner.** Como a dificuldade empilha no PS4,
terminar a run do 100% no Proud entrega Proud Player, Final Mix Master e Novice
Player de uma vez. E joga Sephiroth, Kurt Zisa, o Unknown, o Ice Titan e a Hades
Cup para a run em que você tem nível 80+, Ultima Weapon, Ribbon e as seis
invocações — no Beginner esses chefes entregam o ponto.

Tem um ganho que não é óbvio: essa divisão também é a **menos arriscada**. A run
das três travas cai no Beginner, que é onde um erro custa menos. A aba **Builds
& Chefes** traz o bloco *Sobreviver no Proud* para quem começa direto nele.

A alternativa (*Versão tranquila*) inverte: 100% no Beginner e a cronometrada no
Proud — o que significa correr contra o relógio, sem Continue e sem trocar
equipamento, com os inimigos batendo forte.

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
