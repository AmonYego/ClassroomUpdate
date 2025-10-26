import requests

BASE_URL = "http://127.0.0.1:9001"  # change when deployed


def upload_and_extract(lecture_file, pastpaper_file, level):
    files = {
        "lecture_text": (lecture_file.name, lecture_file.getvalue(), lecture_file.type),
        "pastpaper_text": (
            pastpaper_file.name,
            pastpaper_file.getvalue(),
            pastpaper_file.type,
        ),
    }
    data = {"level": level}
    response = requests.post(f"{BASE_URL}/extract/topics", files=files, data=data)
    return response.json()


def mark_answer(qestion_file, level):
    file = {
        "question_file": (
            qestion_file.name,
            qestion_file.getvalue(),
            qestion_file.type,
        )
    }
    data = {"level": level}
    response = requests.post(f"{BASE_URL}/marking/markanswer", files=file, data=data)
    return response.json()


def generate_questions(lecture_file, pastpaper_file, level):
    files = {
        "lecture_text": (lecture_file.name, lecture_file.getvalue(), lecture_file.type),
        "pastpaper_text": (
            pastpaper_file.name,
            pastpaper_file.getvalue(),
            pastpaper_file.type,
        ),
    }
    data = {"level": level}
    response = requests.post(f"{BASE_URL}/questions/generate", files=files, data=data)
    return response.json()


def similar_quiz(question_file, level):
    files = {
        "question_file": (
            question_file.name,
            question_file.getvalue(),
            question_file.type,
        )
    }
    data = {"level": level}
    response = requests.post(f"{BASE_URL}/similar/similarquiz", files=files, data=data)
    return response.json()


def simplify(lecture_file, level):
    files = {
        "lecture_text": (
            lecture_file.name,
            lecture_file.getvalue(),
            lecture_file.type,
        )
    }
    data = {"level": level}
    response = requests.post(f"{BASE_URL}/simplify/explanation", files=files, data=data)
    return response.json()
