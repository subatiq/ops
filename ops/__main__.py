from typing import Any

import typer
import yaml
from typer import Typer

from ops.communicator import get_machines_with_state, load_config, set_config

logo = """
                             ./#&@@@@@@@@@@@@&%(,
                       .(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*
                   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
                #@@@@@@@@@@@@@@@@@@@%(****/#&@@@@@@@@@@@@@@@@@@@,
             /@@@@@@@@@@@@@%,                      ./@@@@@@@@@@@@@&
           %@@@@@@@@@@@(                                ,&@@@@@@@@@@@*
         %@@@@@@@@@@*                                       %@@@@@@@@@@,
       *@@@@@@@@@&                                            *@@@@@@@@@@
      %@@@@@@@@&         (&@@@@@@@@@@(                          *@@@@@@@@@*
     &@@@@@@@@,     ,&@@@@@@@@@@@@@#                              %@@@@@@@@(
    &@@@@@@@@    .@@@@@@@@@@@@@@@@/                                /@@@@@@@@/
   %@@@@@@@@   *@@@@@@@@@@@@@@@@@@                                  /@@@@@@@@.
  .@@@@@@@@. .@@@@@@@@@@@@@@@@@@@@                                   &@@@@@@@&
  %@@@@@@@@ /@@@@@@@@@@@@@@@@@@@@@(                                   @@@@@@@@
  &@@@@@@@/*@@@@@@@@@@@@@@@@@@@@@@@#                    /&            @@@@@@@@*
  &@@@@@@@,@@@@@@@@@@@@@@@@@@@@@@@@@@%                /@@@#           @@@@@@@@/
  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.         &@@@@@@           @@@@@@@@,
  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*         #@@@@@          ,@@@@@@@@
   @@@@@@@@@@@%.  ,&@@%,,#. .&@@@(.  .(@@@@*         %@@@@@          @@@@@@@@%
   (@@@@@@@@@  /@@.  @%  %@%  &@,  #@@@@@@@@@.     *@@@@@@#         %@@@@@@@@
    %@@@@@@@@  (@@,  @%  %@%  &@@@&%,  #@@@@(*&@@@@@@@@@@&         %@@@@@@@@,
     %@@@@@@@@,    /@@%  .   %@@*     /@@@@#  *@@@@@@@@@@        .@@@@@@@@@,
      (@@@@@@@@@@@@@@@%  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%        %@@@@@@@@@.
       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        &@@@@@@@@@#
         *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       /@@@@@@@@@@@
           *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.     .#@@@@@@@@@@@&
              &@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(     .(@@@@@@@@@@@@@@/
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(
                    *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.
                         /&@@@@@@@@@@@@@@@@@@@@@@@@@@@#,
                                 ,/#%&&&&&&&%(*.
________________________________________________________________________________
"""


app = Typer()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Get a list of all machines in the fleet
    """
    if ctx.invoked_subcommand is not None:
        return
    print(logo)
    print("For help, use --help")


def kbytes2gb(bytes):
    return round(bytes / 1024 / 1024, 1)


def build_machines_list(machines: list[dict[str, Any]], compact: bool = False):
    if not machines:
        print("No free machines")
        return

    print("Free machines:\n")
    for machine in machines:
        if compact:
            print(
                f"{machine['ip']}\t{machine['hostname']}\t{machine['processor']['name']}"
            )
            continue
        machine["ram"]["total"] = str(kbytes2gb(machine["ram"]["total"])) + " GB"
        machine["ram"]["free"] = str(kbytes2gb(machine["ram"]["free"])) + " GB"
        print("-" * 20)
        print(
            yaml.dump(
                {
                    key: param
                    for key, param in machine.items()
                    if key not in ["containers", "state"]
                }
            )
        )
        if machine["containers"]:
            print("containers:")
            print(yaml.dump(machine["containers"]))
    print("-" * 20)


@app.command()
def free(compact: bool = False):
    """
    Show a list of free machines
    """
    machines = get_machines_with_state("free")
    build_machines_list(machines, compact)


@app.command()
def busy(compact: bool = False):
    """
    Show a list of free machines
    """
    machines = get_machines_with_state("busy")
    build_machines_list(machines, compact)


@app.command()
def setup():
    """
    Set server configuration
    """
    ip = input("Enter the ip address of the opservatory instance: ")
    port = int(input("Enter the port of the opservatory instance [80]: ") or 80)
    set_config({"host": ip, "port": port})


@app.command()
def config():
    """
    Show server configuration
    """
    print("Server configuration:")
    config = load_config()
    print(yaml.dump(config))


def run():
    app()


if __name__ == "__main__":
    run()
