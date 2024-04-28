# this module contain the AntiVirus class and the main logic behind the program
import platform
import subprocess
import time
import ui
from utils import Scanner, Drive
from tkinter import Tk, messagebox

# default configuration
config = {
    "bad_endings": [".py", ".exe", ".js", ".java", ".ts", ".inf", ".bat", ".cmd"],
    "check_exe": True,
    "bad_names": ["autorun", "autoplay"],
}


class AntiVirus:
    def __init__(self):
        ui.lunch(config)
        self.scanner = Scanner(config)
        self.os = platform.system()
        self.window = Tk()
        self.window.withdraw()
        self.connected_drives = []

    # start the Anti-Virus: find out the OS and trigger the co-responding method
    def start(self) -> None:
        if self.os == "Windows":
            self._win_av()
        elif self.os == "Linux":
            self._lin_av()
        else:
            messagebox.showinfo(
                title="OS Not Supported",
                message=f"{self.os} is not supported in this anti virus"
            )

    # the Windows Anti-Virus logic
    def _win_av(self) -> None:
        ui.start_popup(self.window)
        print("Anti-Virus is active and scanning...")
        while True:  # listener
            try:
                out = subprocess.check_output(args='wmic logicaldisk get DriveType, caption, VolumeSerialNumber',
                                              shell=True)  # question the OS about its connected drive directly
                shell_lines = out.decode('utf-8').strip().split('\r\r\n')[1::]
                drives = [Drive(shell_line=shell_line) for shell_line in shell_lines]
                flash_drives = [drive for drive in drives if drive.is_flash_drive()]
                self._update_connected_devices(flash_drives)
                [self._handle(flash_drive) for flash_drive in flash_drives if flash_drive not in self.connected_drives]
                time.sleep(1)
            except KeyboardInterrupt:
                break
        ui.end_popup(self.window)

    # the Linux Anti-Virus logic
    def _lin_av(self) -> None:
        import pyudev  # only work on linux
        ui.start_popup(self.window)
        print("Anti-Virus is active and scanning...")
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='block', device_type='disk')
        try:
            for device in iter(monitor.poll, None):  # listener
                if device.action == 'add':
                    time.sleep(0.5)  # give linux time to mount the drive
                    block_dev_path = device.device_node
                    result = subprocess.run(["lsblk", block_dev_path], capture_output=True, text=True)
                    try:
                        path = result.stdout.split()[-1]  # get the mount point
                    except IndexError:
                        continue

                    d_name = path
                    d_type = 2
                    d_id = path.split("/")[-1]

                    flash_drive = Drive(d_name=d_name, d_type=d_type, d_id=d_id)
                    self._handle(flash_drive)
        except KeyboardInterrupt:
            pass
        ui.end_popup(self.window)

    # add the new drive to the connected drives, notify the user and asks him if he wants to scan it
    def _handle(self, flash_drive: Drive) -> None:
        self.connected_drives.append(flash_drive)
        should_scan = messagebox.askyesno(
            title="New Flash Drive Detected",
            message=f"A new flash drive named '{flash_drive.name}' detected\n"
                    f"Do you want to scan it?"
        )
        if should_scan:
            self._scan(flash_drive)

    # uses Scanner from util to scan the flash drive, notify the user if there isn't potential threats else handles them
    def _scan(self, flash_drive: Drive) -> None:
        pot_threats = self.scanner.scan(flash_drive)
        if len(pot_threats) == 0:
            messagebox.showinfo(
                title="Scanning Complete",
                message=f"The scan of '{flash_drive.name}' is complete\n"
                        f"There is no potential threats"
            )
        else:
            self._handle_threats(flash_drive, pot_threats)

    # notify the user about the threats and asks if he wants to deal with them
    def _handle_threats(self, flash_drive: Drive, pot_threats: list[str]) -> None:
        # if else block for the visual representation of the threats
        if len(pot_threats) > 10:
            pot_threats_str = "\n".join(f"*{path}" for path in pot_threats[:10]) + ("\n."*3)
        else:
            pot_threats_str = "\n".join(f"*{path}" for path in pot_threats)
        further_action = messagebox.askyesno(
            title="Scanning Complete",
            message=f"The scan of '{flash_drive.name}' is complete\n"
                    f"--------------------------------------------\n"
                    f"Found {len(pot_threats)} potential threats:\n"
                    f"{pot_threats_str}\n"
                    f"--------------------------------------------\n"
                    f"Do you want to take further action?"
        )
        if further_action:
            self._deal(pot_threats)

    def _update_connected_devices(self, curr_connected_flash_drives: list[Drive]) -> None:
        self.connected_drives = [flash_drive for flash_drive in self.connected_drives
                                 if flash_drive in curr_connected_flash_drives]

    # prompt the menu from ui module that deals with the threats with a gui
    def _deal(self, pot_threats: list[str]) -> None:
        ui.menu(pot_threats, on_remove=self.remove)

    # the func that being triggered once the user decide to remove files that been prompts in the menu
    def remove(self, files_to_remove: list[str]) -> list[bool] | bool | None:
        if len(files_to_remove) == 0:
            messagebox.showinfo(
                title="No Selected Files",
                message="There is no selected files ro remove"
            )
            return

        files_str = "\n".join(f"*{file}" for file in files_to_remove)
        remove = messagebox.askyesno(
            title="Just Making Sure",
            message=f"Are you sure wo want to delete the following files?\n{files_str}?"
        )
        if remove:
            results = []
            for file in files_to_remove:
                try:
                    self.scanner.remove(file)
                    results.append(True)
                except OSError:
                    results.append(False)
                    messagebox.showinfo(
                        title="Error Removing File",
                        message=f"Could not remove {file} duo to an OSError."
                    )

            return results
        else:
            return False
