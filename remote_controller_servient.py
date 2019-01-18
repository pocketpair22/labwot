# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response, request
import RPi.GPIO as GPIO

app = Flask(__name__)
# 設定する動作のリスト
operation_list = ['on', 'off']
# 物理ボタンに対応するGPIO
gpio_list = [4, 17, 27, 18, 5, 6, 13, 12, 22, 23]

@app.route('/', methods=['POST'])
def operation():
    request_data = request.get_json(force=True)
    operation = request_data['operation']
    GPIO.setmode(GPIO.BCM)
    if operation in operation_list:
        GPIO.setup(gpio_list[operation_list.index(operation)],GPIO.OUT)
        result = jsonify({'result': 'Operation Success'})
        GPIO.cleanup()

    else:
        result = jsonify({'result': 'Operation Failed'})

    return make_response(result)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
