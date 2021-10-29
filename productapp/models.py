from django.db import models
from PIL import Image
import pytesseract
import urllib.request



# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='product/', null=True, blank=True)

    # def gogo(self):
    #     input_data = self.file
    #     outputs = self.before_go(input_data)
    #     return outputs
    #
    # def before_go(self, input_data):
    #     output_1 = '/static/assets/img/about-bg.jpg'
    #     return output_1

    def tesseract(self):
        input_data = self.file
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(Image.open('C:/Users/doch2/PycharmProjects/pragmatic/media/'+str(input_data)), lang='kor')
        text = text.replace(" ", "")
        return text

    def api(self, text):
        client_id = "ts9b5Uc6k8PiyyA1osDt"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "wKUn63Qwyw"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(text)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()

        if (rescode == 200):
            response_body = response.read()
            response_text = response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)

        # 정규표현식으로 불필요한 내용 제거
        response_text = response_text.replace(
            "{\"message\":{\"@type\":\"response\",\"@service\":\"naverservice.nmt.proxy\",\"@version\":\"1.0.0\",\"result\":{\"srcLangType\":\"ko\",\"tarLangType\":\"en\",\"translatedText\":\"",
            '')
        response_text = response_text.replace("\\n", '')
        response_text = response_text.replace("\\", '')
        response_text = response_text.replace("\"", ' ')
        response_text = response_text.replace("engineType", ' ')
        response_text = response_text.replace(":", ' ')
        response_text = response_text.replace("UNDEF_MULTI_SENTENCE", ' ')
        response_text = response_text.replace("pivot", ' ')
        response_text = response_text.replace("null", ' ')
        response_text = response_text.replace("}", ' ')
        response_text = response_text.replace(",", ' ')
        response_text = response_text.replace("\",\"engineType\":\"UNDEF_MULTI_SENTENCE\",\"pivot\":null}}}", "")
        return response_text



