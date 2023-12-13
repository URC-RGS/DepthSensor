import serial


class SerialPort:
    def __init__(self, config_serial : dict):
        '''`Класс для работы с последовательным портом'''

        self.check_connect = False
        self.logi = config_serial['logger']

        self.serial_port = serial.Serial(
                                        port=config_serial['port'],
                                        baudrate=config_serial['bitrate'],
                                        timeout=config_serial['timeout']
                                        )
                                        
        self.check_cor = False
        self.logi.info(f'Serial port init: {config_serial}')

    def receiver_data(self): 
        #прием информации с аппарата
        data = None
        try:
            while data == None or data == b'':
                data = str(self.serial_port.readline())[2:-5]
                
                self.logi.debug(f'Receiver data: {data}')
                return data

        except:
            self.logi.warning('Error converting data')
            return None

    def send_data(self, data : list):
        #отправка массива на аппарат
        try:
            data = (f'{str(data)[1:-1]}\n').replace(', ', ' ').encode()
            self.serial_port.write(data)
            self.logi.debug(f'Send data: {data}')

        except:
            self.logi.warning('Error send data')

    def close(self):
        self.serial_port.close()
            
