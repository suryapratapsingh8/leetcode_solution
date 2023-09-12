# cook your dish here
def solve():
    veda_n = int(input())
    veda_s = input()
    veda_count_1 = 0
    for veda_char in veda_s:
        if veda_char == '1':
            veda_count_1 += 1
    veda_count_0 = veda_n - veda_count_1
    veda_ans = min(veda_count_1, veda_count_0)
    if veda_ans % 2 == 0:
        print("Ramos")
    else:
        print("Zlatan")
veda_t = int(input())
for _ in range(veda_t):
    solve()