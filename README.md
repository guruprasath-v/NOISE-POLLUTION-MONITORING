# IoT Noise Pollution Monitoring System 

## Overview

This project presents an Internet of Things (IoT) Noise Pollution Monitoring System. It utilizes an ESP8266-based Arduino board to measure noise levels, display results on a Liquid Crystal Display (LCD), and send data to a cloud platform (ThingSpeak). The system also supports real-time noise level monitoring via the Blynk platform.

## Table of Contents

1. [Hardware and Software Requirements](#hardware-and-software-requirements)
2. [Hardware Setup](#hardware-setup)
3. [Software Setup](#software-setup)
4. [Uploading the Code](#uploading-the-code)
5. [Using the System](#using-the-system)
6. [Customizing Parameters](#customizing-parameters)
7. [Data Visualization](#data-visualization)
8. [Images](#images)
9. [Troubleshooting](#troubleshooting)

## Hardware and Software Requirements

### Hardware

- NodeMCU ESP8266 Breakout Board
- DFRobot Gravity Analog Sound Level Meter
- 0.96" OLED 64x128 Display Module
- LEDs (Red, Yellow, Green)
- USB-A to Micro-USB Cable
- Resistor (220 ohm)

### Software

- Arduino IDE
- Blynk (Mobile App)
- ThingSpeak Account

## Hardware Setup

1. Connect the sound sensor (DFRobot Gravity Analog Sound Level Meter) to **Analog Pin A0** on the NodeMCU board.

2. Connect the 0.96" OLED display module and LEDs (Red, Yellow, Green) to the appropriate pins on the NodeMCU board. Refer to the code for pin assignments.

## Software Setup

1. Install the Arduino IDE on your computer.

2. Install the Blynk mobile app on your smartphone and create a new project. You will receive an **authentication code**.

3. Create a ThingSpeak account and obtain your **Write API key**.

## Uploading the Code

1. Open the Arduino IDE and load the provided code.

2. Set up the Arduino IDE for your NodeMCU board (select "NodeMCU 1.0 (ESP-12E Module)" under "Tools" > "Board").

3. Configure your Wi-Fi credentials, Blynk authentication code, and ThingSpeak API key in the code.

4. Connect your NodeMCU board to your computer via USB.

5. Click the "Upload" button in the Arduino IDE to upload the code to your NodeMCU board.

## Using the System

1. After uploading the code, disconnect the NodeMCU from your computer and power it using a USB power source.

2. The OLED display will show the current noise level in decibels (dB).

3. LED indicators will change based on the noise level:
   - **Red LED**: High noise level
   - **Yellow LED**: Moderate noise level
   - **Green LED**: Quiet noise level

## Customizing Parameters

You can customize parameters in the code to suit your specific use case. For example, you can adjust the noise level thresholds for different LED indications or change the Wi-Fi network credentials.

## Data Visualization

The system sends noise level data to your ThingSpeak channel. You can visualize this data on the ThingSpeak platform. Log in to ThingSpeak to access the data.



## Images:




## Troubleshooting

- If you encounter issues with the system, refer to the serial monitor in the Arduino IDE for debugging information.
- Ensure your Wi-Fi network is operational.
- Double-check the hardware connections.
- Verify that the authentication code and API key are correctly entered in the code.

For more information and support, visit our project documentation and community forums.

---

**Note:** Please refer to the project documentation for more detailed information and advanced features.

For any questions or issues, please feel free to reach out to our community for assistance.
