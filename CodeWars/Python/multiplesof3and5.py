def solution(number):
    return((1.5*((number-1)//3 * ((number-1)//3+1))+2.5*((number-1)//5 * ((number-1)//5+1)))-7.5*(((number-1)//15 * ((number-1)//15+1))))
