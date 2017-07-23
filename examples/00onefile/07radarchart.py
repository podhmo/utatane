from utatane import as_command, yield_fixture, subplot
from utatane.decoration import create_radar_projection


@yield_fixture
def data():
    labels = ["面白さ", "わかりやすさ", "手軽さ", "フォ-マルさ", "学習効果?", "zzz"]
    data = [
        [12, 14, 18, 9, 9],
        list(reversed([12, 14, 18, 9, 9])),
        [13, 13, 13, 13, 13],
    ]
    yield {"data": data, "labels": labels}


@as_command(legend=None)
def main(plt, *, data, labels):
    radar, theta = create_radar_projection(5, frame="polygon")

    with subplot(plt, nrows=2, ncols=1) as nth:
        with nth(1, projection=radar):
            plt.plot(theta, data[0], "b", label="あ")
            plt.fill(theta, data[0], facecolor="b", alpha=0.25)
            plt.plot(theta, data[1], "g", label="い")
            plt.fill(theta, data[1], facecolor="g", alpha=0.25)
            plt.plot(theta, data[2], "r", label="う")
            plt.fill(theta, data[2], facecolor="r", alpha=0.25)
            plt.gca().set_varlabels(labels)
            plt.legend(loc=(0.9, .95), labelspacing=0.1, fontsize='small')
        with nth(2, projection=radar):
            plt.plot(theta, data[0], "b", label="A")
            plt.fill(theta, data[0], facecolor="b", alpha=0.25)
            plt.plot(theta, data[1], "g", label="B")
            plt.fill(theta, data[1], facecolor="g", alpha=0.25)
            plt.plot(theta, data[2], "r", label="C")
            plt.fill(theta, data[2], facecolor="r", alpha=0.25)
            plt.gca().set_varlabels(labels)
            plt.legend(loc=(0.9, .95), labelspacing=0.1, fontsize='small')
