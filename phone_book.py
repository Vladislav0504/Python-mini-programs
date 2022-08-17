from sys import stdin


def main():
    n = int(input())
    phone_book = {}
    for line in stdin:
    	oper = line.split()
    	if oper[0] == 'add':
    		phone_book[oper[1]] = oper[2]
    	elif oper[0] == 'find':
    		print(phone_book.get(oper[1], 'not found'))
    	else:
    		phone_book.pop(oper[1], 'not found')


if __name__ == '__main__':
    main()
