# импорт библиотек 
import tkinter as tk
from tkinter import ttk, messagebox
import random
# определение используемой темы (ака попытка dark academia)
THEME = {
    'colors': {
        'bg_main': '#1a1a2e',
        'bg_secondary': '#16213e',
        'bg_accent': '#0f3460',
        'text_light': '#f5e8c7',
        'text_gold': '#d4af37',
        'button_brown': '#5c4033',
    },
    'fonts': {
        'title': ('Georgia', 22, 'bold'),
        'heading': ('Palatino Linotype', 15, 'bold'),
        'body': ('Book Antiqua', 11),
        'small': ('Times New Roman', 10),
    }
}
# создание БД по книгам, с представленными характеристиками 
BOOKS = [
    {
        'id': 1,
        'title': 'Преступление и наказание',
        'author': 'Фёдор Достоевский',
        'year': 1866,
        'trauma': 'Чувство вины, самобичевание, кризис личности',
        'description': 'Пугает ответственность? Почитайте про убийство старухи-процентщицы — ваши проблемы покажутся мелочью!',
        'quote': 'Он, ну хоть немного, да порядочный человек... ну, так чем же тут гордиться, что порядочный человек? Всякий должен быть порядочный человек.'
    },
    {
        'id': 2,
        'title': 'Хребты безумия',
        'author': 'Говард Филлипс Лавкрафт',
        'year': 1936,
        'trauma': 'Давление, паранойя, мнительность',
        'description': 'Вам кажется, что кто-то постоянно контролирует ваши действия? Родители всегда говорили, что делать? Интересно.',
        'quote': 'Как и большинство молодых людей, он с упоением лелеял планы мести, триумфа и великодушного прощения в финале.'
    },
    {
        'id': 3,
        'title': 'Волшебная гора',
        'author': 'Томас Манн',
        'year': 1924,
        'trauma': 'Страх Самое себя, непринятие, цинизм',
        'description': 'Пытаетесь найти себя среди всех этих "лицемеров" вокруг? Предупреждение: может усилить ваш экзистенциальный кризис.',
        'quote': 'Злость, сударь мой, это душа критики, а критика – источник развития и просвещения..'
    },
    {
        'id': 4,
        'title': 'Петербург',
        'author': 'Андрей Белый',
        'year': 1913,
        'trauma': 'Экзистенциальный кризис, абсурд',
        'description': 'Жизнь кажется бессмысленной? Переезжайте в Петербург! Ваша бессмысленность - ничто.',
        'quote': 'Весь Петербург - бесконечность проспекта, возведенного в энную степень. За Петербургом же - ничего нет.'
    },
    {
        'id': 5,
        'title': 'Демиан',
        'author': 'Герман Гессе',
        'year': 1919,
        'trauma': 'Потеря, меланхолия, ностальгия',
        'description': 'У вас когда-был близкий друг? Вы уверены?',
        'quote': 'Моя история... отдает бессмыслицей и душевной смутой, безумием и бредом, как жизнь всех, кто уже не хочет обманываться.'
    },
    {
        'id': 6,
        'title': 'О мышах и людях',
        'author': 'Джон Стейнбек',
        'year': 1937,
        'trauma': 'Наивность, недопонимание, страх',
        'description': 'Взрослый мир кажется таким пугающим, правда?',
        'quote': 'У нас люди редко друг друга держатся, – сказал он задумчиво. – Не знаю почему. Может, в этом проклятом мире все боятся друг друга.'
    }
]
# кортежи с вопросами
QUESTIONS = [
    ("В детстве вы часто чувствовали себя одиноким?",
     ["Никогда", "Иногда", "Часто", "Я все еще одинок"]),
    ("Родители сравнивали вас с другими детьми?",
     ["Никогда", "Редко", "Часто", "Это была их любимая тема"]),
    ("В школе над вами смеялись и издевались?",
     ["Нет", "Иногда", "Да, регулярно", "Я - изгой"]),
    ("Вы боялись публично опозориться?",
     ["Нет", "Немного", "Очень", "До тошноты"]),
    ("Гордятся ли вами ваши родители?",
     ["Безусловно", "Думаю, что да", "Гордыня - грех", "Я - сплошное разочарование"]),
]
# основной класс програмы
class TraumaBookApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.answers = []
        self.create_interface()
    def setup_window(self):
        self.root.title("Trauma & Books • Литературная психотерапия")
        self.root.geometry("900x750")
        self.root.configure(bg=THEME['colors']['bg_main'])
        self.root.update_idletasks()
        width = 900
        height = 750
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    def create_interface(self):
        main_frame = tk.Frame(self.root, bg=THEME['colors']['bg_main'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.create_header(main_frame)
        content_frame = tk.Frame(main_frame, bg=THEME['colors']['bg_main'])
        content_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        self.create_questions_panel(content_frame)
        self.create_results_panel(content_frame)
        self.show_welcome()
    def create_header(self, parent): #чтобы было красиво - в верхней панельке
        tk.Frame(parent, height=2, bg=THEME['colors']['text_gold']).pack(fill=tk.X, pady=(0, 15))
        title_frame = tk.Frame(parent, bg=THEME['colors']['bg_main'])
        title_frame.pack()
        tk.Label(title_frame, text="✧˖°.", font=("Symbol", 18),
                 bg=THEME['colors']['bg_main'], fg=THEME['colors']['text_gold']).pack(side=tk.LEFT, padx=5)
        tk.Label(title_frame, text="TRAUMA & BOOKS", font=THEME['fonts']['title'],
                 bg=THEME['colors']['bg_main'], fg=THEME['colors']['text_light']).pack(side=tk.LEFT)
        tk.Label(title_frame, text="˖⁺‧₊☽", font=("Symbol", 18),
                 bg=THEME['colors']['bg_main'], fg=THEME['colors']['text_gold']).pack(side=tk.LEFT, padx=5)
        tk.Label(parent, text="Ваш личный литературный психотерапевт | 5 вопросов и Ваша рекомендация",
                 font=THEME['fonts']['small'], bg=THEME['colors']['bg_main'],
                 fg=THEME['colors']['text_gold']).pack(pady=5)
        tk.Frame(parent, height=1, bg=THEME['colors']['text_gold']).pack(fill=tk.X, pady=(10, 0))
    def create_questions_panel(self, parent):
        questions_frame = tk.Frame(parent, bg=THEME['colors']['bg_secondary'],
                                   relief=tk.RAISED, borderwidth=2)
        questions_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        panel_header = tk.Frame(questions_frame, bg=THEME['colors']['bg_accent'], height=40)
        panel_header.pack(fill=tk.X)
        panel_header.pack_propagate(False)
        tk.Label(panel_header, text=" Отвечайте честно на вопросы, мы вам обязательно поможем",
                 font=THEME['fonts']['heading'], bg=THEME['colors']['bg_accent'],
                 fg=THEME['colors']['text_light'], padx=15).pack(side=tk.LEFT)
        canvas = tk.Canvas(questions_frame, bg=THEME['colors']['bg_secondary'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(questions_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=THEME['colors']['bg_secondary'])
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True, padx=15, pady=15)
        scrollbar.pack(side="right", fill="y")
        self.answer_vars = []
        for i, (question, options) in enumerate(QUESTIONS):
            self.create_question(scrollable_frame, i + 1, question, options)
        self.create_control_buttons(questions_frame)
    def create_question(self, parent, number, question_text, options):
        q_frame = tk.Frame(parent, bg=THEME['colors']['bg_accent'],
                           relief=tk.SUNKEN, borderwidth=1, padx=15, pady=10)
        q_frame.pack(fill=tk.X, pady=8)
        tk.Label(q_frame, text=f"{number}.", font=THEME['fonts']['body'],
                 bg=THEME['colors']['bg_accent'], fg=THEME['colors']['text_gold'],
                 width=3).pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(q_frame, text=question_text, font=THEME['fonts']['body'],
                 bg=THEME['colors']['bg_accent'], fg=THEME['colors']['text_light'],
                 wraplength=250, justify=tk.LEFT).pack(side=tk.LEFT, fill=tk.X, expand=True)
        var = tk.StringVar(value=options[0])
        self.answer_vars.append(var)
        combo = ttk.Combobox(q_frame, textvariable=var, values=options,
                             state="readonly", width=18, font=THEME['fonts']['small'])
        combo.pack(side=tk.RIGHT, padx=(10, 0))
    def create_control_buttons(self, parent):
        button_frame = tk.Frame(parent, bg=THEME['colors']['bg_secondary'], pady=20)
        button_frame.pack(fill=tk.X, padx=15)
        button_style = {
            'font': THEME['fonts']['body'],
            'padx': 25,
            'pady': 10,
            'cursor': 'hand2',
            'borderwidth': 2,
            'relief': tk.RAISED
        }
        analyze_btn = tk.Button(button_frame, text="𖡼𖤣𖥧𖡼Диагностировать (5 ответов)",
                                command=self.analyze,
                                bg=THEME['colors']['button_brown'],
                                fg=THEME['colors']['text_light'], **button_style)
        analyze_btn.pack(fill=tk.X, pady=5)
        random_btn = tk.Button(button_frame, text="Случайный том 𖡼𖤣𖥧𖡼",
                               command=self.show_random_book,
                               bg=THEME['colors']['button_brown'],
                               fg=THEME['colors']['text_light'], **button_style)
        random_btn.pack(fill=tk.X, pady=5)
        reset_btn = tk.Button(button_frame, text="Очистить ответы ⩇⩇:⩇⩇",
                              command=self.reset_answers,
                              bg=THEME['colors']['button_brown'],
                              fg=THEME['colors']['text_light'], **button_style)
        reset_btn.pack(fill=tk.X, pady=5)
        for btn in [analyze_btn, random_btn, reset_btn]:
            self.add_hover_effect(btn)
    def add_hover_effect(self, button):
        original_color = button.cget('bg')
        def on_enter(e):
            button.config(bg=THEME['colors']['text_gold'], fg=THEME['colors']['bg_main'])
        def on_leave(e):
            button.config(bg=original_color, fg=THEME['colors']['text_light'])
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    def create_results_panel(self, parent):
        self.results_frame = tk.Frame(parent, bg=THEME['colors']['bg_main'])
        self.results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        results_header = tk.Frame(self.results_frame, bg=THEME['colors']['bg_accent'],
                                  height=40, relief=tk.RAISED, borderwidth=2)
        results_header.pack(fill=tk.X)
        results_header.pack_propagate(False)
        tk.Label(results_header, text="Вы готовы начать терапию", font=THEME['fonts']['heading'],
                 bg=THEME['colors']['bg_accent'], fg=THEME['colors']['text_light'],
                 padx=15).pack(side=tk.LEFT)

        self.results_canvas = tk.Canvas(self.results_frame, bg=THEME['colors']['bg_main'],
                                        highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical",
                                  command=self.results_canvas.yview)
        self.results_content = tk.Frame(self.results_canvas, bg=THEME['colors']['bg_main'])
        self.results_content.bind("<Configure>",
                                  lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all")))
        self.results_canvas.create_window((0, 0), window=self.results_content, anchor="nw")
        self.results_canvas.configure(yscrollcommand=scrollbar.set)
        self.results_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def show_welcome(self):
        self.clear_results()
        welcome_frame = tk.Frame(self.results_content, bg=THEME['colors']['bg_secondary'],
                                 relief=tk.RIDGE, borderwidth=3, padx=25, pady=30)
        welcome_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(welcome_frame, text="༄˖°.🍂.ೃ࿔*:･", font=("Segoe UI Emoji", 48),
                 bg=THEME['colors']['bg_secondary'], fg=THEME['colors']['text_gold']).pack(pady=(0, 20))

        welcome_text = """⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹.

Ответьте на 5 вопросов слева, чтобы получить терапевтическую литературную рекомендацию.

Как это работает:
1. Ответьте на 5 вопросов о ваших травмах
2. Получите оценку тяжести вашего переживаний
3. Узнайте, какая книга вам обязательно поможет"""

        tk.Label(welcome_frame, text=welcome_text, font=THEME['fonts']['body'],
                 bg=THEME['colors']['bg_secondary'], fg=THEME['colors']['text_light'],
                 justify=tk.CENTER, wraplength=350).pack(pady=10)
    def clear_results(self):
        for widget in self.results_content.winfo_children():
            widget.destroy()
    def analyze(self):
        for i, var in enumerate(self.answer_vars):
            if not var.get():
                messagebox.showwarning("Неполная анкета",
                                       f"Пожалуйста, ответьте на вопрос №{i + 1}!",
                                       parent=self.root)
                return
        answers = [var.get() for var in self.answer_vars]
        score = self.calculate_score(answers)

        if score >= 8:
            diagnosis = "Глубокие душевные раны"
            comment = f"Ваш показатель: {score}/10 баллов. Кажется, вам правда грустно."
            filtered_books = [b for b in BOOKS if b['id'] in [1, 4, 5]]
        elif score >= 4:
            diagnosis = "Меланхолия"
            comment = f"Ваш показатель: {score}/10 баллов. Типичная русская тоска."
            filtered_books = [b for b in BOOKS if b['id'] in [2, 3]]
        else:
            diagnosis = "Хандра"
            comment = f"Ваш показатель: {score}/10 баллов. Кажется, вы слишком счастливы."
            filtered_books = [b for b in BOOKS if b['id'] == 6]
        if not filtered_books:
            filtered_books = BOOKS
        book = random.choice(filtered_books)
        self.show_results(diagnosis, comment, book, score)

    def calculate_score(self, answers):
        score = 0
        for answer in answers:
            if answer in ["Часто", "Я все еще одинок", "Это была их любимая тема",
                          "Да, регулярно", "Я - изгой", "Очень",
                          "До тошноты", "Я - сплошное разочарование"]:
                score += 2
            elif answer in ["Иногда", "Редко", "Немного", "Думаю, что да", "Гордыня - грех"]:
                score += 1
        return score

    def show_results(self, diagnosis, comment, book, score):
        self.clear_results()
        main_frame = tk.Frame(self.results_content, bg=THEME['colors']['bg_main'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        diagnosis_frame = tk.Frame(main_frame, bg=THEME['colors']['bg_accent'],
                                   relief=tk.RAISED, borderwidth=2, padx=15, pady=15)
        diagnosis_frame.pack(fill=tk.X, pady=(0, 15))

        tk.Label(diagnosis_frame, text="Литературный диагноз",
                 font=THEME['fonts']['heading'], bg=THEME['colors']['bg_accent'],
                 fg=THEME['colors']['text_gold']).pack(anchor="w")

        tk.Label(diagnosis_frame, text=diagnosis, font=("Garamond", 16, "bold"),
                 bg=THEME['colors']['bg_accent'], fg=THEME['colors']['text_light']).pack(anchor="w", pady=(5, 0))
        tk.Label(diagnosis_frame, text=f"📊 Показатель: {score}/10 баллов",
                 font=THEME['fonts']['body'], bg=THEME['colors']['bg_accent'],
                 fg=THEME['colors']['text_gold']).pack(anchor="w", pady=(5, 0))
        tk.Label(diagnosis_frame, text=comment, font=THEME['fonts']['small'],
                 bg=THEME['colors']['bg_accent'], fg=THEME['colors']['text_light'],
                 wraplength=400).pack(anchor="w", pady=(10, 0))
        tk.Frame(main_frame, height=2, bg=THEME['colors']['text_gold']).pack(fill=tk.X, pady=10)
        book_frame = tk.Frame(main_frame, bg=THEME['colors']['bg_secondary'],
                              relief=tk.GROOVE, borderwidth=2, padx=20, pady=20)
        book_frame.pack(fill=tk.X)

        tk.Label(book_frame, text="Ваша литературная рекомендация", font=THEME['fonts']['heading'],
                 bg=THEME['colors']['bg_secondary'], fg=THEME['colors']['text_light']).pack(anchor="w", pady=(0, 15))
        tk.Label(book_frame, text=book['title'],
                 font=("Garamond", 16, "bold"), bg=THEME['colors']['bg_secondary'],
                 fg=THEME['colors']['text_gold'], wraplength=350).pack(anchor="w", pady=(0, 10))
        tk.Label(book_frame, text=f"{book['author']} ({book['year']})",
                 font=THEME['fonts']['body'], bg=THEME['colors']['bg_secondary'],
                 fg=THEME['colors']['text_light']).pack(anchor="w", pady=5)
        tk.Label(book_frame, text=f"Подходит при: {book['trauma']}",
                 font=THEME['fonts']['small'], bg=THEME['colors']['bg_secondary'],
                 fg=THEME['colors']['text_light']).pack(anchor="w", pady=5)
        tk.Label(book_frame, text="Описание:", font=THEME['fonts']['small'],
                 bg=THEME['colors']['bg_secondary'], fg=THEME['colors']['text_gold']).pack(anchor="w", pady=(15, 5))
        tk.Label(book_frame, text=book['description'], font=THEME['fonts']['small'],
                 bg=THEME['colors']['bg_secondary'], fg=THEME['colors']['text_light'],
                 wraplength=350, justify=tk.LEFT).pack(anchor="w", pady=(0, 15))

        if 'quote' in book and book['quote']:
            quote_frame = tk.Frame(book_frame, bg=THEME['colors']['bg_accent'],
                                   padx=15, pady=12)
            quote_frame.pack(fill=tk.X, pady=(10, 0))
            tk.Label(quote_frame, text=f"«{book['quote']}»",
                     font=("Courier New", 10, "italic"), bg=THEME['colors']['bg_accent'],
                     fg=THEME['colors']['text_light'], wraplength=350,
                     justify=tk.CENTER).pack()

        button_frame = tk.Frame(main_frame, bg=THEME['colors']['bg_main'])
        button_frame.pack(pady=20)

        new_trauma_btn = tk.Button(button_frame, text="Новая травма (5 вопросов)⋆.ೃ࿔*:･",
                                   command=self.analyze,
                                   bg=THEME['colors']['button_brown'],
                                   fg=THEME['colors']['text_light'],
                                   font=THEME['fonts']['body'],
                                   padx=20, pady=8, cursor="hand2")
        new_trauma_btn.pack()

        self.add_hover_effect(new_trauma_btn)

    def show_random_book(self):
        book = random.choice(BOOKS)
        self.show_results(
            "Случайный выбор",
            "Классика сама выбрала вас. Это знак.",
            book,
            "?"
        )

    def reset_answers(self):
        for i, var in enumerate(self.answer_vars):
            var.set(QUESTIONS[i][1][0])
        self.show_welcome()
        messagebox.showinfo("Сброс",
                            "Все ответы очищены. Готовы к новому сеансу литературной психотерапии? ",
                            parent=self.root)

def main():
    root = tk.Tk()
    app = TraumaBookApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
