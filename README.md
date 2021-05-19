#### File-sharing-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://github.com/jokokendi/File-Sharing-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/CodeXBotz/File-Sharing-Bot?style=social">
  </a>
  <a href="https://github.com/jokokendi/File-Sharing-Bot/fork">
    <img src="https://img.shields.io/github/forks/jokokendi/File-Sharing-Bot?label=Fork&style=social">
  </a>  
</p>


Telegram Bot untuk menyimpan Postingan dan Dokumen dan dapat diakses dengan Tautan Khusus. Kurasa Ini Akan Bermanfaat Bagi Banyak Orang .....😇.
### FITUR

- Dapat disesuaikan sepenuhnya.
- Pesan selamat datang yang dapat disesuaikan.
- Lebih dari satu Posting dalam Satu Link.
- Dapat diterapkan di heroku secara langsung.

### SETUP
- Tambahkan bot ke Saluran Database dengan semua izin
- Tambahkan bot ke saluran ForceSub sebagai Admin dengan Undang Pengguna melalui Izin Tautan jika Anda mengaktifkan ForceSub

### Installation
#### Buat di heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>
<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>
**Cek tutorialnya di youtube kalau butuh bantuan**<br>

#### Deploy in your VPS
```bash
git clone https://github.com/jokokendi/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
```
##

### Khusus Admin

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

```

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `API_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML parsemode format
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/CodeXBotz/File-Sharing-Bot/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Star this Repo if you Liked it ⭐⭐⭐**
