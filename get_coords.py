import numpy as np
import cv2 as cv
from typing import List


def getcords(img_name: str, cont=True,) -> List:
    """
    Функция возвращает список контуров
    img_name: string with path to image
    cont: True   Возвращается список контуров
          False  Возвращается ссписок всех координат контуров.
    :return: cords : list of coordinates
    Пример вызова
    cords = getcords('filename.jpg')
    """
    # параметры цветового фильтра
    cords = []
    hsv_min = np.array((0, 0, 0), np.uint8)
    hsv_max = np.array((10, 10, 10), np.uint8)

    fn = img_name # путь к файлу с картинкой
    img = cv.imread(fn)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max) # применяем цветовой фильтр
    # ищем контуры и складируем их в переменную contours
    contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #апроксимация контура

    cnt = contours[0]
    peri = cv.arcLength(cnt, True)
    cnt = cv.approxPolyDP(cnt, 0.02 * peri, True)
    if cont:
        #Возвращается контур
        return cnt
    else:
        #Возвращается список кординат контура
        for i_cnt in cnt:
            for point in i_cnt:
                x = int(point[0])
                y = int(point[1])
                cords.append((x, y))
        return cords


def get_delta(filename: str) -> list:
    """

    :param filename: string with path to image:
    :return:
    """

    cords = getcords(filename)
    deltas = []
    #находим ддлину списка с координатами
    length = len(cords)-1

    for num, coord in enumerate(cords):
        if num < length:
            delta_x = cords[num + 1][0] - coord[0]
            delta_y = cords[num + 1][1] - coord[1]
            deltas.append((delta_x, delta_y))
    return deltas


# if __name__ == "__main__":
#  #cords = (getcords('din.png'))
#  #print(cords)
#  print(get_delta('din.png'))


