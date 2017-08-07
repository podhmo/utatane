from utatane import as_command, get_parser


def get_parser_plus():
    parser = get_parser()
    parser.add_argument("-v", action="append", required=True, type=float)
    return parser


@as_command(parser=get_parser_plus())
def render(plt, args):
    plt.plot(range(len(args.v)), args.v)
