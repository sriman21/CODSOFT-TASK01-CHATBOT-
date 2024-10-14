import random
import re

class RuleBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_question = (
        "What is your favorite sport?",
        "Do you support any sports team?",
        "What was the last game you watched?",
        "Do you play any sports?",
        "Which sport is popular where you're from?",
        "Who is your favorite athlete?"
    )

    def __init__(self):
        self.sports_babble = {
            'favorite_sport_intent': r'.*\sfavorite sport.*|.*like sports.*',
            'favorite_team_intent': r'.*\sfavorite team.*|.*support.*team.*',
            'last_game_intent': r'.*\slast game.*|.*recent game.*|.*watch.*game.*',
            'play_sports_intent': r'.*\splay.*sport.*|.*athlete.*|.*exercise.*',
            'popular_sport_intent': r'.*\spopular sport.*|.*most popular.*sport.*',
            'favorite_athlete_intent': r'.*\sfavorite athlete.*|.*best player.*'
        }
        self.memory = {}

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am a sports-loving bot! Will you chat with me about sports?\n"
        )
        if will_help.lower() in self.negative_res:
            print("Alright! Maybe some other time. Have a great day!")
            return
        else:
            self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply.lower() == command:
                print("Goodbye! Enjoy the next game!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.sports_babble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent == 'favorite_sport_intent':
                    return self.favorite_sport_intent()
                elif intent == 'favorite_team_intent':
                    return self.favorite_team_intent()
                elif intent == 'last_game_intent':
                    return self.last_game_intent()
                elif intent == 'play_sports_intent':
                    return self.play_sports_intent()
                elif intent == 'popular_sport_intent':
                    return self.popular_sport_intent()
                elif intent == 'favorite_athlete_intent':
                    return self.favorite_athlete_intent()
        return self.no_match_intent()

    def favorite_sport_intent(self):
        responses = (
            "My favorite sport is basketball! What about you?\n",
            "I enjoy watching football. What's your favorite sport?\n"
        )
        return random.choice(responses)

    def favorite_team_intent(self):
        responses = (
            "I support the Lakers! Which team do you support?\n",
            "I'm a big fan of Manchester United. What about you?\n"
        )
        return random.choice(responses)

    def last_game_intent(self):
        responses = (
            "The last game I watched was the NBA finals. What was the last game you watched?\n",
            "I recently saw a great soccer match. How about you?\n"
        )
        return random.choice(responses)

    def play_sports_intent(self):
        responses = (
            "I enjoy playing virtual sports! Do you play any sports?\n",
            "I try to exercise regularly. What sport do you play?\n"
        )
        return random.choice(responses)

    def popular_sport_intent(self):
        responses = (
            "Soccer seems to be the most popular sport worldwide! What about in your area?\n",
            "Basketball is very popular where I'm from. What is the most popular sport where you are?\n"
        )
        return random.choice(responses)

    def favorite_athlete_intent(self):
        responses = (
            "My favorite athlete is LeBron James. Who's yours?\n",
            "I really admire Lionel Messi. Who is your favorite athlete?\n"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Interesting! Tell me more.\n",
            "I'd love to hear more about that!\n",
            "Can you elaborate on that?\n",
            "That's cool! Let's talk more about sports.\n"
        )
        return random.choice(responses)
bot = RuleBot()
bot.greet()
