
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


def string_count(string):
        # dictionary counter
        string = {}

        for str in string:
            if str in string:
                 string[str] +=1
            elif i not in dict:
                 string[str] = 1
            else:
                 return {}

        return string


print(string_count("aabb"))
