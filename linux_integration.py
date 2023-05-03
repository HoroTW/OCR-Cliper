import subprocess


def get_from_xclip(primary: bool = False, image: bool = False):
    selection = "c"  # DEFAULT_SELECTION
    if primary:
        selection = "p"  # PRIMARY_SELECTION

    command = ["xclip", "-selection", selection, "-o"]
    if image:
        command += ["-t", "image/png"]  # Pass mime as argument?
    p = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
    )
    stdout, stderr = p.communicate()
    # Intentionally ignore extraneous output on stderr when clipboard is empty
    if not image:
        return stdout.decode("utf-8")
    else:
        return stdout


def copy_to_xclip(text: str, primary: bool = False):
    selection = "p" if primary else "c"
    p = subprocess.Popen(
        ["xclip", "-selection", selection],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
    )
    p.communicate(input=text.encode("utf-8"))


def notify(title: str, message: str):
    subprocess.Popen(
        ["notify-send", title, message],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
    )
