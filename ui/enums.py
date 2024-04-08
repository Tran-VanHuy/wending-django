from enum import Enum;
class AlbumEnums(Enum):
    image_1 = 1
    image_2 = 2
    image_3 = 3
    image_4 = 4
    image_5 = 5
    image_6 = 6
    image_7 = 7
    image_8 = 8
    image_9 = 9
    image_10 = 10
    image_11 = 11

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]

class LocationBannerEnums(Enum):
    location_banner_1 = 1
    location_banner_2 = 2
    location_banner_3 = 3
    location_banner_4 = 4

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]

