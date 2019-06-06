import code
# code.interact(local=dict(globals(), **locals()))
import requests
import xml.etree.ElementTree as ET
import html
class Ttl:
    @staticmethod
    def utf8_to_sgml(utf8string):
        url = "http://ws.racai.ro:8080/pdk/ttlws"
        headers = {'content-type': 'text/xml'}
        body = f"""<?xml version="1.0" encoding="UTF-8"?>
                <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
                    <Body>
                        <UTF8toSGML xmlns="http://ws.racai.ro/pdk/ttlws">
                            <instr>{utf8string}</instr>
                        </UTF8toSGML>
                    </Body>
                </Envelope>"""
        body = body.encode('utf-8')
        response = requests.post(url, data=body, headers=headers)
        root = ET.fromstring(response.content)
        # print(f"utf8_to_sgml:  {root[0][0][0].text}")
        return root[0][0][0].text #.encode('utf-8')

# Maria are bl&amp;abreve;nuri. Ele sunt foarte frumoase.
    @staticmethod
    def xces(sgml_string):
        url = "http://ws.racai.ro:8080/pdk/ttlws"
        headers = {'content-type': 'text/xml'}
        body = """<?xml version="1.0" encoding="UTF-8"?>
                <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
                    <Body>
                        <XCES xmlns="http://ws.racai.ro/pdk/ttlws">
                            <lang>ro</lang>
                            <parid>example</parid>
                            <instr>sgml_string</instr>
                        </XCES>
                    </Body>
                </Envelope>"""
        # body = body.encode('utf-8')
        body = body.replace("sgml_string",  html.escape(sgml_string))
        response = requests.post(url, data=body, headers=headers)
        root = ET.fromstring(response.content)
        # print(f"xces:  {root[0][0][0].text}")
        return root[0][0][0].text
    
    @staticmethod
    def sgml_to_utf8(xces_string):
        url = "http://ws.racai.ro:8080/pdk/ttlws"
        headers = {'content-type': 'text/xml'}
        body = """<?xml version="1.0" encoding="UTF-8"?>
                <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
                    <Body>
                        <SGMLtoUTF8 xmlns="http://ws.racai.ro/pdk/ttlws">
                            <instr>xces_string</instr>
                        </SGMLtoUTF8>
                    </Body>
                </Envelope>"""
        # body = body.encode('utf-8')
        body = body.replace("xces_string", html.escape(xces_string))
        response = requests.post(url, data=body, headers=headers)
        root = ET.fromstring(response.content)
        # print(f"utf:  {root[0][0][0].text}")
        return root[0][0][0].text.strip()

    @staticmethod
    def pos_tag(text):
        sgml = Ttl.utf8_to_sgml(text)
        xces = Ttl.xces(sgml)
        utf = Ttl.sgml_to_utf8(xces)
        return utf
