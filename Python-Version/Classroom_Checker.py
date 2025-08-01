"""
Description: The following Python script will automate the classroom checks and offers some documents in the event of an error

Author: Caleb Peters/Arcerite

Version: 2.0 Python : Python 3.13.1

Date 8/1/25
"""

import os
import webbrowser
import socket
import sys


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
    Opens the Windows Sound Settings to allow manual speaker test.

    Returns:
        bool: True if the sound is working correctly, False otherwise.
    """
    clear()
    print("Testing Audio...")
    print("The Sound Control Panel will now open.")
    print("Please click on the 'Playback' tab, select the correct output, and use the 'Test' button to confirm sound.")
    print("You may need to increase the volume on the button panel. Ensure it's set to PC.")

    try:
        os.system("control mmsys.cpl sounds")
    except Exception as e:
        print(f"Error opening sound settings: {e}")
        input("Press enter to continue")
        return False

    return prompter("Is the sound working?")


def camera_check(mode: int = 0) -> bool:
    """
    Open the camera app and prompt the user to verify functionality.

    Args:
        mode (int): 0 for normal camera, 1 for doc cam.

    Returns:
        bool: True if the camera is working, False otherwise.
    """
    clear()
    print("Say Cheese! Camera test!")
    try:
        if mode == 0:
            os.system("start microsoft.windows.camera:")
            return prompter("Is the camera working?")
        else:
            print("In the top right corner of the camera app should be an option to swap cameras.")
            print("Please do so and check if Elmo is an option. It may show a white screen initially; give it a few seconds.")
            return prompter("Is the doc cam working?")
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
    print(f"Duo Bypass Check    \t {duo}")
    input("Press enter to continue")


def troubleshoot(ac: bool, ec: bool, cc: bool, oc: bool) -> None:
    """
    Offer troubleshooting help if any tests failed.

    Args:
        ac (bool): Audio check result.
        ec (bool): Elmo (doc cam) check result.
        cc (bool): Camera check result.
        oc (bool): MFA Duo override check result.
    """
    if prompter("Would you like help troubleshooting?"):

        if not cc:
            print("***CAMERA HELP***\n\n\tCheck to see the camera is plugged into the computer, try replugging it into its current port.")
            print("If that doesn't work, try plugging it into a different port. You may need a USB hub.")
            print("If the camera still doesn't work, you may have to replace it.")
            prompter("Are you ready to continue?")
            cc = camera_check()

        if not ac:
            print("***AUDIO HELP***\n\n\tTry changing the audio source — it should typically be on Extron Scaler.")
            print("Check the instructor station audio inputs on the right side and see if anything is plugged into port 4.")
            print("If necessary, trace the audio cord and ensure it's connected to the PC.")
            print("Try restarting the system power. If issues persist, contact pro staff.")
            prompter("Are you ready to continue?")
            ac = audio_check()

        if not ec:
            print("***DOC CAM HELP***\n\n\tCheck the model number of the doc cam.")
            print("If it's a basic TT-12 without letters (like i or id), it may not support UVC.")
            print("If it does support UVC, enable it via the settings menu. Find USB settings and enable UVC — it will reboot.")
            print("If it still doesn't work, unplug and replug the USB cable into the computer.")
            prompter("Are you ready to continue?")
            ec = camera_check(1)

    results(ac, ec, cc, oc)


if __name__ == "__main__":
    intro()
    camera_result = camera_check()
    elmo_result = camera_check(1)
    duo_result = mfa_override_test()
    audio_result = audio_check()
    troubleshoot(audio_result, elmo_result, camera_result, duo_result)
