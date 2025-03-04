# بوت بث مباريات ريال مدريد

بوت Discord لبث مباريات ريال مدريد في القنوات الصوتية. يدعم البث المباشر للمباريات مع دعم الصوت والفيديو.

## المميزات
- بث مباشر للمباريات
- دعم الصوت والفيديو
- أوامر سهلة الاستخدام (Slash Commands)
- إمكانية التحكم في البث (إيقاف، تشغيل)

## المتطلبات
- Python 3.8 أو أحدث
- FFmpeg
- توكن بوت Discord
- حساب على Railway (للاستضافة)

## التثبيت المحلي

1. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

2. قم بتثبيت FFmpeg على نظامك

3. قم بإنشاء ملف `.env` وأضف توكن البوت:
```
DISCORD_TOKEN=your_bot_token_here
```

## الاستضافة على Railway
1. قم بربط حسابك على GitHub
2. قم بإضافة المتغيرات البيئية في Railway:
   - `DISCORD_TOKEN`: توكن البوت الخاص بك

## الأوامر المتاحة
- `/join` - انضمام البوت إلى القناة الصوتية
- `/leave` - مغادرة القناة الصوتية
- `/stream [url]` - بدء البث من الرابط المحدد
- `/stop` - إيقاف البث الحالي

## المساهمة
نرحب بمساهماتكم! يمكنكم:
1. عمل Fork للمشروع
2. إنشاء فرع جديد (`git checkout -b feature/new-feature`)
3. عمل Commit للتغييرات (`git commit -am 'Add new feature'`)
4. رفع التغييرات (`git push origin feature/new-feature`)
5. فتح Pull Request 