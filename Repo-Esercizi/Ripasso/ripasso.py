
#1

def find_numbers():
    selected = []
    for x in range(2000, 3201):
        if x % 7 == 0 and x % 5 != 0:
            selected.append(x)
    return selected
result = find_numbers()
print(result)

#2

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n - 1)

n = 8
print(factorial(n))

#3

def factorial(n):
    
    fact =  1
    for factor in range(1, n + 1):
        fact *= factor
    
    return fact

mylist = [ 2, 5, 8, 10]
my_factorial = [factorial(x) for x in mylist]
print(my_factorial)

#4

def dictionary_numbers(n):
    return {i: i*i for i in range(1, n + 1)}

n = 8
result = dictionary_numbers(n)
print(result)

#5

def sort_words(input_string):
    words = input_string.split(',')
    sorted_words = sorted(words)
    result = ','.join(sorted_words)
    return result

input_string = "without,hello,bag,world"
output = sort_words(input_string)
print(output)

#6

def capitalize_sentences(sentences):
    capitalized_sentences = [sentence.upper() for sentence in sentences]
    return capitalized_sentences

input_sentences = ["Practice makes perfect", "hello world", "python programming"]
output_sentences = capitalize_sentences(input_sentences)

for sentence in output_sentences:
    print(sentence)

#7

