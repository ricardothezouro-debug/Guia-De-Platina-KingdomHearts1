"""Página do guia: 5 abas, com a VISITA como unidade central."""
from __future__ import annotations

import html
import json
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QFileDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMessageBox, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout, QWidget,
)

from . import guide_data
from . import progress as keys
from .image_loader import ImageLoader
from .paths import guide_dir_label
from .storage import load_progress, load_ui, save_progress, save_ui
from .topbar import InfoCorner, TopBar

_PHOTO_W = 560
_PHOTO_H = 316
_IMG_TIMEOUT_MS = 26000
_SEARCH_LIMIT = 18

# Cores de tier da convenção da aba Platinas (GUIA_DE_PLATINA.md, seção 2).
_TIER_COLORS = {
    "bronze": "#CD7F32", "prata": "#C0C0C0", "ouro": "#FFD700", "platina": "#E5E4E2",
}
# o tipo da visita: história é obrigatória, limpeza é a fase de 100% da Run 2
_KIND_COLORS = {
    "história": "#E7C64A", "opcional": "#A8B0BC",
    "limpeza": "#B9FF43", "final": "#F87171",
}
# a etiqueta de cada passo — vermelho é o que você não pode deixar passar
_TAG_COLORS = {
    "missable": "#F87171", "chefe": "#FF9E64", "baú": "#E7C64A",
    "coletável": "#E7C64A", "troféu": "#7FE7FF", "build": "#B9FF43",
    "minijogo": "#C4A7FF", "puzzle": "#C4A7FF", "farm": "#B9FF43",
    "100%": "#7FE7FF", "gummi": "#7FE7FF",
}
_TRINITY_COLORS = {
    "Azul": "#7FE7FF", "Vermelha": "#F87171", "Verde": "#B9FF43",
    "Amarela": "#E7C64A", "Branca": "#F3F6FF",
}

_PROGRESS_QSS = (
    "QProgressBar{background:#0B111A;border:1px solid #273140;border-radius:9px;"
    "min-height:18px;text-align:center;color:#F3F6FF;font-weight:600}"
    "QProgressBar::chunk{border-radius:8px;background:qlineargradient(x1:0,y1:0,x2:1,y2:0,"
    "stop:0 #37F2FF,stop:0.5 #B9FF43,stop:1 #FF4FD8)}"
)
_NAV_QSS = (
    "QPushButton#NavButton{background:#0D121B;border:1px solid #273140;border-radius:8px;"
    "padding:7px 10px;color:#A8B0BC;text-align:left}"
    "QPushButton#NavButton:hover{border-color:#3C4A5C;color:#F3F6FF}"
    "QPushButton#NavButton:checked{background:#101922;border-color:%s;color:#F3F6FF;"
    "font-weight:600}" % guide_data.ACCENT
)
# o bloco de um passo dentro do card da visita
_ITEM_QSS = (
    "QFrame#ItemBlock{background:#0B111A;border:1px solid #1E2733;border-radius:8px}"
)


def _norm(text) -> str:
    stripped = unicodedata.normalize("NFD", str(text or ""))
    return "".join(c for c in stripped if not unicodedata.combining(c)).lower()


def _esc(text) -> str:
    return html.escape(str(text or ""))


def _flat(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return " ".join(_flat(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return " ".join(_flat(v) for v in value)
    return str(value)


def _label(text: str, object_name: str = "", wrap: bool = True) -> QLabel:
    label = QLabel(str(text or ""))
    if object_name:
        label.setObjectName(object_name)
    label.setWordWrap(wrap)
    label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    return label


def _link(text: str, url: str) -> QLabel:
    label = QLabel(f'<a href="{_esc(url)}" style="color:{guide_data.ACCENT}">{_esc(text)}</a>')
    label.setOpenExternalLinks(True)
    label.setWordWrap(True)
    return label


def _card() -> tuple[QFrame, QVBoxLayout]:
    frame = QFrame()
    frame.setObjectName("NeonPanel")
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(14, 12, 14, 12)
    layout.setSpacing(6)
    return frame, layout


def _notice(text: str, tone: str = "info") -> QFrame:
    frame = QFrame()
    frame.setObjectName("NeonPanel")
    color = "#F87171" if tone == "red" else guide_data.ACCENT
    frame.setStyleSheet(
        "QFrame{background:#0D121B;border:1px solid #273140;"
        "border-left:3px solid %s;border-radius:10px}" % color)
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(14, 11, 14, 11)
    layout.addWidget(_label(text, "Muted"))
    return frame


def _pill(text: str) -> QLabel:
    label = QLabel(str(text or ""))
    label.setObjectName("StatusPill")
    label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
    return label


def _tag(text: str, color: str) -> QLabel:
    label = QLabel(str(text or "").upper())
    label.setStyleSheet(f"color:{color};font-weight:700;font-size:11px;")
    label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
    return label


def _detail(layout: QVBoxLayout, title: str, value: str) -> None:
    if not value:
        return
    row = QLabel(f"<b>{_esc(title)}:</b> {_esc(value)}")
    row.setObjectName("Muted")
    row.setWordWrap(True)
    row.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    layout.addWidget(row)


def _scroll_page(build_content) -> QWidget:
    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(0, 0, 10, 0)
    layout.setSpacing(12)
    build_content(layout)
    layout.addStretch(1)

    scroll = QScrollArea()
    scroll.setObjectName("PageScroll")
    scroll.setWidgetResizable(True)
    scroll.setFrameShape(QFrame.Shape.NoFrame)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll.setWidget(container)
    return scroll


class GuidePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._done = load_progress()
        self._image_loader = ImageLoader(self)
        self._boxes: dict[str, list[QCheckBox]] = {}
        self._built: set[int] = set()
        self._visit_rows: list[tuple[QWidget, str, str, int]] = []
        self._trophy_rows: list[tuple[QWidget, str, str]] = []
        self._collect_rows: list[tuple[QWidget, str, str]] = []
        self._section_index = {s["key"]: i for i, s in enumerate(guide_data.SECTIONS)}

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 22, 0)
        outer.setSpacing(12)
        self._build_header(outer)
        self._build_progress(outer)
        self._build_nav(outer)
        self.top = TopBar(
            self, title=self._title_box, header=self._header_box,
            progress=self._progress_box, nav=self._nav_box, bar=self.progress,
            pills=self._progress_pills, load_ui=load_ui, save_ui=save_ui)
        outer.addWidget(self.top.widget)

        self.stack = QStackedWidget()
        self._holders: list[QVBoxLayout] = []
        for _section in guide_data.SECTIONS:
            placeholder = QWidget()
            holder = QVBoxLayout(placeholder)
            holder.setContentsMargins(0, 0, 0, 0)
            holder.addWidget(_label("Carregando…", "Muted"))
            holder.addStretch(1)
            self._holders.append(holder)
            self.stack.addWidget(placeholder)
        self.stack.currentChanged.connect(self._ensure_built)
        outer.addWidget(self.stack, 1)
        # O caminho é montado na hora: cada sistema guarda numa pasta diferente,
        # e escrever "%APPDATA%" mentiria para quem está no Mac.
        outer.addWidget(InfoCorner(
            f"{guide_data.FOOTER} • progresso salvo em {guide_dir_label()}"))

        self._update_progress()
        # Constrói a primeira aba só depois que o event loop girar, para que
        # build_page() retorne instantaneamente (regra 2 do padrão de plugins).
        QTimer.singleShot(0, lambda: self._ensure_built(0))

        # Downloads em andamento precisam ser encerrados antes que o Qt destrua
        # a página (fechar o app ou atualizar o plugin), senão o processo aborta.
        app = QApplication.instance()
        if app is not None:
            app.aboutToQuit.connect(self._image_loader.shutdown)

    def closeEvent(self, event):  # noqa: N802 (assinatura do Qt)
        self._image_loader.shutdown()
        super().closeEvent(event)

    def hideEvent(self, event):  # noqa: N802 (assinatura do Qt)
        if self.window() is not None and self.window().isHidden():
            self._image_loader.shutdown()
        super().hideEvent(event)

    # ------------------------------------------------------------------ topo
    def _build_header(self, outer: QVBoxLayout) -> None:
        """O topo tem três níveis (ver topbar.py). Aqui só se montam as peças:
        o título, e o bloco que some primeiro — abertura, números, busca e
        botões de progresso."""
        self._title_box = QWidget()
        title_row = QHBoxLayout(self._title_box)
        title_row.setContentsMargins(0, 0, 0, 0)
        title_row.addWidget(_label(guide_data.GAME_NAME, "PageTitle", wrap=False), 1)

        self._header_box = QWidget()
        box = QVBoxLayout(self._header_box)
        box.setContentsMargins(0, 0, 0, 0)
        box.setSpacing(12)
        box.addWidget(_label(guide_data.INTRO, "Muted"))
        stats = QHBoxLayout()
        stats.setSpacing(8)
        for stat in guide_data.HERO_STATS:
            stats.addWidget(_pill(f"{stat['value']}  {stat['label']}"))
        stats.addStretch(1)
        box.addLayout(stats)
        self._build_search(box)
        self._build_toolbar(box)

    def _build_search(self, outer: QVBoxLayout) -> None:
        row = QHBoxLayout()
        row.setSpacing(8)
        self.global_search = QLineEdit()
        self.global_search.setPlaceholderText(
            "Buscar visita, passo, troféu, dálmata ou trinity... Ex.: Oogie, "
            "Glide, Ultima, Sephiroth, dálmata 61")
        self.global_search.textChanged.connect(self._global_search)
        clear = QPushButton("Limpar")
        clear.clicked.connect(lambda: self.global_search.setText(""))
        row.addWidget(self.global_search, 1)
        row.addWidget(clear, 0)
        outer.addLayout(row)

        self.results_box = QWidget()
        self.results_layout = QVBoxLayout(self.results_box)
        self.results_layout.setContentsMargins(0, 0, 0, 0)
        self.results_layout.setSpacing(6)
        self.results_box.hide()
        outer.addWidget(self.results_box)

    def _build_progress(self, outer: QVBoxLayout) -> None:
        self._progress_box = QWidget()
        row = QHBoxLayout(self._progress_box)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(8)
        self.progress = QProgressBar()
        self.progress.setStyleSheet(_PROGRESS_QSS)
        self.progress.setRange(0, max(1, len(keys.all_keys())))
        self.progress_label = _pill("")
        self.trophy_label = _pill("")
        self.puppy_label = _pill("")
        self.trinity_label = _pill("")
        row.addWidget(self.progress, 1)
        row.addWidget(self.progress_label, 0)
        row.addWidget(self.trophy_label, 0)
        row.addWidget(self.puppy_label, 0)
        row.addWidget(self.trinity_label, 0)
        self._progress_pills = [self.progress_label, self.trophy_label, self.puppy_label, self.trinity_label]

    def _build_toolbar(self, outer: QVBoxLayout) -> None:
        row = QHBoxLayout()
        row.setSpacing(8)
        for text, slot in (("Exportar progresso", self._export),
                           ("Importar progresso", self._import),
                           ("Resetar marcações", self._reset)):
            button = QPushButton(text)
            button.clicked.connect(slot)
            row.addWidget(button)
        row.addStretch(1)
        outer.addLayout(row)

    def _build_nav(self, outer: QVBoxLayout) -> None:
        holder = QWidget()
        holder.setStyleSheet(_NAV_QSS)
        grid = QGridLayout(holder)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(6)
        self._nav_buttons: list[QPushButton] = []
        for i, section in enumerate(guide_data.SECTIONS):
            button = QPushButton(f"{section['num']}  {section['nav']}")
            button.setObjectName("NavButton")
            button.setCheckable(True)
            button.setChecked(i == 0)
            button.clicked.connect(lambda _=False, index=i: self.show_section(index))
            grid.addWidget(button, 0, i)
            self._nav_buttons.append(button)
            grid.setColumnStretch(i, 1)
        self._nav_box = holder

    def show_section(self, index: int) -> None:
        for i, button in enumerate(self._nav_buttons):
            button.setChecked(i == index)
        self.stack.setCurrentIndex(index)

    # -------------------------------------------------------------- progresso
    def _checkbox(self, key: str, text: str = "") -> QCheckBox:
        box = QCheckBox(text)
        box.setChecked(key in self._done)
        box.toggled.connect(lambda checked, k=key: self._on_toggle(k, checked))
        self._boxes.setdefault(key, []).append(box)
        return box

    def _on_toggle(self, key: str, checked: bool) -> None:
        if checked:
            self._done.add(key)
        else:
            self._done.discard(key)
        for box in self._boxes.get(key, []):
            if box.isChecked() != checked:
                box.blockSignals(True)
                box.setChecked(checked)
                box.blockSignals(False)
        save_progress(self._done)
        self._update_progress()

    def _update_progress(self) -> None:
        all_keys = keys.all_keys()
        done = sum(1 for key in all_keys if key in self._done)
        percent = round(done / len(all_keys) * 100) if all_keys else 0
        self.progress.setValue(done)
        self.progress_label.setText(f"{done} / {len(all_keys)}  •  {percent}%")
        trophies = keys.trophy_keys()
        self.trophy_label.setText(
            f"{sum(1 for k in trophies if k in self._done)}/{len(trophies)} troféus")
        puppies = keys.puppy_keys()
        got = sum(1 for k in puppies if k in self._done)
        self.puppy_label.setText(f"{got * 3}/99 dálmatas")
        trinities = keys.trinity_keys()
        self.trinity_label.setText(
            f"{sum(1 for k in trinities if k in self._done)}/{len(trinities)} trinities")
        if hasattr(self, "top"):
            self.top.sync()

    def _refresh_boxes(self) -> None:
        for key, boxes in self._boxes.items():
            checked = key in self._done
            for box in boxes:
                box.blockSignals(True)
                box.setChecked(checked)
                box.blockSignals(False)
        self._update_progress()
        if self._trophy_rows:
            self._filter_trophies()
        if self._visit_rows:
            self._filter_visits()

    # ------------------------------------------------------ exportar/importar
    def _export(self) -> None:
        path, _ = QFileDialog.getSaveFileName(
            self, "Exportar progresso", "kh1-platina-progresso.json", "JSON (*.json)")
        if not path:
            return
        payload = {
            "guide": guide_data.GUIDE_ID, "version": 1,
            "exportedAt": datetime.now(timezone.utc).isoformat(),
            "state": {key: True for key in sorted(self._done)},
        }
        try:
            Path(path).write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                                  encoding="utf-8")
        except OSError as error:
            QMessageBox.warning(self, "Exportar", f"Não foi possível salvar: {error}")

    def _import(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Importar progresso", "", "JSON (*.json)")
        if not path:
            return
        try:
            raw = json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            QMessageBox.warning(self, "Importar", "Arquivo JSON inválido.")
            return
        state = raw.get("state", raw) if isinstance(raw, dict) else raw
        self._done = keys.normalize_imported(state)
        save_progress(self._done)
        self._refresh_boxes()

    def _reset(self) -> None:
        if QMessageBox.question(self, "Resetar",
                                "Apagar todas as marcações deste guia?") != \
                QMessageBox.StandardButton.Yes:
            return
        self._done = set()
        save_progress(self._done)
        self._refresh_boxes()

    # ------------------------------------------------------------- busca geral
    def _global_search(self) -> None:
        while self.results_layout.count():
            item = self.results_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        query = _norm(self.global_search.text()).strip()
        if len(query) < 2:
            self.results_box.hide()
            return

        hits: list[tuple[str, str, str, str, str]] = []
        for visit in guide_data.VISITS:
            if query in _norm(_flat(visit)):
                hits.append(("VISITA", visit["name"], visit["kind"],
                             visit["note"] or visit["run"], "route"))
        for trophy in guide_data.TROPHIES:
            if query in _norm(_flat(trophy)):
                hits.append(("TROFÉU", trophy["name"], trophy["tier"].upper(),
                             f"{trophy['requirement']} {trophy['shortcut']}", "trophies"))
        for puppy in guide_data.PUPPIES:
            if query in _norm(_flat(puppy)):
                hits.append(("DÁLMATAS", puppy["group"],
                             f"{puppy['world']} · {puppy['area']}",
                             puppy["where"], "collect"))
        for trinity in guide_data.TRINITIES:
            if query in _norm(_flat(trinity)):
                hits.append((f"TRINITY {trinity['color']}", f"#{trinity['num']}",
                             trinity["world"],
                             f"{trinity['where']} → {trinity['reward']}", "collect"))
        for boss in guide_data.BOSSES:
            if query in _norm(_flat(boss)):
                hits.append(("CHEFE", boss["name"], boss["level"],
                             boss["unlock"], "systems"))

        if not hits:
            self.results_layout.addWidget(
                _notice("Nada encontrado. Tente o nome de um mundo, chefe, troféu ou item."))
            self.results_box.show()
            return

        for kind, name, where, text, page in hits[:_SEARCH_LIMIT]:
            frame, layout = _card()
            head = QHBoxLayout()
            head.setSpacing(8)
            head.addWidget(_label(kind, "Kicker", wrap=False))
            head.addWidget(_label(f"<b>{_esc(name)}</b>", "SectionTitle"), 1)
            if where:
                head.addWidget(_pill(where))
            layout.addLayout(head)
            layout.addWidget(_label(text, "Muted"))
            go = QPushButton(
                f"Ir para “{guide_data.SECTIONS[self._section_index[page]]['nav']}”")
            go.clicked.connect(
                lambda _=False, target=page: self.show_section(self._section_index[target]))
            row = QHBoxLayout()
            row.addWidget(go)
            row.addStretch(1)
            layout.addLayout(row)
            self.results_layout.addWidget(frame)
        if len(hits) > _SEARCH_LIMIT:
            self.results_layout.addWidget(
                _label(f"…e mais {len(hits) - _SEARCH_LIMIT} resultado(s). Refine a busca.",
                       "Muted"))
        self.results_box.show()

    # ---------------------------------------------------------------- imagens
    def _add_image(self, layout, url: str, max_w: int = _PHOTO_W,
                   max_h: int = _PHOTO_H) -> None:
        if not url:
            return
        holder = QLabel("Carregando foto…")
        holder.setObjectName("Muted")
        layout.addWidget(holder)
        state = {"loaded": False}

        def show(pixmap: QPixmap) -> None:
            state["loaded"] = True
            holder.setText("")
            holder.setPixmap(pixmap.scaled(
                max_w, max_h, Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))

        cached = self._image_loader.load(url, show)
        if cached is not None:
            show(cached)
            return

        def timeout() -> None:
            if not state["loaded"]:
                holder.setText(
                    f'Foto indisponível offline — <a href="{_esc(url)}" '
                    f'style="color:{guide_data.ACCENT}">abrir no navegador</a>')
                holder.setOpenExternalLinks(True)

        QTimer.singleShot(_IMG_TIMEOUT_MS, timeout)

    # ------------------------------------------------------- construção lazy
    def _ensure_built(self, index: int) -> None:
        if index in self._built or index < 0:
            return
        self._built.add(index)
        holder = self._holders[index]
        # Troca o "Carregando…" pelo conteúdo real. Esvaziar o layout (em vez de
        # trocar a página do QStackedWidget) evita depender de deleteLater().
        while holder.count():
            item = holder.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
        builder = getattr(self, f"_build_{guide_data.SECTIONS[index]['key']}")
        holder.addWidget(_scroll_page(lambda layout: self._with_header(layout, index, builder)))
        self._update_progress()

    def _with_header(self, layout: QVBoxLayout, index: int, builder) -> None:
        section = guide_data.SECTIONS[index]
        layout.addWidget(_label(section["eyebrow"], "Kicker", wrap=False))
        layout.addWidget(_label(section["title"], "CardTitle"))
        layout.addWidget(_label(section["lead"], "Muted"))
        for notice in section["notices"]:
            layout.addWidget(_notice(notice["text"], notice["tone"]))
        builder(layout)

    # ═══════════════════════════════════════════════════════ 01 Rota
    def _build_route(self, layout: QVBoxLayout) -> None:
        filters = QHBoxLayout()
        filters.setSpacing(8)
        self.visit_search = QLineEdit()
        self.visit_search.setPlaceholderText(
            "Buscar parada, passo ou coletável dela... Ex.: Oogie, dálmatas 58, Lady Luck")
        self.visit_search.textChanged.connect(self._filter_visits)
        self.visit_world = QComboBox()
        self.visit_world.addItem("Todos os mundos", "")
        for world in dict.fromkeys(v["world"] for v in guide_data.VISITS):
            self.visit_world.addItem(world, world)
        self.visit_world.currentIndexChanged.connect(self._filter_visits)
        self.visit_pending = QCheckBox("só pendentes")
        self.visit_pending.toggled.connect(self._filter_visits)
        filters.addWidget(self.visit_search, 1)
        filters.addWidget(self.visit_world, 0)
        filters.addWidget(self.visit_pending, 0)
        layout.addLayout(filters)

        self.visit_empty = _label("Nenhuma parada corresponde ao filtro.", "Muted")
        self.visit_empty.hide()
        layout.addWidget(self.visit_empty)

        # Uma lista só, numerada, na ordem de jogo. Sem agrupar por mundo: a
        # ordem É a informação — Traverse Town aparece seis vezes porque você
        # volta lá seis vezes, e cada volta libera coisas diferentes.
        for i, visit in enumerate(guide_data.VISITS):
            card = self._visit_card(i, visit)
            layout.addWidget(card)
            haystack = _norm(" ".join([
                _flat(visit),
                " ".join(_flat(item) for _, _, _, item in keys.items_of(visit)),
            ]))
            self._visit_rows.append((card, haystack, visit["world"], i))

    def _visit_card(self, index: int, visit: dict) -> QFrame:
        frame, card = _card()
        head = QHBoxLayout()
        head.setSpacing(8)
        head.addWidget(self._checkbox(keys.visit_key(index)), 0, Qt.AlignmentFlag.AlignTop)
        head.addWidget(_label(f"{index + 1:02d}", "Kicker", wrap=False), 0)
        head.addWidget(_tag(visit["kind"], _KIND_COLORS.get(visit["kind"], "#A8B0BC")), 0,
                       Qt.AlignmentFlag.AlignTop)
        principal = visit["kind"] in ("história", "final")
        title = ("★ " if principal else "") + visit["name"]
        head.addWidget(_label(title, "SectionTitle"), 1)
        if visit["level"] and visit["level"] != "—":
            head.addWidget(_pill(visit["level"]), 0, Qt.AlignmentFlag.AlignTop)
        head.addWidget(_pill(visit["run"]), 0, Qt.AlignmentFlag.AlignTop)
        card.addLayout(head)

        if visit["note"]:
            card.addWidget(_notice(visit["note"],
                                   "red" if visit["kind"] == "final" else "info"))
        if visit["trophies"]:
            _detail(card, "Troféus aqui", ", ".join(visit["trophies"]))

        steps = visit["steps"]
        card.addWidget(_label(f"<b>Passo a passo ({len(steps)}):</b>", "Muted"))
        for j, step in enumerate(steps):
            card.addWidget(self._step_block(index, j, step))

        # Os coletáveis que dá para pegar NESTA ida, com a mesma chave da aba
        # Coletáveis — marcar aqui marca lá.
        items = keys.items_of(visit)
        if items:
            card.addWidget(_label(
                f"<b>Coletáveis desta parada ({len(items)}):</b>", "Muted"))
            for kind, key, _i, item in items:
                card.addWidget(self._route_item_block(kind, key, item))
        return frame

    def _route_item_block(self, kind: str, key: str, item: dict) -> QFrame:
        if kind == "puppy":
            return self._collect_block(
                key, f"Dálmatas {item['group']}", item["area"], item["where"],
                item["image"], "#E7C64A", "dálmatas")
        if kind == "trinity":
            return self._collect_block(
                key, f"Trinity {item['color']} #{item['num']}", "",
                f"{item['where']}  →  {item['reward']}", item["image"],
                _TRINITY_COLORS.get(item["color"], "#A8B0BC"), item["color"])
        if kind == "postcard":
            return self._collect_block(
                key, item["num"], item["prize"], item["where"], item["image"],
                "#7FE7FF", "postal")
        return self._collect_block(
            key, f"Torn {item['num']}", item["world"], item["where"], item["image"],
            "#C4A7FF", "página")

    def _step_block(self, visit_index: int, step_index: int, step: dict) -> QFrame:
        frame = QFrame()
        frame.setObjectName("ItemBlock")
        frame.setStyleSheet(_ITEM_QSS)
        box = QVBoxLayout(frame)
        box.setContentsMargins(11, 9, 11, 9)
        box.setSpacing(5)
        head = QHBoxLayout()
        head.setSpacing(8)
        head.addWidget(self._checkbox(keys.step_key(visit_index, step_index)), 0,
                       Qt.AlignmentFlag.AlignTop)
        head.addWidget(_label(f"{step_index + 1}", "Kicker", wrap=False), 0)
        head.addWidget(_label(step["title"], "SectionTitle"), 1)
        tag = str(step.get("tag") or "")
        if tag:
            head.addWidget(_tag(tag, _TAG_COLORS.get(tag, "#A8B0BC")), 0,
                           Qt.AlignmentFlag.AlignTop)
        box.addLayout(head)
        box.addWidget(_label(step["do"], "Muted"))
        self._add_image(box, step.get("image", ""))
        return frame

    def _filter_visits(self) -> None:
        query = _norm(self.visit_search.text()).strip()
        world = self.visit_world.currentData() or ""
        pending = self.visit_pending.isChecked()
        visible = 0
        for frame, haystack, row_world, index in self._visit_rows:
            done = keys.visit_key(index) in self._done
            show = (query in haystack and (not world or row_world == world)
                    and (not pending or not done))
            frame.setVisible(show)
            visible += int(show)
        self.visit_empty.setVisible(visible == 0)

    # ═══════════════════════════════════════════════════════ 02 Troféus
    def _build_trophies(self, layout: QVBoxLayout) -> None:
        filters = QHBoxLayout()
        filters.setSpacing(8)
        self.trophy_search = QLineEdit()
        self.trophy_search.setPlaceholderText("Buscar troféu ou requisito...")
        self.trophy_search.textChanged.connect(self._filter_trophies)
        self.trophy_tier = QComboBox()
        self.trophy_tier.addItem("Todos os tiers", "")
        for tier in ("platina", "ouro", "prata", "bronze"):
            self.trophy_tier.addItem(tier.capitalize(), tier)
        self.trophy_tier.currentIndexChanged.connect(self._filter_trophies)
        self.trophy_pending = QCheckBox("só pendentes")
        self.trophy_pending.toggled.connect(self._filter_trophies)
        filters.addWidget(self.trophy_search, 1)
        filters.addWidget(self.trophy_tier, 0)
        filters.addWidget(self.trophy_pending, 0)
        layout.addLayout(filters)

        self.trophy_empty = _label("Nenhum troféu corresponde ao filtro.", "Muted")
        self.trophy_empty.hide()
        layout.addWidget(self.trophy_empty)

        for trophy in guide_data.TROPHIES:
            frame, card = _card()
            head = QHBoxLayout()
            head.setSpacing(10)
            head.addWidget(self._checkbox(keys.trophy_key(trophy["id"])), 0,
                           Qt.AlignmentFlag.AlignTop)
            head.addWidget(_label(trophy["name"], "SectionTitle"), 1)
            head.addWidget(_tag(trophy["tier"], _TIER_COLORS.get(trophy["tier"], "#A8B0BC")),
                           0, Qt.AlignmentFlag.AlignTop)
            card.addLayout(head)
            _detail(card, "Requisito", trophy["requirement"])
            _detail(card, "Como fazer", trophy["shortcut"])
            layout.addWidget(frame)
            self._trophy_rows.append((frame, _norm(_flat(trophy)), trophy["id"]))

    def _filter_trophies(self) -> None:
        query = _norm(self.trophy_search.text()).strip()
        tier = self.trophy_tier.currentData() or ""
        pending = self.trophy_pending.isChecked()
        visible = 0
        for (frame, haystack, trophy_id), trophy in zip(self._trophy_rows,
                                                        guide_data.TROPHIES):
            got = keys.trophy_key(trophy_id) in self._done
            show = (query in haystack and (not tier or trophy["tier"] == tier)
                    and (not pending or not got))
            frame.setVisible(show)
            visible += int(show)
        self.trophy_empty.setVisible(visible == 0)

    # ═══════════════════════════════════════════════════════ 03 Coletáveis
    def _build_collect(self, layout: QVBoxLayout) -> None:
        filters = QHBoxLayout()
        filters.setSpacing(8)
        self.collect_search = QLineEdit()
        self.collect_search.setPlaceholderText(
            "Buscar por mundo, área ou item... Ex.: Monstro, Glide, Orichalcum")
        self.collect_search.textChanged.connect(self._filter_collect)
        self.collect_pending = QCheckBox("só pendentes")
        self.collect_pending.toggled.connect(self._filter_collect)
        filters.addWidget(self.collect_search, 1)
        filters.addWidget(self.collect_pending, 0)
        layout.addLayout(filters)

        self.collect_empty = _label("Nada corresponde ao filtro.", "Muted")
        self.collect_empty.hide()
        layout.addWidget(self.collect_empty)

        # ── 99 dálmatas
        layout.addWidget(_label("Os 99 dálmatas — 33 baús de 3 filhotes", "CardTitle"))
        prizes = " · ".join(f"{r['count']}: {r['prize']}" for r in guide_data.PUPPY_REWARDS)
        layout.addWidget(_notice(
            "Prêmios do Pongo e da Perdita conforme você devolve — " + prizes))
        for i, puppy in enumerate(guide_data.PUPPIES):
            frame = self._collect_block(
                keys.puppy_key(i), puppy["group"],
                f"{puppy['world']} · {puppy['area']}", puppy["where"],
                puppy["image"], "#E7C64A", "dálmatas")
            layout.addWidget(frame)
            self._collect_rows.append((frame, _norm(_flat(puppy)), keys.puppy_key(i)))

        # ── 46 trinities
        layout.addWidget(_label("As 46 trinities", "CardTitle"))
        layout.addWidget(_notice(
            "As cores vão abrindo com a história: Azul desde o começo, Vermelha "
            "depois da Selva Profunda, Verde depois de Agrabah, Amarela com a "
            "trinity do Coliseu e Branca só depois de vencer o Riku no Hollow "
            "Bastion. Trinity precisa de Donald E Goofy na equipe."))
        for i, trinity in enumerate(guide_data.TRINITIES):
            frame = self._collect_block(
                keys.trinity_key(i), f"Trinity {trinity['color']} #{trinity['num']}",
                trinity["world"],
                f"{trinity['where']}  →  {trinity['reward']}",
                trinity["image"],
                _TRINITY_COLORS.get(trinity["color"], "#A8B0BC"), trinity["color"])
            layout.addWidget(frame)
            self._collect_rows.append((frame, _norm(_flat(trinity)), keys.trinity_key(i)))

        # ── 5 Torn Pages
        layout.addWidget(_label("As 5 Torn Pages", "CardTitle"))
        for i, page in enumerate(guide_data.PAGES):
            frame = self._collect_block(
                keys.page_key(i), page["num"], page["world"], page["where"],
                page["image"], "#C4A7FF", "página")
            layout.addWidget(frame)
            self._collect_rows.append((frame, _norm(_flat(page)), keys.page_key(i)))

        # ── 10 postais
        layout.addWidget(_label("Os 10 postais (todos na Cidade do Trânsito)", "CardTitle"))
        layout.addWidget(_notice(
            "Deposite cada postal na caixa de correio do 1º Distrito para "
            "receber o prêmio. Vários deles são Mythril e Orichalcum, que a "
            "síntese consome."))
        for i, card_item in enumerate(guide_data.POSTCARDS):
            frame = self._collect_block(
                keys.postcard_key(i), card_item["num"], card_item["prize"],
                card_item["where"], card_item["image"], "#7FE7FF", "postal")
            layout.addWidget(frame)
            self._collect_rows.append(
                (frame, _norm(_flat(card_item)), keys.postcard_key(i)))

        # ── 13 relatórios
        layout.addWidget(_label("Os 13 Relatórios do Ansem", "CardTitle"))
        for i, report in enumerate(guide_data.REPORTS):
            frame = self._collect_block(
                keys.report_key(i), report["num"], "", report["how"], "",
                "#B8C0CC", "relatório")
            layout.addWidget(frame)
            self._collect_rows.append((frame, _norm(_flat(report)), keys.report_key(i)))

        # ── materiais da Ultima
        layout.addWidget(_label("Os materiais raros da Ultima Weapon", "CardTitle"))
        for i, material in enumerate(guide_data.MATERIALS):
            frame = self._collect_block(
                keys.material_key(i), material["name"], "", material["how"], "",
                "#B9FF43", "síntese")
            layout.addWidget(frame)
            self._collect_rows.append((frame, _norm(_flat(material)), keys.material_key(i)))

    def _collect_block(self, key: str, name: str, where: str, text: str,
                       image: str, color: str, kind: str) -> QFrame:
        frame = QFrame()
        frame.setObjectName("ItemBlock")
        frame.setStyleSheet(_ITEM_QSS)
        box = QVBoxLayout(frame)
        box.setContentsMargins(11, 9, 11, 9)
        box.setSpacing(5)
        head = QHBoxLayout()
        head.setSpacing(8)
        head.addWidget(self._checkbox(key), 0, Qt.AlignmentFlag.AlignTop)
        head.addWidget(_tag(kind, color), 0, Qt.AlignmentFlag.AlignTop)
        head.addWidget(_label(name, "SectionTitle"), 1)
        if where:
            head.addWidget(_pill(where), 0, Qt.AlignmentFlag.AlignTop)
        box.addLayout(head)
        box.addWidget(_label(text, "Muted"))
        self._add_image(box, image)
        return frame

    def _filter_collect(self) -> None:
        query = _norm(self.collect_search.text()).strip()
        pending = self.collect_pending.isChecked()
        visible = 0
        for frame, haystack, key in self._collect_rows:
            got = key in self._done
            show = query in haystack and (not pending or not got)
            frame.setVisible(show)
            visible += int(show)
        self.collect_empty.setVisible(visible == 0)

    # ═══════════════════════════════════════════════════════ 04 Builds & Chefes
    def _build_systems(self, layout: QVBoxLayout) -> None:
        layout.addWidget(_label("Como a platina se divide", "CardTitle"))
        for item in guide_data.PLAN:
            frame, card = _card()
            head = QHBoxLayout()
            head.setSpacing(8)
            head.addWidget(_label(item["name"], "SectionTitle"), 1)
            head.addWidget(_pill(item["when"]), 0, Qt.AlignmentFlag.AlignTop)
            card.addLayout(head)
            card.addWidget(_label(item["why"], "Muted"))
            _detail(card, "Entrega", item["gets"])
            layout.addWidget(frame)

        layout.addWidget(_label("Sobreviver no Proud desde a primeira run", "CardTitle"))
        layout.addWidget(_notice(
            "A Versão gamox começa no Proud sem você conhecer o jogo. Estes sete "
            "pontos são o que separa uma run dura de uma run travada — marque "
            "conforme cada um vira hábito.", "red"))
        for i, item in enumerate(guide_data.PROUD):
            frame, card = _card()
            head = QHBoxLayout()
            head.setSpacing(8)
            head.addWidget(self._checkbox(keys.proud_key(i)), 0, Qt.AlignmentFlag.AlignTop)
            head.addWidget(_label(item["name"], "SectionTitle"), 1)
            head.addWidget(_pill(item["when"]), 0, Qt.AlignmentFlag.AlignTop)
            card.addLayout(head)
            _detail(card, "Por quê", item["why"])
            layout.addWidget(frame)

        layout.addWidget(_label("Hábitos que decidem cada run", "CardTitle"))
        for i, item in enumerate(guide_data.PREP):
            frame, card = _card()
            head = QHBoxLayout()
            head.setSpacing(8)
            head.addWidget(self._checkbox(keys.prep_key(i)), 0, Qt.AlignmentFlag.AlignTop)
            head.addWidget(_label(item["name"], "SectionTitle"), 1)
            head.addWidget(_pill(item["when"]), 0, Qt.AlignmentFlag.AlignTop)
            card.addLayout(head)
            _detail(card, "Por quê", item["why"])
            layout.addWidget(frame)

        layout.addWidget(_label("Os cinco chefes opcionais", "CardTitle"))
        layout.addWidget(_notice(
            "Todos são da Run 2. Três deles (Kurt Zisa, Phantom e Sephiroth) só "
            "abrem depois do primeiro episódio do Hollow Bastion; o Unknown "
            "exige que você entre no Fim do Mundo e veja a primeira cena antes."))
        for i, boss in enumerate(guide_data.BOSSES):
            frame, card = _card()
            head = QHBoxLayout()
            head.setSpacing(8)
            head.addWidget(self._checkbox(keys.boss_key(i)), 0, Qt.AlignmentFlag.AlignTop)
            head.addWidget(_label(boss["name"], "SectionTitle"), 1)
            head.addWidget(_pill(boss["level"]), 0, Qt.AlignmentFlag.AlignTop)
            card.addLayout(head)
            _detail(card, "Onde", boss["where"])
            _detail(card, "Como abrir", boss["unlock"])
            _detail(card, "Build", boss["build"])
            _detail(card, "Estratégia", boss["how"])
            _detail(card, "Prêmio", boss["reward"])
            layout.addWidget(frame)

    # ═══════════════════════════════════════════════════════ 05 Fontes
    def _build_sources(self, layout: QVBoxLayout) -> None:
        for source in guide_data.SOURCES:
            frame, card = _card()
            card.addWidget(_label(source["title"], "SectionTitle"))
            card.addWidget(_label(source["note"], "Muted"))
            card.addWidget(_link("Abrir fonte ↗", source["url"]))
            layout.addWidget(frame)
