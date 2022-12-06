#part 1
class DataCircBuffer:
    _oldest_el_in_buffer = 0
    _element_count = 0

    def __int__(self, size:int):
        self._size=size
        self.buffer = ['']*size

    def check_for_char_uniqueness(self, character:str):
        return True

    def _insert(self, char):
        self._element_count +=1
        self._oldest_el_in_buffer = self._element_count%self._size

marker_found = False
with open('input6', mode='r') as f:
    data_buffer = ['','','']
    data_count = 0
    oldest_el_in_buffer = 0
    character_duplicate = 3
    while not marker_found:
        character = f.read(1)
        oldest_el_in_buffer = data_count%3
        duplicate_element_idx = next((x for x in reversed(range(0,len(data_buffer))) if data_buffer[x] == character),-1)
        if duplicate_element_idx >=0:
            tmp = (3+duplicate_element_idx - oldest_el_in_buffer)%3
            if character_duplicate < tmp:
                character_duplicate = tmp
        else:
            character_duplicate -= 1
        print(f'{data_buffer[oldest_el_in_buffer]}{data_buffer[(oldest_el_in_buffer+1)%3]}{data_buffer[(oldest_el_in_buffer+2)%3]}{character}', character_duplicate)
        data_buffer[oldest_el_in_buffer] = character
        data_count +=1
        if character_duplicate < -1:
            break