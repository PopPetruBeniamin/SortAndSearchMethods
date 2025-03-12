import traceback
from application.entities.validators import MasinaException


class MasinaConsole:
    def __init__(self, masina_service):
        self.__masina_service = masina_service

    def __search(self, token):
        print(self.__masina_service.find(token))

    def __sort_by_token(self):
        print(*self.__masina_service.sort_by_token(), sep='\n')

    def __sort_by_marca_model(self):
        print(*self.__masina_service.sort_by_marca_model(), sep='\n')

    def __sort_by_marca_model_token(self):
        print(*self.__masina_service.sort_by_marca_model_token(), sep='\n')

    def __sort_by_profit(self):
        print(*self.__masina_service.sort_by_profit(), sep='\n')

    def run_console(self):
        commands = self.__create_commands()
        while True:
            self.__print_commands(commands)
            try:
                cmd, args = self.__read_commands()
            except ValueError as ve:
                print(ve)
                continue
            except Exception as e:
                print(e)
                continue

            if cmd == 'exit':
                break

            try:
                commands[cmd](*args)
            except MasinaException as ce:
                print(ce)
                traceback.print_exc()
            except ValueError as ve:
                print(ve)
                traceback.print_exc()
            except KeyError as ke:
                print(ke)
                traceback.print_exc()
            except Exception as e:
                print(e)

    @staticmethod
    def __help_commands(cmd):
        help_commands = {'SEARCH': 'Usage: SEARCH <token>',
                         'SORT-TOKEN': 'Usage: SORT TOKEN',
                         'SORT-MARCA-MODEL': 'Usage: SORT MARCA MODEL',
                         'SORT-MARCA-MODEL-TOKEN': 'Usage: SORT MARCA MODEL TOKEN',
                         'SORT-PROFIT': 'Usage: SORT PROFIT',
                         'help': 'help <command>'}
        try:
            print(help_commands[cmd])
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def __create_commands(self):
        return {'SEARCH': self.__search,
                'SORT-TOKEN': self.__sort_by_token,
                'SORT-MARCA-MODEL': self.__sort_by_marca_model,
                'SORT-MARCA-MODEL-TOKEN': self.__sort_by_marca_model_token,
                'SORT-PROFIT': self.__sort_by_profit,
                'help': self.__help_commands}

    @staticmethod
    def __print_commands(commands):
        print("Available commands: ")
        print(*commands.keys(), 'exit', sep=' --- ')
        print("For help, type: help <command>")

    @staticmethod
    def __read_commands():
        command = input("Command = ")
        pos = command.find(' ')

        if pos == -1:
            return command, []

        cmd = command[:pos]
        args = command[pos:]
        args = args.split(',')
        args = [s.strip() for s in args]

        return cmd, args
