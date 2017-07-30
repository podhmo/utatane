import numpy as np
from utatane import as_command


def sample(N, sample_size=10 ** 5):
    xs = np.random.gumbel(1.5, 3.0, [sample_size, N])
    return xs[:, :].mean(1)


@as_command
def render(plt):
    def draw_guasian_curve(sample_data, bins):
        mu = sample_data.mean()
        sigma = sample_data.std()
        a = sample_data.size * (bins[1] - bins[0])
        plt.hold(True)
        plt.plot(
            bins, a / (np.sqrt(2 * np.pi) * sigma) * np.exp(-(bins - mu) ** 2 / (2 * sigma ** 2)),
            'b-'
        )

    bins = np.linspace(-5, 15, 100)
    xs = sample(1)
    plt.hist(xs, bins)
    plt.xlabel("x")
    plt.ylabel("p(x)")
    draw_guasian_curve(xs, bins)
