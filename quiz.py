import csv
import random
import time
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import RoundedRectangle
from kivy.core.window import Window


class QuizApp(App):
    def build(self):
        self.questions = []
        self.current_question_index = 0
        self.num_correct = 0
        self.timer = 0
        self.load_questions()

        LabelBase.register("B612 Mono", fn_regular="B612Mono-Regular.ttf")

        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)
        top_layout = BoxLayout(orientation="vertical", size_hint=(1, 0.2))
        self.question_label = Label(text=self.questions[self.current_question_index]["question"],
                                    font_name="B612 Mono", font_size="36sp",
                                    halign="center", valign="middle", color=(0.18, 0.37, 0.56, 1))
        top_layout.add_widget(self.question_label)
        layout.add_widget(top_layout)

        alternatives = self.get_shuffled_alternatives()

        self.alternative_buttons = []
        for alternative in alternatives:
            button = Button(font_name="B612 Mono", font_size="36sp",
                            size_hint=(None, None), size=(1500, 90),
                            background_color=(0.18, 0.37, 0.56, 1),
                            background_normal='', background_down='',
                            color=(1, 1, 1, 1), disabled_color=(0.8, 0.8, 0.8, 1),
                            on_release=self.check_answer)
            button.text = alternative
            layout.add_widget(button)
            self.alternative_buttons.append(button)

        root = ScrollView(size_hint=(1, 0.8))
        root.add_widget(layout)

        Clock.schedule_interval(self.update_timer, 1)

        return root

    def load_questions(self):
        with open("questions.csv", "r", newline="") as file:
            csv_reader = csv.DictReader(file)
            self.questions = list(csv_reader)

    def get_shuffled_alternatives(self):
        question = self.questions[self.current_question_index]
        correct_answer = question["correct_answer"]
        alternatives = question["alternatives"].split(", ")
        alternatives.append(correct_answer)
        random.shuffle(alternatives)
        return alternatives

    def check_answer(self, instance):
        selected_answer = instance.text
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        if selected_answer == correct_answer:
            self.num_correct += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.update_gui()
        else:
            self.show_results()

    def update_gui(self):
        question = self.questions[self.current_question_index]
        self.question_label.text = question["question"]

        alternatives = self.get_shuffled_alternatives()
        for button in self.alternative_buttons:
                button.halign = "center"
                button.valign = "middle"
        for button, alternative in zip(self.alternative_buttons, alternatives):
            button.text = alternative
            button.disabled = False

        if self.current_question_index == 0:
            random.shuffle(self.alternative_buttons)
        elif self.current_question_index == len(self.questions) - 1:
            random.shuffle(self.alternative_buttons)

    def show_results(self):
        for button in self.alternative_buttons:
            button.disabled = True
            button.background_color = (0, 0, 0, 0)  # Hide buttons
            button.text = ""  # Clear button text

        self.question_label.text = f"Quiz finished!\nScore: {self.calculate_score():.2f}"
        self.question_label.halign = "center"
        self.question_label.valign = "middle"


    def update_timer(self, dt):
        self.timer += 1

    def calculate_score(self):
        score = (self.num_correct / self.timer) * 100
        return score


if __name__ == "__main__":
    QuizApp().run()