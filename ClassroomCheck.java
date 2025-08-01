import java.io.*;
import java.net.*;
import java.util.Scanner;
import java.awt.Desktop;

/**
 * ClassroomCheck.java
 *
 * Description:
 * Automates a classroom AV and MFA setup walkthrough including speaker, camera, doc cam,
 * and Duo MFA bypass testing. Provides guidance and troubleshooting steps for each test.
 *
 * Author: Caleb Peters / Arcerite
 * Version: 1.5
 * Date: 2025-05-30
 */
public class ClassroomCheck {

    // Used for all user prompts
    static Scanner scanner = new Scanner(System.in);

    /**
     * Entry point for the application.
     * Guides the user through classroom equipment checks.
     */
    public static void main(String[] args) {
        intro();

        boolean cameraResult = cameraCheck(0);       // Default webcam
        boolean elmoResult = cameraCheck(1);         // Document camera
        boolean duoResult = mfaOverrideTest();       // Duo MFA test
        boolean audioResult = audioCheck();          // Room speaker test

        troubleshoot(audioResult, elmoResult, cameraResult, duoResult);
    }

    /**
     * Clears the Windows terminal screen using 'cls'.
     */
    static void clear() {
        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e) {
            System.out.println("Could not clear screen.");
        }
    }

    /**
     * Prompts the user for a Yes/No response.
     *
     * @param message The message/question to display.
     * @return True if the user responds positively, false otherwise.
     */
    static boolean prompter(String message) {
        while (true) {
            System.out.print(message + " (Y/N)\n: ");
            String response = scanner.nextLine().trim().toLowerCase();
            if (response.equals("y") || response.equals("yes")) {
                return true;
            } else if (response.equals("n") || response.equals("no")) {
                return false;
            }
        }
    }

    /**
     * Displays the welcome message and basic usage instructions.
     */
    static void intro() {
        clear();
        System.out.println("Welcome to the classroom check walkthrough!");
        System.out.println("This command prompt window will have instructions and guide you through the process!");
        System.out.print("Press enter to continue...");
        scanner.nextLine();
    }

    /**
     * Performs an audio test by opening Windows Sound Settings.
     * User manually tests speakers via system test options.
     *
     * @return True if the user confirms audio is working.
     */
    static boolean audioCheck() {
        clear();
        System.out.println("Audio Test");
        System.out.println("----------------------------------");
        System.out.println("We'll now open the Windows Sound Settings.");
        System.out.println("In the Playback tab, right-click the default device and choose 'Test'.");
        System.out.println("Make sure the sound plays through the room speakers.");
        System.out.println("You may need to increase the volume on the Extron panel and ensure it's set to PC.");
        System.out.println();

        try {
            Runtime.getRuntime().exec("control mmsys.cpl sounds");
        } catch (IOException e) {
            System.out.println("Error opening sound settings: " + e.getMessage());
        }

        return prompter("Did the audio test play correctly through the correct speakers?");
    }

    /**
     * Tests either the default webcam or document camera.
     *
     * @param mode 0 = webcam, 1 = document camera (Elmo).
     * @return True if the user confirms the camera is working.
     */
    static boolean cameraCheck(int mode) {
        clear();
        System.out.println("Say Cheese! Camera test!");

        try {
            if (mode == 0) {
                // Open Windows Camera app
                Runtime.getRuntime().exec("cmd /c start microsoft.windows.camera:");
                return prompter("Is the camera working?");
            } else {
                // Prompt for document camera specific checks
                System.out.println("In the top right corner of the camera app should be an option to swap cameras.");
                System.out.println("Check to see if Elmo is an option. It may show a white screen; give it a few seconds.");
                return prompter("Is the doc cam working?");
            }
        } catch (IOException e) {
            System.out.println("Error with camera: " + e.getMessage());
            return false;
        }
    }

    /**
     * Opens a Duo login site and asks if the MFA bypass occurred.
     * Provides the IP address if troubleshooting is needed.
     *
     * @return True if bypass worked (no Duo push required), false otherwise.
     */
    static boolean mfaOverrideTest() {
        clear();
        System.out.println("Testing Duo Bypass...");
        System.out.println("A website will open. Log in and follow the Duo prompt.");
        System.out.println("If prompted to check your phone, the answer is NO.");
        System.out.println("If it skips the phone prompt, the answer is YES.");

        try {
            Desktop.getDesktop().browse(new URI("https://my.gvsu.edu/"));
        } catch (Exception e) {
            System.out.println("Error opening browser: " + e.getMessage());
            return false;
        }

        boolean result = prompter("Is Duo Bypass working?");
        if (!result) {
            try {
                String ip = InetAddress.getLocalHost().getHostAddress();
                System.out.println("Your IP address is: " + ip);
                System.out.print("Press enter once you've noted it down...");
                scanner.nextLine();
            } catch (UnknownHostException e) {
                System.out.println("Could not get IP address.");
            }
        }
        return result;
    }

    /**
     * Prints a summary of the results of all checks.
     *
     * @param audio  Audio check result.
     * @param elmo   Document camera check result.
     * @param camera Webcam check result.
     * @param duo    MFA Duo bypass check result.
     */
    static void results(boolean audio, boolean elmo, boolean camera, boolean duo) {
        clear();
        System.out.println("Test                 \t Results");
        System.out.println("----------------------------------------");
        System.out.println("Audio Check         \t " + audio);
        System.out.println("Camera Check        \t " + camera);
        System.out.println("Elmo Check          \t " + elmo);
        System.out.println("Duo Bypass Check    \t " + duo);
        System.out.print("Press enter to continue...");
        scanner.nextLine();
    }

    /**
     * Provides optional troubleshooting help for failed tests.
     * Offers re-tests after instructions are followed.
     *
     * @param ac Audio check result.
     * @param ec Document camera result.
     * @param cc Webcam result.
     * @param oc MFA Duo result.
     */
    static void troubleshoot(boolean ac, boolean ec, boolean cc, boolean oc) {
        if (prompter("Would you like help troubleshooting?")) {

            if (!cc) {
                System.out.println("***CAMERA HELP***");
                System.out.println("\tCheck to see the camera is plugged in. Try replugging or switching USB ports.");
                System.out.println("\tYou may need a USB hub if all ports are used.");
                prompter("Are you ready to continue?");
                cc = cameraCheck(0);
            }

            if (!ac) {
                System.out.println("***AUDIO HELP***");
                System.out.println("\tTry changing the audio source. Common options: Extron Scaler, Realtek Audio.");
                System.out.println("\tCheck port 4 on the instructor station. Trace and verify connection.");
                System.out.println("\tTry restarting the system power. Contact Pro Staff if issue persists.");
                prompter("Are you ready to continue?");
                ac = audioCheck();
            }

            if (!ec) {
                System.out.println("***DOC CAM HELP***");
                System.out.println("\tCheck doc cam model. TT-12 (without suffix) may not support UVC.");
                System.out.println("\tIf UVC is supported, enable it in the doc cam's settings menu.");
                System.out.println("\tTry unplugging and replugging the USB connection.");
                prompter("Are you ready to continue?");
                ec = cameraCheck(1);
            }
        }

        results(ac, ec, cc, oc);
    }
}
