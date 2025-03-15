# Arch hello! 

Эта страница для меня и моих друзей, где я подробно расскажу о том как
установить arch с виндой, используя archinstall, а также напишу
о настройке hyprland и hyprpanel! Приятного чтения)

# Начало установки
Ещё не до конца определился для какого уровня людей буду писать эту статью тк сам не так уж много знаю, но напишу о своём опыте. Вдруг полезно будет

1. На винде идем в программу *"Создание и форматирование разделов жёсткого диска"*. Выделяем диск правой кнопкой мыши и выбираем сжать том. Затем указываем сколько выделим памяти под линукс.
2. Для установки арча нужно создать образ диска на флешку. Качаем iso файл с офицального сайта *archlinux* и чтобы сделать флешку я делал, использовал программу *rufus*. Далее интуитивно понятный интерфейс, обычно всё настраивается автоматически.
3. Вставляем флешку и перезагружаем пк. Далее нужно попасть в bios (пробуйте тыкать F12, delete или даже esc подряд. Ну или снова лезем в гугл и ищем как попасть в биос на вашем устройстве) Идём в boot и выбираем нашу флешку и пробуем запуститься.
   * ! Сталкивался с такой проблемой, что нельзя было запуститься тк флешка не безопасно. Это значит включён скорее всего security mode, тогда в биосе ищем это в параметрах boot и выключаем.
4. Загрузившись на флешку нажимаем enter и видем как у нас загружается arch :)
5. Первым делом хорошо было бы подключить устройство к wifi:
   ```
   setfont ter-124n    // Сделаем шрифт крупнее
   
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
   * ">>" что вводим когда просят
   * Думаю понятно, но управление стрелочками
   ```
   lsblk   // Увидим разделы в диске
   cfdisk /dev/nvme0n1    // nvme0n1 - диск, с которым будем работать
   
   ! кликаем до free space   !New >> 1GiB
   ! Выбираем новосозданный раздел и !Type > EFI System

   !Free space  !New >> Нажимаем enter чтобы использовать всю оставшиеся память
   Затем с самым новым разделом  !Write >> yes

   // Запоминаем какой раздел у нас под EFI и последний будет под саму ОС. Далее буду помечать как nvme0n1p{efi/arch}

   !quit
   ```

7. Задаём файловую систему и форматируем
    ```
    clear
    lsblk

    mkfs.fat -F32 /dev/nvme0n1p{efi}
    mkfs.ext4 /dev/nvme0n1p{arch}

    mount /dev/nvme0n1p{arch} /mnt
    mount --mkdir /dev/nvme0n1p{efi} /mnt/boot
    ```
8. Установка с помощью archinstall
   ```
    archinstall

   ! Благодаря крутому cli приложению идём в disk configuration
   ! Выбираем pre-mounted configuration
   ! И указываем точку монтирования /mnt

   # Действия начиная с 6 пункта нужны, для того, чтобы избежать проблем с виндой. Далее начинается полная веселуха и можно пробовать что хотите.
   Но я покажу для hyprland
   * Управление стрелочками и чтобы выйти esc или в крайнем случае ctr+z Но последнее вообще закроект archinstall
   ! Mirrors >> Mirror region
   Нажимаем клавишу с "/"
   и вводим название Russia и когда появится в интерфейсе, то enter
   >> Back

   ! Bootloader >> Grub
   ! Root password >> Придумываем пароль, повторяем его
   ! User account >> Add a user >> Ну там имя и пароль...
   Это интуитивно понятно
   
   ! Profile >> Type >> Desktop >> Hyprland >> polkit
     ^ Далее появится взможность выбрать Graphics driver
   >> Выбираем от характеристик пк, но советую ориентироваться на надпись open-source
     ^ После Greeter >> ly   // Тк я его люблю и всем советую
     ^ Ну back нажать ты и без меня догадаешься) 
   
   ! Audio >> pipewire
   ! Network configuration >> NetworkManager
   ! Additional packages >> Вводим: git firefox hyprpaper
   ! Optional repositories >> multilib
   
   ! Timezone >> Нажимаем "/" И вводим название главного
   города, от которого у вас идёт время на английском
   
   ! Теперь идём вниз где Install и протыкиваем )

   Наблюдаем загрузку и наслаждаемся. Если что-то пойдет не так, а это Линукс - Добро пожаловать xD
   В таком случае просто молимся ...
   ```
   Если всё прошло удачно, то нажимаем `yes`  и в консоли пишем
   ```
   exit

   //Тут стоит вытащить флешку из пк
   reboot
   ```
   * Если загрузилась винда, то придётся через bios/boot запускать как флешку (возможно именуется UEFI)
# Настройки hyprland)
    ```
    win+Q   // Откроем консоль
    cd .config/hypr
    vim hyprland.conf

    ОПА нужна инструкция по VIM !!!
    ```

    * a - редактировать (текст после курсора)
    * Esc - выйти из режима редактирования
    * :w Сохранить изменения
    * :q Выйти из vim (ШОК КОНТЕНТ)
    * :wq Сохранить и выйти
    * i редактировать (текст перед курсором)
    * u отменить последнее действие
    * уу скопировать последнюю строку
    * p Вставить скопированный или вырезанный текст после курсора
    * 0 переместить курсор в начало строки
    * $ переместить курсор в конец строки
    * gg переместить курсор в начало файла
    * G переместить курсор в конец файла

   
  Избавляемся от блока желтого сверху комментируя первую строчку где можно) 
  Ну и сохраняемся
  
  **Настраиваем монитор:**
  смотрим настройки экрана с помощью команды hyprctl monitors 
  И затем там где монитор написано параметр авто. Мы можем настроить 
  экран по принципу monitor= интерфейс, разрешение@герцовка, позиция, масштаб 
  Пример: monitor=eDP-1, 1920x1080@60, 0x0, 1.25

  **Настраиваем язык и переключение раскладки:**
  Идем к input {} и рядом с us (язык клавиатуры) ставим запятую 
  и пишем ru 
  Затем в kb_options пишем: grp:win_space_toggle
  
  **Настраиваем глобальные программы**
  Там где $terminal = … Можем написать браузер: 
  `$browser = firefox`
  Идем где написано exec-once. Это показывает что запустите при запуске ОС.
  Для будущего можем вписать ниже
  `exec-once = hyprpaper`
  
  В general {} находим gaps_out и делаем их 5 потому что блин, отступ 20 это много :/
  Затем можем настроить бинды по аналогии, ну там разобраться можно) 
  Учитывая что глобальную переменную браузера делали

  В самом низу можно найти бинды, увы лень щас это писать, может поправлю,
  но там по аналогии. Уж простите, кто хотел всё готовенькое) Просто это не сильно обязательно

  
  **Подключаемся к wifi уже в системе** 
  закрываем прошлую консоль (ctr + C) и открыть новую (ctr + Q)
  ```
  nmcli device wifi list
  nmcli device wifi connect SSID password PASS
  nmcli device wifi connection show

  !если возникают странная ошибка попробуй удалить это же соединение.
  Может быть если использовал одну и ту же сеть
  что и при установке линукса:
  nmcli connection delete "NameOfWifi"
  ```

  **Обновись! : sudo pacman -Syu**

  **Делаем настройку wofi**
  качаем конфиг hyprland Делаем с помощью гита. 
  ```
  git clone https://github.com/adeline2007/archlinux
  cd archlinux
  cp -r wofi ~/.config/

  Что бы воспользоваться, пробуем нажать ctr + R   вауля)
  ```

  **установка yay!**
  ```
  Лучше закрыть прошлую консоль (ctr + C) и открыть новую (ctr + Q)

  git clone https://aur.archlinux.org/yay.git
  cd yay
  makepkg -si
  ```
  
  **установка шрифтов крутых** 
  ```
  sudo pacman -S ttf-font-awesome otf-font-awesome ttf-jetbrains-mono
  ```

  **устанавливаем fish**
  ```
  sudo pacman -S fish pkgfile ttf-dejavu powerline-fonts inetutils
  chsh   >> Вводим в панельке /bin/fish
  ```

  
  **восстанавливаем в grub выбор других ОС** 
  ```
  sudo pacman -S os-prober ntfs-3g
  sudo os-prober
  sudo vim /etc/default/grub

  ! листаем до момента (в конце может быть)
  где написано
  #GRUB_DISABLE_OS_PROBER=false
  и раскомментируем её убрав #
  Сохраняемся и выходим из vim xD

  sudo grub-mkconfig -o /boot/grub/grub.cfg

  ! Lополнительно можно зайти в
  sudo vim /boot/grub/grub.cfg
  Находим названия ОС в ковычках и делаем названия, что нам нужны
  !!! В этом файле МАКСИМАЛЬНО АККУРАТНО. Лучше ждите моё видео на ютубе)
  ```

  **Вводим в консоль заветное: reboot** 
  
  Ребутиться - это святое!

# Настройка hyprpanel
К сожалению, мне почему-то тяжело далась установка. Команды здесь избыточны и повторяются,
но пока мне лень что-то менять, поэтому советую ctr+C - ctr+shift+V

(О да. Чтобы копировать и вставлять из консоли, к класике
ctr+C ctr+V добавляется ещё +shift)

А вот собственно и команды. Первые три можно скопировать вместе,
потом по отдельности. 

Пока будет загрузка то будут проситься подтверждение
Там либо нажимаем `y  и enter` или `a   и enter` (Там по контексту можно понять)

!Это очень долгая загрузка.. Запаситесь чаёчком)
```
yay -S aylurs-gtk-shell-git wireplumber libgtop bluez bluez-utils networkmanager dart-sass wl-clipboard upower gvfs
yay -S --needed aylurs-gtk-shell-git grimblast-git gpu-screen-recorder-git hyprpicker matugen-bin python-gpustat hyprsunset-git hypridle-git
sudo pacman -S --needed wireplumber libgtop bluez bluez-utils btop networkmanager dart-sass wl-clipboard brightnessctl swww python upower pacman-contrib power-profiles-daemon gvfs

git clone https://github.com/Jas-SinghFSU/HyprPanel.git
cd HyprPanel
yay -S meson
meson setup build
meson compile -C build
meson install -C build

./scripts/install_fonts.sh

// далее идём в конфиг hyprland
vim .config/hypr/hyprland.conf

// и там где мы указывали hyprpaper ниже вставляем
exec-once = hyprpanel

// Выходим из vim и делаем reboot xD
```
   
