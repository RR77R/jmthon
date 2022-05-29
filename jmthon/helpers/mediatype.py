from .progress import humanbytes
from .formats import yaml_format


async def mediadata(e_media):
    jmthon = ""
    if e_media.file.name:
        jmthon += f"- الأسـم :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        jmthon += f"- نوع الميديا:  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        jmthon += f"- الحجم :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        jmthon += f"- التاريخ :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        jmthon += f"- الايدي :  {e_media.file.id}<br>"
    if e_media.file.ext:
        jmthon += f"- الابعاد :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        jmthon += f"- الايموجي :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        jmthon += f"- العنوان :  {e_media.file.title}<br>"
    if e_media.file.performer:
        jmthon += f"- الاداء :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        jmthon += f"- المدة :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        jmthon += f"- الارتفاع :  {e_media.file.height}<br>"
    if e_media.file.width:
        jmthon += f"- العرض :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        jmthon += f"- تم وضع الملصقات :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            jmthon += f"- الخلفيه  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return jmthon


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None

