import requests
import json


class ReadWorks():
    def __init__(self, lesson_data_link):
        self.lesson_data_link = lesson_data_link
        self.lesson_data = requests.get(lesson_data_link)
        self.lesson_data_json = json.loads(self.lesson_data.text)

    def activity_types(self):
        return self.lesson_data_json['activity_types']

    def added_to_rw(self):
        return self.lesson_data_json['created']

    def all_answers(self):
        qsTotals = self.lesson_data_json['qsTotals']
        index = list(qsTotals['qt'].keys())[-1]
        questionSets = self.lesson_data_json['questionSets']
        belowQuestionSets = questionSets[index]
        answers = belowQuestionSets['questions']
        return answers

    def all_data(self):
        return self.lesson_data_json

    def author(self):
        try:
            return self.lesson_data_json['a']
        except KeyError:
            return None

    def canonical_grade(self):
        return self.lesson_data_json['canonical_grade']

    def correct_answers(self):
        qsTotals = self.lesson_data_json['qsTotals']
        index = list(qsTotals['qt'].keys())[-1]
        questionSets = self.lesson_data_json['questionSets']
        secondInDict = questionSets[index]
        allQuestions = secondInDict["questions"]
        correctAnswers = []
        for question in allQuestions:
            if 'answers' in question:
                for answer in question['answers']:
                    if answer['correct'] == True:
                        correctAnswers.append(answer)
        return correctAnswers

    def created(self):
        return self.lesson_data_json['first_published']

    def excerpt(self):
        return self.lesson_data_json['excerpt']

    def genres(self):
        try:
            return self.lesson_data_json['genres']
        except KeyError:
            return None

    def image(self):
        return self.lesson_data_json['img']

    def lexile(self):
        return self.lesson_data_json['lc'][0]

    def page_title(self):
        return self.lesson_data_json['page_title']

    def story_text(self):
        return self.lesson_data_json['content']

    def title(self):
        return self.lesson_data_json['title']

    def get_uuid(self):
        return self.lesson_data_json['uuid']

    def word_count(self):
        return self.lesson_data_json['wordcount']
