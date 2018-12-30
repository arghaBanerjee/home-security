import logging
import uploadPhoto
import sendEmail

def main():

    logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename='home-security.log',
                    level=logging.DEBUG)

    fileName = '3.jpg'

    logging.info("Start to uplaod File:  -- \'{}\'".format(fileName))

    uploadPhoto.fileUpload(fileName)

    sendEmail.send(fileName)

    logging.info("Completed sending Email!")


if __name__ == '__main__':
  main()
