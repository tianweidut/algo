class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        def backtrack(choices, state, points_cnt):
            if points_cnt > 4 or (points_cnt < 4 and not choices):
                return

            if points_cnt == 4 and not choices:
                results.append(".".join(state))
                return
       
            for idx in range(0, len(choices)):
                ip_slice = choices[0: idx + 1]
                if not self.is_valid(ip_slice):
                    continue
                state.append(ip_slice)
                backtrack(choices=choices[idx+1:], state=state, points_cnt=points_cnt+1)
                state.pop()

        backtrack(choices=s, state=[], points_cnt = 0)
        return results

    def is_valid(self, ip_item):
        if ip_item == "":
            return False

        if ip_item[0] == "0" and len(ip_item) > 1:
            return False

        return 0<= int(ip_item) <= 255

