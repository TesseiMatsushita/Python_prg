# 単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

text = text.replace(',', "")
text = text.replace(';', "")
text = text.replace('.', "")
print(text)
#split関数を使用して英単語を抜き出す
words = text.split()
print(words)

counter = {}
for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

#「セット:登場回数」のディクショナリを作成して表示する
print(words.count(words))