def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    i, count = 0, 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
            i += 1
        i += 1
        if count >= n:
            return True
    return count >= n
