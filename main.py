from bs4 import BeautifulSoup as bs

def open_xml(file_name):
    with open(f'{file_name}', 'r') as file:
        content = file.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")
    return bs_content

def getContent(file_num):
    if file_num == 1:
        return open_xml(FILES_NAME[0])
    elif file_num == 2:
        return open_xml(FILES_NAME[1])

def Flights(flight):
    print(f'Какие рейсы входят в маршрут ({len(flight)} шт.):')
    for f in flight:
        print(f"{f.flightnumber.text}: {f.source.text} -> {f.destination.text} ({f.carrier.text})")
    print('--------------------------------------------------')

def Time(flight):
    print('Время начала и время конца маршрута:')
    start_time = []
    finish_time = []
    for f in flight:
        start_time.append(f.departuretimestamp.text)
        finish_time.append(f.arrivaltimestamp.text)
    print(f'Время начала маршрута: {start_time[0]}')
    print(f'Время конца маршрута: {finish_time[-1]}')
    print('--------------------------------------------------')

def Price(pricing):
    total = {}
    for p in range(len(pricing)):
        total.update({f'type{p}': pricing[p]['type'], f'price{p}': float(pricing[p].text)})

    print('Цена маршрута:')
    for p in range(len(total)//2):
        print(f"{total.get(f'type{p}')} - {total.get(f'price{p}')}")

if __name__ == '__main__':

    QUANTITY = 0
    TAG = 'flights'
    FILES_NAME = ('RS_Via-3.xml', 'RS_ViaOW.xml')

    while True:
        print('--------------------------------------------------')
        print('По какому файлу получить информацию?')
        print(f'1) {FILES_NAME[0]}, 2) {FILES_NAME[1]}')
        file_num = int(input('Выберите файл: '))

        content = getContent(file_num)

        all_flights = content.find_all(TAG)

        for i in range(len(all_flights)):
            if all_flights[i].parent.name == 'priceditineraries':
                QUANTITY += 1
                print('--------------------------------------------------')
                print('')
                print('--------------------------------------------------')
                print(f'>> Маршрут {QUANTITY}')
                print('--------------------------------------------------')

                flight = all_flights[i]('flight')
                pricing = all_flights[i](chargetype="TotalAmount")

                Flights(flight)
                Time(flight)
                Price(pricing)

        print('--------------------------------------------------')
        print(f'Итого кол-во маршрутов: {QUANTITY}')
        print('--------------------------------------------------')
        print('Повторить? y/N')
        exit = input('Ваш выбор: ')
        if exit == 'N':
            break






















