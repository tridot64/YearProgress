import matplotlib.pyplot as plt


def year_make(list_val):
    ans = 0
    true_val = []
    for i in list_val:
        ans = ans + int(i)
        true_val.append(ans)
    return true_val


def calcu_year(list_val):
    ans = 0
    list_v = [int(i)*0.01 for i in list_val]
    for i in list_v:
        ans = ans + i
    return ans

with open("test.txt", "r") as f:
    comma_sep = f.readline()
    value_list = comma_sep.split(",")
    value_list.pop()
    to_print = year_make(value_list)
    plt.title("Improvement of " + str(calcu_year(value_list)))
    plt.plot(to_print)
    plt.show()

