def squareSequenceDigit(n):
    original_num = int(149162536496481100121144169196)
    copy_num = original_num
    counter_number = 0
    
    while copy_num > 0:
        copy_num = copy_num // 10
        counter_number += + 1 #находим число цифр в числе
        
    difference = counter_number - n # находим разность для степени
    temp = original_num // (10**difference)
    result = temp % 10
    return result


if __name__ == '__main__':
    print(squareSequenceDigit(1))
    print(squareSequenceDigit(2))
    print(squareSequenceDigit(7))
    print(squareSequenceDigit(12))
    print(squareSequenceDigit(17))
    print(squareSequenceDigit(27))