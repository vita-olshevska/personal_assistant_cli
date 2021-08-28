import random

BOT_CONFIG = {
    "intents": {
        "word": {
            "comand_list": ["add", "change", "delete", "filter", "show birthday", "tag", "sort", "record", "note"],
            "responses": [" "]
        }
    },
    "failure_phrases": [
        "Please write it in a different way.",
        "Something went wrong.",
        "I don't understand :( ",
        "I'm just a bot, please put it in a simpler way ;)"
    ]
}


def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in "abcdefghijklmnopqrstuvwxyz- "]
    text = " ".join(text)
    return text


def get_intent(word):
    for intent, intent_data in BOT_CONFIG["intents"].items():
        for example in intent_data["comand_list"]:
            if example.lower() == word.lower():
                return intent


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG["intents"]:
        phrases = BOT_CONFIG["intents"][intent]["responses"]
        return random.choice(phrases)


def generate_answer_by_text(word):
    pass


def get_failure_phrase():
    phrases = BOT_CONFIG["failure_phrases"]
    return random.choice(phrases)


def if_command_correctly(word):
    # NLU
    intent = get_intent(word)
    # Poly4enie otweta

    # ishem gotovuj otvet
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer
    # Geniriryem podxodjashij otvet po konteksty
    answer = generate_answer_by_text(word)
    if answer:
        return answer
    # Saglyshky ispolsyem
    answer = get_failure_phrase()
    return answer


word = None

while word not in ["exit", "вихід", "выход", "Ausgang"]:
    word = input()
    answer = if_command_correctly(word)
    print(answer)