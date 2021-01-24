from flask import Flask,jsonify,request
from wsgiref.simple_server import make_server
import os,socket,random,re

#端口检测
def echeck_port_in_us(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.settimeout(1)
        s.shutdown(2)
        return True
    except:
        return False
#随机字符串
def ranstr():
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(8):
        salt += random.choice(H)

    return salt

app = Flask(__name__)
@app.route('/host',methods=['get'])
def _host():
    ip = request.args.get('ip')#使用request.args.get方式获取拼接的入参数据
    port = request.args.get('port')
    set_port = request.args.get('sport')
    echeck_port = echeck_port_in_us(set_port,'52.83.60.154') #检测端口是否使用
    print(ranstr())
    ips = re.findall("^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$", ip)
    if not ips:
            return "IP不合法"
    else:
        if port.isnumeric():
            if set_port.isnumeric():
                if echeck_port:
                    return "端口占用"
                else:
                    os.system('./setfrp.sh '+ranstr()+' '+ip+' '+port+' '+set_port) 
                    return "52.83.60.154:"+set_port
            else:
                return "外穿端口不合法"
        else:
            return "端口不合法"
      
  


app.run(host='127.0.0.1',port=8802,debug=True)
# server = make_server('', 8802, app)
# server.serve_forever()