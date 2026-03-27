import os


class GameStats:
    """Trace statistics for the game"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # The game launches in inactive state
        self.game_active = False
        self.game_paused = False
        self.game_ended = False

        # Best score shouldn't reset
        try:
            if os.path.exists("score.txt"):
                score_file = open('score.txt', 'r')
                high_score = int(score_file.read())
                score_file.close()
            else:
                score_file = open('score.txt', 'w')
                score_file.write("0")
                score_file.close()
                high_score = 0
        except:
            # File operations may not work in web browsers
            high_score = 0

        self.high_score = high_score

    def reset_stats(self):
        """Initialize in process statistics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
