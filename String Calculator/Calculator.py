class Calculator:
    def test(self):
        return 'some str'

    def add(self, string: str) -> int:
        if string == "":
            return 0

        try:
            string.index(',')
        except ValueError:
            return int(string)

        return sum([int(i.strip()) for i in string.split(',')])
