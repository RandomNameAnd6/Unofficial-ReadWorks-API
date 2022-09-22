import requests
from bs4 import BeautifulSoup
import json

class ReadWorks():
    def __init__(self, lesson_data_link, threeorfour):
        self.lesson_data_link = lesson_data_link
        self.threeorfour = threeorfour
        self.lesson_data = requests.get(lesson_data_link)
        self.lesson_data_json = json.loads(self.lesson_data.text)
        self.lesson_data_html = BeautifulSoup(self.lesson_data.text, 'html.parser')

    def all_answers(self):
        questionSets = self.lesson_data_json['questionSets']
        first_question_set = list(questionSets.keys())[0]
        question_set_value = questionSets[first_question_set]
        questions_dict = list(question_set_value.keys())[3]
        questions_dict_value = question_set_value[questions_dict]
        return questions_dict_value

    def correct_answers(self):
        questionSets = self.lesson_data_json['questionSets']
        first_question_set = list(questionSets.keys())[0]
        question_set_value = questionSets[first_question_set]
        questions_dict = list(question_set_value.keys())[self.threeorfour]
        questions_dict_value = question_set_value[questions_dict]
        correct_answers = [q['answers'] for q in questions_dict_value]
        correct_answers = [q for q in correct_answers for q in q]
        correct_answers = [q for q in correct_answers if q["correct"] is True]
        return correct_answers

    def story_text(self):
        content = self.lesson_data_json['content']
        return content

    def word_count(self):
        word_count = self.lesson_data_json['wordcount']
        return word_count

    def added_to_rw(self):
        creation_time = self.lesson_data_json['created']
        return creation_time

    def title(self):
        title = self.lesson_data_json['title']
        return title

    def created(self):
        date = self.lesson_data_json['first_published']
        return date

    #genres sometimes works
    def genres(self):
        genres = self.lesson_data_json['genres']
        return genres
