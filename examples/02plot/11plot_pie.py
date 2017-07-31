from utatane import as_command


@as_command
def render(plt):
    from matplotlib.colors import colorConverter as c
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    colors = [c.to_rgba(x, alpha=0.5) for x in ["r", "g", "b", "y"]]
    plt.pie(sizes, labels=labels, startangle=90, colors=colors)
    plt.gca().axis('equal')
