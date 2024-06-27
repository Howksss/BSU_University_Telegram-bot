import re

import fake_user_agent
import requests
from bs4 import BeautifulSoup

link = "https://me.bgu.ru/"
user = fake_user_agent.user_agent()
session = requests.Session()

header = {
    'user-agent': user
}


def get_points(user_log, user_pass):
    with requests.Session() as session:
        resp1 = session.get(link, headers=header).text
        innit = BeautifulSoup(resp1, "html.parser")
        viewstate = innit.find("input", id="__VIEWSTATE")
        eventavalid = innit.find("input", id="__EVENTVALIDATION")
        data = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": f"{viewstate['value']}",
            "__EVENTVALIDATION": f"{eventavalid['value']}",
            "ctl00$MainContent$HF": "",
            "ctl00$MainContent$TBlogin": f"{user_log}",
            "ctl00$MainContent$TBpswd": f"{user_pass}",
            "ctl00$MainContent$BtnAD": "Войти",
            "ctl00$MainContent$TBseria": "",
            "ctl00$MainContent$TBnumber": ""
        }
        response = session.post(link, data=data, headers=header).text
        study_points = 'https://me.bgu.ru/user/study/markscurrent.aspx'
        profile_points_response = session.get(study_points, headers=header).text
        session2 = requests.Session()
        points = {}
        soup = BeautifulSoup(profile_points_response, "html.parser")
        alph = (list("АБВГДЕЁЖЗИКЛМНОПРСТУФЦЧШЩЫЬЪЭЮЯ"))
        objects = soup.find_all("tr", class_="tt")
        numbers = soup.find_all("span", id=re.compile("MainContent_LV_LmyBall_"))
        counter = 0
        for object in objects:
            for string in object.stripped_strings:
                for letter in alph:
                    if string.startswith(letter):
                        if "Зачет" not in string and "Экзамен" not in string and "Курсовая" not in string:
                            try:
                                if numbers[counter].text != '':
                                    points[f"{string}"] = numbers[counter].text
                                    counter += 1
                                elif numbers[counter].text == '':
                                    counter += 1
                                    pass
                            except IndexError:
                                pass
        return points
