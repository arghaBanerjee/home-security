from __future__ import print_function
import logging
import uploadPhoto
import sendEmail
from gpiozero import *
from picamera import PiCamera
from random import *
from time import sleep


def main():

    logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='home-security.log',
                    level=logging.DEBUG)

    pir = MotionSensor(4)

    camera = PiCamera()
    camera.rotation = 180

    while True:

    	fileName = 'file-' + str(randint(1, 9999)) + '.jpg'
    	print('Filename: ', fileName)

    	pir.wait_for_motion()
    	print('Motion detected!')

    	camera.start_preview()
    	sleep(5)
    	camera.capture('/home/pi/camera-files/%s' % fileName)
    	camera.stop_preview()
    	print('Image captured!')

    	logging.info("Start to uplaod File:  -- \'{}\'".format(fileName))

    	uploadPhoto.fileUpload(fileName)
    	print('Image Uploaded!')

    	sendEmail.send(fileName)
    	print('Image Send to Email!')

    	logging.info("Completed sending Email!")
    	pir.wait_for_no_motion()
    	print('No Motion!')


if __name__ == '__main__':
  main()
