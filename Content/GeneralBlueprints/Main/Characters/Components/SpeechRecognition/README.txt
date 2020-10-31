Если ты собрался менять местоположение папки выше (и/или переименовать её) то тебе обязательно надо заменить 
"GeneralBlueprints/Main/Characters/Components/SpeechRecognition/SpeechRecognitionRuleSet/"  <--  [1]
на новый путь куда ты собираешься закинуть эту папку (и изменить текст после последнего слеша на новое название папки) в скриптах плагина;
перейди на ProjectL_Mash\Plugins\SpeechRecognition\Source\SpeechRecognition\Private, найди SpeechRecognitionWorker.cpp, там
на строках 47, 183, 185, 186, 187 замени [1] на новый путь относительно Content в том же формате (без слеша вначале, со слешем в конце).
Сейчас папка находится в "ProjectL_Mash\Content\GeneralBlueprints\Main\Characters\Components\SpeechRecognition", плагин отталкивается от папки Content.
!!!не знабудь пересоздать файлы проекта и перекомпилировать их.