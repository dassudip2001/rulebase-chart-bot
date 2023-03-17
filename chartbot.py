import random
import re


class RuleBot():
    #     negative responsive
    negative_response = ("no", "nope", "nah", "sorry")
    #     exit conversation
    exit_commands = ("quit", "pause", "exit", "goodby", "bye")
    #     random question
    random_questions = (

        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume  ",
        "Is there intelligent life on this planet "

    )

    def __init__(self):
        self.alienable = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about': r'.*\s*intelligent'
        }

    def greet(self):
        self.name = input("what is your name?\n")
        will_help = input(
            f"hiii {self.name}, i am a rule base chart bot.Learn About your planet?\n"
        )
        if will_help in self.negative_response:
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
            print(reply, 'user question')

    def match_reply(self, reply):
        for key, value in self.alienable.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about':
                return self.about()
            elif not found_match:
                return self.not_match_intent()

    def describe_planet_intent(self):
        responses = ("The planets in our solar system didn’t appear out of nowhere.\n", "Neither did the sun.\n",
                     "They were all part of a big cloud of gas and dust.\n",
                     "Gravity collected lots of material in the center to create the sun.\n",
                     "The left over stuff swirled around the forming sun, colliding and collecting together.\n",
                     "Some would have enough gravity to attract even more gas and dust, eventually forming planets.\n",
                     "Watch this to learn more.\n")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("This definition is very much focused on our own solar system.\n",
                     "But there are also planets in places that are not our solar system.\n",
                     "TheseThis definition is very much focused on our own solar system.\n",
                     " These planets are called exoplanets.\n",
                     "They can be found circling around stars, just like the planets here in our own solar system.\n",
                     " Does that mean that all planets form the same way?\n",
                     " Are all planets made from a star’s leftovers?\n",
                     )
        return random.choice(responses)

    def about(self):
        responses = ("Organisation is the backbone of management because without an efficient organization no management can perform its functions smoothly.\n",
                     " In the management process this organization stands as a second state which tries to combine various activities in a business to accomplish pre-determined goals.\n",
                     "It is the structural framework of duties and responsibilities required of personnel in performing various functions with a view to achieve business goals.\n")
        return random.choice(responses)

    def not_match_intent(self):
        responses = (" there is no match found \n",
                     "please tell me more information.\n", "why do you say that?\n", "why?\n")
        return random.choice(responses)


AlienBot = RuleBot()
AlienBot.greet()
