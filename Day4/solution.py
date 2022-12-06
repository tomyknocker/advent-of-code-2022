def sections_contain(section1, section2) -> bool:
    if ((section1[0] <= section2[0] and section1[1] >= section2[1])
            or (section2[0] <= section1[0] and section2[1] >= section1[1])):
        return True
    return False


def sections_overlap(section1, section2) -> bool:
    if (section1[0] > section2[1] or section1[1] < section2[0]):
        return False
    return True


contained_sections = 0
overlapped_sections = 0
with open('input4', mode='r') as f:
    for line in f.readlines():
        sections_pair = [[int(section_id) for section_id in section.split('-')]
                         for section in line.strip().split(',')]

        if sections_contain(sections_pair[0], sections_pair[1]):
            contained_sections += 1
        if sections_overlap(sections_pair[0], sections_pair[1]):
            overlapped_sections += 1

print(f"{contained_sections=}")
print(f"{overlapped_sections=}")