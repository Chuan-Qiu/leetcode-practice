class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_sort_key(logs):
            key, val = logs.split(" ", 1)

            if val[0].isnumeric():
                return (1,)
            else:
                return (0, val, key)

        return sorted(logs, key=get_sort_key)
