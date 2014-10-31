#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
# This module has been tested on python ver.2.6.6.
# ver0.141030
# (C) 2014 Matsuda Hiroaki 

import pyrs
import time

class Bell():
        # ID    Pitch   Hand
        # 1	A3	R	
        # 2	A#3	R
        # 3	B3	L
        # 4	C4	R
        # 5	C#4	L
        # 6	D4	L
        # 7	D#4	R
        # 8	E4	R
        # 9	F4	L
        #10	F#4	L
        #11	G4	R
        #12	G#4	R
        #13	A4	L
        #14	A#4	L
        #15	B4	R
        #16	C5	L
        #17	C#5	R
        #18	D5	R
        #19	D#5	L
        #20	E5	L

    def __init__(self, port = 'COM4', baudrate = 115200,
             down_position = 1500, up_position = 1100):
        self.rs = pyrs.Rs()
        self.rs.open_port(port, baudrate)
        self.down_position = down_position
        self.up_position = up_position
        self.note_dictionary = {57: 1, 58: 2, 59: 3, 60: 4, 61: 5,
                                62: 6, 63: 7, 64: 8, 65: 9, 66:10,
                                67:11, 68:12, 69:13, 70:14, 71:15,
                                72:16, 73:17, 74:18, 75:19, 76:20}

    def get_note_numbers(self):
        note_numbers = self.note_dictionary.keys()
        note_numbers.sort()
        return note_numbers

    def get_note_dictionary(self):
        return self.note_dictionary
        
    def all_servo_on(self, mode):
        servos_data = [[ 1, mode],
                       [ 2, mode],
                       [ 3, mode],
                       [ 4, mode],
                       [ 5, mode],
                       [ 6, mode],
                       [ 7, mode],
                       [ 8, mode],
                       [ 9, mode],
                       [10, mode],
                       [11, mode],
                       [12, mode],
                       [13, mode],
                       [14, mode],
                       [15, mode],
                       [16, mode],
                       [17, mode],
                       [18, mode],
                       [19, mode],
                       [20, mode]]
        
        self.rs.multi_torque_on(servos_data)
        time.sleep(1)

    def set_positions(self, position, move_time):

        servos_data = [[ 1, -position, move_time],
                       [ 2, -position, move_time],
                       [ 3,  position, move_time],
                       [ 4, -position, move_time],
                       [ 5,  position, move_time],
                       [ 6,  position, move_time],
                       [ 7, -position, move_time],
                       [ 8, -position, move_time],
                       [ 9,  position, move_time],
                       [10,  position, move_time],
                       [11, -position, move_time],
                       [12, -position, move_time],
                       [13,  position, move_time],
                       [14,  position, move_time],
                       [15, -position, move_time],
                       [16,  position, move_time],
                       [17, -position, move_time],
                       [18, -position, move_time],
                       [19,  position, move_time],
                       [20,  position, move_time]]

        self.rs.multi_target_position(servos_data)
        time.sleep(1)

    def note_on(self, note_number, time_down, return_packet = 0x01):

        servo_id = self.note_dictionary[note_number]

        if servo_id in [3, 5, 6, 9, 10, 13, 14, 16, 19, 20]:        
            self.rs.target_position(servo_id,  self.down_position, time_down, return_packet)

        elif servo_id in [1, 2, 4, 7, 8, 11, 12, 15, 17, 18]:
            self.rs.target_position(servo_id, -self.down_position, time_down, return_packet)

    def note_off(self, note_number, time_up, return_packet = 0x01):

        servo_id = self.note_dictionary[note_number]

        if servo_id in [3, 5, 6, 9, 10, 13, 14, 16, 19, 20]:        
            self.rs.target_position(servo_id,  self.up_position, time_up, return_packet)

        elif servo_id in [1, 2, 4, 7, 8, 11, 12, 15, 17, 18]:
            self.rs.target_position(servo_id, -self.up_position, time_up, return_packet)

    def multi_note_on(self, note_numbers, time_down):

        servos = [] 
        for note_number in note_numbers:
            
            servo_id = self.note_dictionary[note_number]
            
            if servo_id in [3, 5, 6, 9, 10, 13, 14, 16, 19, 20]: 
                servos.append([servo_id,  self.down_position, time_down])

            elif servo_id in [1, 2, 4, 7, 8, 11, 12, 15, 17, 18]:
                servos.append([servo_id, -self.down_position, time_down])

        self.rs.multi_target_position(servos)

    def multi_note_off(self, note_numbers, time_up):

        servos = [] 
        for note_number in note_numbers:

            servo_id = self.note_dictionary[note_number]
            
            if servo_id in [3, 5, 6, 9, 10, 13, 14, 16, 19, 20]: 
                servos.append([servo_id,  self.up_position, time_up])

            elif servo_id in [1, 2, 4, 7, 8, 11, 12, 15, 17, 18]:
                servos.append([servo_id, -self.up_position, time_up])

        self.rs.multi_target_position(servos)

if __name__ == '__main__':

    import bell
    bears = bell.Bell('COM4', 460800, 1500, 1100)
    
    bears.all_servo_on(1)  
    bears.set_positions(1100, 300)
    time.sleep(3)
    print "Status: Initialized Position"

    note_numbers = bears.get_note_numbers()

    for note_number in note_numbers:
        bears.note_on(note_number, 20, 0x00)
        time.sleep(0.5)

    for note_number in note_numbers:
        bears.note_off(note_number, 30, 0x00)
    print "Status: Single Ring"

    time.sleep(2)
    for note_number in note_numbers:
        bears.note_on(note_number, 30, 0x00)
        
    time.sleep(0.3)

    for note_number in note_numbers:
        bears.note_off(note_number, 30, 0x00)
    print "Status: Single Ring no time"

    time.sleep(1)

    bears.set_positions(1400, 500)
    time.sleep(5)
    bears.all_servo_on(0)
    print "Status: Finalized Position"
    
