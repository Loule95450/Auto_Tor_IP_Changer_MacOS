import tkinter as tk
import autoTOR as auto


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AutoTOR")
        self.window.geometry("200x400")

        self.title_label = tk.Label(
            self.window, text="AutoTOR", padx=20, pady=20, font=("Arial", 21)
        )
        self.title_label.pack(padx=10, pady=10)

        self.vpn_button = tk.Button(
            self.window,
            text="VPN ON" if auto.run_autoTOR else "VPN OFF",
            command=self.toggle_vpn,
        )
        self.vpn_button.pack(padx=10, pady=10)

        self.change_button = tk.Button(
            self.window,
            text="Change actual IP",
            command=self.change_ip,
            state="normal" if auto.run_autoTOR else "disable",
        )
        self.change_button.pack(padx=10, pady=10)

        self.loop_button = tk.Button(
            self.window,
            text="Loop ON" if auto.loop_mode else "Loop OFF",
            command=self.toggle_loop,
        )
        self.loop_button.pack(padx=10, pady=10)

        self.loop_time_var = tk.StringVar()
        self.loop_time_var.trace("w", self.set_loop_time)
        self.loop_time_var.set("300")

        self.loop_time = tk.Entry(self.window, textvariable=self.loop_time_var)
        self.loop_time.pack(padx=10, pady=10)

        self.window.mainloop()

    def toggle_vpn(self):
        auto.switch_autoTOR()
        self.change_button.config(state="normal" if auto.run_autoTOR else "disable")
        self.vpn_button.config(text="VPN ON" if auto.run_autoTOR else "VPN OFF")

    def toggle_loop(self):
        auto.switch_loop()
        self.loop_button.config(text="Loop ON" if auto.loop_mode else "Loop OFF")

    def set_loop_time(self, *args):
        auto.loop_time = int(self.loop_time_var.get())

    def change_ip(self):
        auto.change_ip()


if __name__ == "__main__":
    auto.tor_status()
    app = App()
