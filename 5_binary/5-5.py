"""
((n & (n-1)) == 0) について説明してください（？）
１(10)を2の補数に変化した２進数は111
xxx & (xxx + 111)　←これが０になるので、
上記の式が成り立つのは、
nは２進数に変換すると、左端の数のみが１になる数値
n = 4 のとき
ex)
((100 & (100 + 111)) == 0)
"""
