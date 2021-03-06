from PIL import Image, ImageDraw
from random import Random
from math import pi, sin, cos

from pathlib import PurePath

class Face:
    def __init__(
            self,
            face_size = (320,240),
            face_color = (255,255,255),

            eye_pos = (100,80),
            eye_size = (100,80),
            eye_corn_rad = 10,
            eye_line_width = 3,
            eye_color = (255,255,255),
            eye_line_color = (0,0,0),
            eye_left_closed = 0.2,              # 0...1
            eye_right_closed = 0.2,             # 0...1

            pup_size = 20,
            pup_color = (0,0,0),
            pup_pos_hor = 0,                    # -1...1
            pup_pos_vert = 0,                   # -1...1

            mouth_pos = (160,160),
            mouth_size = (150,50),
            mouth_scale = 0.5,                  # ]0...1]
            mouth_open = False,
            mouth_line_width = 3,
            mouth_color = (0,0,0),
            mouth_line_color = (0,0,0),

            mood = 'happy',                     # 'happy'/'sad'/'surprised'/

            ani_blink_rate = 0.1,               # 0...1
            ani_blink_closed = 0.9,             # 0...1
            ani_pup_move_rate = 0.2,            # 0...1
            ani_pup_sigm_hor = 0.4,             # Std. dev. hor
            ani_pup_sigm_vert = 0.2,            # Std. dev. vert
            ani_talk = False
        ):
        self.face_size = face_size
        self.face_color = face_color
        self.eye_pos = eye_pos
        self.eye_size = eye_size
        self.eye_corn_rad = eye_corn_rad
        self.eye_line_width = eye_line_width
        self.eye_color = eye_color
        self.eye_line_color = eye_line_color
        self.eye_left_closed = eye_left_closed
        self.eye_right_closed = eye_right_closed
        self.pup_size = pup_size
        self.pup_color = pup_color
        self.pup_pos_hor = pup_pos_hor
        self.pup_pos_vert = pup_pos_vert
        self.mouth_pos = mouth_pos
        self.mouth_size = mouth_size
        self.mouth_scale = mouth_scale
        self.mouth_open = mouth_open
        self.mouth_line_width = mouth_line_width
        self.mouth_color = mouth_color
        self.mouth_line_color = mouth_line_color

        self.mood = mood

        self.ani_blink_rate = ani_blink_rate
        self.ani_blink_closed = ani_blink_closed
        self.ani_pup_move_rate = ani_pup_move_rate
        self.ani_pup_sigm_hor = ani_pup_sigm_hor
        self.ani_pup_sigm_vert = ani_pup_sigm_vert
        self.ani_talk = ani_talk

        # Internal attributes
        self.__ani_blink = False                # Blink indicator
        self.__ani_backup_eye_left_closed = 0
        self.__ani_backup_eye_right_closed = 0
        self.__ani_pup_move = False             # Rand eye move indicator

        # Object that holds the current frame for the face
        self.frame = Image.new('RGB',
            self.face_size,
            color=self.face_color,
        )
        # Get a drawing context for the face to draw
        # e.g. eyes and mouth
        self.dc = ImageDraw.Draw(self.frame)

        # Initialize the face (no output)
        self.draw()

    def draw(self):
        self.eyes_erase()
        self.eyes()
        self.pupils()
        self.mouth_erase()
        self.mouth()

    def update(self):
        # Initiate independent Random instances
        r1 = Random()   # Eye blinking
        r2 = Random()   # Movement of pupils
        r3 = Random()   # Horizontal displacement of pupils
        r4 = Random()   # Vertical displacement of pupils

        # Simulate blinking
        if self.__ani_blink:
            # Reset back blinking indicator to False
            self.__ani_blink = False
            # Reset status of eye closed
            self.eye_left_closed = self.__ani_backup_eye_left_closed
            self.eye_right_closed = self.__ani_backup_eye_right_closed
        else:
            if r1.random() > (1-self.ani_blink_rate):
                # Set blinking indicator to True
                self.__ani_blink = True
                # Backup the current status of eyes closed
                self.__ani_backup_eye_left_closed = self.eye_left_closed
                self.__ani_backup_eye_right_closed = self.eye_right_closed
                # Close eyes for blinking
                self.eye_left_closed = self.ani_blink_closed
                self.eye_right_closed = self.ani_blink_closed

        # Simulate random movement of pupils. But only, if face
        # looks straight forward
        if self.__ani_pup_move:
            # Reset back random eye mov indicator
            self.__ani_pup_move = False
            # Reset position of pupils
            self.pup_pos_hor = 0
            self.pup_pos_vert = 0
        else:
            if (
                0==self.pup_pos_hor and
                0==self.pup_pos_vert and
                r2.random() > (1-self.ani_pup_move_rate)
            ):
                # Set random eye movement indicator to True
                self.__ani_pup_move = True
                # Determine gaussian-distributed random horizontal
                # and vertical offsets for position of pupils but
                # confine the offsets to [-1.0...1.0]
                oh = r3.gauss(0.0, self.ani_pup_sigm_hor)
                if oh < -1.0:
                    oh = -1.0
                if oh > 1.0:
                    oh = 1.0
                ov = r4.gauss(0.0, self.ani_pup_sigm_vert)
                if ov < -1.0:
                    ov = -1.0
                if ov > 1.0:
                    ov = 1.0
                self.pup_pos_hor = oh
                self.pup_pos_vert = ov

        # Simulate talking by opening and closing
        # mouth
        if self.ani_talk:
            self.mouth_open = not self.mouth_open

        # Draw the current face frame
        self.draw()

    def eyes_erase(self):
        eyes_box=[
            self.eye_pos[0]-self.eye_size[0]/2,
            self.eye_pos[1]-self.eye_size[1]/2,
            self.face_size[0]-self.eye_pos[0]+self.eye_size[0]/2,
            self.eye_pos[1]+self.eye_size[1]/2
        ]
        self.dc.rectangle(
            eyes_box,
            fill = self.face_color,
        )

    def eyes(self):
        # Left eye
        eye_left_box=[
            self.eye_pos[0]-self.eye_size[0]/2,
            self.eye_pos[1]-self.eye_size[1]*(1-self.eye_left_closed)/2,
            self.eye_pos[0]+self.eye_size[0]/2,
            self.eye_pos[1]+self.eye_size[1]*(1-self.eye_left_closed)/2
        ]
        self.dc.rounded_rectangle(
            eye_left_box,
            radius = self.eye_corn_rad,
            fill = self.eye_color,
            outline = self.eye_line_color,
            width = self.eye_line_width,
        )

        # Right eye
        eye_right_box=[
            self.face_size[0]-self.eye_pos[0]-self.eye_size[0]/2,
            self.eye_pos[1]-self.eye_size[1]*(1-self.eye_right_closed)/2,
            self.face_size[0]-self.eye_pos[0]+self.eye_size[0]/2,
            self.eye_pos[1]+self.eye_size[1]*(1-self.eye_right_closed)/2
        ]
        self.dc.rounded_rectangle(
            eye_right_box,
            radius = self.eye_corn_rad,
            fill = self.eye_color,
            outline = self.eye_line_color,
            width = self.eye_line_width,
        )

    def pupils(self):
        # Shortcuts for variables to make equations more readable
        fsx = self.face_size[0]
        fsy = self.face_size[1]
        epx = self.eye_pos[0]
        epy = self.eye_pos[1]
        esx = self.eye_size[0]
        esy = self.eye_size[1]
        ecl = 1 - max(self.eye_left_closed, self.eye_right_closed)
        elw = self.eye_line_width
        ps = self.pup_size
        pph = self.pup_pos_hor
        ppv = self.pup_pos_vert

        # The pupils shall only be drawed if the eyes are sufficiently
        # opened. This way, the pupils will not be drawn ouside the
        # eyes.

        # Left pupil
        if (ps <= (esy*(1-self.eye_left_closed)-2*elw)):
            pup_left_box=[
                epx-ps/2+(esx/2-ps/2-elw)*pph,
                epy-ps/2+(esy/2*ecl-ps/2-elw)*ppv,
                epx+ps/2+(esx/2-ps/2-elw)*pph,
                epy+ps/2+(esy/2*ecl-ps/2-elw)*ppv,
            ]
            self.dc.rounded_rectangle(
                pup_left_box,
                radius = ps,
                fill = self.pup_color
            )

        # Right pupil
        if (ps <= (esy*(1-self.eye_right_closed)-2*elw)):
            pup_right_box=[
                fsx-epx-ps/2+(esx/2-ps/2-elw)*pph,
                epy-ps/2+(esy/2*ecl-ps/2-elw)*ppv,
                fsx-epx+ps/2+(esx/2-ps/2-elw)*pph,
                epy+ps/2+(esy/2*ecl-ps/2-elw)*ppv,
            ]
            self.dc.rounded_rectangle(
                pup_right_box,
                radius = ps,
                fill = self.pup_color
            )

    def mouth(self):
        if 'happy'==self.mood or 'sad'==self.mood:
            self.mouth_happy_sad()
        else:
            self.mouth_surprised()

    def mouth_surprised(self):
        mouth_box=[
            self.mouth_pos[0]-self.mouth_size[1]/2,
            self.mouth_pos[1]-self.mouth_size[1]/2,
            self.mouth_pos[0]+self.mouth_size[1]/2,
            self.mouth_pos[1]+self.mouth_size[1]/2,
        ]
        self.dc.rounded_rectangle(
            mouth_box,
            radius = self.mouth_size[1]/2,
            fill = self.mouth_color
        )

    def mouth_happy_sad(self):

        # Empty list for polygon forming the mouth
        # [x0, y0, x1, y1, x2, y2, ...]
        mouth_polygon=[]

        # Happy or sad mouth
        factor = 1
        if 'sad'==self.mood:
            factor = -1

        # Populating the polygon
        n = 90  # Number of points forming the polygon
        for i in range(n):
            # Horizontal coordinate
            mouth_polygon.append(
                -self.mouth_size[0]/2*cos(pi*i/(n-1))
                +self.mouth_pos[0]
            )
            # Vertical coordinate
            mouth_polygon.append(
                self.mouth_size[1]
                *self.mouth_scale
                *factor                 # mood, see above
                *(sin(pi*i/(n-1))-0.5)
                +self.mouth_pos[1]
            )

        # Distinguish between open/closed mouth
        if self.mouth_open:
            self.dc.polygon(
                mouth_polygon,
                outline=self.mouth_line_color,
                fill=self.mouth_color,
                width=self.mouth_line_width,
            )
        else:
            self.dc.line(
                mouth_polygon,
                fill=self.mouth_color,
                width=self.mouth_line_width,
                joint='curve',
            )

    def mouth_erase(self):
        mouth_box=[
            self.mouth_pos[0]-self.mouth_size[0]/2-self.mouth_line_width,
            self.mouth_pos[1]-self.mouth_size[1]/2-self.mouth_line_width,
            self.mouth_pos[0]+self.mouth_size[0]/2+self.mouth_line_width,
            self.mouth_pos[1]+self.mouth_size[1]/2+self.mouth_line_width,
        ]

        self.dc.rectangle(
            mouth_box,
            outline=self.face_color,
            fill=self.face_color,
        )

