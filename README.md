# IoT Noise Pollution Monitoring System

![prototype](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/27dd11c5-4f96-426f-a906-ede66dff068f)


## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Configuration](#docker-configuration)
- [Dependencies](#dependencies)
- [Images](#images)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to create an IoT-based noise pollution monitoring system to raise awareness of noise pollution levels in areas with heavy traffic and encourage measures to reduce noise pollution. This README provides detailed instructions on how to set up and run the project, including the use of Docker for easy deployment.

## Project Overview

The project uses an ESP8266-based Arduino board, a sound sensor (microphone), a 16x2 LCD display, LED indicators, and a Wi-Fi module to monitor and display noise pollution levels. It also integrates with a cloud-based platform to store and visualize data.

## Prerequisites

Before you begin, make sure you have the following prerequisites:
- ESP8266-based Arduino board
- Sound sensor (microphone)
- 16x2 LCD display
- LED indicators (Quiet, Moderate, High)
- Wi-Fi module (ESP8266)
- Docker (if using Docker for deployment)

## Installation

1. Clone this repository to your local machine.
2. Install the necessary Python packages using the `requirements.txt` file:
3. pip install -r requirements.txt


## Usage

1. Set up the hardware components as described in the project documentation.
2. Configure your Wi-Fi settings.
3. Open the Arduino IDE and upload the provided code to the ESP8266 board.

## Docker Configuration

To use Docker for deployment:

1. Ensure you have Docker installed on your system.
2. Build the Docker image by running: `docker build -t iot-noise-monitor .`
3. Run the Docker container: `docker run -p 80:80 iot-noise-monitor`

Your project should now be accessible at `http://localhost`.

## Dependencies

This project uses the following dependencies:

- Blynk for IoT connectivity
- Arduino IDE for code compilation
- Python for Docker configuration


## Images

**UI:**

  ![Screenshot from 2023-11-01 17-57-36](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/99c294cc-1f4d-45af-aede-2409fa33eef9)


**components:**





  ![download](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/170d8e70-5b17-496f-9ba1-a1a8e5c2b954)
  ![Led's](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/ab6ab24b-ba65-443b-8d3f-9a8419cc2454)
  ![WIFI_module](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/6e4d2993-86f3-434b-98eb-e840847e7376)
  ![download](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/ecbedf95-87db-4447-8b0c-acc25efc2245)
  ![display-1](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/d14f67c3-251a-4160-9f13-17a4bc83efcc)
  ![display](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/7610957c-82e7-4603-bc19-8eb56461c509)

**Data Sharing PLatform:**

  ![Capture-1](https://github.com/quantum-scripter/NOISE-POLLUTION-MONITORING/assets/138384576/a02cba99-0d2d-4854-af41-443fc7abfe28)











## Contributing

If you'd like to contribute to this project, please open an issue or create a pull request.

## License

This project is licensed under the XYZ License - see the [LICENSE.md](LICENSE.md) file for details.
