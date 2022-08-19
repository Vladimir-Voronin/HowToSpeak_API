from pyhts.hts_words_priority.priority_calculations import WordsPriorityCalculations


class WordsPriorityInput:
    def __init__(self, freq_current_dict, freq_rating_type, user_dict, number_of_words):
        self.freq_current_dict = freq_current_dict
        self.freq_rating_type = freq_rating_type
        self.user_dict = user_dict
        self.number_of_words = number_of_words


# All staticmethods should recieve WordsPriorityInput object
class WordsPriorityHandler:
    @staticmethod
    def words_using_less_than_1(wpi: WordsPriorityInput):
        words_list = WordsPriorityCalculations.get_words_classic(wpi.freq_current_dict, wpi.user_dict,
                                                                 wpi.number_of_words, 1)
        return words_list

    @staticmethod
    def words_using_less_than_5(wpi: WordsPriorityInput):
        words_list = WordsPriorityCalculations.get_words_classic(wpi.freq_current_dict, wpi.user_dict,
                                                                 wpi.number_of_words, 5)
        return words_list

    @staticmethod
    def words_using_less_than_10(wpi: WordsPriorityInput):
        words_list = WordsPriorityCalculations.get_words_classic(wpi.freq_current_dict, wpi.user_dict,
                                                                 wpi.number_of_words, 10)
        return words_list


Handler_methods_dict = {"words_using_less_than_1": WordsPriorityHandler.words_using_less_than_1,
                        "words_using_less_than_5": WordsPriorityHandler.words_using_less_than_5,
                        "words_using_less_than_10": WordsPriorityHandler.words_using_less_than_10, }
