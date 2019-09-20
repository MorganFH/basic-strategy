import time

from helpers import ACTIONS, SUITS, VALUES, get_correct_action, print_line, draw_card


class BasicStratTrainer:
    """
    Blackjack hand simulator in order to practice basic strategy.
    Deals player two cards at random and shows dealer's upcard.
    Assumes at least 3 decks are used (as is normal in casinos), so all 3 cards may be identical.
    The player should then choose the correct action according to basic strategy.
    see https://www.cs.bu.edu/~hwxi/academic/courses/CS320/Spring02/assignments/06/basic-strategy.html
    or https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
    """

    def __init__(self, surrender=False):
        self.score = 0
        self.round = 0
        self.dealer_upcard = None
        self.player_hand = []
        self.surrender = surrender

    def new_round(self):
        """
        Setup new round
        """
        self.round += 1
        print("\n")
        print_line(30)
        print(f"ROUND {self.round}")
        print(f"SCORE: {self.score}\n")

    def deal_hand(self):
        """
        Deal one card to dealer (his upcard) and 2 cards to player.
        """
        print_line(27)
        self.dealer_upcard = draw_card()
        print(f"Dealer is dealt {self.dealer_upcard}.")
        self.player_hand = [draw_card() for i in range(2)]
        print(f"You are dealt {self.player_hand}")
        print_line(27)
        print("\n")

    def take_player_action(self):
        """
        Accept an action from the player
        """
        print("What do you want to do?")
        print("Options are:")
        options = [
            f"{i}: {list(ACTIONS.values())[i]}\t" for i in range(len(ACTIONS.values()))
        ]
        print("".join(options) + "\n")
        action = list(ACTIONS.values())[int(input("Enter option: "))]
        print(f"\nYou chose: {action}")
        return action

    def get_correct_action(self):
        """
        Evaluate the current dealer card and player hand and
        return the correct action according to basic strategy
        """
        pair = self.player_hand[0].value == self.player_hand[1].value
        ace = 14 in [card.value for card in self.player_hand]
        hand_value = sum([min(card.value, 10) for card in self.player_hand])
        hand_value = hand_value + 1 if ace else hand_value
        dealer = (
            min(self.dealer_upcard.value, 10) if self.dealer_upcard.value < 14 else 11
        )

        return get_correct_action(pair, ace, hand_value, dealer, self.surrender)

    def evaluate_action(self, action, corr):
        """
        Determine whether the player selected the correct action.
        """
        correct = action == corr
        if correct:
            self.score += 1
            print(f"You were correct! The correct answer is indeed {action}.")
            print(f"Your score has increased.")
        else:
            print(f"Your answer was incorrect. The correct answer is {corr}.")
        print(f"Accuracy: {float(self.score)/float(self.round) * 100}%")

    def play(self):
        while True:
            self.new_round()
            self.deal_hand()
            correct = self.get_correct_action()
            action = self.take_player_action()
            time.sleep(0.5)
            self.evaluate_action(action, correct)
            time.sleep(3)


trainer = BasicStratTrainer()
trainer.play()
