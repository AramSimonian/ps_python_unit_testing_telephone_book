
class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        names = list(self.entries.keys())
        nums = list(self.entries.values())
        
        def dupe_name(self, name):
            return (names.count(name) > 1)

        def dupe_num(self, num):
            return (nums.count(num) > 1)

        def dupe_prefix(self, original_num):
            prefix_is_dupe = False
            for num in nums:
                if num != original_num:
                    if num[:len(original_num)] == original_num:
                        prefix_is_dupe = True
            return prefix_is_dupe

        if len(self.entries) == 0:
            return True
        else:
            dup_name_count = (len(list(name for name in names if dupe_name(self, name))))
            dup_num_count = (len(list(num for num in nums if dupe_num(self, num))))
            dup_prefix_count = (len(list(num for num in nums if dupe_prefix(self, num))))

            return (dup_name_count + dup_num_count + dup_prefix_count) == 0

    
