import random
import re


class RuleBot():
    #     nagative responcive
    negative_responce = ("no", "nope", "nah", "sorry")
    #     exit conversation
    exit_commands = ("quit", "pause", "exit", "goodby", "bye")
    #     random question
    random_questions = (

        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume",
        "Is there intelligent life on this planet"

    )

    def __init__(self):
        self.alienbabble = {
            'describle_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about': r'.*\s*intellipaat'
        }

    def greet(self):
        self.name = input("what is your name?\n")
        will_help = input(
            f"hiii {self.name}, i am a rule base chart bot.how i can help you?\n"
        )
        if will_help in self.negative_responce:
            print("ok,have a nice day")
            return
        self.chart()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("ok, have a nice day")
                return True

    def chart(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describle_planet_intent':
                return self.describle_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about':
                return self.about()
            elif not found_match:
                return self.not_match_intent()

    def describle_planet_intent(self):
        responses = ("my planet is earth")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("my planet is earth")
        return random.choice(responses)

    def about(self):
        responses = ("my planet is earth")
        return random.choice(responses)

    def not_match_intent(self):
        responses = (" there is no match found")
        return random.choice(responses)


AlienBot = RuleBot()
AlienBot.greet()
