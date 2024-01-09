import platform, subprocess
import time

from utils import Scanner, Drive
from tkinter import Tk, messagebox


class AntiVirus:
    def __init__(self):
        self.scanner = Scanner()
        self.os = platform.system()
        self.window = Tk()
        self.window.withdraw()
        self.connected_drives = []

    def start(self):
        if self.os == "Windows":
            self.win_av()
        elif self.os == "Linux":
            self.lin_av()
        else:
            messagebox.showinfo(
                title="OS Not Supported",
                message=f"{self.os} is not supported in this anti virus"
            )

    def win_av(self):
        print("Anti Virus Starting...\nPress Ctrl+C To Exit")
        while True:
            try:
                out = subprocess.check_output(args='wmic logicaldisk get DriveType, caption, VolumeSerialNumber',
                                              shell=True)
                shell_lines = out.decode('utf-8').strip().split('\r\r\n')[1::]
                flash_drives = [Drive(shell_line) for shell_line in shell_lines if Drive(shell_line).is_flash_drive()]
                self.update_connected_devices(flash_drives)
                [self.handle(flash_drive) for flash_drive in flash_drives if flash_drive not in self.connected_drives]
                time.sleep(1)
            except KeyboardInterrupt:
                break
        print("Anti Virus Ending...")

    def lin_av(self):
        messagebox.showinfo(
            title="Linux not supported yet",
            message="Linux os is yet to be supported by this anti virus"
        )

    def handle(self, flash_drive):
        self.connected_drives.append(flash_drive)
        should_scan = messagebox.askyesno(
            title="New Flash Drive Detected",
            message=f"A new flash drive named {flash_drive.name} detected\nDo you want to scan it?"
        )
        if should_scan:
            pot_threats = self.scanner.scan(flash_drive.name)
            for dir_name in pot_threats:
                further_action = messagebox.askyesno(
                    title="Potential Threat Detected",
                    message=f"{flash_drive.name} has a file called {dir_name} that may be harmful\n"
                            f"do you want to take further action?"
                )
                if further_action:
                    self.deal(flash_drive, dir_name)

    def update_connected_devices(self, curr_connected_flash_drives):
        self.connected_drives = [flash_drive for flash_drive in self.connected_drives
                                 if flash_drive in curr_connected_flash_drives]

    def deal(self, flash_drive, dir_name):
        print(f"Dealing with bad file at {flash_drive.name}/{dir_name}")