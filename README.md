# CalculatorKata

## Description

Create a simple String calculator with a method signature:

```
int Add(string numbers)
```

The method can take up to two numbers, separated by commas, and will return their sum. For example `“”` or `“1”`
or `“1,2”` as inputs.
For an empty string it will return 0.

## Steps

1. Start with the simplest test case of an empty string and move to 1 and two numbers
2. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
3. Remember to refactor after each passing test
4. Allow the Add method to handle an unknown amount of numbers
5. Allow the Add method to handle new lines between numbers (instead of commas).
    - the following input is ok:  “1\n2,3”  (will equal 6)
    - the following input is NOT ok:  “1,\n” (not need to prove it - just clarifying)
6. Support different delimiters
    - to change a delimiter, the beginning of the string will contain a separate line that looks like this:
      “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
    - the first line is optional. all existing scenarios should still be supported
7. Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was
   passed.
8. If there are multiple negatives, show all of them in the exception message.

--------------------TDD ASSESSMENT ENDS HERE-------------------

9. Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
10. Delimiters can be of any length with the following format:  “//[delimiter]\n” for example: “//[***]\n1***2***3”
    should return 6
11. Allow multiple delimiters like this:  “//[delim1][delim2]\n” for example “//[*][%]\n1*2%3” should return 6.
12. Make sure you can also handle multiple delimiters with length longer than one char