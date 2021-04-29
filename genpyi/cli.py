import argparse
import os

from genmsg import MsgContext, command_line, msg_loader

from . import generator
from ._typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, Dict, List, Optional

    SrvMsgCallback = Callable[
        [str, List[str], Optional[str], Dict[str, List[str]]], None
    ]


def run_message(
    package,  # type: str
    package_files,  # type: List[str]
    outdir,  # type: Optional[str]
    search_paths,  # type: Dict[str, List[str]]
):
    # type: (...) -> None
    msg_context = MsgContext.create_default()

    for target_path in package_files:
        target_path = os.path.abspath(target_path)
        output_dir = outdir
        if output_dir is None:
            output_dir = os.path.abspath(os.path.join(target_path, os.path.pardir))

        generator.generate_stub(
            msg_context,
            msg_loader.load_msg_from_file,
            generator.generate_message_stub,
            package,
            target_path,
            output_dir,
            search_paths,
        )


def run_service(
    package,  # type: str
    package_files,  # type: List[str]
    outdir,  # type: Optional[str]
    search_paths,  # type: Dict[str, List[str]]
):
    # type: (...) -> None
    msg_context = MsgContext.create_default()

    for target_path in package_files:
        target_path = os.path.abspath(target_path)
        output_dir = outdir
        if output_dir is None:
            output_dir = os.path.abspath(os.path.join(target_path, os.path.pardir))

        generator.generate_stub(
            msg_context,
            msg_loader.load_srv_from_file,
            generator.generate_service_stub,
            package,
            target_path,
            output_dir,
            search_paths,
        )


def run_module(
    package_dir,  # type: str
    outdir,  # type: str
    module_finder,  # type: str
):
    # type: (...) -> None
    generator.generate_module_stub(package_dir, outdir, module_finder)


def _start_msg_srv(args):
    # type: (argparse.Namespace) -> None
    search_paths = command_line.includepath_to_dict(
        args.include_path
    )  # type: Dict[str, List[str]]
    args.handler(args.package, args.files, args.out_dir, search_paths)


def _start_module(args):
    # type: (argparse.Namespace) -> None
    package_dir = args.package_dir
    out_dir = args.out_dir
    if out_dir is None:
        out_dir = package_dir

    run_module(package_dir, out_dir, args.module_finder)


def _setup_module_options(parser):
    # type: (argparse.ArgumentParser) -> None
    parser.add_argument(
        "package_dir",
        type=str,
        help="Package directory to create __init__.pyi",
    )
    parser.add_argument(
        "--module-finder",
        type=str,
        choices=generator.GenPyModuleFinders.keys(),
        help=(
            "Method to find generated messages/services. "
            "(genmsg: Files with .msg, .srv would be regarded as modules. "
            "py: Python files starting with `_` would be regarded as modules.)"
        ),
        default="genmsg",
    )
    parser.add_argument(
        "--out-dir",
        type=str,
        help=(
            "Output directory. "
            "If the option is unset, __init__.pyi will be generated in the same "
            "directory as package_dir."
        ),
    )
    parser.set_defaults(func=_start_module)


def _setup_msg_srv_options(parser, handler):
    # type: (argparse.ArgumentParser, SrvMsgCallback) -> None
    parser.add_argument(
        "package", type=str, help="Package name of given files", default="out"
    )
    parser.add_argument("files", type=str, help="Files to generate stubs", nargs="+")
    parser.add_argument(
        "--out-dir",
        type=str,
        help=(
            "Output directory. "
            "If the option is unset, each stub file will be generated in the same "
            "directory as each input."
        ),
    )
    parser.add_argument(
        "--include-path",
        "-I",
        type=str,
        action="append",
        help="Include paths for processing given files",
    )
    parser.set_defaults(func=_start_msg_srv)
    parser.set_defaults(handler=handler)


def cli():
    # type: (...) -> None
    prog = "genpyi"
    parser = argparse.ArgumentParser(
        prog,
        description="""Generate python stub files from genmsg specs

Examples:
$ {0} msg custom_msgs custom_msgs/msg/Custom.msg
$ {0} msg sensor_msgs --out-dir out \\
    -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \\
    -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \\
    /opt/ros/melodic/share/sensor_msgs/msg/PointCloud2.msg
$ {0} srv custom_msgs custom_msgs/srv/Custom.msg
$ {0} srv nav_msgs --out-dir out \\
    -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \\
    -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \\
    /opt/ros/melodic/share/sensor_msgs/srv/SetCameraInfo.srv
$ {0} module custom_msgs/msg/""".format(
            prog
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparser = parser.add_subparsers()
    _setup_msg_srv_options(
        subparser.add_parser("msg", help="Generate stub files from .msg files"),
        run_message,
    )
    _setup_msg_srv_options(
        subparser.add_parser("srv", help="Generate stub files from .srv files"),
        run_service,
    )
    _setup_module_options(
        subparser.add_parser(
            "module", help="Generate __init__.pyi from a msg/srv directory"
        )
    )
    args = parser.parse_args()
    args.func(args)
