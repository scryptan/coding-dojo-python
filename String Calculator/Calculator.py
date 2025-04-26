class Calculator:
    def test(self):
        return 'some str'

    def add(self, string: str) -> int:
        if string == "":
            return 0

        string = string.replace('\n', ',')
        string = string.replace(' ', ',')
        string = string.replace('|', ',')
        string = string.replace(';', ',')

        try:
            string.index(',')
        except ValueError:
            return int(string)

        return sum([int(i.strip()) for i in string.split(',')])
