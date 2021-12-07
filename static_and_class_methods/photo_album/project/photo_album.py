from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__photo_matrix()

    def __photo_matrix(self):
        result = []
        for i in range(self.pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label):
        for index, row in enumerate(self.photos):
            if len(row) < 4:
                self.photos[index].append(label)
                return  f"{label} photo added successfully on page " \
                               f"{index + 1} slot " \
                               f"{len(self.photos[index])}"
        return "No more free slots"

    def display(self):
        result = '-' * 11
        result += '\n'
        for r in self.photos:
            result += ' '.join( ['[]' for el in r])
            result += '\n'
            result += '-' * 11
            result += '\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
