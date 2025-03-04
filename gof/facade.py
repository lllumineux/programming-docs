# Часть сложной системы #1
class VideoFile:
    pass  # ...


# Часть сложной системы #2
class OggCompressionCodec:
    pass  # ...


# Часть сложной системы #3
class MPEG4CompressionCodec:
    pass  # ...


# Часть сложной системы #4
class CodecFactory:
    def extract(self, file):
        return ''  # ...


# Часть сложной системы #5
class BitrateReader:
    @staticmethod
    def read(filename, codec):
        return ''  # ...

    @staticmethod
    def convert(buffer, codec):
        return ''  # ...


# Часть сложной системы #6
class AudioMixer:
    def fix(self, result):
        return ''  # ...


# Фасад
class VideoConverter:
    def convert(self, filename, frmt):
        file = VideoFile(filename)
        source_codec = CodecFactory().extract(file)
        if frmt == 'mp4':
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)
        return result


# Клиентский код
def main():
    # Не нужно знать детали сложной системы, можно просто пользоваться
    converter = VideoConverter()
    mp4 = converter.convert('funny-cats-video.ogg', 'mp4')
