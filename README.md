# Arch hello! 

Эта страница для меня и моих друзей, где я подробно расскажу о том как
установить arch с виндой, используя archinstall, а также напишу
о настройке hyprland и hyprpanel! Приятного чтения)

# Начало установки
Ещё не до конца определился для какого уровня людей буду писать эту статью тк сам не так уж много знаю, но напишу о своём опыте. Вдруг полезно будет

1. На винде идем в программу *"Создание и форматирование разделов жёсткого диска"*. Выделяем диск правой кнопкой мыши и выбираем сжать том. Затем указываем сколько выделим памяти под линукс.
2. Для установки арча нужно создать образ диска на флешку. Качаем iso файл с офицального сайта archlinux и чтобы сделать флешку я делал, использовал программу rufus. Далее интуитивно понятный интерфейс, обычно всё настраивается автоматически.
3. Вставляем флешку и перезагружаем пк. Далее нужно попасть в bios (пробуйте тыкать F12, delete или даже esc подряд. Ну или снова лезем в гугл и ищем как попасть в биос на вашем устройстве) Идём в boot и выбираем нашу флешку и пробуем запуститься.
   * ! Сталкивался с такой проблемой, что нельзя было запуститься тк флешка не безопасно. Это значит включён скорее всего security mode, тогда в биосе ищем это в параметрах boot и выключаем.
4. Загрузившись на флешку нажимаем enter и видем как у нас загружается arch :)
5. Первым делом хорошо было бы подключить устройство к wifi:
   ```
   iwctl     // Войти в режим настройки сети
   device list    // увидим имя сети, например wlan0, далее будем его использовать (Вместо wlan0 указывайте ваше название)
   station wlan0 scan
   station wlan0 get-networks   // увидим доступные wifi
   station wlan0 connect Название_сети_которое_хотите_выбрать    // появится поле ввода с паролем, вводим свой
   exit

   ping google.com    // Проверим работает ли вай фай, чтобы выйти нажимаем ctr+Z
   ```
6. Делаем разделы в диске под новую ОС. Для удобства далее буду использовать такую легенду
   * "!" будут помечаться то что выбрать в cfdisk
   * ">" что вводим когда просят
   ```
   lsblk   // Увидим разделы в диске
   cfdisk /dev/nvme0n1    // nvme0n1 - диск, с которым будем работать
   
   ! кликаем до free space   !New   > 1GiB
   
   ```
