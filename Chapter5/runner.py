from Chapter5.FourCal import FourCal
from Chapter5.MoreFourCal import MoreFourCal

if __name__ == '__main__':
    main = FourCal()
    main.setData(5, 4)
    print(main.add())
    print(main.mul())
    print(main.div())
    print(main.mul())

    main2 = MoreFourCal()
    main2.setData(2, 3)
    print(main2.pow())
