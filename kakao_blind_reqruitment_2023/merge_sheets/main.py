from typing import List, Any


class ControlSheet:
    def __init__(self, sheet: List[List[Any]], pointer_sheet: List[List[Any]]):
        self._sheet = sheet
        self._pointer_sheet = pointer_sheet

    # condition 1, 2 -> python은 오버로딩 지원하지 않음
    def update(self, *args):
        if len(args) == 3:
            r, c, value = args
            r = int(r) - 1
            c = int(c) - 1

            # 해당 포인터를 가진 모든 시트 값 update
            pointer_value = self._pointer_sheet[r][c]

            for row in range(len(self._pointer_sheet)):
                for col in range(len(self._pointer_sheet[row])):
                    if self._pointer_sheet[row][col] == pointer_value:
                        self._sheet[row][col] = value

        elif len(args) == 2:
            value1, value2 = args
            self._sheet = [list(map(lambda x: value2 if x == value1 else x, row)) for row in self._sheet]

    # condition 3
    def merge(self, r1: str, c1: str, r2: str, c2: str):
        r1 = int(r1) - 1
        c1 = int(c1) - 1
        r2 = int(r2) - 1
        c2 = int(c2) - 1

        self._pointer_sheet[r2][c2] = self._pointer_sheet[r1][c1]  # 포인터 저장
        self._sheet[r2][c2] = self._sheet[r1][c1]  # 값 저장

    # condition 4
    def unmerge(self, r: str, c: str):
        r = int(r) - 1
        c = int(c) - 1

        pointer_value = self._pointer_sheet[r][c]
        sheet_value = self._sheet[r][c]

        for row in range(len(self._pointer_sheet)):
            for col in range(len(self._pointer_sheet[row])):
                if self._pointer_sheet[row][col] == pointer_value:
                    self._pointer_sheet[row][col] = (row, col)
                    self._sheet[row][col] = None

        self._sheet[r][c] = sheet_value

    # condition 5
    def print(self, r: str, c: str):
        r = int(r) - 1
        c = int(c) - 1

        if self._sheet[r][c]:
            return self._sheet[r][c]
        else:
            return "EMPTY"


def solution(commands):
    sheet_width = 50  # 가로
    sheet_length = 50  # 세로
    pointer_sheet = [[(row, col) for col in range(sheet_width)] for row in range(sheet_length)]  # 포인터 시트 생성
    value_sheet = [[None for _ in range(sheet_width)] for __ in range(sheet_length)]  # 시트 생성
    control_sheet = ControlSheet(value_sheet, pointer_sheet)

    command_ouput_list = []
    for command in commands:
        func_name, *args = command.split(" ")

        if hasattr(ControlSheet, func_name.lower()):
            result = getattr(ControlSheet, func_name.lower())(control_sheet, *args)

            if result:
                command_ouput_list.append(result)
        else:
            raise

    return command_ouput_list
