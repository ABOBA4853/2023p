class Checker:
    def Check(self, *exc_types):
        def Check(function):
            def Check(*args, **kwargs):
                try:
                    print(function(*args, **kwargs))
                #except Exception as ex:
                except (exc_types) as ex:
                    print(ex)
                else:
                    print('No exceptions')
            return Check
        return Check
    @Check(NameError, TypeError, SyntaxError, ZeroDivisionError, Exception)
    def Calculate(self, expresion):
        return eval(expresion)