from  limiterror import LimitError
class Checker:
    def Check(self, amount, limit):
        if(amount > limit):
            raise LimitError(amount, limit)
        return True





