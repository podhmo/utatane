import numpy as np
from utatane import as_command, subplot


def sample(N, sample_size=10 ** 5):
    xs = np.random.gumbel(1.5, 3.0, [sample_size, N])
    return xs[:, :].mean(1)


@as_command
def render(plt):
    def draw_guasian_curve(sample_data, bins):
        mu = sample_data.mean()
        sigma = sample_data.std()
        a = sample_data.size * (bins[1] - bins[0])
        plt.plot(
            bins, a / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(bins - mu) ** 2 / (2 * sigma ** 2)),
            'g-'
        )

    bins = np.linspace(-5, 15, 100)

    def draw(ax, n):
        xs = sample(n)
        ax.hist(xs, bins, color="g", alpha=0.5)
        ax.set_title("n={}".format(n))
        ax.set_xlabel("x")
        ax.set_ylabel("p(x)")
        ax.get_yaxis().set_ticks([])
        ax.get_xaxis().set_ticks([])
        draw_guasian_curve(xs, bins)

    with subplot(plt, ncols=2, nrows=2) as nth:
        with nth(1) as ax:
            draw(ax, 1)

        with nth(2) as ax:
            draw(ax, 3)

        with nth(3) as ax:
            draw(ax, 7)

        with nth(4) as ax:
            draw(ax, 20)
