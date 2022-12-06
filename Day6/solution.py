class DataCircBuffer:
    _oldest_el_in_buffer = 0
    _element_count = 0
    _duplicate_el_idx = 0

    def __init__(self, size: int):
        self._size = size
        self.buffer = [''] * size
        self._duplicate_el_idx = size

    def check_for_char_uniqueness(self, char: str):
        unique = False
        for x in range(1, self._size + 1):
            # start from the newest el in buffer = idx
            idx = (self._oldest_el_in_buffer - x) % self._size
            if char == self.buffer[idx]:
                if self._size - x > self._duplicate_el_idx:
                    self._duplicate_el_idx = self._size - x
                break
        else:
            if self._duplicate_el_idx <= -1:
                unique = True
        self._insert(char)

        return unique

    def _insert(self, char):
        self.buffer[self._oldest_el_in_buffer] = char
        self._element_count += 1
        self._oldest_el_in_buffer = self._element_count % self._size
        self._duplicate_el_idx -= 1


marker_found = False
with open('input6', mode='r') as f:
    data_buffer = DataCircBuffer(13)
    data_count = 0
    while character := f.read(1):
        marker_found = data_buffer.check_for_char_uniqueness(character)
        data_count += 1

        if marker_found:
            print("DONE")
            print(data_count)
            break
