
from colorama import  Fore, Back, Style


print(Fore.BLUE + Back.YELLOW + Style.DIM + 'Слава Україні!')
print(Fore.YELLOW + Back.BLUE + Style.DIM + 'Героям Слава!')
print(Fore.WHITE + Back.BLACK + Style.BRIGHT  + 'Colorama допомагає додати колір у термінал:\n'
                                            'Цей пакет чудово покращує Python-скрипти.\n'
                                            'Документація проста і зрозуміла,\n'
                                            'прочитати її можна на сторінці Colorama в PyPI. https://pypi.org/project/colorama/\n'
                                            'Або за допомогою Ctrl+ліва кнопка миші\n'
                                            'Метод dir() виведе список всіх атрибутів і методів модуля colorama. \n'
                                            'Деякі з найважливіших методів і атрибутів: init(autoreset=False, strip=None, wrap=True, convert=None, **kwargs): \n'
                                            'метод для ініціалізації бібліотеки, який налаштовує параметри виведення кольорового тексту в консоль. \n'
                                            'Наприклад, colorama.init() встановлює стандартні налаштування. Якщо autoreset дорівнює True, \n'
                                            'то кольорові налаштування скидаються після кожного виведення. strip вказує, чи видаляти кольорові налаштування з тексту, \n'
                                            'wrap - чи переносити рядок при досягненні кінця рядка, convert - тип конвертації кольорів (для AnsiToWin32 або Win32ToAnsi).\n'
                                            'Fore: клас з атрибутами, які дозволяють задавати кольорові налаштування для переднього плану тексту. \n'
                                            'Наприклад, colorama.Fore.RED задає червоний колір переднього плану.\n'
                                            'Back: клас з атрибутами, які дозволяють задавати кольорові налаштування для заднього плану тексту. \n'
                                            'Наприклад, colorama.Back.GREEN задає зелений колір заднього плану.\n'
                                            'Style: клас з атрибутами, які дозволяють задавати стиль тексту (жирний, курсивний тощо). \n'
                                            'Наприклад, colorama.Style.DIM зменшує яскравість тексту.\n')