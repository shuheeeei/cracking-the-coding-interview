"""
((n & (n-1)) == 0) について説明してください（？）

１(10)を2の補数に変化した２進数は111(２)。

xxx & (xxx + 111)　←これが０になるので、
上記の式が成り立つのは、nを２進数に変換したときに左端の数のみが１になる数値

ex)
n = 4 のとき
((100 & (100 + 111)) == 0)
"""
