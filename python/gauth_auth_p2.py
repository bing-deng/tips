# coding:utf8
import hmac, base64, struct, hashlib, time
def calGoogleCode(secretKey):
    input = int(time.time())//30
    key = ''
    try:
        key = base64.b32decode(secretKey)
    except:
        pass
    msg = struct.pack(">Q", input)
    googleCode = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(googleCode[19]) & 15
    googleCode = str((struct.unpack(">I", googleCode[o:o+4])[0] & 0x7fffffff) % 1000000)
    if len(googleCode) == 5:             # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
        googleCode = '0' + googleCode
    return googleCode
print calGoogleCode("GAGAGAGAGAGAGAGA")
