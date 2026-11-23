kostka_foulkes(shape, content, t=Symbol('t'))
    sum(t**charge(reading_word(T)) for T in SSYT(shape, content)) as a SymPy expression, S.Zero if there is no such T

    float, complex or Decimal t is sympified first

    must handle every content when: sum(shape) <= 16; or shape == (n,) or (1,) * n with n <= 2000; or sum(shape) <= 30 and content[6:] is all 1s

charge(word)
    Lascoux-Schutzenberger charge of word (up to 2000 letters), a tuple of positive integers with content(word) a partition

    charge(word) == sum of index over each standard subword (right-to-left), index(1) == 0, index(r + 1) == index(r) + (pos(r + 1) > pos(r))

IntegerPartition.kostka_foulkes(content, t) == kostka_foulkes(self, content, t)

Parts: () or a weakly decreasing tuple of positive integers (shape and content); an IntegerPartition works wherever Parts does

SSYT(shape, content) denotes the fillings T of the cells (i, j) with j < shape[i] by integers >= 1, T[i][j] <= T[i][j + 1], T[i][j] < T[i + 1][j] where both cells exist, and content[i] == number of entries equal to i + 1
reading_word(T) denotes tuple(x for row in reversed(T) for x in row)

module sympy.combinatorics.tableaux (new); kostka_foulkes and charge are exported from sympy.combinatorics
