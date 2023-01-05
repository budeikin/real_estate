from sample import create_samples
from advertisment import ApartmentSell, ApartmentRent, HouseRent, HouseSell, StoreSell, StoreRent


class Handler:
    ADVERTISEMENT_TYPES = {1: ApartmentSell, 2: ApartmentRent, 3: HouseSell, 4: HouseRent, 5: StoreRent, 6: StoreSell}

    SWITCHES = {'r': 'get report', 's': 'show all'}

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            print(adv, adv.manager.count())
        self.run()

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPES.values():
            for obj in adv.objects_list:
                print(obj.show_detail())
        self.run()

    def run(self):
        print('(--here there is some guide for you--)')
        for key in self.SWITCHES:
            print(f'--press {key} for {self.SWITCHES[key]} ')

        user_input = input('please enter your command : ')
        if user_input not in self.SWITCHES.keys():
            self.run()
        if user_input == 'r':
            return self.get_report()
        elif user_input == 's':
            return self.show_all()
        else:
            self.run()


if __name__ == '__main__':
    create_samples()
    handler = Handler().run()
