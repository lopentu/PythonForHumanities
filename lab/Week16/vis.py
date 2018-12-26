import random
import matplotlib.pyplot as plt

def generate_data():
    N = 1000
    c = [0]; x = []; y = []; s = []; w = []
    for _ in range(N):
        c.append(c[-1] + random.normalvariate(0, 1))
        x.append(random.normalvariate(0, 1))
        y.append(random.normalvariate(0, 1))
        s.append(random.randint(0, 5)*10)
        w.append(random.randint(0, 9))

    return {"serial": list(range(len(x))),
            "xdata": x, "ydata": y, "cdata": c[1:],
            "wdata": w, "sdata": s}

def prepare_data(opts):
    if not opts["X"]:
        plot_data = generate_data()
    else:
        plot_data = {}
        plot_data["xdata"] = opts["X"]
        if opts["Y"]:
            plot_data["ydata"] = opts["Y"]
        plot_data["serial"] = list(range(len(opts["X"])))
        plot_data["cdata"] = opts["X"]
        plot_data["wdata"] = [1] * len(opts["X"])
        plot_data["sdata"] = [20] * len(opts["X"])

    return plot_data

def visualize_data(ctype, plot_data):
    if ctype == "line":
        plt.plot("serial", "cdata", '-', data=plot_data)
    elif ctype == "scatter":
        plt.scatter("xdata", "ydata",
                    c="wdata", s="sdata",
                    cmap="Set1", data=plot_data)
    elif ctype == "boxplot":
        plt.boxplot("xdata", data=plot_data, vert=False)
        plt.yticks([1], ["xdata"])
    elif ctype == "hist":
        plt.hist("xdata", data=plot_data)
        plt.title("Histogram")
    elif ctype == "bar":
        plt.bar("serial", "xdata", data=plot_data)
    else:
        print("not supported chart type")

def make_figure(opts, chart_type):
    plot_data = prepare_data(opts)
    visualize_data(chart_type, plot_data)

def show_data_menu():
    print("輸入資料（以逗號分隔）")
    print("若無第二變項，則直接按Enter略過：")
    print("若兩變項資料都未輸入，則使用自動產生的資料：")
    xinput = input("輸入變項一資料: ")
    yinput = input("輸入變項二資料: ")
    xdata = []
    ydata = []
    if xinput:
        xdata = [float(x) for x in xinput.split(",")]
    if yinput:
        ydata = [float(y) for y in yinput.split(",")]

    opts = {"X": xdata, "Y": ydata}

    return opts

def show_chart_menu():
    chart_dict = {
        "line": "折線圖(line chart)",
        "scatter": "散佈圖(scatter plot)",
        "boxplot": "箱形圖(boxplot)",
        "hist": "直方圖(histogram)",
        "bar": "長條圖(bar chart)"}

    print("圖表類型：")
    for idx, chart_names in enumerate(chart_dict.values()):
        print("{}. {}".format(idx+1, chart_names))
    print("Q. (離開)")

    chart_in = input("> ")
    if chart_in.lower() == "q":
        return chart_in.lower()
    else:
        chart_keys = list(chart_dict.keys())
        chart_type = chart_keys[int(chart_in or 1)-1]
        return chart_type

def main():
    print("--- 看見Python ---")
    data_opts = show_data_menu()
    while True:
        chart_type = show_chart_menu()
        if chart_type == "q":
            break
        make_figure(data_opts, chart_type)
        print("（請關掉圖形後繼續）")
        plt.show()

if __name__ == "__main__":
    main()
