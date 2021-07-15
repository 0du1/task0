from random import randint

src = [randint(-100, 100) for _ in range(30)]
print(f'Source list: {src}')
maxint = max(src)
print('Max item: {} by the index of {}'.format(maxint, src.index(maxint)))
odds = sorted([num for num in src if num % 2], reverse=True)
if not odds:
    print('Odd numbers not found')
else:
    print(odds)

