import requests
from bs4 import BeautifulSoup, Tag

class SqlTutorialParser:
    __slots__ = ('_html')

    BASE_URL = "http://www.sql-tutorial.ru"

    def __init__(self) -> None:
        self._html = SqlTutorialParser._retrieve_html("/ru/content.html")

    @staticmethod
    def _retrieve_html(url: str) -> BeautifulSoup:
        response = requests.get(SqlTutorialParser.BASE_URL + url)
        return BeautifulSoup(response.content, 'html.parser')

    @staticmethod
    def _parse_hints_and_solutions(url):
        soluion_html = SqlTutorialParser._retrieve_html(url)
        return soluion_html('pre', class_='sql')

    def _parse_exercise(self, url):
        exercise_html = SqlTutorialParser._retrieve_html(url)
        if not 'Упражнение' in exercise_html.find('h1').text:
            return None
        task = exercise_html.find('p', class_='task')
        if task is None:
            task = exercise_html.find('p')
        answers = []
        found_answers = exercise_html('pre', class_='sql')
        if not found_answers:
            url = exercise_html.find('a', class_='e')['href']
            if 'sql-ex.ru' in url:
                return None
            found_answers =  SqlTutorialParser._parse_hints_and_solutions(url)
        for answer in found_answers:
            answers.append("\n".join(x.text.replace('\xa0', '') for x in answer('div', class_='de1')))
        result = {
            'task': task.text.strip(),
            'answers': answers,
            'url' : SqlTutorialParser.BASE_URL + url
        }
        return result

    def _parse_topic(self, url):
        exercises = {}
        topic_html = SqlTutorialParser._retrieve_html(url)
        for exercise in topic_html('div', class_='in'):
            a_tag = exercise.find('a')
            parsed_exercise = self._parse_exercise(a_tag['href'])
            if parsed_exercise is not None:
                exercises[a_tag.text] = parsed_exercise 
        return exercises

    def _parse_topics(self):
        topics = {}
        for topic in self._html.find_all('div', class_='in1'):
            a_tag = topic.find('a')
            if not isinstance(a_tag, Tag):
                continue
            parsed_topic = self._parse_topic(a_tag['href'])
            if parsed_topic:
                topics[a_tag.text] = parsed_topic
        return topics

    def parse(self):
        return self._parse_topics()