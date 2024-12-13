$ssid = (netsh wlan show networks) | Select-String -Pattern "SSID \d : (\w+)" | ForEach-Object {$_.Matches.Groups[1].Value}
$key = (netsh wlan show profile name=$ssid key=clear) | Select-String -Pattern "Key Content\s+: (\w+)" | ForEach-Object {$_.Matches.Groups[1].Value}
"ssid: $ssid | key: $key"
