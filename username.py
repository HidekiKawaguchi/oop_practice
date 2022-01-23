"""
データ型の宣言: UserName
    属性:
        実際のユーザー名
    ルール:
        ユーザ名は4文字以上20文字以内である
    できること:
        ユーザ名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        #nameのチェック
        if not 4 <= len(name) <= 20:
            raise ValueError(f'{name}はルール違反です')
        self.name = name

    def battle_name(self):
        return self.name.upper()


bob = UserName(name='Bob Smith')
print(bob.name)
print(bob.battle_name())