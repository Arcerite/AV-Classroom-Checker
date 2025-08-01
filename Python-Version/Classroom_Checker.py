"""
Description: The following Python script will automate the classroom checks and offers some documents in the event of an error

Author: Caleb Peters/Arcerite

Version: 1.5 : Python 3.13.1

Date 5/30/25
"""

import os
import webbrowser
import socket
import sys
import winsound


def prompter(message: str) -> bool:
    """
    Prompt the user with a yes/no question.

    Args:
        message (str): The prompt message.

    Returns:
        bool: True if the user responds positively, False otherwise.
    """
    response = None
    while response is None:
        response = input(f"{message} (Y/N)\n: ").strip().lower()
        if response in {"y", "yes"}:
            return True
        elif response in {"n", "no"}:
            return False
        else:
            response = None
    return False


def clear() -> None:
    """Clear the console screen."""
    os.system('cls')


def intro() -> None:
    """Display the welcome message and instructions."""
    clear()
    print("Welcome to the classroom check walkthrough!")
    print("This command prompt window will have instructions and guide you through the process!")
    input("Press enter to continue")


def audio_check() -> bool:
    """
    Play a test sound and verify speaker output.

    Returns:
        bool: True if the sound is working correctly, False otherwise.
    """
    clear()
    print("Testing Audio...")
    print("Audio is playing. Please ensure it is coming from the room speakers (not the computer).")
    print("You may need to increase the volume on the button panel. Ensure it's set to PC.")

    try:
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        wav_path = os.path.join(base_path, "sound_test.wav")

        while True:
            done = input("Press 'd' to end the loop. Press any other key to play the sound again\n")
            if done.lower() == "d":
                break
            winsound.PlaySound(wav_path, winsound.SND_FILENAME)
        return prompter("Is the sound working?")
    except Exception as e:
        print(f"Error with sound: {e}")
        input("Press enter to continue")
        return False


def camera_check() -> bool:
    """
    Open the camera app and prompt the user to verify functionality.

    Returns:
        bool: True if the camera is working, False otherwise.
    """
    clear()
    print("Say Cheese! Camera test!")
    try:
        os.system("start microsoft.windows.camera:")
        return prompter("Is the camera working?")
    except Exception as e:
        print(f"Error with camera: {e}")
        input("Press enter to continue")
        return False


def mfa_override_test() -> bool:
    """
    Open a website to test Duo MFA bypass and provide IP address if needed.

    Returns:
        bool: True if the Duo bypass is working, False otherwise.
    """
    clear()
    print("Testing Duo Bypass...")
    print("A website will open. Log in and follow the Duo prompt.")
    print("If prompted to check your phone, the answer is NO.")
    print("If it skips the phone prompt, the answer is YES.")
    try:
        webbrowser.open("https://my.gvsu.edu/")
        result = prompter("Is Duo Bypass working?")
        if not result:
            print("To set up Duo Bypass, we need your device IP:")
            ip_address = socket.gethostbyname(socket.gethostname())
            print(f"Your IP address is: {ip_address}")
            input("Press enter once you've noted it down")
        return result
    except Exception as e:
        print(f"Error with MFA: {e}")
        input("Press enter to continue")
        return False


def results(audio: bool, elmo: bool, camera: bool, duo: bool) -> None:
    """
    Print the results of the system checks.

    Args:
        audio (bool): Audio check result.
        elmo (bool): Elmo (doc cam) check result.
        camera (bool): Camera check result.
        duo (bool): MFA Duo override check result.
    """
    clear()
    print("Test                 \t Results")
    print("----------------------------------------")
    print(f"Audio Check         \t {audio}")
    print(f"Camera Check        \t {camera}")
    print(f"Elmo Check          \t {elmo}")
    print(f"Duo Bypass Check  \t {duo}")
    input("Press enter to continue")


def troubleshoot(ac: bool, ec: bool, cc: bool, oc: bool) -> None:
    """
    Offer troubleshooting PDF help if any tests failed.

    Args:
        ac (bool): Audio check result.
        ec (bool): Elmo (doc cam) check result.
        cc (bool): Camera check result.
        oc (bool): MFA Duo override check result.
    """
    def open_pdf(filename: str) -> None:
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, filename)
        os.startfile(file_path)

    if not cc and prompter("Do you want to open a PDF to help troubleshoot the camera?"):
        open_pdf("Camera.pdf")
        cc = camera_check()

    if not ac and prompter("Do you want to open a PDF to help troubleshoot the sound?"):
        open_pdf("Audio.pdf")
        ac = audio_check()

    if not ec and prompter("Do you want to open a PDF to help troubleshoot the doc cam?"):
        open_pdf("Elmo.pdf")
        ec = elmo_check()

    results(ac, ec, cc, oc)


def elmo_check() -> bool:
    """
    Open the Elmo (doc cam) website and prompt for confirmation.

    Returns:
        bool: True if the Elmo/doc cam is working, False otherwise.
    """
    clear()
    print("Testing doc cam USB...")
    print("A website will open. Allow access if prompted.")
    print("You may need to close a pop-up box.")
    webbrowser.open("https://imagemate-c.com/")
    return prompter("Is the doc cam working?")


if __name__ == "__main__":
    intro()
    audio_result = audio_check()
    camera_result = camera_check()
    elmo_result = elmo_check()
    duo_result = mfa_override_test()
    troubleshoot(audio_result, elmo_result, camera_result, duo_result)
