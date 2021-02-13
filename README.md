# rounter-RUC

## auto-connect to
```bash
vim config/login.json # {"account": "xxx", "password": "xxx"} ruc account and password
vim src/autoconnect.service # edit the absolute path
cp src/autoconnect.service ~/.config/systemd/user/autoconnect.service
systemctl --user enable X.service
systemctl --user daemon-reload
systemctl --user restart autoconnect.service
systemctl --user status autoconnect.service
```