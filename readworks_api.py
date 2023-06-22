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
        creation_time = self.lesson_data_json['created']
        return creation_time

    def all_answers(self):
        questionSets = self.lesson_data_json['questionSets']
        firstInDict = list(questionSets.keys())[0]
        belowQuestionSets = questionSets[firstInDict]
        answers = belowQuestionSets['questions']
        return answers

    def all_data(self):
        return self.lesson_data_json

    def author(self):
        try:
            author = self.lesson_data_json['a']
            return author
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
        date = self.lesson_data_json['first_published']
        return date

    def excerpt(self):
        return self.lesson_data_json['excerpt']

    def genres(self):
        try:
            genres = self.lesson_data_json['genres']
            return genres
        except KeyError:
            return None

    def image(self):
        return self.lesson_data_json['img']

    def lexile(self):
        return self.lesson_data_json['lc'][0]

    def page_title(self):
        return self.lesson_data_json['page_title']

    def story_text(self):
        content = self.lesson_data_json['content']
        return content

    def title(self):
        title = self.lesson_data_json['title']
        return title

    def get_uuid(self):
        return self.lesson_data_json['uuid']

    def word_count(self):
        word_count = self.lesson_data_json['wordcount']
        return word_count
