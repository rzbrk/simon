# SIMON Phase 0 Report

## Note
This document is written in markdown. You can read a rendered version visiting
the SIMON GitHub repository <https://github.com/rzbrk/simon>. Alternatively,
you can render the markdown by using a tool like [Grip -- GitHub Readme Instant Preview](https://github.com/joeyespo/grip).

## Table of Content
* [Introduction](#introduction)
* [System Requirements](#system-requirements)
* [Design Concept](#design-concept)

## Introduction
SIMON is a project to build an interactive robot for educational and
entertainment purposes. The robot shall be used stationary and is housed in a
hollow sphere. Interaction with humans can be done by voice recognition, via a
3.2" TFT screen at the front that shows a face and built-in speakers. The heart
of SIMON is a single-board computer (SBC) running a GNU/Linu operating system
and ROS (Robotic Operation System) as middleware. The voice recognition is
facilitated by using a special pcb and microphone. The voice recognition board
can be trained to recognize up to 255 short voice commands. The recognized
commands are then send to the ROS middleware on the SBC for further processing
and for triggering reactions.

SIMON is an acronym and means **S**imple **I**nteractive **M**achine
with**O**ut **N**ose.

SIMON features a couple of other components:
* Speaker for audio output
* A 9 degree-of-freedom inertia measurement unit (accelerometer, gyroscope,
  magnetometer)
* An ultrasonic sensor on the front side
* A air pressure and temperature sensor
* Multiple temperature sensors for measuring the temperature of internal
  components (potential thermal hotspots)
* A vaporizer and an air pump to produce non-hazardous steam for simulating the
  activity of a rocket engine on the back side of SIMON (tbc)

Although SIMON is meant to be used indoors and on-ground it is inspired by
multiple space projects as well as space-related objects:

* [Experiment CIMON (**C**rew **I**nteractive **MO**bile **C**ompanion) by the German Space Center DLR flown on the International Space Station (ISS)](https://duckduckgo.com/?q=cimon+iss&t=h_&iax=images&ia=images)
* [The character Schlupp from the German children television series "Schlupp vom grünen Stern" by Augsburger Puppenkiste](https://duckduckgo.com/?q=schlupp+vom+gr%C3%BCnen+stern&t=h_&iar=images&iax=images&ia=images)
* [The first artifical satellite Sputnik 1, launched by the Soviet Union in
  1957](https://duckduckgo.com/?q=sputnik+1+1957&t=h_&iar=images&iax=images&ia=images)

## System Requirements
To define the scope and boundaries of the project a set of requirements were
established. The requirements are listed in [sim-rs-01_requirements](sim-rs-01_requirements.md). 

## Design Concept

### Mechanical Design
The design of SIMON comprises basically of two half spheres fittet together.
The front shell (blue-grey part in the following figure) has a face plate with
the display. In the face plate also the camera, the microphone and the
ultrasonic sensor will be integrated. Exclusively for aestetical reasons on
both sides of the front shell two fake solar generators will be magnetically
attached. The dimensions in the following figures are not to scale and for
illustration of the design concept, only.

![SIMON mechanical design - front
view](/assets/images/simon_design_concept_01.png)<br>
SIMON mechanical design - exploded view (front)

The back shell (green part) will be magnetically attached to the front shell -
no screws are needed to bond both half spheres together. Propper fit will be
provided by a circumferencing lip and the round "ears" on the left and right
side of SIMON.

![SIMON mechanical design - back
view](/assets/images/simon_design_concept_02.png)<br>
SIMON mechanical design - exploded view (back)

The back shell will also have a "back pack". The back pack provides extra space
needed for the vaporizer of the fake thruster attached to the outside of the
back shell. The vaporizer produces steam that exists through the nozzle of the
thruster and will be illuminated by flashing LEDs.

The red box in the above figures represents the stack of electronics inside
SIMON. It is planned to have a cage-like structure in which the circuit boards
can be mounted. The whole cage is then attached to then front shell -
preferrably also magnetically for easier access. To hold the cage in propper
position the inside of the front shell shall feature guiding rails for the
cage.

![SIMON mechanical design - closed half shells](/assets/images/simon_design_concept_03.png)<br>
SIMON mechanical design

SIMON can be placed on a flat suface by placing the assembled sphere on a ring.
This also allows orienting SIMON to various directions.

### Electrical Design

#### Block Diagram
![SIMON block diagram](/assets/images/simon_prelimdesign.drawio.png "Preliminary design")

#### Raspberry Pi GPIO Pin Assignment
See [sim-tn-01_raspi_gpio](sim-tn-01_raspi_gpio.md).

### Thermal Design
Internal components like the Raspberry Pi computer, the electronics for and the
heating coil in the vaporizer as well as the power conditioning boards will
dissipate heat. To avoid over-heating cooling by convection will be
implemented. Two or three fans in lower part of the front shell will suck cool
air from the outside to the inside of SIMON. The warm air from inside can exit
the inside through ventilation slits on the top side of the sphere.

## Design Justification

### Development Model

For HW tests, evaluation and SW development a development model (breadboard)
was build as shown in the figure below. The development board features most of
the components forseen for the final model of SIMON. For the "fake" thruster
and the vaporizer a separate development model will be build.

![SIMON breadboard](/assets/images/breadboard.jpg)<br>
SIMON development model

### Assessments, Tests and SW Prototypes

#### TFT Display

#### Sound Output

#### Text-to-Speak

#### Voice Recognition
