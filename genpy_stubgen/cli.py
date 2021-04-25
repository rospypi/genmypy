import argparse
import os
import sys

from genmsg import MsgContext, command_line, msg_loader

from . import generator
from ._typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, Dict, List, Optional

    CliHandler = Callable[
        [str, List[str], Optional[str], Dict[str, List[str]], bool], None
    ]


def run_message_stubgen(
    package,  # type: str
    package_files,  # type: List[str]
    outdir,  # type: Optional[str]
    search_paths,  # type: Dict[str, List[str]]
    no_initpyi=False,  # type: bool
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

        if not no_initpyi:
            generator.generate_pyi(output_dir)


def run_service_stubgen(
    package,  # type: str
    package_files,  # type: List[str]
    outdir,  # type: Optional[str]
    search_paths,  # type: Dict[str, List[str]]
    no_initpyi=False,  # type: bool
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

        if not no_initpyi:
            generator.generate_pyi(output_dir)


_FileKindMapping = {
    "srv": run_service_stubgen,
    "msg": run_message_stubgen,
}  # type: Dict[str, CliHandler]


def cli():
    # type: (...) -> None
    prog = "genpy_stubgen"
    parser = argparse.ArgumentParser(
        prog,
        description="""Generate python stub files from genmsg specs

Examples:
$ {0} msg custom_msgs custom_msgs/msg/Custom.msg
$ {0} msg std_msgs --out-dir out /opt/ros/melodic/share/std_msgs/msg/Header.msg
$ {0} msg sensor_msgs --out-dir out \\
    -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \\
    -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \\
    /opt/ros/melodic/share/sensor_msgs/msg/PointCloud2.msg
$ {0} srv custom_msgs custom_msgs/srv/Custom.msg
$ {0} srv nav_msgs --out-dir out \\
    -Istd_msgs:/opt/ros/melodic/share/std_msgs/msg \\
    -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/msg \\
    /opt/ros/melodic/share/sensor_msgs/srv/SetCameraInfo.srv""".format(
            prog
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "file_kind", help="Type of given files", choices=_FileKindMapping.keys()
    )
    parser.add_argument(
        "package", type=str, help="Package name of given files", default="out"
    )
    parser.add_argument("files", type=str, help="Files to generate stubs", nargs="+")
    parser.add_argument(
        "--out-dir",
        type=str,
        help=(
            "Output directory."
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
    parser.add_argument(
        "--no-init-pyi",
        action="store_true",
        help="Do not generate `__init__.pyi` file along with generated stub files",
    )
    args = parser.parse_args()

    func = _FileKindMapping[args.file_kind]
    search_paths = command_line.includepath_to_dict(
        args.include_path
    )  # type: Dict[str, List[str]]
    func(args.package, args.files, args.out_dir, search_paths, args.no_init_pyi)
