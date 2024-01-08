class A:
    def roll(self, k, n):
        self.memo = {}
        import sys

        def _do_roll(r, h):
            if r == 0 or h == 0:
                return 0
            if r == 1 or h == 1:
                return h

            if (r, h) not in self.memo:
                res = sys.maxsize
                lo, hi = 1, h
                while lo <= hi:
                    mid = (lo + hi) // 2
                    b_cnt = _do_roll(r-1, mid - 1)
                    nb_cnt = _do_roll(r, h - mid)

                    if b_cnt > nb_cnt:
                        hi = mid - 1
                        res = min(res, b_cnt + 1)
                    else:
                        lo = mid + 1
                        res = min(res, nb_cnt + 1)

                self.memo[(r, h)] = res

            return self.memo[(r, h)]

        return _do_roll(k, n)


if __name__ == "__main__":
    print(A().roll(1, 2))
    print(A().roll(2, 6))
    print(A().roll(3, 14))
