# SIMON Requirements

## Note
This document is written in markdown. You can read a rendered version visiting
the SIMON GitHub repository <https://github.com/rzbrk/simon>. Alternatively,
you can render the markdown by using a tool like [Grip -- GitHub Readme Instant Preview](https://github.com/joeyespo/grip).

## System Requirements
To define the scope and boundaries of the project a set of requirements were
established. The requirements are organized by type. The approach was inspired
by the [OpenDendrometer project on Hackaday.io](https://hackaday.io/project/185224-opendendrometer/log/206183-preliminary-requirements).

| ID | Shall/Should | Requirement text |
|----|--------------|------------------|
||| **Programmatic requirements** |
| P01 | Shall | SIMON shall be intended for educational and entertainment purposes. |
| P02 | Shall | SIMON shall comprise an interactive robot and shall be usable in laboratory and home environment. |
| P03 | Shall | Any information regarding the design, manufaturing, testing of the project shall be made public, preferable using free and open licenses. This shall include software and firmware produced within the project. |
| P04 | Shall | For the design of the project free or at least open source software shall be used to the maximum extend possible. Any exception shall be justified.|
||| **Functional requirements** |
| F01 | Shall | SIMON shall have a software controlled display and shall be able to display a face and status data. |
| F02 | Shall | SIMON shall have a capabilities to detect trained voice commands and to trigger pre-defined actions. |
| F03 | Should | SIMON should have means to perform natural language processing to understand conversation. |
| F04 | Shall | SIMON shall have a sound output capabilities (speakers). |
| F05 | Shall | SIMON shall have a color camera imaging the area in front of the display. |
| F06 | Shall | SIMON shall have a means to detect objects approaching it on the side of the display. Remark: The detection should be limited by the near surrounding (< 2m).<br>NOTE: An ultrasonic sensor may be used. |
| F07 | Shall | SIMON shall have means to measure ambient temperature and air pressure. |
| F08 | Should | SIMON should have a "fake" engine on the back side that can produce steam with no toxic, mechanical or thermal hazard. |
| F09 | Shall | SIMON shall not have a nose. |
||| **Interface requirements** |
| I01 | Shall | SIMON shall be powered by a single DC voltage < 15 volts. |
| I02 | Shall | SIMON shall be able to be monitored remotely. |
| I03 | Shall | SIMON shall be able to be controlled remotely. |
| I04 | Shall | SIMON shall have a spherical housing. |
||| **Development requirements** |
| D01 | Shall | The project shall comprise of the development model and the final product. After verification of the design on the development model parts can be used to build the final product. |
| D02 | Shall | The project shall be splitted in the following phases: <ul><li>concept phase (phase 0)</li><li>design phase (phase 1)</li><li>development phase (phase 2)</li><li>acceptance testing phase (phase 3)</li></ul> Each phase shall be finished with a review. |
| D03 | Shall | In phase 0 the system requirements shall be finalized and the technical feasibility of the project shall be demonstrated by a review of the concept as well as by test of critical functions. |
| D04 | Shall | In phase 1 a detailed design shall be established that satisfies the system requirements. |
| D05 | Shall | In phase 2 the final product shall be developed and pre-tested. |
| D06 | Shall | In phase 3 the close-out of the system requiremets by the end product (acceptance) shall be achieved. |
| D07 | Shall | Throughout the project a risk register shall be maintained. For any unacceptable risks mitigation measures shall be defined. |
