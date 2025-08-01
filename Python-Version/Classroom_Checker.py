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


def camera_check(mode:int=0) -> bool:
    """
    Open the camera app and prompt the user to verify functionality.

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
            print("In the top right corner of the camera app shoud be an option to swap cameras, please do so. \nCheck to see if Elmo is an option, it may show a white screen, give it a few seconds")
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
    if prompter("Would you like help troubleshooting?"):

        if not cc:
            print("***CAMERA HELP***\n\n\tCheck to see the camera is plugged into the computer, try replugging it in to its current port\n\nIf that didnt work try plugging it in to a different port. If this works you may need a USB hub for everything to be plugged in at once\n\nIf that did not work or if the camera is broken you may have to replace it")
            prompter("Are you ready to continue?")
            cc = camera_check()

        if not ac:
            print("***AUDIO HELP***\n\n\tTry changing the audio source, most of the time it should be on extron scaler however some situations may require it to be on speakers or realtek audio instead\n\nOpen the instructor station and check audio inputs, this would be on the right side. Check to see if anything is plugged into port 4. If so trace this cord and make sure its plugged into the computer\n\nTry restarting the system power, if issues still persist contact pro staff")
            prompter("Are you ready to continue?")
            ac = audio_check()

        if not ec:
            print("***DOC CAM HELP***/n/n/tCheck the model number of the doc cam, If it is a basic TT-12 with no letters (typically I or id) afterwards, then the doc cam is too old to support UVC and therefore wont work with doc cam usb\n\nIf the doc cam can support the UVC setting it has to be enabled. To do this, turn on the doc cam and click the settings/menu button. Find prefferences and look for USB options, Under this setting click UVC, the doc cam will reboot\n\n If the doc cam still doesn't work, try unplugging and replugging in the USB cord to the computer")
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
