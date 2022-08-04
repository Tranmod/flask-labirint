import random


class Game():
    
    house = [['','Балкон',''], ['Спальня','Холл','Кухня'], ['Кладовка','Гостиная','Подвал']]

    def __init__(self, current_place=0, user_name=''):
            if current_place == 0:
                self.current_place = [random.randint(1, 2), random.randint(0, 2)]
            else:
                self.current_place = current_place

            self.alert = ['Пора отсюда выбираться', 'alert-primary']
            self.moving = 0

            if not user_name:
                self.user_name = 'Гость'
            else:
                self.user_name = user_name
                self.alert = ['{}, пора отсюда выбираться'.format(self.user_name), 'alert-primary']

    def search_room(self):
            if self.moving == 0:
                self.alert = ['Туда не возможно пройти, попробуй в другом направлении', 'alert-danger']
            else:
                if Game.house[self.current_place[0]][self.current_place[1]] == '':
                    self.alert = ['Туда не возможно пройти, попробуй в другом направлении', 'alert-danger']
                elif Game.house[self.current_place[0]][self.current_place[1]] == 'Балкон':
                    self.alert = ['Ура, тебе удалось. {}, ты на балконе'.format(self.user_name), 'alert-success']
                else:
                    self.alert = ['Ты попал(а) в комнату: {} '.format(Game.house[self.current_place[0]][self.current_place[1]]),
                                  'alert-warning']

    def move(self, current_place, direction, stages):
            if direction == 'north':
                if 0 <= int(current_place[0]) - stages <= 2:
                    if Game.house[self.current_place[0] - stages][self.current_place[1]] != '':
                        self.current_place[0] = int(current_place[0]) - stages
                        self.moving = 1
                self.search_room()

            elif direction == 'sout':
                if 0 <= int(current_place[0]) + stages <= 2:
                    if Game.house[self.current_place[0] + stages][self.current_place[1]] != '':
                        self.current_place[0] = int(current_place[0]) + stages
                        self.moving = 1
                self.search_room()
            elif direction == 'west':
                if 0 <= int(current_place[1]) - stages <= 2:
                    if Game.house[self.current_place[0]][self.current_place[1] - stages] != '':
                        self.current_place[1] = int(current_place[1]) - stages
                        self.moving = 1
                self.search_room()
            elif direction == 'east':
                if 0 <= int(current_place[1]) + stages <= 2:
                    if Game.house[self.current_place[0]][self.current_place[1] + stages] != '':
                        self.current_place[1] = int(current_place[1]) + stages
                        self.moving = 1
                self.search_room()