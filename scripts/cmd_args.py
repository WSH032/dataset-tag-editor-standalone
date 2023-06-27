import argparse
import logging

parser = argparse.ArgumentParser()

parser.add_argument(
    "--share",
    action="store_true",
    help="Launch gradio with share=True option and make accessible from internet",
    default=False,
)
parser.add_argument(
    "--port", type=int, help="Launch gradio with given port number", default=None
)
parser.add_argument(
    "--tls-key",
    type=str,
    help="Key file for TLS, also requires --tls-cert to enable TLS",
    default=None,
)
parser.add_argument(
    "--tls-cert",
    type=str,
    help="Certification file for TLS, also requires --tls-key to enable TLS",
    default=None,
)
parser.add_argument(
    "--gradio-debug",
    action="store_true",
    help="Launch gradio with debug option",
    default=False,
)
parser.add_argument(
    "--server-name", type=str, help="Host name of gradio server", default=None
)
parser.add_argument(
    "--auth",
    type=str,
    nargs="*",
    help='"username:password" pairs to accept in authenication',
    default=None,
)
parser.add_argument(
    "--device-id", type=int, help="CUDA Device ID to use interrogators", default=None
)
parser.add_argument(
    "--force-install-torch",
    choices=['cu117', 'cu118', 'cpu'],
    help="Force install the latest PyTorch with specified compute platform (if not installed in this computer)",
    default=None,
)

try:
    # 尝试从总ui配置中导入参数
    import modules.shared
    opts = modules.shared.cmd_opts
    logging.info(f"Tag-editor: Loaded cmd_opts from modules.shared.cmd_opts: {opts}")
except Exception as e:
    # 如果不行，就代表是独立启动，则自行从命令行中获取参数
    opts = parser.parse_args()
    logging.info(f"Tag-editor: Loaded cmd_opts from CMD: {opts}")
