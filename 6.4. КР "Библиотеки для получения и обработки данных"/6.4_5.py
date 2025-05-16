import matplotlib.pyplot as plt


def apples(*args, color=None, kind='bar'):
    names = []
    counts = []
    for arg in args:
        if isinstance(arg, tuple) and len(arg) == 2:
            names.append(arg[0])
            counts.append(arg[1])
    plt.figure()
    if kind == 'barh':
        plt.barh(names, counts, color=color)
    else:
        plt.bar(names, counts, color=color)
    plt.title('Apples')
    plt.legend().remove()
    plt.savefig('result.png')
    plt.close()
